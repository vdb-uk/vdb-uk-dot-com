#!/usr/bin/env python3
"""
Idempotent insertion of the "Partnerships" link into the header nav and the
footer "Company" column on every content page of vdb-uk.com.

Why a script: the site has no build step (nginx serves the HTML directly), so
shared chrome is hand-duplicated per page. This is the one site-wide change the
partnerships work needs; running it keeps all ~23 pages consistent and can be
re-run safely after new pages are added.

- Header: inserts a Partnerships <li> immediately after the "About" item inside
  <ul class="header__links">. Handles both href forms in use (/about.html and
  the /#about anchor used on a couple of capability pages).
- Footer: inserts a Partnerships <li> immediately after the "About VDB" item in
  the Company column. Handles all three Welsh encodings of "About VDB".
- Idempotent: skips a page (header or footer independently) if it already links
  to /partnerships.html in that region.
- Safety: requires the anchor to be unique within the file before touching it;
  otherwise it skips that page and reports, rather than guessing.

Run from the repo root:  python3 scripts/add-partnerships-nav.py
Redirect/legacy stubs under projects/ have no nav and are skipped.
"""
import glob
import re
import sys

PARTNER_LI = ('<li><a href="/partnerships.html">'
              '<span data-en>Partnerships</span>'
              '<span data-cy>Partneriaethau</span></a></li>')

# Header "About" item — href is /about.html on most pages, /#about on a couple.
HEADER_ABOUT = re.compile(
    r'<li><a href="(?:/about\.html|/#about)">'
    r'<span data-en>About</span><span data-cy>Amdanom</span></a></li>')

# Footer "About VDB" item — data-cy varies across three Welsh encodings.
FOOTER_ABOUT = re.compile(
    r'<li><a href="/about\.html">'
    r'<span data-en>About VDB</span><span data-cy>[^<]*</span></a></li>')

HEADER_UL = re.compile(r'<ul class="header__links">(.*?)</ul>', re.S)


def line_indent(s, pos):
    """Leading whitespace of the line containing index `pos`."""
    start = s.rfind('\n', 0, pos) + 1
    return s[start:pos]


def insert_header(s):
    ul = HEADER_UL.search(s)
    if not ul:
        return s, 'header: no header__links (skip)'
    block = ul.group(1)
    if '/partnerships.html' in block:
        return s, 'header: already present'
    hits = list(HEADER_ABOUT.finditer(block))
    if len(hits) != 1:
        return s, f'header: About anchor count={len(hits)} (skip)'
    rel = hits[0].end()                      # offset within block
    abs_end = ul.start(1) + rel              # offset within full string
    indent = line_indent(s, ul.start(1) + hits[0].start())
    new = s[:abs_end] + '\n' + indent + PARTNER_LI + s[abs_end:]
    return new, 'header: inserted'


def insert_footer(s):
    hits = list(FOOTER_ABOUT.finditer(s))
    if len(hits) != 1:
        return s, f'footer: About VDB anchor count={len(hits)} (skip)'
    m = hits[0]
    if '/partnerships.html' in s[m.end():m.end() + 250]:
        return s, 'footer: already present'
    indent = line_indent(s, m.start())
    new = s[:m.end()] + '\n' + indent + PARTNER_LI + s[m.end():]
    return new, 'footer: inserted'


def main():
    files = sorted(
        f for f in glob.glob('**/*.html', recursive=True)
        if not f.startswith('projects/') and not f.startswith('.git/')
    )
    changed = 0
    for f in files:
        s = open(f, encoding='utf-8').read()
        orig = s
        s, h = insert_header(s)
        s, ft = insert_footer(s)
        if s != orig:
            open(f, 'w', encoding='utf-8').write(s)
            changed += 1
        print(f'{f:45s} | {h:28s} | {ft}')
    print(f'\n{len(files)} pages processed, {changed} changed.')


if __name__ == '__main__':
    main()
