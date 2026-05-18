// Scroll reveal
const io = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

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

// Area tab filter (city-level, inside a region)
const areaTabs = document.querySelectorAll('.area-tab');
const areaGroups = document.querySelectorAll('.area-group');
areaTabs.forEach(tab => {
  tab.addEventListener('click', () => {
    areaTabs.forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
    const area = tab.dataset.area;
    areaGroups.forEach(g => {
      g.style.display = (!area || g.dataset.area === area) ? '' : 'none';
    });
  });
});

// Search filter
const searchInput = document.querySelector('.hero-search input');
const searchBtn = document.querySelector('.hero-search button');
function doSearch() {
  if (!searchInput) return;
  const q = searchInput.value.trim().toLowerCase();
  if (!q) {
    areaGroups.forEach(g => g.style.display = '');
    areaTabs.forEach(t => { t.classList.remove('active'); if (!t.dataset.area) t.classList.add('active'); });
    return;
  }
  let found = 0;
  areaGroups.forEach(g => {
    const cards = g.querySelectorAll('.spot-card');
    let groupVisible = false;
    cards.forEach(c => {
      const text = c.textContent.toLowerCase();
      const match = text.includes(q);
      c.style.display = match ? '' : 'none';
      if (match) groupVisible = true;
    });
    g.style.display = groupVisible ? '' : 'none';
    if (groupVisible) found++;
  });
  areaTabs.forEach(t => t.classList.remove('active'));
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
