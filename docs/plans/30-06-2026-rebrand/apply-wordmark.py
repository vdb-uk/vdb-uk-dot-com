#!/usr/bin/env python3
"""Apply the lowercase 'vdb' wordmark (DM Sans 700) to the site logo, for the
COMPONENT/build architecture introduced 2026-07-01 (build.py + _partials/ +
extracted styles.css).

- Markup lives in `_partials/header.html` and `_partials/footer.html`.
- Styling lives in `styles.css`, where the logo rules are duplicated ~22x
  (one block per original page's <style>), in both multi-line and single-line
  forms. We rewrite every copy.

Wordmark = DM Sans 700 lowercase "vdb" (brand folder 1HlDfJo98rkhTfh9uSiMkuN-ah3nrzOIs).
Rendered as native text so it inherits the brand font and themes via `color`:
white on the dark default theme, brand purple on the light theme.

Run from repo root, then `python3 build.py`.
"""
import re
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]
HEADER = ROOT / '_partials' / 'header.html'
FOOTER = ROOT / '_partials' / 'footer.html'
CSS = ROOT / 'styles.css'

HEADER_SPAN = '<span class="header__logo-text" aria-hidden="true">vdb</span>'
FOOTER_SPAN = '<span class="footer__logo-text" aria-hidden="true">vdb</span>'

RE_HEADER_SVG = re.compile(
    r'(?:<!-- VDB Logo, geometric monogram -->\s*)?'
    r'<svg viewBox="0 0 92 40" fill="none" xmlns="http://www\.w3\.org/2000/svg" aria-hidden="true">'
    r'.*?</svg>', re.DOTALL)
RE_FOOTER_SVG = re.compile(
    r'<svg viewBox="0 0 92 40" fill="none" xmlns="http://www\.w3\.org/2000/svg" width="100" aria-hidden="true">'
    r'.*?</svg>', re.DOTALL)

HEADER_CSS_OLD = '.header__logo svg { height: 36px; width: auto; }'
HEADER_CSS_NEW = (
    '.header__logo { text-decoration: none; }\n'
    '    .header__logo-text { font-family: var(--font-body); font-weight: 700; '
    'font-size: 1.9rem; letter-spacing: 0.01em; line-height: 1; color: #fff; }'
)
RE_FOOTER_CSS_ANCHOR = re.compile(r'(?<!\] )\.footer__brand p \{')
FOOTER_CSS_NEW = (
    '.footer__logo-text { font-family: var(--font-body); font-weight: 700; '
    'font-size: 1.7rem; letter-spacing: 0.01em; line-height: 1; color: #fff; '
    'display: inline-block; }\n'
    '    .footer__brand p {'
)


def light_rule(selector_re):
    return re.compile(
        r'\n[ \t]*\[data-theme="light"\][ \t\n]*' + selector_re + r'[ \t\n]*\{[^}]*\}')


RE_LIGHT_HEADER_PATH = light_rule(r'\.header__logo svg path:not\(:first-child\)')
RE_LIGHT_HEADER_TEXT = light_rule(r'\.header__logo svg text')
RE_LIGHT_HEADER_LINE = light_rule(r'\.header__logo svg line')
RE_LIGHT_FOOTER_PATH = light_rule(r'\.footer__brand svg path:not\(:first-child\)')
RE_LIGHT_FOOTER_TEXT = light_rule(r'\.footer__brand svg text')
LIGHT_HEADER_NEW = '\n    [data-theme="light"] .header__logo-text { color: var(--red-500); }'
LIGHT_FOOTER_NEW = '\n    [data-theme="light"] .footer__logo-text { color: var(--red-500); }'


def edit(path, fn, label):
    text = path.read_text()
    new, counts = fn(text)
    path.write_text(new)
    print(f"{path.relative_to(ROOT)}: {counts}")


def do_header(t):
    t, n = RE_HEADER_SVG.subn(HEADER_SPAN, t)
    return t, {'header_svg': n}


def do_footer(t):
    t, n = RE_FOOTER_SVG.subn(FOOTER_SPAN, t)
    return t, {'footer_svg': n}


def do_css(t):
    c = {}
    t, c['header_css'] = re.subn(re.escape(HEADER_CSS_OLD), HEADER_CSS_NEW, t)
    t, c['footer_css'] = RE_FOOTER_CSS_ANCHOR.subn(FOOTER_CSS_NEW, t)
    t, c['light_header_path'] = RE_LIGHT_HEADER_PATH.subn(LIGHT_HEADER_NEW, t)
    t, c['light_header_text'] = RE_LIGHT_HEADER_TEXT.subn('', t)
    t, c['light_header_line'] = RE_LIGHT_HEADER_LINE.subn('', t)
    t, c['light_footer_path'] = RE_LIGHT_FOOTER_PATH.subn(LIGHT_FOOTER_NEW, t)
    t, c['light_footer_text'] = RE_LIGHT_FOOTER_TEXT.subn('', t)
    return t, c


if __name__ == '__main__':
    edit(HEADER, do_header, 'header')
    edit(FOOTER, do_footer, 'footer')
    edit(CSS, do_css, 'css')
    print('done — now run: python3 build.py')
