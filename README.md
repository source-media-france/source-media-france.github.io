# SOURCE ? — le site de coulisses

Le site public qui complète les vidéos de SOURCE ? : pour chaque vidéo, la transcription, les sources complètes, ce qu'elle montre et ne montre pas, les données et les calculs des graphiques, les noms des relecteurs, les corrections. Plus une page « Notions », la méthode, et qui nous sommes.

C'est le « site de coulisses » décidé lors de la première réunion du comité (point 3 de l'ordre du jour, option C : transcription, sources, relecteurs, données et code, onglet notions).

## Ce qu'il y a dedans

```
index.html            Accueil : ce qu'est SOURCE ?, les dernières vidéos, les trois questions
videos/index.html     Toutes les vidéos, et la série « Les bases »
videos/*.html         Une page par vidéo (trois pilotes pour l'instant)
videos/_modele.html   Le gabarit à copier pour une nouvelle vidéo
notions.html          Les mots qu'on emploie, expliqués une fois
methode.html          Comment une vidéo est fabriquée, qui vérifie quoi
a-propos.html         Mission, engagements, comité, indépendance, contribuer, contact
corrections.html      Toutes les corrections publiées, et comment signaler une erreur
style.css             La charte graphique en CSS : couleurs, trois polices, crochets
assets/logo/          Le logo (trois versions)
assets/ecrans/        Les écrans des vidéos (copiés depuis SOURCE/gabarits/)
```

Aucun outil à installer, aucune étape de construction : ce sont des pages HTML écrites à la main, qui se modifient dans n'importe quel éditeur de texte, ou directement sur GitHub (icône crayon sur un fichier). Les polices (Source Sans 3, Source Serif 4, Source Code Pro) sont chargées depuis Google Fonts.

## Ajouter une vidéo

1. Copier `videos/_modele.html` sous un nom court, en minuscules, sans accent ni espace : `videos/mon-sujet.html`.
2. Remplacer tout ce qui est entre `[[ ]]`. La transcription vient de la colonne « Voix » du script ; les sources, du document de script ; la relecture, du tableau de suivi.
3. Copier les écrans de la vidéo dans `assets/ecrans/mon-sujet/` (depuis `SOURCE/gabarits/`), ou supprimer la section « Les écrans ».
4. Ajouter une carte dans `videos/index.html` (copier-coller une carte existante). Si la vidéo est une des trois dernières, l'ajouter aussi dans `index.html` et retirer la plus ancienne.
5. Si la vidéo explique une notion nouvelle, ajouter une entrée dans `notions.html` (un titre `h2` avec un `id`, une définition, un exemple, le lien vers la vidéo), et une ligne dans le sommaire en haut de la page.
6. Quand la vidéo est publiée : remplacer le badge « pilote » par « publiée le … » et ajouter les liens TikTok et Instagram.

## Corriger une erreur publiée

Dans la page de la vidéo, section « Corrections », remplacer « Aucune correction » par le tableau (le modèle est en commentaire dans `_modele.html`). Ajouter la même ligne dans `corrections.html`. On ne supprime jamais une page.

## Publier sur GitHub Pages

Une seule fois :

1. Créer un dépôt sur github.com (par exemple `source-coulisses`), public, vide (sans README).
2. Dans ce dossier, envoyer le site :

   ```bash
   git remote add origin https://github.com/VOTRE-COMPTE/source-coulisses.git
   git push -u origin main
   ```

3. Sur GitHub : Settings → Pages → Build and deployment → Source : « Deploy from a branch » → Branch : `main`, dossier `/ (root)` → Save.
4. Après une ou deux minutes, le site est en ligne à `https://VOTRE-COMPTE.github.io/source-coulisses/`.

Ensuite, à chaque modification :

```bash
git add -A
git commit -m "Ajoute la vidéo sur les sondages"
git push
```

Le site se met à jour tout seul en une minute. Les liens entre pages sont relatifs : le site fonctionne quel que soit le nom du dépôt ou du domaine.

Un nom de domaine propre (par exemple `source-media.fr`) pourra être ajouté plus tard dans Settings → Pages → Custom domain, sans rien changer aux pages.

## Ce qui reste à décider ou à compléter

Ces points sont marqués dans les pages par un encadré gris « EN DISCUSSION » ou « À VENIR », ou par un crochet `[à vérifier]`. Les retirer quand c'est tranché.

- **Le cartouche** : discipline seule, ou aussi l'institution (réunion du comité, point 7). Les pages affichent pour l'instant « Hanna Bony · économiste ».
- **La règle de relecture** : un second chercheur quand le sujet le justifie (texte actuel), ou deux pairs extérieurs pour chaque vidéo (point 3). `methode.html`, section 7.
- **Les corrections graduées** : coquille en description, vidéo pour une erreur de fond (point 2). `methode.html` section 10 et `corrections.html`.
- **L'adresse de courriel** de contact. `a-propos.html`, section 8, et `corrections.html`.
- **Les chiffres `[à vérifier]`** des trois pilotes, et les liens vers les sources (Insee Première 2025, CIRC 2015 et *Lancet Oncology* 2015, Messerli 2012 *NEJM*), à compléter dans chaque page de vidéo une fois ouverts à la source.
- **Les noms des relecteurs** des trois pilotes, section « Relecture et validation » de chaque page.
- **Les plateformes** : les pages mentionnent TikTok et Instagram ; ajouter YouTube Shorts, X ou LinkedIn si le comité les retient (point 2).

## La charte graphique dans le site

- Noir `#111111`, jaune surligneur `#FFE500`, papier `#F4F0E6`, gris `#6B6B6B`. Pas de rouge ni de vert, pas de dégradé ni d'ombre.
- Le jaune ne sert qu'aux crochets et au surlignage. Un seul élément surligné par écran.
- Trois voix : **nous** en Source Sans gras ; *ce qui se dit* en Source Serif italique (`class="dit"`) ; `[la source]` en Source Code Pro entre crochets sur jaune (`class="crochet"`).
- Les numéros de section sont des appels de référence : `<span class="num">1</span>`.
- Encadré « principe » : `class="principe"`. Encadré « à décider » : `class="adecider"`.

Tout se change dans `style.css`, en haut, dans le bloc `:root`.
