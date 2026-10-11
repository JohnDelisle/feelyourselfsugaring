// Mobile menu toggle
const toggle = document.querySelector('.menu-toggle');
const nav = document.getElementById('site-nav');
if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open);
    toggle.textContent = open ? 'Close' : 'Menu';
  });
}

// Preview-only theme and variant switcher. Shows on github.io, localhost, or with ?preview in the URL.
// Themes are defined in styles.css. The chosen theme is remembered per browser. Remove this block at launch.
(() => {
  const host = location.hostname;
  const preview = host.endsWith('github.io') || host === 'localhost' || host === '127.0.0.1' ||
    location.protocol === 'file:' || location.search.includes('preview');
  if (!preview) return;

  const themes = [
    ['pine', 'Pine', '#1E3A32', '#E39B2D'],
    ['brand', 'Brand', '#1C1C1C', '#F385AA'],
    ['teal', 'Teal', '#1A9DA8', '#FACBD0'],
    ['noir', 'Noir', '#161616', '#F6A9C4'],
  ];
  const root = document.documentElement;
  const current = () => root.dataset.theme || 'pine';

  const bar = document.createElement('div');
  bar.className = 'preview';
  bar.setAttribute('aria-label', 'Preview options');
  bar.innerHTML = '<span>Theme</span>';
  const buttons = themes.map(([id, name, a, b]) => {
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.innerHTML = `<i class="swatch" style="background:linear-gradient(90deg,${a} 50%,${b} 50%)"></i>${name}`;
    btn.addEventListener('click', () => {
      root.dataset.theme = id;
      try { localStorage.setItem('fys-theme', id); } catch (e) {}
      update();
    });
    bar.appendChild(btn);
    return [id, btn];
  });
  function update() { buttons.forEach(([id, btn]) => btn.setAttribute('aria-pressed', String(id === current()))); }
  update();

  // Link to the same page in the other structural variant (prices on the home page vs. on their own page).
  const inVariant = location.pathname.includes('/variants/prices-page/');
  let file = location.pathname.split('/').pop() || 'index.html';
  if (file && !file.includes('.')) file += '.html';
  if (!file) file = 'index.html';
  const link = document.createElement('a');
  if (inVariant) {
    link.href = '../../' + (file === 'prices.html' ? 'index.html#prices' : file);
    link.textContent = 'Prices on home page';
  } else {
    link.href = 'variants/prices-page/' + (['home.html', 'why-us.html', '404.html'].includes(file) ? 'index.html' : file);
    link.textContent = 'Prices on own page';
  }
  link.title = 'Switch to the other layout variant';
  bar.appendChild(link);
  document.body.appendChild(bar);
})();
