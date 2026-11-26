# Refonte du 25 novembre 2026 : menus, calendrier, pages par thème, À propos en plusieurs pages,
# contribuer (formulaire), contact. Lancer depuis site/ : python3 -I refonte.py
import os, re, glob

SITE = os.getcwd()
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Source+Code+Pro:wght@400;700&family=Source+Sans+3:wght@400;700&family=Source+Serif+4:ital@1&display=swap" rel="stylesheet">')

EMAIL = "source.media.france@gmail.com"
INSTA = "https://www.instagram.com/source.media.france/"
TIKTOK = "https://www.tiktok.com/@source.media.france"
LINKEDIN = "https://www.linkedin.com/company/source-media-france/"

UGE = "Université Gustave Eiffel"
PERS = {
    "HB": ("Hanna Bony", "Doctorante en économie", UGE),
    "MC": ("Melchior Clerc", "Doctorant", "CERDI, Université Clermont Auvergne"),
    "MT": ("Marine de Talancé", "Enseignante-chercheuse en économie", UGE),
    "MF": ("Marin Ferry", "Enseignant-chercheur en économie", UGE),
    "AR": ("Andrea Rouchon", "Doctorant en économie", UGE),
}
def cartouche(k):
    nom, titre, etab = PERS[k]
    return f'<span class="cartouche">{nom} · {titre} · {etab}</span>'

# ------------------------------------------------------------------ thèmes et vidéos
THEMES = [
    ("le-media", "Le média", "Qui sommes-nous, et comment on travaille ?", "Les vidéos qui expliquent notre méthode : d'où viennent les chiffres, pourquoi on ne dit jamais « vrai » ou « faux », ce qu'on fait quand on se trompe."),
    ("comprendre-les-chiffres", "Comprendre les chiffres", "Comment lire un chiffre ou une étude sans se faire avoir ?", "Une série de fond, sans lien avec l'actualité : une confusion par vidéo. Les autres séries y renvoient au lieu de tout réexpliquer."),
    ("immigration", "Immigration", "Que peut-on affirmer avec certitude sur l'immigration en France ?", "Une série de Marine de Talancé. On commence par les mots : sans les définitions, aucun chiffre ne se comprend."),
    ("dette-publique", "Dette publique", "La dette publique est-elle un vrai problème, et pour qui ?", "Une série de Marin Ferry : ce qu'est la dette, pourquoi elle augmente, puis s'il faut s'en inquiéter."),
    ("corruption", "Corruption", "Comment définir, mesurer et combattre la corruption ?", "Une série d'Andrea Rouchon en trois épisodes : la définition, la mesure, la lutte. Les titres sont provisoires."),
    ("education", "Éducation", "Parmi les mesures dont on parle à l'école, lesquelles ont fait leurs preuves ?", "Ce que la recherche a mesuré sur l'école, mesure par mesure."),
    ("violences", "Violences sexistes et sexuelles", "Que sait-on de ce qui réduit les violences conjugales ?", "Un sujet sensible : chaque vidéo est relue par le comité, et le numéro d'écoute 3919 est à l'écran."),
]
TH = {k: (n, q, d) for k, n, q, d in THEMES}

# statut : "date" (sortie prévue à une date), "pilote" (tourné, non publié), "prevue" (date à fixer)
V = [
 dict(t="Présentation du média", th="le-media", date="2026-12-01", page="presentation-du-media.html", a="HB", duree="45 s",
      x="Qui nous sommes et comment on travaille : partir d'un chiffre qui circule, lire ce que la recherche en dit, et le raconter en une minute, la source à l'écran."),
 dict(t="Immigré ou étranger : est-ce la même chose ?", th="immigration", ep=1, date="2026-12-01", page="immigre-ou-etranger.html", a="MT",
      x="La différence entre immigré et étranger, selon l'Insee : on reste immigré toute sa vie, on cesse d'être étranger en devenant français."),
 dict(t="La dette publique, c'est quoi ?", th="dette-publique", ep=1, date="2026-12-01", page="dette-publique-c-est-quoi.html", a="MF",
      x="Qui emprunte quand on parle de dette publique, et comment un déficit se transforme en dette."),
 dict(t="Corruption, épisode 1 : la définition", th="corruption", ep=1, date="2026-12-01", a="AR",
      x="Ce qu'on appelle corruption, et ce qui n'en est pas. Page en préparation."),
 dict(t="Moins d'élèves par classe, ça marche ?", th="education", date="2026-12-01", page="taille-des-classes.html", a="HB", duree="70 s",
      x="Ce qu'ont montré deux expériences, au Tennessee et dans les CP dédoublés en France, et ce qu'on ne sait pas encore pour le lycée."),
 dict(t="Le Français « moyen » existe-t-il ?", th="comprendre-les-chiffres", date="2026-12-06", page="moyenne-mediane.html", a="HB", duree="45 s",
      x="Pourquoi le salaire moyen n'est pas le salaire du milieu, avec les chiffres 2025 de l'Insee : la moyenne et la médiane."),
 dict(t="Migrant ou réfugié : est-ce la même chose ?", th="immigration", ep=2, date="2026-12-07", page="migrant-ou-refugie.html", a="MT",
      x="Pourquoi « migrant » est un mot large et « réfugié » un statut précis, défini par la Convention de Genève de 1951."),
 dict(t="Pourquoi la dette publique augmente-t-elle ?", th="dette-publique", ep=2, date="2026-12-09", page="dette-publique-pourquoi-elle-augmente.html", a="MF",
      x="La différence entre le déficit et la dette, et pourquoi la dette monte tant que le déficit dépasse ce qui est remboursé : l'image de la baignoire."),
 dict(t="Corruption, épisode 2 : la mesure", th="corruption", ep=2, date="2026-12-11", a="AR",
      x="Comment mesure-t-on quelque chose de caché ? Page en préparation."),
 dict(t="Les dépenses d'éducation en France", th="education", date="2026-12-14", a="MT",
      x="Combien la France dépense pour l'école, et ce que la recherche en dit. Page en préparation."),
 # pilotes
 # date à fixer
 dict(t="Un million, un milliard", th="comprendre-les-chiffres", a="HB", x="Comment comprendre un chiffre en milliards : le diviser par le nombre d'habitants."),
 dict(t="Ce graphique dit-il la vérité ?", th="comprendre-les-chiffres", a="HB", x="Pourquoi il faut regarder d'où part l'échelle d'un graphique avant de regarder les barres."),
 dict(t="Pourquoi on ne dit jamais « vrai » ou « faux »", th="le-media", a="HB", x="Pourquoi un même chiffre peut donner deux titres vrais, et nos quatre réponses possibles."),
 dict(t="Pourquoi on ne nomme jamais personne", th="le-media", a="HB", x="Pourquoi on répond à la phrase, pas à la personne qui l'a dite."),
 dict(t="C'est quoi, une source ?", th="le-media", a="HB", x="Ce qui est une source et ce qui n'en est pas : une source, c'est ce que vous pouvez lire vous-mêmes."),
 dict(t="Et si on se trompe ?", th="le-media", a="HB", x="Ce qu'on fait quand on se trompe : on corrige en public, jamais en silence."),
 dict(t="Combien y a-t-il d'immigrés en France ?", th="immigration", ep=3, a="MT", x="Pourquoi on entend des chiffres si différents : ça dépend de qui compte, et comment."),
 dict(t="Faut-il s'inquiéter de la dette ?", th="dette-publique", ep=3, a="MF", x="Pourquoi tout dépend de la taille de la dette par rapport à l'économie. Titre provisoire."),
 dict(t="Corruption, épisode 3 : la lutte", th="corruption", ep=3, a="AR", x="Ce qui marche contre la corruption. Titre provisoire."),
 dict(t="285 000 victimes : les violences augmentent-elles ?", th="violences", a="HB", x="Ce que compte le chiffre des violences conjugales enregistrées, et pourquoi il ne suffit pas à dire si les violences augmentent."),
 dict(t="Tribunaux spécialisés : ce que l'Espagne a vu", th="violences", a="HB", x="Ce qu'ont changé, en Espagne, les tribunaux spécialisés dans les violences conjugales : plus de plaintes, jugées plus vite, pas moins d'homicides."),
 dict(t="Le loyer protège-t-il des violences conjugales ?", th="violences", a="HB", x="Ce qu'une étude sur San Francisco a trouvé : pouvoir payer un logement, c'est pouvoir partir."),
]

JOURS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
def date_long(iso, jour=True):
    import datetime
    d = datetime.date.fromisoformat(iso)
    n = "1<sup>er</sup>" if d.day == 1 else str(d.day)
    return (JOURS[d.weekday()] + " " if jour else "") + f"{n} {MOIS[d.month-1]}"

def carte(v, prefix="", montrer_theme=False, montrer_date=True):
    bits = []
    if montrer_theme: bits.append(TH[v["th"]][0])
    if v.get("ep"): bits.append(f"épisode {v['ep']}")
    if v.get("date"):
        if montrer_date: bits.append("sortie le " + date_long(v["date"]))
    else: bits.append("bientôt")
    h3 = f'<h3><a href="{prefix}{v["page"]}">{v["t"]}</a></h3>' if v.get("page") else f'<h3>{v["t"]}</h3>'
    p = f'<p>{v["x"]}</p>' if v.get("page") else f'<p class="gris">{v["x"]}</p>'
    if v.get("a"):
        nom, titre, etab = PERS[v["a"]]
        sous = f'<span class="qui-titre">{titre} · {etab}</span>'
        avec = f'\n      <p class="avec">Avec <strong>{nom}</strong>{sous}</p>'
    else:
        avec = ""
    return f'''    <article class="carte{'' if v.get('page') else ' a-venir'}">
      <span class="format">{" · ".join(bits)}</span>
      {h3}
      {p}{avec}
    </article>'''

def cartes(vs, prefix="", montrer_theme=False, montrer_date=True):
    return '  <div class="cartes">\n' + "\n".join(carte(v, prefix, montrer_theme, montrer_date) for v in vs) + '\n  </div>'

# ------------------------------------------------------------------ gabarit commun
def nav(p, cur):
    th = "\n".join(f'        <a href="{p}videos/{k}.html">{n}</a>' for k, n, _, _ in THEMES)
    c = lambda key: ' aria-current="page"' if cur == key else ''
    return f'''<nav class="nav" aria-label="Navigation">
    <details class="menu">
      <summary{c("videos")}>Vidéos</summary>
      <div class="menu-liste">
        <a href="{p}videos/calendrier.html">Le calendrier des sorties</a>
        <a href="{p}videos/index.html">Toutes les séries</a>
        <span class="menu-titre">Par thème</span>
{th}
      </div>
    </details>
    <a href="{p}notions.html"{c("notions")}>Notions</a>
    <a href="{p}methode.html"{c("methode")}>Méthode</a>
    <details class="menu menu-droite">
      <summary{c("apropos")}>À propos</summary>
      <div class="menu-liste">
        <a href="{p}a-propos.html">Notre mission</a>
        <a href="{p}equipe.html">Qui sommes-nous ?</a>
        <a href="{p}contribuer.html">Contribuer</a>
        <a href="{p}contact.html">Contact</a>
      </div>
    </details>
    <a href="{p}contribuer.html" class="nav-contribuer"{c("contribuer")}>Contribuer</a>
  </nav>'''

def footer(p):
    return f'''<footer class="pied"><div class="wrap">
  <p class="signature"><span class="surligne">T'as la source ? On va la chercher.</span></p>
  <p>SOURCE ? est un collectif de chercheurs. Toutes les contributions sont bénévoles ; le média n'a ni financement ni partenaire.</p>
  <p class="reseaux"><a href="{INSTA}">Instagram</a> · <a href="{TIKTOK}">TikTok</a> · <a href="{LINKEDIN}">LinkedIn</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
  <p>Une erreur dans une vidéo ? <a href="{p}corrections.html">Signalez-la</a>. Vous êtes chercheur ou chercheuse ? <a href="{p}contribuer.html">Proposez un script</a>.</p>
  <p class="meta">Site de coulisses de SOURCE ? · <a href="{p}contact.html">contact</a></p>
</div></footer>'''

def doc(fname, titre, desc, sur, h1, sous, main, cur, sous_voix="nous"):
    p = "../" if fname.startswith("videos/") else ""
    sous_html = f'<p class="sous">{sous}</p>' if sous_voix == "dit" else f'<p class="explique">{sous}</p>'
    html = f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titre}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{p}assets/logo/logo-jaune.png">
{FONTS}
<link rel="stylesheet" href="{p}style.css?v=20261128">
</head>
<body>
<a class="saut" href="#contenu">Aller au contenu</a>
<header class="entete"><div class="wrap">
  <a class="logo" href="{p}index.html"><span class="c">[</span>SOURCE<span class="q">?</span><span class="c">]</span></a>
  {nav(p, cur)}
</div></header>

<section class="titre"><div class="wrap">
  <p class="sur">{sur}</p>
  <h1>{h1}</h1>
  {sous_html}
</div></section>

<main id="contenu" class="contenu"><div class="wrap">

{main}

</div></main>

{footer(p)}
<script src="{p}site.js?v=20261128"></script>
</body>
</html>
'''
    open(os.path.join(SITE, fname), "w", encoding="utf-8").write(html)
    print("ok", fname)

def num(i, t, ident=None):
    idattr = f' id="{ident}"' if ident else ''
    return f'<h2{idattr}><span class="num">{i}</span>{t}</h2>'

# ------------------------------------------------------------------ 1. Calendrier
dates = sorted({v["date"] for v in V if v.get("date")})
blocs = []
for d in dates:
    vs = [v for v in V if v.get("date") == d]
    blocs.append(f'  <h3 class="jour">{date_long(d).capitalize()}</h3>\n' + cartes(vs, montrer_theme=True, montrer_date=False))
main = f'''  <p>Les dates de sortie des vidéos, de la plus proche à la plus lointaine. Chaque vidéo a sa page, avec ses sources et ses données, dès sa sortie.</p>

  {num(1, "Décembre 2026")}

{chr(10).join(blocs)}

  {num(2, "Bientôt")}

  <p>Ces vidéos sont écrites ou tournées. Leur date de sortie sera ajoutée ici.</p>

{cartes([v for v in V if not v.get("date") and not v.get("pilote")], montrer_theme=True)}
'''
doc("videos/calendrier.html", "Le calendrier des sorties · SOURCE ?",
    "Les dates de sortie des vidéos SOURCE ? à partir du 1er décembre 2026, et les vidéos prévues.",
    "vidéos", "Le calendrier des sorties", "Lancement le mardi 1<sup>er</sup> décembre 2026 : cinq vidéos le premier jour, puis de nouvelles vidéos chaque semaine.", main, "videos")

# ------------------------------------------------------------------ 2. Une page par thème
def ordre(v):
    groupe = 0 if (v.get("page") and v.get("date")) else 1 if v.get("pilote") else 2 if v.get("date") else 3
    return (groupe, v.get("ep") or 99, v.get("date") or "9999")
for k, n, q, d in THEMES:
    vs = sorted([v for v in V if v["th"] == k], key=ordre)
    autres = " · ".join(f'<a href="{kk}.html">{nn}</a>' for kk, nn, _, _ in THEMES if kk != k)
    main = f'''  <p>{d}</p>

{cartes(vs)}

  <p class="meta">Les autres séries : {autres}</p>'''
    doc(f"videos/{k}.html", f"{n} · SOURCE ?", f"{q} Les vidéos SOURCE ? sur ce thème, avec leurs sources et leurs données.",
        "série", n, q, main, "videos")

# ------------------------------------------------------------------ 3. Toutes les séries
tuiles = []
for k, n, q, d in THEMES:
    vs = [v for v in V if v["th"] == k]
    prochaines = sorted(v["date"] for v in vs if v.get("date"))
    info = f"{len(vs)} vidéo{'s' if len(vs) > 1 else ''}"
    if prochaines: info += " · première sortie le " + date_long(prochaines[0], jour=False)
    tuiles.append(f'''    <a class="serie" href="{k}.html">
      <span class="format">{info}</span>
      <h3>{n}</h3>
      <p>{q}</p>
    </a>''')
main = f'''  <p>Chaque série prend un thème et le découpe en vidéos d'une minute, qui se comprennent chacune seule. Pour voir les vidéos dans l'ordre de leur sortie, ouvrez <a href="calendrier.html">le calendrier</a>.</p>

  <div class="series">
{chr(10).join(tuiles)}
  </div>'''
doc("videos/index.html", "Les séries · SOURCE ?", "Les séries de vidéos SOURCE ?, par thème : le média, comprendre les chiffres, immigration, dette publique, corruption, éducation, violences.",
    "vidéos", "Les séries", "Une série par thème. Chaque vidéo a sa page, avec un résumé, l'explication en images, les sources et les données.", main, "videos")

# ------------------------------------------------------------------ 4. Notre mission (À propos)
main = f'''  <div class="sommaire"><ul>
    <li><a href="#mission">Notre mission</a></li>
    <li><a href="#pas">Ce que SOURCE ? n'est pas</a></li>
    <li><a href="#engagements">Nos engagements</a></li>
    <li><a href="#independance">Indépendance</a></li>
  </ul></div>

  {num(1, "Notre mission", "mission")}

  <p>SOURCE ? utilise la recherche scientifique pour aider à comprendre les sujets qui circulent dans la société et sur Internet.</p>

  <p>Nous partons d'une question, d'une affirmation, d'une donnée, d'une actualité ou d'un contenu qui interpelle le public, puis nous cherchons ce que les travaux scientifiques permettent réellement d'en dire.</p>

  <p>Nous nous adressons d'abord aux 18-30 ans, et plus largement à toute personne qui s'informe sur les réseaux sociaux. <strong>Personne n'est censé connaître le sujet avant de regarder la vidéo.</strong> Nous simplifions l'explication, pas la science.</p>

  <div class="principe"><p>Tout peut devenir un sujet.<br>La recherche est notre méthode.<br>La vulgarisation est notre responsabilité.</p></div>

  {num(2, "Ce que SOURCE ? n'est pas", "pas")}

  <ul>
    <li><strong>Pas un média politique ni militant.</strong> Nous pouvons traiter de politique ou de politiques publiques quand la recherche permet d'éclairer le sujet. Nous ne soutenons ni parti ni candidat.</li>
    <li><strong>Pas un distributeur de verdicts.</strong> Nous ne répondons pas « vrai » ou « faux ». La conclusion peut être : confirmé, démonté, plus compliqué, ou « on ne sait pas ».</li>
    <li><strong>Pas un compte qui démonte les gens.</strong> Un contenu ou un commentaire est une porte d'entrée vers le sujet, pas une cible. Nous répondons à la phrase, pas à la personne.</li>
    <li><strong>Pas un média d'économie.</strong> Le comité compte surtout des économistes, mais la question détermine l'expertise nécessaire : nous mobilisons les disciplines pertinentes et nous faisons relire par elles.</li>
  </ul>

  {num(3, "Nos engagements", "engagements")}

  <ul>
    <li>Citer nos sources, à l'écran et sur ce site.</li>
    <li>Corriger nos erreurs, publiquement : voir <a href="corrections.html">les corrections</a>.</li>
    <li>Signaler les incertitudes importantes.</li>
    <li>Ne pas exagérer les résultats scientifiques, et choisir nos mots selon le degré de certitude.</li>
    <li>Ne pas fabriquer artificiellement une controverse.</li>
    <li>Respecter les chercheurs et les populations concernées.</li>
    <li>Privilégier la compréhension au sensationnel : l'accroche peut être accrocheuse, jamais trompeuse.</li>
  </ul>

  <p>Chaque vidéo distingue le résultat de son interprétation, la corrélation de la causalité, une étude isolée de l'ensemble de la recherche, et l'opinion du chercheur du résultat scientifique. Le détail est dans <a href="methode.html">notre méthode</a>.</p>

  {num(4, "Indépendance", "independance")}

  <p>SOURCE ? est un collectif de chercheurs, qui a vocation à devenir une association loi 1901. Il n'a ni financement ni partenaire, et toutes les contributions sont bénévoles. Si un financement se présente un jour, nous dirons publiquement de qui il vient et à quoi il sert.</p>

  <p>Les chercheurs parlent en leur nom, pas au nom de leur institution. Les prises de position n'engagent que leur auteur.</p>

  <p><strong>Intelligence artificielle.</strong> Les scripts sont écrits par des humains. L'intelligence artificielle peut servir au montage (sous-titres, découpe, son), jamais à l'écriture.</p>'''
doc("a-propos.html", "Notre mission · SOURCE ?", "La mission de SOURCE ?, ce que le média n'est pas, ses engagements et son indépendance.",
    "à propos", "Notre mission", "Un média fait par des chercheurs, pour comprendre ce qui circule.", main, "apropos")

# ------------------------------------------------------------------ 5. Qui sommes-nous ?
LIENS = {
    "HB": [("Site", "https://hannabony.com/"), ("LinkedIn", "https://www.linkedin.com/in/hannabony/")],
    "MC": [("Site", "https://melchiorclerc.github.io/")],
    "MT": [("Site", "https://marinedetalance.weebly.com/"), ("LinkedIn", "https://www.linkedin.com/in/marine-de-talanc%C3%A9-71893b46/")],
    "MF": [("Site", "https://marinferry.github.io/"), ("LinkedIn", "https://www.linkedin.com/in/marin-ferry/")],
    "AR": [("LinkedIn", "https://www.linkedin.com/in/andrearouchon/")],
}
MEMBRES = [
    ("HB", "Membre du comité directeur. Elle publie les vidéos sur Instagram, TikTok et Facebook."),
    ("MC", "Membre du comité directeur."),
    ("MT", "Membre du comité directeur."),
    ("MF", "Membre du comité directeur. Il publie les vidéos sur LinkedIn."),
    ("AR", "Membre du comité directeur. Il a construit l'espace de travail du collectif."),
]
SPECIALITES = {
    "HB": "Violences faites aux femmes, normes sociales, évaluation des politiques publiques",
    "MC": "Migrations et dynamiques familiales",
    "MT": "Économie de l'éducation, migrations, évaluation des politiques publiques",
    "MF": "Financement international et intérieur, économie politique, politiques environnementales",
    "AR": "Corruption, dette, performances des firmes",
}
SERIES = {
    "HB": ["le-media", "comprendre-les-chiffres", "education", "violences"],
    "MC": [],
    "MT": ["immigration", "education"],
    "MF": ["dette-publique"],
    "AR": ["corruption"],
}
def serie_html(k):
    if not SERIES[k]: return ""
    liens = ", ".join(f'<a href="videos/{s}.html">{TH[s][0]}</a>' for s in SERIES[k])
    return f'\n        <p><span class="etiquette-membre">Ses vidéos</span> {liens}</p>'
fiches = []
for k, role in MEMBRES:
    nom, titre, etab = PERS[k]
    initiales = "".join(w[0] for w in nom.replace("de ", "").split())
    t = f"{titre} · {etab}"
    fiches.append(f'''    <article class="membre">
      <!-- Pour mettre une photo : déposer assets/equipe/{nom.lower().replace(" ", "-").replace("é", "e")}.jpg (carrée), puis remplacer la ligne suivante par
           <img class="portrait" src="assets/equipe/{nom.lower().replace(" ", "-").replace("é", "e")}.jpg" alt="{nom}"> -->
      <div class="portrait" aria-hidden="true">{initiales}</div>
      <div>
        <h3>{nom}</h3>
        <p class="titre-membre">{t}</p>
        <p>{role}</p>
        <p><span class="etiquette-membre">Spécialités</span> {SPECIALITES[k]}</p>{serie_html(k)}
        <p class="liens">{" · ".join(f'<a href="{u}">{l}</a>' for l, u in LIENS[k])}</p>
      </div>
    </article>''')
main = f'''  <p>SOURCE ? a été fondé par cinq chercheurs, qui forment son comité directeur. Le comité tient la ligne éditoriale, choisit les sujets, relit et valide chaque script et chaque vidéo avant publication. Pendant les deux premiers mois, ce sont aussi les visages des vidéos.</p>

  <div class="membres">
{chr(10).join(fiches)}
  </div>

  {num(1, "Et les autres chercheurs")}

  <p>Le collectif a vocation à s'ouvrir, et à d'autres disciplines que l'économie. Chaque vidéo est écrite par un chercheur ou une chercheuse qui connaît le sujet, et son nom est donné à l'écran, dans la description et sur ce site. Vous voulez proposer un sujet ? <a href="contribuer.html">Contribuez</a>.</p>'''
doc("equipe.html", "Qui sommes-nous ? · SOURCE ?", "Les cinq membres du comité directeur de SOURCE ? : Hanna Bony, Melchior Clerc, Marine de Talancé, Marin Ferry et Andrea Rouchon.",
    "à propos", "Qui sommes-nous ?", "Cinq chercheurs, un comité directeur, et une porte ouverte à tous les autres.", main, "apropos")

# ------------------------------------------------------------------ 6. Contribuer
ONGLETS = [("contribuer.html", "Proposer un script", "chercheurs"), ("contribuer-sujet.html", "Proposer un sujet ou une question", "tout le monde"), ("contribuer-relecture.html", "Devenir relecteur ou relectrice", "chercheurs")]
def onglets(actif):
    liens = "\n".join(f'    <a href="{h}"{" aria-current=" + chr(34) + "page" + chr(34) if h == actif else ""}><strong>{n}</strong><span>{q}</span></a>' for h, n, q in ONGLETS)
    return f'  <nav class="onglets" aria-label="Façons de contribuer">\n{liens}\n  </nav>'

def entete_form(sujet, merci):
    return f'''    <input type="hidden" name="_subject" value="{sujet}">
    <input type="hidden" name="_template" value="table">
    <input type="hidden" name="_next" value="https://source-media-france.github.io/merci.html">
    <input type="hidden" name="_autoresponse" value="{merci}">
    <input type="text" name="_honey" class="piege" tabindex="-1" autocomplete="off" aria-hidden="true">'''

STATUTS = ["Doctorant ou doctorante", "Post-doctorant ou post-doctorante", "ATER (attaché temporaire d'enseignement et de recherche)",
           "Maître ou maîtresse de conférences", "Maître ou maîtresse de conférences HDR", "Professeur ou professeure des universités",
           "Chargé ou chargée de recherche", "Directeur ou directrice de recherche", "Chercheur associé ou chercheuse associée",
           "Ingénieur ou ingénieure de recherche", "Enseignant-chercheur ou enseignante-chercheuse (autre statut)",
           "Chercheur ou chercheuse hors université (organisme public, institut, association)", "Autre"]
FORMATS = ["Format libre", "LE CHIFFRE : une statistique qui circule", "L'ÉTUDE : une étude comme point de départ", "REACT : réagir à un contenu",
           "ACTU : éclairer une actualité", "ON EST ALLÉ VOIR : remonter une piste", "3 MINUTES AVEC… : un phénomène ou sa propre recherche"]
MAX_MOTS = 350
opts = lambda xs: "\n".join(f'          <option>{x}</option>' for x in xs)
main = f'''{onglets("contribuer.html")}

  <p>Chercheurs et chercheuses, nous sommes là pour vulgariser vos idées et vos connaissances. Vous connaissez un sujet, une étude, un chiffre qui circule mal ? Proposez-nous un script.</p>

  {num(1, "Comment ça se passe")}

  <ol>
    <li><strong>Vous proposez une idée</strong>, vous rassemblez la documentation, et vous lisez <a href="a-propos.html">nos engagements</a> et <a href="methode.html">notre méthode</a>.</li>
    <li><strong>Vous écrivez un script</strong> : une question, une réponse, une source principale, une limite. Une minute de vidéo, c'est environ 150 mots.</li>
    <li><strong>Le comité directeur le relit</strong>, le valide ou non, et propose si besoin des changements sur la forme.</li>
    <li><strong>Vous validez</strong> la version retravaillée. Vous avez le dernier mot sur ce qui est vrai ; nous, sur ce qui est clair.</li>
    <li><strong>Si vous ne souhaitez pas vous filmer</strong>, le comité prend en charge la vidéo, et vous validez la version finale. Rien n'est publié sans votre accord, et vous êtes nommé et crédité.</li>
  </ol>

  <div class="principe"><p>Vous parlez en votre nom de chercheur ou de chercheuse, pas au nom de votre institution. Vous pouvez présenter vos propres travaux : dites-le simplement. Et vous n'intervenez pas sur un sujet avec lequel vous avez un conflit d'intérêts.</p></div>

  {num(2, "Proposer un script", "formulaire")}

  <form class="formulaire" action="https://formsubmit.co/{EMAIL}" method="POST">
    <input type="hidden" name="_subject" value="SOURCE ? : nouvelle proposition de script">
    <input type="hidden" name="_template" value="table">
    <input type="hidden" name="_next" value="https://source-media-france.github.io/merci.html">
    <input type="hidden" name="_autoresponse" value="Merci pour votre proposition ! Le comité de SOURCE ? la lit et vous répond à cette adresse. T'as la source ? On va la chercher.">
    <input type="text" name="_honey" class="piege" tabindex="-1" autocomplete="off" aria-hidden="true">

    <div class="deux">
      <label><span class="libelle">Prénom et nom <span class="requis">*</span></span><input type="text" name="nom" required autocomplete="name"></label>
      <label><span class="libelle">Adresse e-mail <span class="requis">*</span></span><input type="email" name="email" required autocomplete="email"></label>
    </div>
    <div class="deux">
      <label><span class="libelle">Statut <span class="requis">*</span></span>
        <select name="statut" required>
          <option value="" disabled selected>Choisir…</option>
{opts(STATUTS)}
        </select>
      </label>
      <label><span class="libelle">Affiliation <span class="requis">*</span></span><input type="text" name="affiliation" required placeholder="laboratoire, université ou organisme"></label>
    </div>
    <div class="deux">
      <label><span class="libelle">Discipline <span class="requis">*</span></span><input type="text" name="discipline" required placeholder="économie, sociologie, épidémiologie…"></label>
      <label><span class="libelle">Format souhaité</span>
        <select name="format">
{opts(FORMATS)}
        </select>
      </label>
    </div>
    <label><span class="libelle">La question de la vidéo <span class="requis">*</span></span><input type="text" name="question" required maxlength="200" placeholder="par exemple : les jeunes travaillent-ils moins que leurs parents ?"></label>
    <label><span class="libelle">Le script <span class="requis">*</span> <span class="aide">{MAX_MOTS} mots au maximum, soit un peu plus de deux minutes de vidéo</span></span>
      <textarea name="script" rows="12" required data-max-mots="{MAX_MOTS}"></textarea>
      <span class="compteur" aria-live="polite"></span>
    </label>
    <label><span class="libelle">Les sources <span class="aide">un lien ou une référence par ligne : article, rapport, base de données</span></span>
      <textarea name="sources" rows="4"></textarea>
    </label>
    <fieldset>
      <legend>Souhaitez-vous apparaître dans la vidéo ?</legend>
      <label class="choix"><input type="radio" name="tournage" value="oui"> Oui, je me filme</label>
      <label class="choix"><input type="radio" name="tournage" value="non"> Non, le comité s'en charge</label>
      <label class="choix"><input type="radio" name="tournage" value="à discuter" checked> À discuter</label>
    </fieldset>
    <label class="choix"><input type="checkbox" name="engagement" value="oui" required> J'ai lu les engagements de SOURCE ? et je n'ai pas de conflit d'intérêts, économique ou politique, avec ce sujet. <span class="requis">*</span></label>

    <button type="submit">Envoyer ma proposition</button>
    <p class="meta">Le formulaire passe par le service FormSubmit, qui transmet votre message à {EMAIL}. Vos informations ne servent qu'à vous répondre.</p>
  </form>

  {num(3, "Une autre idée ?")}

  <p>Vous voulez nous parler d'un sujet sans avoir encore de script, ou vous filmer pour une vidéo ? Écrivez-nous à <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>'''
doc("contribuer.html", "Contribuer · SOURCE ?", "Chercheurs et chercheuses : proposez un script de vidéo à SOURCE ?. Le comité le relit, vous validez, et la vidéo est publiée avec votre nom.",
    "contribuer", "Contribuer", "Vous écrivez le script, nous en faisons une vidéo, et vous validez avant toute publication.", main, "contribuer")

# ------------------------------------------------------------------ 6 bis. Proposer un sujet (ouvert à tous)
PUBLICS = ["Étudiant ou étudiante", "Lycéen ou lycéenne", "Enseignant ou enseignante", "Chercheur ou chercheuse", "Journaliste", "Autre"]
MAX_SUJET = 200
main = f'''{onglets("contribuer-sujet.html")}

  <p>Un chiffre vous intrigue, une affirmation vous paraît bizarre, une question vous trotte dans la tête ? Proposez-la. Pas besoin d'être chercheur : les meilleures idées de vidéos viennent souvent de questions toutes simples.</p>

  <div class="principe"><p>Une bonne question est précise. « Les jeunes et le travail » n'est pas une question. « Les jeunes travaillent-ils moins que leurs parents au même âge ? » en est une.</p></div>

  {num(1, "Proposer un sujet ou poser une question", "formulaire")}

  <form class="formulaire" action="https://formsubmit.co/{EMAIL}" method="POST">
{entete_form("SOURCE ? : nouvelle question ou idée de sujet", "Merci pour votre question ! Le comité de SOURCE ? la lit. Si elle devient une vidéo, nous vous le dirons. T'as la source ? On va la chercher.")}

    <div class="deux">
      <label><span class="libelle">Prénom ou pseudo</span><input type="text" name="nom" autocomplete="given-name"></label>
      <label><span class="libelle">Adresse e-mail <span class="aide">si vous voulez une réponse</span></span><input type="email" name="email" autocomplete="email"></label>
    </div>
    <label><span class="libelle">Vous êtes</span>
      <select name="profil">
        <option value="" selected>Je préfère ne pas le dire</option>
{opts(PUBLICS)}
      </select>
    </label>
    <label><span class="libelle">Votre sujet ou votre question <span class="requis">*</span> <span class="aide">{MAX_SUJET} mots au maximum</span></span>
      <textarea name="question" rows="7" required data-max-mots="{MAX_SUJET}" placeholder="par exemple : on entend partout que… est-ce vrai ?"></textarea>
      <span class="compteur" aria-live="polite"></span>
    </label>
    <label><span class="libelle">Où l'avez-vous vu ? <span class="aide">un lien vers la vidéo, l'article ou le post, si vous l'avez</span></span>
      <input type="text" name="lien">
    </label>

    <button type="submit">Envoyer ma question</button>
    <p class="meta">Le formulaire passe par le service FormSubmit, qui transmet votre message à {EMAIL}. Vos informations ne servent qu'à vous répondre.</p>
  </form>'''
doc("contribuer-sujet.html", "Proposer un sujet · SOURCE ?", "Proposez un sujet ou posez une question à SOURCE ? : un chiffre qui vous intrigue, une affirmation qui vous paraît bizarre. Ouvert à tout le monde.",
    "contribuer", "Proposer un sujet", "Une question, un chiffre qui circule, une affirmation qui vous paraît bizarre : dites-le-nous.", main, "contribuer")

# ------------------------------------------------------------------ 6 ter. Devenir relecteur ou relectrice
DISPOS = ["Une relecture par mois", "Deux ou trois par mois", "Ponctuellement, quand un sujet touche ma spécialité"]
main = f'''{onglets("contribuer-relecture.html")}

  <p>Chaque script est relu avant d'être tourné. Quand un sujet sort de notre spécialité, nous cherchons un chercheur ou une chercheuse du domaine pour vérifier que ce que dit la vidéo correspond à l'état des connaissances.</p>

  {num(1, "Ce qu'on vous demande")}

  <ul>
    <li><strong>Relire un script court</strong>, de quelques centaines de mots au plus, avec ses sources.</li>
    <li><strong>Vérifier le fond</strong> : les chiffres, ce que disent les études citées, le degré de certitude des mots employés. La forme, c'est notre travail.</li>
    <li><strong>Répondre dans un délai raisonnable</strong>, convenu avec le comité pour chaque script. Vous pouvez toujours refuser un sujet.</li>
    <li><strong>Signaler tout conflit d'intérêts</strong>, économique ou politique, avec le sujet.</li>
  </ul>

  {num(2, "Proposer de relire", "formulaire")}

  <form class="formulaire" action="https://formsubmit.co/{EMAIL}" method="POST">
{entete_form("SOURCE ? : proposition de relecture", "Merci de proposer votre aide ! Le comité de SOURCE ? vous écrira quand un script touchera votre domaine. T'as la source ? On va la chercher.")}

    <div class="deux">
      <label><span class="libelle">Prénom et nom <span class="requis">*</span></span><input type="text" name="nom" required autocomplete="name"></label>
      <label><span class="libelle">Adresse e-mail <span class="requis">*</span></span><input type="email" name="email" required autocomplete="email"></label>
    </div>
    <div class="deux">
      <label><span class="libelle">Statut <span class="requis">*</span></span>
        <select name="statut" required>
          <option value="" disabled selected>Choisir…</option>
{opts(STATUTS)}
        </select>
      </label>
      <label><span class="libelle">Affiliation <span class="requis">*</span></span><input type="text" name="affiliation" required placeholder="laboratoire, université ou organisme"></label>
    </div>
    <div class="deux">
      <label><span class="libelle">Discipline <span class="requis">*</span></span><input type="text" name="discipline" required placeholder="économie, sociologie, épidémiologie…"></label>
      <label><span class="libelle">Disponibilité</span>
        <select name="disponibilite">
{opts(DISPOS)}
        </select>
      </label>
    </div>
    <label><span class="libelle">Vos domaines de spécialité <span class="requis">*</span> <span class="aide">les sujets sur lesquels vous pouvez relire</span></span>
      <textarea name="domaines" rows="4" required data-max-mots="150"></textarea>
      <span class="compteur" aria-live="polite"></span>
    </label>
    <label><span class="libelle">Une page qui présente vos travaux <span class="aide">page personnelle, page de laboratoire, Google Scholar, HAL…</span></span>
      <input type="text" name="page">
    </label>
    <label class="choix"><input type="checkbox" name="engagement" value="oui" required> J'ai lu les engagements de SOURCE ? et je signalerai tout conflit d'intérêts avec un sujet qu'on me propose de relire. <span class="requis">*</span></label>

    <button type="submit">Proposer de relire</button>
    <p class="meta">Le formulaire passe par le service FormSubmit, qui transmet votre message à {EMAIL}. Vos informations ne servent qu'à vous recontacter pour une relecture.</p>
  </form>'''
doc("contribuer-relecture.html", "Devenir relecteur · SOURCE ?", "Chercheurs et chercheuses : proposez de relire les scripts de SOURCE ? dans votre domaine.",
    "contribuer", "Devenir relecteur ou relectrice", "Vous connaissez un domaine ? Aidez-nous à vérifier que nos vidéos disent juste.", main, "contribuer")

# ------------------------------------------------------------------ 7. Contact
main = f'''  <div class="contacts">
    <a class="contact" href="mailto:{EMAIL}"><span class="format">e-mail</span><strong>{EMAIL}</strong><span>questions, signalements d'erreur, chercheurs intéressés</span></a>
    <a class="contact" href="{INSTA}"><span class="format">Instagram</span><strong>@source.media.france</strong><span>les vidéos et les carrousels</span></a>
    <a class="contact" href="{TIKTOK}"><span class="format">TikTok</span><strong>@source.media.france</strong><span>les vidéos</span></a>
    <a class="contact" href="{LINKEDIN}"><span class="format">LinkedIn</span><strong>SOURCE ?</strong><span>les vidéos et les nouvelles du collectif</span></a>
  </div>

  <ul>
    <li>Pour <strong>signaler une erreur</strong> : écrivez-nous en indiquant la vidéo, le moment et la source qui vous fait penser qu'il y a une erreur. Voir <a href="corrections.html">les corrections</a>.</li>
    <li>Pour <strong>proposer un sujet ou poser une question</strong> : passez par <a href="contribuer-sujet.html">ce formulaire</a>, ouvert à tout le monde.</li>
    <li>Pour <strong>proposer un script</strong> ou <strong>devenir relecteur</strong>, si vous êtes chercheur ou chercheuse : voir <a href="contribuer.html">Contribuer</a>.</li>
    <li>Pour <strong>une question sur une vidéo</strong> : posez-la en commentaire. Une bonne question est souvent le sujet d'une prochaine vidéo.</li>
  </ul>'''
doc("contact.html", "Contact · SOURCE ?", "Où trouver SOURCE ? : e-mail, Instagram, TikTok et LinkedIn.",
    "à propos", "Contact", "Où nous trouver, et comment nous écrire.", main, "apropos")

# ------------------------------------------------------------------ 8. Merci
doc("merci.html", "Merci · SOURCE ?", "Votre proposition a bien été envoyée.", "contribuer", "Merci !",
    "Votre message est bien parti.", '''  <p>Le comité directeur le lit. Si vous avez laissé une adresse e-mail, nous vous répondrons, et un e-mail de confirmation vient de vous être envoyé.</p>

  <p><a href="videos/calendrier.html">Voir les prochaines vidéos</a> · <a href="index.html">Revenir à l'accueil</a></p>''', "contribuer")

# ------------------------------------------------------------------ 9. Menu et pied de page des autres pages
NEW = {"videos/calendrier.html", "videos/index.html", "a-propos.html", "equipe.html", "contribuer.html", "contribuer-sujet.html", "contribuer-relecture.html", "contact.html", "merci.html"} | {f"videos/{k}.html" for k, *_ in THEMES}
for f in sorted(glob.glob("*.html") + glob.glob("videos/*.html")):
    if f in NEW: continue
    t = open(f, encoding="utf-8").read()
    p = "../" if f.startswith("videos/") else ""
    cur = "videos" if f.startswith("videos/") else {"notions.html": "notions", "methode.html": "methode"}.get(f, "")
    t = re.sub(r'<nav class="nav" aria-label="Navigation">.*?</nav>', lambda m: nav(p, cur), t, count=1, flags=re.S)
    t = re.sub(r'<footer class="pied">.*?</footer>', lambda m: footer(p), t, count=1, flags=re.S)
    open(f, "w", encoding="utf-8").write(t)
    print("menu", f)

# ------------------------------------------------------------------ 10. Accueil : le lancement
f = "index.html"; t = open(f, encoding="utf-8").read()
a = t.index('<h2><span class="num">2</span>'); b = t.index('<h2><span class="num">3</span>')
lancement = [v for v in V if v.get("date") == "2026-12-01"]
t = t[:a] + f'''<h2><span class="num">2</span>Le lancement : mardi 1<sup>er</sup> décembre</h2>

  <p>Cinq vidéos le premier jour, puis de nouvelles vidéos chaque semaine.</p>

{cartes(lancement, prefix="videos/", montrer_theme=True, montrer_date=False)}

  <p><a href="videos/calendrier.html">Le calendrier des sorties</a> · <a href="videos/index.html">toutes les séries</a></p>

  ''' + t[b:]
t = t.replace('<p><a href="a-propos.html">Qui nous sommes, nos engagements, et comment contribuer</a></p>',
              '<p><a href="equipe.html">Qui sommes-nous ?</a> · <a href="a-propos.html">notre mission</a> · <a href="contribuer.html">contribuer</a></p>')
open(f, "w", encoding="utf-8").write(t); print("ok index.html")
