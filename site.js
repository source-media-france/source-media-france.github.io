/* SOURCE ? — le seul script du site.
   1. Ferme le menu déroulant quand on clique ailleurs.
   2. Sur la page des vidéos : bascule entre « par thème » et « par date ». */

document.addEventListener('click', function (e) {
  document.querySelectorAll('details.menu[open]').forEach(function (d) {
    if (!d.contains(e.target)) d.removeAttribute('open');
  });
});

(function () {
  var vueTheme = document.getElementById('vue-theme');
  var vueDate = document.getElementById('vue-date');
  var boutons = document.querySelectorAll('#vues button');
  if (!vueTheme || !vueDate || !boutons.length) return;

  document.getElementById('vues').hidden = false;

  function construireParDate() {
    var cible = document.getElementById('cartes-date');
    cible.innerHTML = '';
    var cartes = Array.prototype.slice.call(vueTheme.querySelectorAll('.carte[data-date]'));
    cartes.sort(function (a, b) { return b.dataset.date.localeCompare(a.dataset.date); });
    cartes.forEach(function (c) {
      var clone = c.cloneNode(true);
      var section = c.closest('section');
      var theme = section ? section.querySelector('h2').textContent.replace(/^\s*\d+\s*/, '').trim() : '';
      var ligne = clone.querySelector('.format');
      if (ligne && theme) ligne.textContent = theme + ' · ' + ligne.textContent;
      cible.appendChild(clone);
    });
    if (!cartes.length) cible.innerHTML = '<p class="gris">Aucune vidéo pour l’instant.</p>';
  }

  function montrer(vue) {
    var parDate = vue === 'date';
    if (parDate) construireParDate();
    vueTheme.hidden = parDate;
    vueDate.hidden = !parDate;
    boutons.forEach(function (b) { b.setAttribute('aria-pressed', b.dataset.vue === vue ? 'true' : 'false'); });
  }

  boutons.forEach(function (b) {
    b.addEventListener('click', function () {
      montrer(b.dataset.vue);
      history.replaceState(null, '', b.dataset.vue === 'date' ? '#par-date' : location.pathname);
    });
  });

  if (location.hash === '#par-date') montrer('date');
  window.addEventListener('hashchange', function () {
    if (location.hash === '#par-date') montrer('date');
    else if (location.hash) { montrer('theme'); var el = document.getElementById(location.hash.slice(1)); if (el) el.scrollIntoView(); }
  });
})();
