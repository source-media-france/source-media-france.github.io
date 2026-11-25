/* SOURCE ? — le seul script du site.
   1. Ferme les menus déroulants quand on clique ailleurs.
   2. Formulaire « Contribuer » : compte les mots du script et bloque l'envoi au-delà de la limite. */

document.addEventListener('click', function (e) {
  document.querySelectorAll('details.menu[open]').forEach(function (d) {
    if (!d.contains(e.target)) d.removeAttribute('open');
  });
});

document.querySelectorAll('textarea[data-max-mots]').forEach(function (zone) {
  var max = parseInt(zone.dataset.maxMots, 10);
  var compteur = zone.parentNode.querySelector('.compteur');
  var bouton = zone.form && zone.form.querySelector('button[type=submit]');
  function maj() {
    var n = zone.value.trim() ? zone.value.trim().split(/\s+/).length : 0;
    var trop = n > max;
    if (compteur) {
      compteur.textContent = n + ' / ' + max + ' mots' + (trop ? ' : raccourcissez de ' + (n - max) + ' mot' + (n - max > 1 ? 's' : '') : '');
      compteur.classList.toggle('trop', trop);
    }
    zone.setCustomValidity(trop ? 'Le script dépasse ' + max + ' mots.' : '');
    if (bouton) bouton.disabled = trop;
  }
  zone.addEventListener('input', maj);
  maj();
});
