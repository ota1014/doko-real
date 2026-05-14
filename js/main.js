// Scroll reveal
const io = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// Area tab filter (top page)
const areaTabs = document.querySelectorAll('.area-tab');
const cards = document.querySelectorAll('.spot-card[data-area]');
areaTabs.forEach(tab => {
  tab.addEventListener('click', () => {
    areaTabs.forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
    const area = tab.dataset.area;
    cards.forEach(c => {
      c.parentElement.style.display = (!area || c.dataset.area === area) ? '' : 'none';
    });
  });
});

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
