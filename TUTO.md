# Tuto : modifier le site de SOURCE ?

Ce guide explique, pas à pas, comment corriger, compléter et ajouter des pages au site, sans connaître GitHub ni le code.

- **Le site** : https://source-media-france.github.io/
- **Les fichiers du site** (le « dépôt ») : https://github.com/source-media-france/source-media-france.github.io

Il y a trois façons de modifier le site, de la plus simple à la plus complète :

1. **En ligne, sur github.com.** Rien à installer. Parfait pour corriger un mot, un chiffre, ajouter un lien ou un relecteur. Voir la [partie 1](#1-modifier-une-page-en-ligne).
2. **Depuis son ordinateur, avec GitHub Desktop.** Pour les gros changements, quand on veut voir le résultat avant de publier. Voir la [partie 3](#3-travailler-depuis-son-ordinateur-avec-github-desktop).
3. **Demander à Claude.** Pour tout ce qui touche plusieurs pages à la fois : un nouveau thème dans le menu, une nouvelle vidéo complète avec ses graphiques, un changement de mise en page. Voir la [partie 4](#4-demander-à-claude).

Sommaire :

- [0. Avant de commencer](#0-avant-de-commencer)
- [1. Modifier une page en ligne](#1-modifier-une-page-en-ligne)
- [2. Les recettes](#2-les-recettes)
- [3. Travailler depuis son ordinateur avec GitHub Desktop](#3-travailler-depuis-son-ordinateur-avec-github-desktop)
- [4. Demander à Claude](#4-demander-à-claude)
- [5. Les règles du site](#5-les-règles-du-site)
- [6. Quand quelque chose ne va pas](#6-quand-quelque-chose-ne-va-pas)

---

## 0. Avant de commencer

### Accepter l'invitation (une seule fois)

1. Avoir un compte GitHub (gratuit, sur github.com).
2. Ouvrir l'e-mail « invited you to join the source-media-france organization » et cliquer sur **Join**. Ou bien aller sur https://github.com/source-media-france une fois connecté : l'invitation s'affiche en haut.
3. L'invitation expire au bout de sept jours. Si elle a expiré, demander à Hanna de la renvoyer.

Sans cette étape, on peut lire les fichiers, mais pas les modifier.

### Où est quoi

| Ce que je veux changer | Le fichier |
|---|---|
| La page d'accueil | `index.html` |
| La page d'une vidéo | `videos/nom-de-la-video.html` |
| La liste des vidéos, les thèmes | `videos/index.html` |
| Les notions (moyenne, corrélation…) | `notions.html` |
| La méthode | `methode.html` |
| À propos, cofondateurs, contact | `a-propos.html` |
| La liste des corrections | `corrections.html` |
| Les fichiers de données à télécharger | le dossier `donnees/` |
| Le logo, les images | le dossier `assets/` |
| Les couleurs, les polices | `style.css` (à ne toucher qu'avec Claude) |
| Le modèle d'une nouvelle vidéo | `videos/_modele.html` |

### Le HTML en deux minutes

Chaque page est un fichier `.html`. Le texte y est entouré de **balises**, des mots entre `<` et `>` qui disent à quoi sert le texte. Une balise ouvre, une autre ferme, avec une barre `/` :

```html
<p>Ceci est un paragraphe.</p>
<strong>ceci est en gras</strong>
<a href="https://www.insee.fr">ceci est un lien</a>
```

**La règle d'or : on change le texte entre les balises, on ne touche pas aux balises.** Si on efface un `<` ou un `>` par erreur, la page peut s'afficher de travers. Ce n'est pas grave : voir la [partie 6](#6-quand-quelque-chose-ne-va-pas).

Les balises propres à SOURCE ?, qui appliquent la charte graphique :

| On écrit | Ça donne | Pour |
|---|---|---|
| `<span class="crochet">Insee, 2024</span>` | `[Insee, 2024]` en chasse fixe sur fond jaune | une référence, une source |
| `<span class="crochet">à vérifier</span>` | `[à vérifier]` sur fond jaune | un chiffre pas encore relu à la source |
| `<span class="dit">« … »</span>` | le texte en italique serif | ce qui se dit, une affirmation qu'on examine |
| `<span class="surligne">mot</span>` | le mot surligné en jaune | le seul mot important d'un passage |
| `<span class="cartouche">Prénom Nom · discipline</span>` | `[Prénom Nom · discipline]` sur fond noir | le nom d'un chercheur |
| `<strong>…</strong>` | gras | |
| `<em>…</em>` | italique | un titre de revue ou de rapport |

---

## 1. Modifier une page en ligne

C'est la méthode à utiliser neuf fois sur dix.

1. Aller sur https://github.com/source-media-france/source-media-france.github.io et se connecter.
2. Cliquer sur le fichier à modifier. Pour une vidéo, cliquer d'abord sur le dossier `videos`, puis sur la page.
3. En haut à droite du fichier, cliquer sur l'**icône crayon** (« Edit this file »). Le fichier s'ouvre dans un éditeur.
4. Pour trouver le passage à changer, cliquer dans le texte puis faire **Cmd + F** (Ctrl + F sur PC) et taper quelques mots du passage.
5. Modifier le texte, sans toucher aux balises.
6. Cliquer sur le bouton vert **Commit changes…** en haut à droite.
7. Dans la fenêtre qui s'ouvre, écrire en une ligne ce qu'on a fait, par exemple « Vidéo 1 : ajoute le relecteur ». Laisser coché « Commit directly to the main branch ». Cliquer sur **Commit changes**.
8. Attendre une à deux minutes, puis ouvrir la page sur le site et la recharger avec **Cmd + Maj + R** (Ctrl + Maj + R sur PC) pour voir le changement.

C'est tout : la modification est en ligne. Il n'y a pas de bouton « publier » à part.

> Une modification en ligne est publiée immédiatement. Pour un gros changement qu'on veut d'abord voir, passer par la [partie 3](#3-travailler-depuis-son-ordinateur-avec-github-desktop) ou demander à Claude.

---

## 2. Les recettes

Chaque recette se fait avec la méthode de la [partie 1](#1-modifier-une-page-en-ligne). Les morceaux de code ont un bouton « copier » en haut à droite : copier, coller, puis remplacer ce qui est entre `[[ ]]`.

### 2.1 Corriger un texte ou un chiffre

Ouvrir la page, chercher le passage avec Cmd + F, corriger, valider. Si le chiffre apparaît à plusieurs endroits (le résumé, l'explication, le tableau des données), le corriger partout : faire Cmd + F sur le chiffre lui-même.

Si le chiffre vient d'un fichier de données téléchargeable, le corriger aussi dans le fichier du dossier `donnees/` (même méthode).

### 2.2 Un chiffre est vérifié à la source

Dans la page de la vidéo, section « Les données et les calculs », remplacer la cellule du statut :

```html
<td><span class="crochet">à vérifier</span> : …</td>
```

par :

```html
<td>vérifié sur [[insee.fr]] le [[3 novembre 2026]] par [[Prénom Nom]]</td>
```

Puis retirer le `<span class="crochet">à vérifier</span>` partout ailleurs où il accompagne ce chiffre dans la page (Cmd + F sur « à vérifier »). Si le chiffre était faux, le corriger d'abord (recette 2.1).

### 2.3 Ajouter un lien vers une source ou une base de données

Dans la section « Les sources », chaque source est une ligne `<li>…</li>` dans une liste. Pour en ajouter une, copier ce bloc juste avant le `</ol>` :

```html
<li><strong>[[Nom A., Nom B. et co-auteurs]]</strong>, « [[Titre de l'article]] », <em>[[Nom de la revue ou de l'organisme]]</em>, [[année]]. [[Une phrase : ce que la source apporte.]] [[Accès libre ou payant.]] <a href="[[https://doi.org/…]]">[[doi.org/…]]</a></li>
```

Pour une base de données, même chose dans la liste « Les bases de données utilisées » :

```html
<li><strong>[[Nom de la base]]</strong> ([[organisme]]) : [[ce qu'elle contient]]. <a href="[[lien vers la base ou le fichier]]">[[nom du lien]]</a></li>
```

Pour un article de recherche, le meilleur lien est son **DOI**, une adresse qui ne change jamais : `https://doi.org/` suivi du code de l'article (on le trouve sur la première page de l'article ou sur la page de la revue).

### 2.4 Remplir la relecture

Dans la page de la vidéo, section « Relecture et validation », chaque étape est une ligne. Remplacer :

```html
<tr><td>Relecture scientifique</td><td class="gris">à compléter</td><td class="gris">en cours</td></tr>
```

par :

```html
<tr><td>Relecture scientifique</td><td>[[Prénom Nom · discipline]]</td><td>fait</td></tr>
```

Pour ajouter un second relecteur, copier la ligne entière et la coller juste en dessous.

### 2.5 Ajouter une nouvelle vidéo

C'est la recette la plus longue. Elle a trois étapes : créer la page, l'ajouter à la liste des vidéos, l'ajouter à l'accueil. Si la vidéo a des graphiques, le plus simple est de demander à Claude (partie 4).

**Étape 1 : créer la page.**

1. Ouvrir le fichier `videos/_modele.html`.
2. En haut à droite du fichier, cliquer sur l'icône **Copy raw file** (deux petits carrés). Tout le modèle est copié.
3. Revenir dans le dossier `videos`, cliquer sur **Add file** puis **Create new file**.
4. Dans la case du nom, taper le nom de la page : court, en minuscules, sans accent ni espace, avec des tirets. Par exemple `parachute-preuves.html`.
5. Coller le modèle dans la grande zone (Cmd + V).
6. Remplacer tout ce qui est entre `[[ ]]` : Cmd + F sur `[[` pour les trouver un par un. Le résumé, la légende et les sources viennent du document de script ; la relecture, du tableau de suivi.
7. Supprimer les sections qui ne servent pas, par exemple « Les données et les calculs » s'il n'y a aucun calcul. Une section va de son `<h2>` jusqu'au `<h2>` suivant. Puis renuméroter les sections qui suivent (le chiffre dans `<span class="num">`).
8. Valider avec **Commit changes**.

**Étape 2 : l'ajouter à la liste des vidéos.** Ouvrir `videos/index.html`, trouver la section du thème (Cmd + F sur le nom du thème) et coller cette carte dans le bloc `<div class="cartes">` du thème :

```html
<article class="carte" data-date="[[2026-11-03]]">
  <span class="format">[[LE CHIFFRE]] · [[80 s]] · [[épisode 2]]</span>
  <h3><a href="[[parachute-preuves.html]]">[[Titre de la vidéo]]</a></h3>
  <p class="dit">« [[L'affirmation ou la question de départ]] »</p>
  <p class="avec">Avec <span class="cartouche">[[Prénom Nom · discipline]]</span></p>
</article>
```

- `data-date` est la date de publication, écrite **année-mois-jour**. C'est elle qui range la vidéo dans la vue « Par date ».
- Si le thème n'a encore aucune vidéo, il a un encadré gris « Aucune vidéo publiée pour l'instant ». Remplacer tout le bloc, de `<div class="vide">` jusqu'à son `</div>`, par :

```html
<div class="cartes">
  [[coller la carte ici]]
</div>
```

- Pour une vidéo de la série « Les bases », mettre aussi à jour sa ligne dans le tableau des seize épisodes : mettre le titre en lien et remplacer `<td class="gris">scriptée</td>` par `<td><span class="statut">publiée</span></td>`.

**Étape 3 : l'ajouter à l'accueil.** Ouvrir `index.html`, section « Les dernières vidéos ». Coller la même carte en premier dans le bloc `<div class="cartes">`, en ajoutant `videos/` devant le nom de la page dans le lien (`href="videos/parachute-preuves.html"`). Puis supprimer la dernière carte, pour qu'il en reste trois.

### 2.6 Une vidéo pilote est publiée sur les réseaux

Dans la page de la vidéo, remplacer le badge et l'encadré « VIDÉO PILOTE », c'est-à-dire tout ce qui va de `<p><span class="statut">pilote</span></p>` jusqu'au `</div>` de l'encadré, par :

```html
<p><span class="statut">publiée le [[3 novembre 2026]]</span></p>

<p>Voir la vidéo : <a href="[[lien TikTok]]">TikTok</a> · <a href="[[lien Instagram]]">Instagram</a></p>
```

Puis, dans `videos/index.html` et dans `index.html` : retirer « · pilote » de la ligne de format de la carte, et mettre la vraie date de publication dans `data-date`.

### 2.7 Ajouter un fichier de données à télécharger

1. Préparer le fichier en CSV (dans Excel : Fichier, Enregistrer sous, format « CSV UTF-8 »). Une ligne par chiffre, avec sa valeur, son champ, sa source, son lien et son statut. Nommer le fichier comme la vidéo : `parachute-preuves.csv`.
2. Sur GitHub, ouvrir le dossier `donnees`, cliquer sur **Add file** puis **Upload files**, glisser le fichier, puis **Commit changes**.
3. Dans la page de la vidéo, section « Nos calculs, à télécharger », ajouter la ligne :

```html
<li><a href="../donnees/[[parachute-preuves.csv]]" download>[[parachute-preuves.csv]]</a> : [[ce que contient le fichier]].</li>
```

Les bases de données des organismes (Insee, Santé publique France…) ne se copient pas dans le dossier : on met un lien vers leur site (recette 2.3).

### 2.8 Ajouter une image

1. Sur GitHub, ouvrir le dossier `assets`, **Add file**, **Upload files**, glisser l'image (PNG ou JPG, moins de 1 Mo, nom sans accent ni espace), **Commit changes**.
2. Dans la page, à l'endroit voulu (par exemple dans « L'explication, en images ») :

```html
<figure class="figure">
  <img src="../assets/[[mon-image.png]]" alt="[[Ce que montre l'image, en une phrase, pour les personnes aveugles]]">
  <figcaption>[[Ce que montre l'image.]]<span class="src">[[[Auteur, année]]]</span></figcaption>
</figure>
```

Depuis une page qui n'est pas dans `videos/` (l'accueil, les notions…), écrire `assets/…` au lieu de `../assets/…`.

Les graphiques des pilotes (barres, grille de cent personnes, schémas à flèches) sont dessinés en code dans la page. Pour en faire un nouveau, demander à Claude.

### 2.9 Ajouter une notion

Dans `notions.html` :

1. Dans le sommaire en haut de la page (le bloc `<div class="sommaire">`), ajouter une ligne :

```html
<li><a href="#[[mot-cle]]">[[Nom de la notion]]</a></li>
```

2. Avant le `</div></main>` de la fin de la page, coller :

```html
<h2 id="[[mot-cle]]"><span class="num">[[9]]</span>[[Nom de la notion]]</h2>

<p><strong>[[La notion]]</strong>, c'est [[la définition, en mots courants]].</p>

<p><strong>L'exemple.</strong> [[Un exemple concret.]]</p>

<p class="meta">Vidéo : <a href="videos/[[nom-de-la-video.html]]">[[Titre de la vidéo]]</a></p>
```

`mot-cle` est le même aux deux endroits, en minuscules, sans accent, avec des tirets. Le numéro suit celui de la dernière notion.

### 2.10 Signaler une correction

Dans la page de la vidéo, section « Corrections », remplacer la phrase « Aucune correction pour l'instant… » par :

```html
<div class="table-scroll"><table>
  <tr><th>Date</th><th>Ce qui était faux</th><th>Ce qui est juste</th><th>Correction</th></tr>
  <tr><td class="mono">[[03/11/2026]]</td><td>[[…]]</td><td>[[…]]</td><td>[[description modifiée · commentaire épinglé · vidéo de correction, avec lien]]</td></tr>
</table></div>
```

Puis, dans `corrections.html`, remplacer la ligne « Aucune correction pour l'instant » par :

```html
<tr><td class="mono">[[03/11/2026]]</td><td><a href="videos/[[nom-de-la-video.html]]">[[Titre]]</a></td><td>[[…]]</td><td>[[…]]</td><td>[[…]]</td></tr>
```

Pour les corrections suivantes, ajouter une ligne en haut du tableau. **On ne supprime jamais une page ni une correction.**

### 2.11 Ce qu'il vaut mieux demander à Claude

- **Ajouter ou renommer un thème.** Le menu « Vidéos » est recopié dans les dix pages du site : il faut le changer partout à la fois.
- **Un nouveau graphique** dessiné aux couleurs de la charte.
- **Une nouvelle vidéo complète**, à partir du script : Claude rédige la page, le résumé, l'explication en images, cherche les liens des sources, et prépare le fichier de données.
- **Changer la mise en page, les couleurs, le menu.**

---

## 3. Travailler depuis son ordinateur avec GitHub Desktop

Utile pour voir le résultat avant de publier, ou pour modifier plusieurs fichiers d'un coup.

### La première fois

1. Installer **GitHub Desktop** (desktop.github.com) et se connecter avec son compte GitHub.
2. Installer un éditeur de texte fait pour le code, par exemple **Visual Studio Code** (gratuit, code.visualstudio.com). **Ne pas utiliser TextEdit ni Word** : ils abîment les fichiers HTML.
3. Récupérer le site sur son ordinateur :
   - **Hanna** : c'est déjà fait, le site est le dossier `site` dans Dropbox, dossier `SOURCE?`.
   - **Les autres** : dans GitHub Desktop, menu **File**, **Clone Repository…**, choisir `source-media-france.github.io`, choisir un dossier dans **Documents** (pas dans un dossier Dropbox partagé), puis **Clone**.

### À chaque fois

1. Ouvrir GitHub Desktop. Cliquer sur **Fetch origin** en haut, puis sur **Pull origin** s'il apparaît. On récupère ainsi les modifications des autres. **Ne jamais sauter cette étape.**
2. Cliquer sur **Open in Visual Studio Code** (ou ouvrir le fichier dans son éditeur). Modifier, enregistrer (Cmd + S).
3. Pour voir le résultat : double-cliquer sur le fichier `.html` dans le Finder. Il s'ouvre dans le navigateur, sur son ordinateur seulement. Recharger après chaque enregistrement.
4. Quand c'est bon, revenir dans GitHub Desktop. Les fichiers modifiés sont listés à gauche. En bas à gauche, écrire un résumé (par exemple « Ajoute la vidéo sur le parachute »), puis cliquer sur **Commit to main**.
5. Cliquer sur **Push origin** en haut. Le site est en ligne une à deux minutes plus tard.

---

## 4. Demander à Claude

Claude peut lire les scripts, les chartes et les documents du dossier SOURCE?, modifier le site, et vérifier que tout s'affiche. Il suffit de lui dire ce qu'on veut, en français, par exemple :

- « Ajoute la page de l'épisode 2 des Bases, sur le parachute, à partir du script. »
- « Le chiffre de 0,79 dans la vidéo sur la corrélation est vérifié. Mets-le à jour. »
- « Ajoute un thème Climat dans le menu. »

Claude enregistre les modifications dans le dossier du site. **Il faut ensuite ouvrir GitHub Desktop et cliquer sur Push origin** pour les mettre en ligne. Avant de demander quelque chose à Claude, faire **Fetch origin** puis **Pull origin**, pour qu'il parte de la dernière version.

---

## 5. Les règles du site

- **Tout est public.** Le site et tous ses fichiers, y compris ce tuto, sont visibles par n'importe qui. Ne jamais y mettre d'adresse personnelle, de numéro de téléphone, de document interne ou de données sur des personnes.
- **La charte graphique.** Le jaune ne sert qu'aux crochets et à un seul mot surligné par passage. Pas de rouge ni de vert, pas de « VRAI » ni de « FAUX ».
- **Les noms de fichiers** : en minuscules, sans accent, sans espace, avec des tirets. `parachute-preuves.html`, pas `Parachute preuves.html`.
- **On ne supprime jamais** une page de vidéo ni une correction. Une erreur se corrige et se signale (recette 2.10).
- **Les cofondateurs** sont toujours cités par ordre alphabétique : Hanna Bony, Marine de Talancé, Marin Ferry, Andrea Rouchon.
- **Les chiffres** : tant qu'un chiffre n'a pas été relu à la source, il garde son `[à vérifier]`.
- **Les sources** : un lien vers le document d'origine (l'article, le rapport, la base), pas vers l'article de presse qui en parle.

---

## 6. Quand quelque chose ne va pas

**Le changement n'apparaît pas sur le site.**
Attendre deux minutes, puis recharger avec Cmd + Maj + R. Si rien ne change, ouvrir l'onglet **Actions** du dépôt sur GitHub : la dernière ligne doit avoir une coche verte. Un rond orange veut dire « en cours », une croix rouge « échec » : dans ce cas, prévenir Hanna ou demander à Claude.

**La page s'affiche de travers après une modification.**
Une balise a sans doute été effacée. Pour revenir en arrière :
- **en ligne** : ouvrir le fichier, cliquer sur **History** en haut à droite, repérer la version d'avant, cliquer sur les trois points `…` puis **View file**, copier tout son contenu (icône **Copy raw file**), puis modifier le fichier actuel (crayon), tout sélectionner (Cmd + A), coller, et valider ;
- **dans GitHub Desktop** : onglet **History** à gauche, clic droit sur la modification fautive, **Revert changes in commit**, puis **Push origin**.

**GitHub Desktop parle de « conflict ».**
Deux personnes ont modifié le même passage en même temps. Ne rien forcer : prévenir Hanna ou demander à Claude, qui sait les résoudre.

**Je ne vois pas l'icône crayon.**
On n'est pas connecté, ou l'invitation à l'organisation n'a pas été acceptée (partie 0).
