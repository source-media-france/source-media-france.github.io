# SOURCE ? — le site de coulisses

Le site public qui complète les vidéos de SOURCE ? : pour chaque vidéo, le résumé, l'explication en images avec ses graphiques, les sources complètes, ce qu'elle montre et ne montre pas, les données et les calculs des graphiques, les noms des relecteurs, les corrections. Plus une page « Notions », la méthode, et qui nous sommes.

C'est le « site de coulisses » décidé lors de la première réunion du comité (point 3 de l'ordre du jour, option C : sources, relecteurs, données et code, onglet notions). Le comité avait aussi évoqué la transcription ; Hanna a choisi un résumé et une explication en images à la place.

## Ce qu'il y a dedans

```
index.html            Accueil : ce qu'est SOURCE ?, les dernières vidéos, les trois questions
videos/index.html     Toutes les vidéos, et la série « Les bases »
videos/*.html         Une page par vidéo (trois pilotes pour l'instant)
videos/_modele.html   Le gabarit à copier pour une nouvelle vidéo
donnees/              Nos calculs en CSV, un fichier par vidéo, à télécharger depuis sa page
site.js               Le seul script : menu déroulant, et classement par thème / par date
notions.html          Les mots qu'on emploie, expliqués une fois
methode.html          Comment une vidéo est fabriquée, qui vérifie quoi
a-propos.html         Mission, engagements, comité, indépendance, contribuer, contact
corrections.html      Toutes les corrections publiées, et comment signaler une erreur
style.css             La charte graphique en CSS : couleurs, trois polices, crochets
assets/logo/          Le logo (trois versions)
```

Aucun outil à installer, aucune étape de construction : ce sont des pages HTML écrites à la main, qui se modifient dans n'importe quel éditeur de texte, ou directement sur GitHub (icône crayon sur un fichier). Les polices (Source Sans 3, Source Serif 4, Source Code Pro) sont chargées depuis Google Fonts.

## Ajouter une vidéo

1. Copier `videos/_modele.html` sous un nom court, en minuscules, sans accent ni espace : `videos/mon-sujet.html`.
2. Remplacer tout ce qui est entre `[[ ]]`. Le résumé et la légende viennent du document de script ; les sources aussi ; la relecture, du tableau de suivi. Pas de transcription mot pour mot : la page est un petit article, pas le script.
3. Écrire la section « L'explication, en images » comme un petit article : un chapeau, un ou deux paragraphes, et au moins un graphique. Un graphique se dessine en SVG directement dans la page (voir les trois pilotes : barres, grille de cent personnes, schémas à flèches), ou se met en image. Règles de la charte : un graphique montre une seule chose, fond papier, traits noirs, le jaune pour le seul élément dont on parle, la source entre crochets sous le graphique, jamais de rouge ni de vert.
4. Dans `videos/index.html`, ajouter une carte dans la section du thème (copier-coller une carte existante) avec la date de publication dans `data-date="AAAA-MM-JJ"` : c'est elle qui sert au classement par date. Si le thème n'a pas encore de carte, remplacer son encadré « Aucune vidéo » par un bloc `<div class="cartes">`. Si la vidéo est une des trois dernières, l'ajouter aussi dans `index.html` et retirer la plus ancienne.
4 bis. Mettre les calculs de la vidéo dans un fichier `donnees/nom-de-la-video.csv` (une ligne par chiffre : valeur, champ, source, lien, statut) et le lier depuis la section « Nos calculs, à télécharger ». Les bases de données d'origine ne sont pas copiées : on met le lien vers l'organisme ou le fichier qu'il publie.
5. Si la vidéo explique une notion nouvelle, ajouter une entrée dans `notions.html` (un titre `h2` avec un `id`, une définition, un exemple, le lien vers la vidéo), et une ligne dans le sommaire en haut de la page.
6. Quand la vidéo est publiée : remplacer le badge « pilote » par « publiée le … » et ajouter les liens TikTok et Instagram.

## Ajouter un thème

Dans `videos/index.html`, copier une section `<section class="theme" id="...">` avec sa question-cadre, puis ajouter le lien `videos/index.html#...` dans le menu déroulant de **toutes** les pages (le bloc `<div class="menu-liste">` est identique partout : un chercher-remplacer suffit).

## Corriger une erreur publiée

Dans la page de la vidéo, section « Corrections », remplacer « Aucune correction » par le tableau (le modèle est en commentaire dans `_modele.html`). Ajouter la même ligne dans `corrections.html`. On ne supprime jamais une page.

## Publier sur GitHub Pages

### La première fois, avec GitHub Desktop (sans terminal)

1. **Un compte GitHub.** Sur github.com, créer un compte gratuit si besoin. Conseillé : créer aussi une **organisation** gratuite au nom du média (icône + en haut à droite, « New organization », offre Free), par exemple `source-media-france`, et y inviter les cofondateurs. Le site appartient alors au média et non à une personne.
2. **GitHub Desktop.** Installer l'application gratuite depuis desktop.github.com, l'ouvrir et se connecter avec son compte GitHub.
3. **Ajouter le site.** Menu File, puis « Add Local Repository… », puis choisir ce dossier `site` (dans Dropbox, dossier `SOURCE?`). L'historique des modifications apparaît.
4. **Publier.** Cliquer sur « Publish repository ». Nom : `source-coulisses`. **Décocher** « Keep this code private » (GitHub Pages gratuit exige un dépôt public). Dans « Organization », choisir l'organisation si elle existe. Valider.
5. **Activer le site.** Sur github.com, ouvrir le dépôt, puis Settings, puis Pages. Dans « Build and deployment » : Source « Deploy from a branch », Branch `main`, dossier `/ (root)`, Save.
6. **Attendre une ou deux minutes.** L'adresse s'affiche en haut de la page Pages, par exemple `https://source-media-france.github.io/source-coulisses/`.

Pour une adresse plus courte, nommer le dépôt exactement `source-media-france.github.io` (le nom de l'organisation suivi de `.github.io`) : le site sera alors à `https://source-media-france.github.io/`.

### Ensuite, à chaque modification

Ouvrir GitHub Desktop : les fichiers modifiés apparaissent à gauche. Écrire un résumé en bas à gauche, cliquer sur « Commit to main », puis sur « Push origin » en haut. Si les modifications ont déjà été validées (par exemple par Claude), seul « Push origin » est à cliquer. Le site se met à jour tout seul en une minute.

### La même chose en ligne de commande

```bash
git remote add origin https://github.com/NOM-DU-COMPTE/source-coulisses.git
git push -u origin main
```

GitHub demande alors un jeton d'accès personnel à la place du mot de passe (Settings, Developer settings, Personal access tokens). Puis, à chaque modification : `git add -A`, `git commit -m "…"`, `git push`.

### Bon à savoir

- Tout ce qui est dans ce dossier devient public, y compris les pages des pilotes et leurs chiffres marqués « à vérifier ». Le fichier `_modele.html` et ce README sont aussi visibles sur GitHub.
- Les liens entre pages sont relatifs : le site fonctionne quel que soit le nom du dépôt ou du domaine.
- Un nom de domaine propre (par exemple `source-media.fr`) pourra être ajouté plus tard dans Settings, Pages, Custom domain, sans rien changer aux pages.

## Ce qui reste à décider ou à compléter

Ces points sont marqués dans les pages par un encadré gris « EN DISCUSSION » ou « À VENIR », ou par un crochet `[à vérifier]`. Les retirer quand c'est tranché.

- **Le cartouche** : discipline seule, ou aussi l'institution (réunion du comité, point 7). Les pages affichent pour l'instant « Hanna Bony · économiste ».
- **La règle de relecture** : un second chercheur quand le sujet le justifie (texte actuel), ou deux pairs extérieurs pour chaque vidéo (point 3). `methode.html`, section 7.
- **Les corrections graduées** : coquille en description, vidéo pour une erreur de fond (point 2). `methode.html` section 10 et `corrections.html`.
- **L'adresse de courriel** de contact. `a-propos.html`, section 8, et `corrections.html`.
- **Les chiffres `[à vérifier]`** des trois pilotes. Les liens vers les sources sont en place (Insee Première n° 2020 d'octobre 2024, communiqué CIRC n° 240 et *Lancet Oncology* 2015, Messerli 2012 *NEJM*). Les salaires moyen et médian ont été vérifiés sur insee.fr le 11 octobre 2026 ; reste le « deux sur trois », le « 18 % par 50 g », le risque de base de cancer colorectal, et le r = 0,79.
- **Une correction dans le script et l'écran de fin de la vidéo 1** : la publication Insee est d'octobre 2024, pas de 2025 (`pilotes.tex` et `make-gabarits.py`).
- **Les noms des relecteurs** des trois pilotes, section « Relecture et validation » de chaque page.
- **Les plateformes** : les pages mentionnent TikTok et Instagram ; ajouter YouTube Shorts, X ou LinkedIn si le comité les retient (point 2).

## La charte graphique dans le site

- Noir `#111111`, jaune surligneur `#FFE500`, papier `#F4F0E6`, gris `#6B6B6B`. Pas de rouge ni de vert, pas de dégradé ni d'ombre.
- Le jaune ne sert qu'aux crochets et au surlignage. Un seul élément surligné par écran.
- Trois voix : **nous** en Source Sans gras ; *ce qui se dit* en Source Serif italique (`class="dit"`) ; `[la source]` en Source Code Pro entre crochets sur jaune (`class="crochet"`).
- Les numéros de section sont des appels de référence : `<span class="num">1</span>`.
- Encadré « principe » : `class="principe"`. Encadré « à décider » : `class="adecider"`.

Tout se change dans `style.css`, en haut, dans le bloc `:root`.
