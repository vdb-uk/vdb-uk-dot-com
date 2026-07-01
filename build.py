#!/usr/bin/env python3
from __future__ import annotations

import os
import shutil
import sys
import time
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
SRC_DIR = ROOT / 'src'
DIST_DIR = ROOT / 'dist'
TMP_DIR = ROOT / 'dist.tmp'
PARTIAL_RE = re.compile(r'<!--\s*@include\s+([^\s>]+)\s*-->')

STATIC_FILE_EXTS = {'.css', '.js', '.png', '.jpg', '.jpeg', '.webp', '.gif', '.svg', '.ico', '.xml', '.txt'}
STATIC_DIRS = {'images', 'capabilities', 'case-studies', 'projects'}
SKIP_FILES = {
    '.gitignore', 'build.py', 'tmp_header.html', 'tmp_footer.html', 'CLAUDE.md'
}
SKIP_DIRS = {
    '.git', '.playwright-mcp', 'test-results', 'docs', 'src', '.vscode', '.mcp'
}


def apply_includes(html: str, depth: int = 8) -> str:
    content = html
    for _ in range(depth):
        changed = False

        def repl(match: re.Match[str]) -> str:
            nonlocal changed
            rel = match.group(1).strip().strip('"\'')
            include_path = (ROOT / rel).resolve()
            try:
                include_path.relative_to(ROOT)
            except ValueError:
                raise ValueError(f'Include path escapes project root: {rel}')

            if not include_path.exists():
                raise FileNotFoundError(f'Include not found: {rel}')

            changed = True
            return include_path.read_text()

        new_content = PARTIAL_RE.sub(repl, content)
        if new_content == content:
            return content
        content = new_content
    if changed:
        return content
    return content


def copy_static_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def publish(src: Path, dst: Path) -> None:
    """Merge the freshly built `src` tree into `dst` *in place*.

    We deliberately do NOT rename `dist.tmp` -> `dist`: nginx serves `dist/`
    through a Docker bind mount, and a bind mount is pinned to the directory's
    inode at container start. Renaming the directory swaps the inode, so the
    running container would keep serving the old (now-unlinked) directory and
    never see new builds. Instead we keep `dst`'s inode stable, replace each
    file atomically with os.replace, and prune anything that disappeared — so a
    concurrent request never observes a missing file.
    """
    if dst.exists() and not dst.is_dir():
        dst.unlink()
    dst.mkdir(parents=True, exist_ok=True)

    keep = set()
    for item in src.iterdir():
        keep.add(item.name)
        target = dst / item.name
        if item.is_dir() and not item.is_symlink():
            publish(item, target)
        else:
            if target.is_dir() and not target.is_symlink():
                shutil.rmtree(target)
            os.replace(item, target)  # atomic within the same filesystem

    for item in dst.iterdir():
        if item.name not in keep:
            if item.is_dir() and not item.is_symlink():
                shutil.rmtree(item)
            else:
                item.unlink()


def build() -> int:
    if not SRC_DIR.exists():
        print('ERROR: src directory missing', file=sys.stderr)
        return 1

    if TMP_DIR.exists():
        shutil.rmtree(TMP_DIR)
    TMP_DIR.mkdir()

    try:
        for html in SRC_DIR.rglob('*.html'):
            source = html.read_text()
            expanded = apply_includes(source)
            rel = html.relative_to(SRC_DIR)
            out = TMP_DIR / rel
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(expanded)

        # Copy static directories and files from repo root that are expected at runtime.
        # Exclude source directories that are already emitted from `src/`.
        for item in ROOT.iterdir():
            if item.name in SKIP_DIRS or item.name.startswith('.'):
                continue
            if item == SRC_DIR or item == DIST_DIR or item == TMP_DIR:
                continue

            if item.is_dir():
                if item.name in {'capabilities', 'case-studies', 'projects'}:
                    continue
                if item.name in STATIC_DIRS:
                    dst = TMP_DIR / item.name
                    shutil.copytree(item, dst)
                continue

            if not item.is_file():
                continue

            if item.name in SKIP_FILES:
                continue

            if item.name == 'CNAME' or item.suffix.lower() in STATIC_FILE_EXTS:
                copy_static_file(item, TMP_DIR / item.name)

        publish(TMP_DIR, DIST_DIR)
        shutil.rmtree(TMP_DIR, ignore_errors=True)
    except Exception as exc:
        if TMP_DIR.exists():
            shutil.rmtree(TMP_DIR)
        print(f'ERROR: build failed: {exc}', file=sys.stderr)
        return 1

    return 0


def main() -> int:
    start = time.perf_counter()
    rc = build()
    elapsed = time.perf_counter() - start
    print(f'build.py completed in {elapsed:.4f}s (exit={rc})')
    return rc


if __name__ == '__main__':
    sys.exit(main())
