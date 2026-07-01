// Screenshot helper for the visual-verify skill. Runs inside dev-browser's
// sandboxed QuickJS runtime (NOT Node) — `browser` pages are full Playwright
// Page objects. Plain JS only inside page.evaluate(...).
//
// shoot.sh injects these two consts ABOVE this file before running it:
//   const BASE  = "http://localhost:8000";   // local server root
//   const PATHS = ["/", "/about.html"];        // page paths to capture
//
// For each path it captures desktop + mobile, in dark + light theme. Two site
// quirks are handled so the shots are truthful (see docs/learnings/0003):
//   • Default theme is dark, driven by localStorage['vdb-theme'] (site.js) — we
//     set both the attribute and the key for each theme.
//   • .reveal sections are opacity:0 until scrolled into view; a full-page shot
//     would show them blank, so we force them visible first.
//
// Saved PNGs are printed as "SAVED: <path>" lines (under ~/.dev-browser/tmp/).

const THEMES = ["dark", "light"];
const VIEWPORTS = [
  { name: "desktop", width: 1440, height: 900 },
  { name: "mobile", width: 390, height: 844 },
];

function slug(p) {
  const s = String(p).replace(/^\/+|\/+$/g, "").replace(/[^A-Za-z0-9]+/g, "-");
  return s || "home";
}

const page = await browser.getPage("visual-verify");
let count = 0;

for (const path of PATHS) {
  const url = BASE.replace(/\/+$/, "") + "/" + String(path).replace(/^\/+/, "");
  for (const vp of VIEWPORTS) {
    await page.setViewportSize({ width: vp.width, height: vp.height });
    await page.goto(url, { waitUntil: "load", timeout: 15000 });
    // Let webfonts settle so headings aren't captured mid font-swap.
    await page.evaluate(() =>
      document.fonts ? document.fonts.ready.then(() => true) : true
    );
    for (const theme of THEMES) {
      await page.evaluate((t) => {
        localStorage.setItem("vdb-theme", t);
        document.documentElement.setAttribute("data-theme", t);
        document.querySelectorAll("[data-set-theme]").forEach((b) =>
          b.classList.toggle("theme-toggle__btn--active", b.dataset.setTheme === t)
        );
        document.querySelectorAll(".reveal").forEach((el) => {
          el.classList.remove("reveal--hidden");
          el.classList.add("reveal--visible");
        });
      }, theme);
      await page.waitForTimeout(350);
      const name = slug(path) + "--" + theme + "--" + vp.name + ".png";
      const saved = await saveScreenshot(
        await page.screenshot({ fullPage: true }),
        name
      );
      console.log("SAVED: " + saved);
      count++;
    }
  }
}
console.log("DONE: " + count + " screenshots in ~/.dev-browser/tmp/");
