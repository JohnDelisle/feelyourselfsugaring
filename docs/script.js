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

// Preview-only switcher for theme, hero art, extra photos and layout variant.
// Shows on github.io, localhost, or with ?preview in the URL. Choices are remembered per browser
// (localStorage) and can be shared as ?theme=…&hero=…&photos=… links. Remove this block at launch.
(() => {
  const host = location.hostname;
  const preview = host.endsWith('github.io') || host === 'localhost' || host === '127.0.0.1' ||
    location.protocol === 'file:' || location.search.includes('preview');
  if (!preview) return;

  const root = document.documentElement;
  const groups = [
    { key: 'theme', label: 'Theme', def: 'pine', options: [
      ['pine', 'Pine', '#1E3A32', '#E39B2D'], ['brand', 'Brand', '#1C1C1C', '#F385AA'],
      ['teal', 'Teal', '#1A9DA8', '#FACBD0'], ['noir', 'Noir', '#161616', '#F6A9C4']] },
    { key: 'hero', label: 'Hero', def: 'blob', options: [
      ['blob', 'Blob'], ['hearts', 'Hearts logo'], ['hips', 'Hips logo'], ['pamela', 'Pamela'],
      ['sugar', 'Sugar ball'], ['legs', 'Legs'], ['studio', 'Studio'], ['none', 'Text only']] },
    { key: 'photos', label: 'Photos', def: 'more', options: [['more', 'More'], ['fewer', 'Fewer']] },
  ];

  const bar = document.createElement('div');
  bar.className = 'preview';
  bar.setAttribute('aria-label', 'Preview options');
  const buttons = [];
  groups.forEach(g => {
    const row = document.createElement('div');
    row.className = 'preview-row';
    row.innerHTML = `<span>${g.label}</span>`;
    g.options.forEach(([id, name, a, b]) => {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.innerHTML = (a ? `<i class="swatch" style="background:linear-gradient(90deg,${a} 50%,${b} 50%)"></i>` : '') + name;
      btn.addEventListener('click', () => {
        root.dataset[g.key] = id;
        try { localStorage.setItem('fys-' + g.key, id); } catch (e) {}
        update();
      });
      row.appendChild(btn);
      buttons.push([g, id, btn]);
    });
    bar.appendChild(row);
  });
  function update() {
    buttons.forEach(([g, id, btn]) => btn.setAttribute('aria-pressed', String((root.dataset[g.key] || g.def) === id)));
  }
  update();

  // Link to the same page in the other structural variant (prices on the home page vs. on their own page),
  // plus a share link that carries the current choices.
  const row = document.createElement('div');
  row.className = 'preview-row';
  row.innerHTML = '<span>Layout</span>';
  const inVariant = location.pathname.includes('/variants/prices-page/');
  let file = location.pathname.split('/').pop() || 'index.html';
  if (file && !file.includes('.')) file += '.html';
  const link = document.createElement('a');
  if (inVariant) {
    link.href = '../../' + (file === 'prices.html' ? 'index.html#prices' : file);
    link.textContent = 'Prices on home page';
  } else {
    link.href = 'variants/prices-page/' + (['home.html', 'why-us.html', '404.html'].includes(file) ? 'index.html' : file);
    link.textContent = 'Prices on own page';
  }
  row.appendChild(link);
  const share = document.createElement('a');
  share.textContent = 'Copy share link';
  share.href = '#';
  share.addEventListener('click', e => {
    e.preventDefault();
    const q = new URLSearchParams();
    groups.forEach(g => q.set(g.key, root.dataset[g.key] || g.def));
    const url = location.origin + location.pathname + '?' + q;
    navigator.clipboard?.writeText(url).then(() => { share.textContent = 'Copied'; setTimeout(() => share.textContent = 'Copy share link', 1500); });
  });
  row.appendChild(share);
  bar.appendChild(row);
  document.body.appendChild(bar);
})();
