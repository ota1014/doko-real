// Scroll reveal
const io = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// ===== NAV DROPDOWN =====
document.querySelectorAll('.nav-dropdown').forEach(dropdown => {
  const btn = dropdown.querySelector('.nav-btn');
  const menu = dropdown.querySelector('.nav-dropdown-menu');
  if (!btn || !menu) return;
  btn.addEventListener('click', e => {
    e.stopPropagation();
    const isOpen = menu.classList.contains('open');
    document.querySelectorAll('.nav-dropdown-menu').forEach(m => m.classList.remove('open'));
    document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('open'));
    if (!isOpen) { menu.classList.add('open'); btn.classList.add('open'); }
  });
});
document.addEventListener('click', () => {
  document.querySelectorAll('.nav-dropdown-menu').forEach(m => m.classList.remove('open'));
  document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('open'));
});

// ===== THEME FILTER (静岡ページのみ動作) =====
function filterByTheme(theme) {
  const groups = document.querySelectorAll('.area-group');
  if (!theme) {
    document.querySelectorAll('.spot-card').forEach(c => c.style.display = '');
    groups.forEach(g => g.style.display = '');
    document.querySelectorAll('.nav-menu-item[data-filter-theme]').forEach(el => el.classList.remove('active-theme'));
    const allItem = document.querySelector('.nav-menu-item[data-filter-theme=""]');
    if (allItem) allItem.classList.add('active-theme');
    return;
  }
  groups.forEach(g => {
    const cards = g.querySelectorAll('.spot-card');
    let visible = false;
    cards.forEach(c => {
      const themes = (c.dataset.theme || '').split(' ');
      const match = themes.includes(theme);
      c.style.display = match ? '' : 'none';
      if (match) visible = true;
    });
    g.style.display = visible ? '' : 'none';
  });
  document.querySelectorAll('.nav-menu-item[data-filter-theme]').forEach(el => {
    el.classList.toggle('active-theme', el.dataset.filterTheme === theme);
  });
}

document.querySelectorAll('.nav-menu-item[data-filter-theme]').forEach(item => {
  item.addEventListener('click', e => {
    e.preventDefault();
    const theme = item.dataset.filterTheme;
    filterByTheme(theme);
    document.querySelectorAll('.nav-dropdown-menu').forEach(m => m.classList.remove('open'));
    document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('open'));
    const section = document.querySelector('.section');
    if (section) window.scrollTo({ top: section.offsetTop - 70, behavior: 'smooth' });
  });
});

// URLパラメータからテーマ適用（外部リンク・トップページからの遷移対応）
const urlTheme = new URLSearchParams(location.search).get('theme');
if (urlTheme) filterByTheme(urlTheme);

// Region tab switching (shizuoka page)
const regionTabs = document.querySelectorAll('.region-tab');
const regionContents = document.querySelectorAll('.region-content');
regionTabs.forEach(tab => {
  tab.addEventListener('click', () => {
    if (tab.classList.contains('coming')) return;
    regionTabs.forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
    const region = tab.dataset.region;
    regionContents.forEach(c => {
      c.classList.toggle('active', c.dataset.region === region);
    });
  });
});

// Area tab filter (city-level, inside a region) — scoped to current region
document.querySelectorAll('.area-tab').forEach(tab => {
  tab.addEventListener('click', () => {
    const rc = tab.closest('.region-content');
    rc.querySelectorAll('.area-tab').forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
    const area = tab.dataset.area;
    rc.querySelectorAll('.area-group').forEach(g => {
      g.style.display = (!area || g.dataset.area === area) ? '' : 'none';
    });
  });
});

// Search filter — scoped to active region
const searchInput = document.querySelector('.hero-search input');
const searchBtn = document.querySelector('.hero-search button');
function doSearch() {
  if (!searchInput) return;
  const q = searchInput.value.trim().toLowerCase();
  const rc = document.querySelector('.region-content.active') || document.querySelector('.region-content');
  const activeGroups = rc.querySelectorAll('.area-group');
  const activeTabs   = rc.querySelectorAll('.area-tab');
  if (!q) {
    activeGroups.forEach(g => g.style.display = '');
    activeTabs.forEach(t => { t.classList.remove('active'); if (!t.dataset.area) t.classList.add('active'); });
    return;
  }
  activeGroups.forEach(g => {
    const cards = g.querySelectorAll('.spot-card');
    let groupVisible = false;
    cards.forEach(c => {
      const text = c.textContent.toLowerCase();
      const match = text.includes(q);
      c.style.display = match ? '' : 'none';
      if (match) groupVisible = true;
    });
    g.style.display = groupVisible ? '' : 'none';
  });
  activeTabs.forEach(t => t.classList.remove('active'));
}
if (searchBtn) searchBtn.addEventListener('click', doSearch);
if (searchInput) searchInput.addEventListener('keydown', e => { if (e.key === 'Enter') doSearch(); });

// Platform tab filter (spot detail pages)
const platformTabs = document.querySelectorAll('.platform-tab');
const platformGroups = document.querySelectorAll('.platform-group');
platformTabs.forEach(tab => {
  tab.addEventListener('click', () => {
    platformTabs.forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
    const selected = tab.dataset.platform;
    platformGroups.forEach(g => {
      if (selected === 'all') {
        g.classList.remove('hidden');
      } else {
        g.classList.toggle('hidden', g.dataset.platform !== selected);
      }
    });
  });
});
