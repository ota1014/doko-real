// Scroll reveal
const io = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// Area tab filter
const tabs = document.querySelectorAll('.area-tab');
const cards = document.querySelectorAll('.spot-card[data-area]');
tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    tabs.forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
    const area = tab.dataset.area;
    cards.forEach(c => {
      c.parentElement.style.display = (!area || c.dataset.area === area) ? '' : 'none';
    });
  });
});
