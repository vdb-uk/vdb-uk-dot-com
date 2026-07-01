(function () {
const html = document.documentElement;

    // ─── Mobile Navigation ───
    const menuBtn = document.querySelector('.header__menu-btn');
    const siteHeader = document.querySelector('.header');

    function setMobileNavOpen(open) {
      if (!siteHeader || !menuBtn) return;
      siteHeader.classList.toggle('header--nav-open', open);
      document.body.classList.toggle('mobile-nav-open', open);
      menuBtn.setAttribute('aria-expanded', String(open));
    }

    menuBtn?.addEventListener('click', () => {
      setMobileNavOpen(!siteHeader.classList.contains('header--nav-open'));
    });

    document.addEventListener('click', (event) => {
      if (!siteHeader?.classList.contains('header--nav-open')) return;
      if (siteHeader.contains(event.target)) return;
      setMobileNavOpen(false);
    });

    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') {
        setMobileNavOpen(false);
      }
    });

    document.querySelectorAll('.header__nav a').forEach((link) => {
      link.addEventListener('click', () => setMobileNavOpen(false));
    });

    window.addEventListener('resize', () => {
      if (window.innerWidth > 768) {
        setMobileNavOpen(false);
      }
    });

    // ─── Header Background on Scroll ───
    const header = document.querySelector('.header');
    function updateHeaderScroll() {
      const scrolled = window.scrollY > 50;
      const isLight = html.getAttribute('data-theme') === 'light';
      if (scrolled) {
        header.style.background = isLight ? 'rgba(255,255,255,0.95)' : 'rgba(15,17,24,0.95)';
        header.style.backdropFilter = 'blur(12px)';
      } else {
        header.style.background = '';
        header.style.backdropFilter = '';
      }
    }
    window.addEventListener('scroll', updateHeaderScroll, { passive: true });

    // ─── Theme Toggle ───
    const savedTheme = localStorage.getItem('vdb-theme');
    const initialTheme = savedTheme || 'dark';

    const themeBtns = document.querySelectorAll('[data-set-theme]');

    function setTheme(theme) {
      html.setAttribute('data-theme', theme);
      localStorage.setItem('vdb-theme', theme);
      themeBtns.forEach(btn => {
        btn.classList.toggle('theme-toggle__btn--active', btn.dataset.setTheme === theme);
      });
      updateHeaderScroll();
    }

    setTheme(initialTheme);

    themeBtns.forEach(btn => {
      btn.addEventListener('click', () => setTheme(btn.dataset.setTheme));
    });

    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
      if (!localStorage.getItem('vdb-theme')) {
        setTheme(e.matches ? 'dark' : 'light');
      }
    });

    // ─── Scroll Reveal ───
    const reveals = document.querySelectorAll('.reveal');
    reveals.forEach(el => el.classList.add('reveal--hidden'));
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('reveal--visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });

    reveals.forEach(el => observer.observe(el));

    // ─── Smooth Scroll for Anchor Links ───
    document.querySelectorAll('a[href^="#"]').forEach(link => {
      link.addEventListener('click', (e) => {
        const target = document.querySelector(link.getAttribute('href'));
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });
  
})();
