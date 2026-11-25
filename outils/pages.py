# Génère les pages des vidéos du lancement (semaines 1 et 2). Lancer depuis le dossier site/ :
#   python3 -I chemin/pages.py
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svg import *
from liens import L, F   # liens et chiffres vérifiés, remplis à part

SITE = os.getcwd()
EXPL = {
 "presentation-du-media.html": "Qui nous sommes et comment on travaille : partir d'un chiffre qui circule, lire ce que la recherche en dit, et le raconter en une minute, la source à l'écran.",
 "immigre-ou-etranger.html": "La différence entre immigré et étranger, selon l'Insee : on reste immigré toute sa vie, on cesse d'être étranger en devenant français.",
 "dette-publique-c-est-quoi.html": "Qui emprunte quand on parle de dette publique, et comment un déficit se transforme en dette.",
 "dette-publique-pourquoi-elle-augmente.html": "La différence entre le déficit et la dette, et pourquoi la dette monte tant que le déficit dépasse ce qui est remboursé.",
 "taille-des-classes.html": "Ce qu'ont montré deux expériences, au Tennessee et dans les CP dédoublés en France, et ce qu'on ne sait pas encore pour le lycée.",
 "moyenne-mediane.html": "Pourquoi le salaire moyen n'est pas le salaire du milieu, avec les chiffres 2025 de l'Insee : la moyenne et la médiane.",
 "migrant-ou-refugie.html": "Pourquoi « migrant » est un mot large et « réfugié » un statut précis, défini par la Convention de Genève de 1951.",
}
GRIS_C = ' class="gris"'
MONO_C = ' class="mono"'
TITRE_IMMIG = "Insee, 2026, L'essentiel sur les immigrés et les étrangers"
base = open(os.path.join(SITE, "videos/presentation-du-media.html"), encoding="utf-8").read()
HEAD = base[:base.index('<section class="titre">')]
FOOT = base[base.index('<footer class="pied">'):]

HB = '<span class="cartouche">Hanna Bony · Doctorante en économie · Université Gustave Eiffel</span>'
MT = '<span class="cartouche">Marine de Talancé · Enseignante-chercheuse en économie · Université Gustave Eiffel</span>'
MF = '<span class="cartouche">Marin Ferry · Enseignant-chercheur en économie · Université Gustave Eiffel</span>'

def a(cle, texte=None):
    url = L[cle]
    if not url:
        return f'{texte or ""} <span class="meta">[lien à compléter]</span>'.strip()
    lib = texte or url.replace("https://", "").replace("http://", "").rstrip("/")
    return f'<a href="{url}">{lib}</a>'

def verif(cle):
    """Statut d'un chiffre : texte libre stocké dans F[cle]['statut']."""
    st = F[cle]["statut"]
    if st.startswith("à vérifier"):
        return '<span class="crochet">à vérifier</span>' + st[len("à vérifier"):]
    return st

def page(fname, titre, desc, sur, accroche, statut, fiche, explication, montre, sources, donnees, relecture):
    sections = []
    sections.append(("En une phrase", '<table class="fiche">\n' + "\n".join(f'    <tr><th>{k}</th><td>{v}</td></tr>' for k, v in fiche) + '\n  </table>'))
    sections.append(("L'explication, en images", explication))
    t_m, oui, non, lab_oui, lab_non = montre
    sections.append((t_m, f'''<div class="montre">
    <div class="oui">
      <span class="etiquette">{lab_oui}</span>
      <ul>
{chr(10).join("        <li>"+x+"</li>" for x in oui)}
      </ul>
    </div>
    <div class="non">
      <span class="etiquette">{lab_non}</span>
      <ul>
{chr(10).join("        <li>"+x+"</li>" for x in non)}
      </ul>
    </div>
  </div>'''))
    sections.append(("Les sources", sources))
    if donnees:
        sections.append(("Les données et les calculs", donnees))
    rel = '<div class="table-scroll"><table>\n    <tr><th>Étape</th><th>Qui</th><th>Statut</th></tr>\n' + "\n".join(
        "    <tr><td>" + e + "</td><td" + (GRIS_C if q.startswith("à ") else "") + ">" + q + "</td><td" + (GRIS_C if s != "fait" else "") + ">" + s + "</td></tr>" for e, q, s in relecture) + '\n  </table></div>'
    sections.append(("Relecture et validation", rel))
    sections.append(("Corrections", '<p>Aucune correction pour l\'instant. Une erreur ? <a href="../corrections.html">Signalez-la</a>.</p>'))
    body = "\n\n".join(f'  <h2><span class="num">{i}</span>{h}</h2>\n\n  {c}' for i, (h, c) in enumerate(sections, 1))
    head = re.sub(r'<title>.*?</title>', f'<title>{titre} · SOURCE ?</title>', HEAD)
    head = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{desc}">', head)
    html = f'''{head}<section class="titre"><div class="wrap">
  <p class="sur">{sur}</p>
  <h1>{titre}</h1>
  <p class="explique">{EXPL.get(fname, accroche)}</p>
</div></section>

<main id="contenu" class="contenu"><div class="wrap">

  <p><span class="statut">{statut}</span></p>

{body}

</div></main>

{FOOT}'''
    open(os.path.join(SITE, "videos", fname), "w", encoding="utf-8").write(html)
    print("ok", fname)

REL_HANNA = [("Écriture du script", "Hanna Bony", "fait"), ("Relecture par le comité", "à compléter", "en cours"),
             ("Validation technique (sous-titres, habillage, sources à l'écran)", "à compléter", "en cours"),
             ("Accord de la chercheuse sur la version montée", "Hanna Bony", "en cours")]
def rel_auteur(nom, chercheur="du chercheur"):
    return [("Écriture du script", nom, "fait"), ("Relecture par le comité", "à compléter", "en cours"),
            ("Validation technique (sous-titres, habillage, sources à l'écran)", "à compléter", "en cours"),
            (f"Accord {chercheur} sur la version montée", nom, "en cours")]

def liste_sources(items):
    return "<ol>\n" + "\n".join(f"    <li>{x}</li>" for x in items) + "\n  </ol>"

def tableau(lignes, entetes=("Chiffre", "Valeur", "Source et statut")):
    s = '<div class="table-scroll"><table>\n    <tr>' + "".join(f"<th>{h}</th>" for h in entetes) + "</tr>\n"
    for l in lignes:
        s += "    <tr>" + "".join("<td" + (MONO_C if i == 1 else "") + ">" + c + "</td>" for i, c in enumerate(l)) + "</tr>\n"
    return s + "  </table></div>"

# =====================================================================================
# 1. Présentation du média
etapes = svg("p1", "Trois étapes : un chiffre qui circule, on lit la recherche, une vidéo d'une minute avec la source à l'écran.", 640, 150,
    boite(10, 40, 180, 70, [("Un chiffre", True), ("qui circule", False)], "noir") +
    fleche(194, 75, 226, 75) +
    boite(230, 40, 180, 70, [("La recherche", True), ("on la lit", False)], "noir") +
    fleche(414, 75, 446, 75) +
    boite(450, 40, 180, 70, [("Une minute", True), ("la source à l'écran", False)], "jaune") +
    texte(320, 140, "le chemin de chaque vidéo", 13, cls="gris"))

page("presentation-du-media.html", "Présentation du média",
     "Qu'est-ce que SOURCE ? Des chercheurs qui prennent un chiffre qui circule, lisent ce que la recherche en dit, et le racontent en une minute avec la source à l'écran.",
     "Le média · à paraître le mardi 1<sup>er</sup> décembre",
     "Huit virgule deux pour cent de chômage. Cinquante-quatre milliards au budget. Deux cent quatre-vingt-cinq mille victimes. Ces chiffres, vous les avez vus passer. Mais ils viennent d'où ?",
     "à paraître le mardi 1<sup>er</sup> décembre 2026, 17 h",
     [("La question", "Qu'est-ce que SOURCE ?, et comment ça marche ?"),
      ("La réponse", "Des chercheurs qui prennent un chiffre qui circule, lisent ce que la recherche en dit, et le racontent en une minute, avec la source à l'écran."),
      ("Résumé", "La vidéo part de trois chiffres que tout le monde a vus passer en novembre 2026 : 8,2 % de chômage, 54 milliards d'euros d'effort au budget 2027, 285 000 victimes de violences conjugales enregistrées. D'où viennent-ils ? Hanna présente le collectif : des chercheurs qui partent d'un chiffre ou d'une affirmation qui circule, vont lire ce que la recherche en dit, et le racontent en une minute, la source à l'écran. Pas de verdict « vrai » ou « faux » : parfois c'est confirmé, parfois démonté, et parfois on ne sait pas. Elle termine en invitant chacun à proposer en commentaire un chiffre qui l'intrigue."),
      ("Avec", HB),
      ("La limite", "La vidéo ne vérifie aucun des trois chiffres : elle montre d'où ils viennent. Chacun aura sa propre vidéo."),
      ("Thème", '<a href="le-media.html">Le média</a>'),
      ("Pour aller plus loin", '<a href="../methode.html">Notre méthode</a> · <a href="../a-propos.html">Qui nous sommes</a>')],
     f'''<p class="chapeau">Chaque mois, des chiffres circulent sans leur source. SOURCE ? part de ces chiffres et va chercher d'où ils viennent, ce qu'ils mesurent, et ce que la recherche en dit.</p>

  <p>Les trois chiffres de la vidéo ont tous été publiés en novembre 2026, et tous ont une source qu'on peut ouvrir. C'est le point de départ de chaque vidéo : un chiffre précis, la personne ou l'organisme qui l'a produit, et le document où il est écrit.</p>

  <div class="table-scroll"><table>
    <tr><th>Le chiffre</th><th>Ce qu'il compte</th><th>D'où il vient</th></tr>
    <tr><td class="mono">8,2 %</td><td>le taux de chômage au troisième trimestre 2026</td><td>{a("insee_chomage", "Insee, Informations rapides n° 270, 10 novembre 2026")}</td></tr>
    <tr><td class="mono">54 milliards €</td><td>l'effort annoncé dans le projet de budget 2027, dont 43 milliards de mesures nouvelles</td><td>{a("plf2027", "Projet de loi de finances pour 2027")}</td></tr>
    <tr><td class="mono">285 000</td><td>les victimes de violences conjugales enregistrées par la police et la gendarmerie en 2025</td><td>{a("ssmsi", "ministère de l'Intérieur (SSMSI), 5 novembre 2026")}</td></tr>
  </table></div>

  <figure class="figure">
    {etapes}
    <figcaption>Le chemin de chaque vidéo : un chiffre qui circule, ce que la recherche en dit, et une minute pour le raconter, la source à l'écran.</figcaption>
  </figure>

  <p>Au bout du chemin, il n'y a pas de tampon « vrai » ou « faux ». Un chiffre répond à une question précise : selon la question, la réponse change. Les vidéos se terminent donc par l'une de ces quatre réponses.</p>

  <div class="tuiles">
    <div class="tuile"><p class="quoi">Confirmé</p><p>La recherche va dans le sens du chiffre ou de l'affirmation.</p></div>
    <div class="tuile"><p class="quoi">Démonté</p><p>La recherche dit autre chose, et on montre quoi.</p></div>
    <div class="tuile"><p class="quoi">Plus compliqué</p><p>C'est vrai dans un cas, pas dans un autre.</p></div>
    <div class="tuile jaune"><p class="quoi">On ne sait pas</p><p>Il n'y a pas encore de résultat solide. C'est une réponse valable.</p></div>
  </div>''',
     ("Ce que SOURCE ? fait, ce qu'il ne fait pas",
      ["Partir d'un chiffre ou d'une affirmation qui circule.", "Aller lire la source d'origine et ce que la recherche en dit.", "Mettre la source à l'écran, et sur cette page, pour que chacun puisse vérifier."],
      ["Dire quoi penser, ou pour qui voter.", "Distribuer des « vrai » ou des « faux ».", "Répondre à une personne : on répond à la phrase, pas à celui ou celle qui l'a dite."],
      "On fait", "On ne fait pas"),
     liste_sources([
       f'<strong>Insee</strong>, « Au troisième trimestre 2026, le taux de chômage… », <em>Informations rapides</em> n° 270, 10 novembre 2026. {a("insee_chomage")}',
       f'<strong>Projet de loi de finances pour 2027</strong>, et le rapport général du Sénat n° 156 : l\'effort de 54 milliards d\'euros, dont 43 de mesures nouvelles. {a("plf2027")}',
       f'<strong>Ministère de l\'Intérieur, service statistique (SSMSI)</strong>, <em>Interstats Info rapide</em> n° 69, 5 novembre 2026 : les victimes de violences conjugales enregistrées en 2025. {a("ssmsi")}',
     ]),
     tableau([
       ["Taux de chômage, troisième trimestre 2026", "8,2 %", verif("chomage")],
       ["Effort du projet de budget 2027", "54 milliards €", verif("budget")],
       ["Victimes de violences conjugales enregistrées en 2025", "285 000", verif("victimes")],
     ]),
     REL_HANNA)

# =====================================================================================
# 2. Immigré ou étranger (Marine)
fi = F["immig"]
venn = svg("i1", f"Deux cercles qui se chevauchent : les immigrés ({fi['immigres_txt']}) et les étrangers ({fi['etrangers_txt']}). Une partie des immigrés sont devenus français ; une partie des étrangers sont nés en France.", 640, 370,
    texte(185, 22, "IMMIGRÉS", 15, gras=True) + texte(185, 40, fi["immigres_txt"], 13, cls="gris") +
    texte(455, 22, "ÉTRANGERS", 15, gras=True) + texte(455, 40, fi["etrangers_txt"], 13, cls="gris") +
    '<g transform="translate(0,35)">' +
    f'<circle cx="245" cy="160" r="135" fill="{ENCRE}" fill-opacity="0.08" stroke="{ENCRE}" stroke-width="2.5"/>'
    f'<circle cx="395" cy="160" r="135" fill="{JAUNE}" fill-opacity="0.45" stroke="{ENCRE}" stroke-width="2.5"/>' +
    texte(170, 150, "immigrés", 14, gras=True) + texte(170, 168, "devenus français", 14, gras=True) +
    texte(170, 192, fi["immig_francais_txt"], 13, cls="gris") + texte(170, 230, "comme Fatou", 13, cls="gris") +
    texte(320, 158, "immigrés", 13, gras=True) + texte(320, 175, "étrangers", 13, gras=True) +
    texte(472, 150, "étrangers", 14, gras=True) + texte(472, 168, "nés en France", 14, gras=True) +
    texte(472, 192, fi["etr_nes_france_txt"], 13, cls="gris") + texte(472, 230, "comme Yanis", 13, cls="gris") +
    '</g>' + texte(320, 362, f"France, {fi['annee']}", 13, cls="gris"))

page("immigre-ou-etranger.html", "Immigré ou étranger : est-ce la même chose ?",
     "Immigré et étranger, ce n'est pas la même chose : un immigré est né étranger à l'étranger, un étranger n'a pas la nationalité française aujourd'hui. Résumé, explication en images et sources de la vidéo de Marine de Talancé.",
     "Immigration · épisode 1 · à paraître le mardi 1<sup>er</sup> décembre",
     "Un immigré sur trois est français. Oui, français. Comment c'est possible ?",
     "à paraître le mardi 1<sup>er</sup> décembre 2026 · carrousel le mercredi 2 décembre",
     [("La question", "Immigré et étranger, est-ce la même chose ?"),
      ("La réponse", "Non. Un immigré est né étranger, à l'étranger, et le reste toute sa vie. Un étranger est quelqu'un qui n'a pas la nationalité française aujourd'hui. On peut donc être immigré et français, ou étranger sans être immigré."),
      ("Résumé", f"En France, c'est l'Insee, l'institut national de la statistique, qui compte, et il compte avec des critères précis. Fatou est née au Sénégal de parents sénégalais et vient vivre à Lyon : elle est immigrée. Dix ans plus tard, elle devient française : elle cesse d'être étrangère, mais elle reste immigrée, car immigré, c'est pour la vie. Yanis, cinq ans, est né en France de parents marocains : il est étranger, mais pas immigré, puisqu'il est né en France. Au total, environ un immigré sur trois est français, comme Fatou, et {fi['etr_nes_france_phrase']} d'étrangers sont nés en France, comme Yanis. Selon le mot qu'on choisit, les chiffres et les personnes ne sont pas les mêmes."),
      ("Avec", MT),
      ("Source principale", f'<span class="crochet long">{a("insee_immig", TITRE_IMMIG)}</span>'),
      ("La limite", "Les chiffres viennent du recensement : ils comptent les personnes qui vivent en France depuis au moins un an, ou qui comptent y rester au moins un an."),
      ("Thème", '<a href="immigration.html">Immigration</a> · épisode 1'),
      ("Légende publiée", '<span class="gris">Immigré, étranger : est-ce la même chose ? Non : un immigré est né étranger à l\'étranger, un étranger n\'a pas la nationalité française aujourd\'hui. Avec Marine de Talancé, enseignante-chercheuse en économie à l\'Université Gustave Eiffel. Les prises de position n\'engagent que leur auteur.</span>')],
     f'''<p class="chapeau">Dans le débat public, « immigré » et « étranger » sont souvent employés l'un pour l'autre. Pour l'Insee, ce sont deux populations différentes, qui se recouvrent en partie seulement.</p>

  <p>Pour être <strong>immigré</strong>, il faut deux choses : être né à l'étranger, et être né sans la nationalité française. C'est une question de naissance, donc ça ne change jamais. Pour être <strong>étranger</strong>, il suffit de ne pas avoir la nationalité française aujourd'hui. C'est une question de nationalité, donc ça peut changer.</p>

  <div class="table-scroll"><table>
    <tr><th></th><th>Née à l'étranger</th><th>Née étrangère</th><th>Française aujourd'hui</th><th>Immigrée ?</th><th>Étrangère ?</th></tr>
    <tr><td><strong>Fatou</strong>, à son arrivée à Lyon</td><td>oui</td><td>oui</td><td>non</td><td><strong>oui</strong></td><td><strong>oui</strong></td></tr>
    <tr><td><strong>Fatou</strong>, dix ans après, naturalisée</td><td>oui</td><td>oui</td><td>oui</td><td><span class="surligne"><strong>oui</strong></span></td><td>non</td></tr>
    <tr><td><strong>Yanis</strong>, cinq ans, né en France de parents marocains</td><td>non</td><td>oui</td><td>non</td><td>non</td><td><strong>oui</strong></td></tr>
  </table></div>

  <p>D'où deux groupes qui se chevauchent. Au milieu, les immigrés qui sont encore étrangers. À gauche, les immigrés devenus français. À droite, les étrangers nés en France.</p>

  <figure class="figure">
    {venn}
    <figcaption>Immigrés et étrangers : deux groupes qui ne se confondent pas. Environ un immigré sur trois est français ; {fi['etr_nes_france_phrase']} d'étrangers sont nés en France.<span class="src">[Insee, {fi['annee']} · L'essentiel sur les immigrés et les étrangers]</span></figcaption>
  </figure>

  <p>Quand un chiffre sur l'immigration circule, la première question à poser est donc : de qui parle-t-on, des immigrés ou des étrangers ? Les deux chiffres sont justes, mais ils ne comptent pas les mêmes personnes.</p>''',
     ("Ce qu'elle montre, ce qu'elle ne montre pas",
      ["Que « immigré » et « étranger » sont deux catégories différentes, définies par l'Insee.", "Qu'on reste immigré toute sa vie, alors qu'on cesse d'être étranger en devenant français.", "Qu'un même débat peut citer deux chiffres justes qui ne comptent pas les mêmes personnes."],
      ["Combien de personnes arrivent en France chaque année : c'est une autre question, et un autre chiffre.", "Ce que coûte ou rapporte l'immigration.", "La différence entre migrant et réfugié : c'est l'épisode suivant."],
      "Elle montre", "Elle ne montre pas"),
     liste_sources([
       f'<strong>Insee</strong>, « L\'essentiel sur les immigrés et les étrangers », {fi["annee"]}. Les définitions, et les chiffres du recensement. Accès libre. {a("insee_immig")}',
       f'<strong>Insee</strong>, « S\'y retrouver dans les chiffres de l\'immigration », blog de l\'Insee. Pourquoi plusieurs chiffres circulent. Accès libre. {a("insee_blog_immig")}',
     ]),
     f'''<h3>Les bases de données utilisées</h3>

  <ul>
    <li><strong>Le recensement de la population</strong> (Insee) : il compte les personnes qui résident en France depuis au moins un an, ou qui comptent y rester au moins un an, y compris les personnes en situation irrégulière. {a("insee_immig", "Tableaux et infographie de l'Insee")}.</li>
  </ul>

  {tableau([
       ["Immigrés vivant en France", fi["immigres_txt"], verif("immig_immigres")],
       ["Étrangers vivant en France", fi["etrangers_txt"], verif("immig_etrangers")],
       ["Part des immigrés qui ont la nationalité française", fi["immig_francais_txt"], verif("immig_francais")],
       ["Étrangers nés en France", fi["etr_nes_france_txt"], verif("immig_nes_france")],
     ])}''',
     rel_auteur("Marine de Talancé", "de la chercheuse"))

# =====================================================================================
# 3. Dette publique, c'est quoi ? (Marin)
apu = svg("d1", "Les administrations publiques regroupent trois ensembles : les administrations centrales, les administrations locales et les administrations de sécurité sociale. La Banque de France et les entreprises publiques comme EDF n'en font pas partie.", 640, 270,
    boite(170, 10, 300, 50, [("Les administrations publiques", True)], "jaune") +
    fleche(250, 62, 110, 106) + fleche(320, 62, 320, 106) + fleche(390, 62, 530, 106) +
    boite(10, 110, 200, 90, [("Centrales", True), ("éducation, sécurité,", False), ("justice", False)], "noir") +
    boite(220, 110, 200, 90, [("Locales", True), ("mairies, petites routes,", False), ("déchets", False)], "noir") +
    boite(430, 110, 200, 90, [("Sécurité sociale", True), ("sécu, hôpitaux,", False), ("chômage", False)], "noir") +
    texte(320, 240, "n'en font pas partie : la Banque de France, les entreprises publiques comme EDF", 13, cls="gris"))

balance = svg("d2", "Les recettes publiques sont plus petites que les dépenses publiques. L'écart, le déficit, est comblé par un emprunt : c'est la dette.", 640, 300,
    f'<line x1="40" y1="250" x2="420" y2="250" stroke="{ENCRE}" stroke-width="1.5"/>'
    f'<rect x="70" y="110" width="120" height="140" fill="{ENCRE}"/>' + texte(130, 275, "Recettes", 15, gras=True) + texte(130, 293, "impôts, TVA, cotisations", 12, cls="gris") +
    f'<rect x="250" y="40" width="120" height="210" fill="{ENCRE}"/>' + texte(310, 275, "Dépenses", 15, gras=True) + texte(310, 293, "profs, hôpitaux, routes…", 12, cls="gris") +
    f'<rect x="70" y="40" width="120" height="70" fill="{JAUNE}" stroke="{ENCRE}" stroke-width="1.5" stroke-dasharray="6 4"/>' +
    texte(130, 72, "déficit", 15, gras=True) + texte(130, 90, "ce qui manque", 12) +
    fleche(196, 75, 450, 75) +
    boite(455, 45, 175, 60, [("Emprunt", True), ("= dette publique", False)], "jaune") +
    texte(540, 135, "auprès des banques", 13, cls="gris") + texte(540, 152, "ou sur les marchés", 13, cls="gris") + texte(540, 169, "financiers", 13, cls="gris") +
    texte(540, 205, "remboursé plus tard", 13, cls="gris"))

page("dette-publique-c-est-quoi.html", "La dette publique, c'est quoi ?",
     "La dette publique, c'est l'argent que les administrations publiques empruntent quand leurs recettes ne couvrent pas leurs dépenses. Résumé, explication en images et sources de la vidéo de Marin Ferry.",
     "Dette publique · épisode 1 · à paraître le mardi 1<sup>er</sup> décembre",
     "Depuis plusieurs mois, on entend beaucoup parler de la dette publique française. Mais savez-vous vraiment ce que c'est ?",
     "à paraître le mardi 1<sup>er</sup> décembre 2026 · carrousel le jeudi 3 décembre",
     [("La question", "La dette publique, c'est quoi ?"),
      ("La réponse", "L'argent que les administrations publiques empruntent quand leurs recettes ne couvrent pas leurs dépenses."),
      ("Résumé", "Une dette, c'est une somme d'argent empruntée, comme quand une personne ou une entreprise emprunte à sa banque. Pour la dette publique, ceux qui empruntent sont les administrations publiques : l'État et ses administrations centrales, les collectivités locales, et la sécurité sociale. La Banque de France et les entreprises publiques comme EDF n'en font pas partie. Ces administrations financent les services publics avec les impôts et les cotisations qu'elles collectent. Quand ces recettes ne suffisent pas à couvrir les dépenses, il manque de l'argent : c'est le déficit. Pour le combler, elles empruntent, auprès des banques ou sur les marchés financiers. Cet emprunt, qu'il faudra rembourser plus tard, c'est la dette publique."),
      ("Avec", MF),
      ("Source principale", f'<span class="crochet long">{a("insee_dette_def", "Insee, définition de la dette publique")}</span>'),
      ("La limite", "La vidéo explique ce qu'est la dette et d'où elle vient, pas s'il faut s'en inquiéter. C'est une autre question, pour un prochain épisode."),
      ("Thème", '<a href="dette-publique.html">Dette publique</a> · épisode 1 · suite : <a href="dette-publique-pourquoi-elle-augmente.html">pourquoi la dette augmente</a>'),
      ("Légende publiée", '<span class="gris">La dette publique, c\'est quoi ? L\'argent que les administrations publiques empruntent quand leurs recettes ne couvrent pas leurs dépenses. Avec Marin Ferry, enseignant-chercheur en économie à l\'Université Gustave Eiffel. Les prises de position n\'engagent que leur auteur.</span>')],
     f'''<p class="chapeau">On parle de « la dette de la France » comme d'un seul bloc. En réalité, ceux qui empruntent sont un ensemble précis d'administrations, et la dette naît d'un mécanisme simple : dépenser plus qu'on ne reçoit.</p>

  <p>Premier point : qui emprunte ? Les statisticiens parlent des <strong>administrations publiques</strong>. Elles regroupent trois ensembles.</p>

  <figure class="figure">
    {apu}
    <figcaption>Les trois ensembles qui forment les administrations publiques, et ce qui n'en fait pas partie.<span class="src">[définition de l'Insee · schéma]</span></figcaption>
  </figure>

  <p>Deuxième point : pourquoi emprunter ? Ces administrations paient les services publics, du salaire des professeurs au matériel des hôpitaux, avec les impôts et les cotisations qu'elles collectent. Quand les dépenses dépassent les recettes, il manque de l'argent : c'est le <strong>déficit</strong>. Pour le combler, elles empruntent.</p>

  <figure class="figure">
    {balance}
    <figcaption>Le mécanisme : quand les recettes ne couvrent pas les dépenses, l'écart est emprunté. Cet emprunt, c'est la dette publique.<span class="src">[schéma, sans échelle]</span></figcaption>
  </figure>

  <p>Le déficit, c'est ce qui manque sur une année. La dette, c'est ce qui a été emprunté et pas encore remboursé. Pourquoi la dette française grossit d'année en année, c'est l'objet de <a href="dette-publique-pourquoi-elle-augmente.html">l'épisode suivant</a>.</p>''',
     ("Ce qu'elle montre, ce qu'elle ne montre pas",
      ["Qui emprunte quand on parle de dette publique : les administrations centrales, locales et de sécurité sociale.", "D'où vient la dette : un déficit, comblé par un emprunt.", "La différence entre l'argent qui manque sur une année (le déficit) et ce qui reste à rembourser (la dette)."],
      ["Combien vaut la dette française aujourd'hui.", "S'il faut s'inquiéter de la dette : tout dépend de sa taille par rapport à l'économie.", "À qui la France doit de l'argent."],
      "Elle montre", "Elle ne montre pas"),
     liste_sources([
       f'<strong>Insee</strong>, définition de la dette publique au sens de Maastricht. {a("insee_dette_def")}',
       f'<strong>Insee</strong>, définition des administrations publiques. {a("insee_apu_def")}',
       '<span class="gris">Le script de la vidéo ne cite pas encore de source : ces deux définitions sont à confirmer par Marin Ferry.</span>',
     ]),
     None,
     rel_auteur("Marin Ferry"))

# =====================================================================================
# 4. Pourquoi la dette augmente (Marin)
baignoire = svg("d3", "Une baignoire : le robinet du déficit la remplit, la bonde du remboursement la vide. Tant que le robinet coule plus fort que la bonde, le niveau, le stock de dette, monte.", 640, 330,
    '<g transform="translate(-40,0)">' +
    # robinet
    f'<rect x="120" y="40" width="130" height="22" fill="{ENCRE}"/><rect x="228" y="62" width="22" height="30" fill="{ENCRE}"/>'
    f'<rect x="232" y="92" width="14" height="120" fill="{JAUNE}"/>' +
    texte(185, 30, "le robinet : le déficit", 14, gras=True) + texte(185, 112, "chaque année,", 13, cls="gris", anchor="end") + texte(185, 128, "une nouvelle dette", 13, cls="gris", anchor="end") +
    # baignoire
    f'<path d="M180,150 L180,270 Q180,290 200,290 L480,290 Q500,290 500,270 L500,150" fill="none" stroke="{ENCRE}" stroke-width="5"/>'
    f'<rect x="183" y="200" width="314" height="87" fill="{JAUNE}" fill-opacity="0.55"/>'
    f'<line x1="183" y1="200" x2="497" y2="200" stroke="{ENCRE}" stroke-width="2"/>' +
    texte(340, 240, "le stock de dette", 16, gras=True) + texte(340, 260, "tout ce qui reste à rembourser", 13) +
    # bonde
    f'<rect x="420" y="290" width="16" height="22" fill="{ENCRE}"/>' + fleche(428, 312, 428, 328, 2) +
    texte(450, 318, "la bonde : le remboursement", 14, gras=True, anchor="start") + '</g>' +
    texte(475, 205, "le niveau monte", 13, cls="gris", anchor="start") + texte(475, 221, "si le robinet coule", 13, cls="gris", anchor="start") + texte(475, 237, "plus fort que la bonde", 13, cls="gris", anchor="start"))

page("dette-publique-pourquoi-elle-augmente.html", "Pourquoi la dette publique augmente-t-elle ?",
     "La dette publique augmente parce que chaque déficit ajoute une nouvelle dette au stock, et que tant que ce déficit dépasse ce qui est remboursé, le stock grossit. Résumé, explication en images et sources de la vidéo de Marin Ferry.",
     "Dette publique · épisode 2 · à paraître le mercredi 9 décembre",
     "La dette publique française ne cesse d'augmenter. Mais avant de s'alarmer : pourquoi augmente-t-elle ?",
     "à paraître le mercredi 9 décembre 2026 · carrousel le jeudi 10 décembre",
     [("La question", "Pourquoi la dette publique augmente-t-elle ?"),
      ("La réponse", "Parce que chaque année de déficit ajoute une nouvelle dette au stock, et que tant que ce déficit dépasse ce qui est remboursé, le stock grossit."),
      ("Résumé", "Si, une année, les dépenses publiques dépassent les recettes, l'État emprunte : c'est le déficit, et il crée une dette. Si le déficit se répète l'année suivante, une nouvelle dette s'ajoute à la précédente, et ainsi de suite : c'est le stock de dette. Une partie de ce stock est remboursée chaque année ; mais si ce remboursement est plus petit que la nouvelle dette, le stock continue de grossir. C'est l'image de la baignoire : tant que le robinet du déficit coule plus fort que la bonde du remboursement, le niveau monte. C'est ce que montre le graphique de la vidéo : depuis 2004, la dette française augmente, avec des comptes publics en déficit chaque année. Marin conclut qu'une dette qui augmente n'est pas une catastrophe en soi, et qu'elle peut même être utile si elle est bien employée : tout dépend de sa taille par rapport à l'économie."),
      ("Avec", MF),
      ("Source principale", f'<span class="crochet long">{a("insee_dette_trim", "Insee, la dette trimestrielle de Maastricht")}</span>'),
      ("La limite", "La vidéo explique pourquoi la dette monte, pas s'il faut s'en inquiéter : la réponse dépend de la taille de la dette par rapport à la richesse produite chaque année. C'est une autre question."),
      ("Thème", '<a href="dette-publique.html">Dette publique</a> · épisode 2 · avant : <a href="dette-publique-c-est-quoi.html">la dette publique, c\'est quoi ?</a>')],
     f'''<p class="chapeau">Fin juin 2026, la dette publique française atteint 3 595,5 milliards d'euros, soit 119 % de la richesse produite en un an, un record <span class="crochet">Insee, 29 septembre 2026</span>. Le chiffre fait peur. Avant de savoir s'il faut s'en inquiéter, il faut comprendre pourquoi elle monte, et pour ça, distinguer deux choses : le déficit et la dette.</p>

  <div class="tuiles">
    <div class="tuile"><p class="quoi">Le déficit</p><p>Ce qui manque <strong>sur une année</strong>, quand les dépenses dépassent les recettes. C'est un flux : il recommence chaque année.</p></div>
    <div class="tuile jaune"><p class="quoi">La dette</p><p><strong>Tout ce qui a été emprunté</strong> et pas encore remboursé, année après année. C'est un stock : il s'accumule.</p></div>
  </div>

  <p>Chaque année de déficit ajoute une nouvelle dette au stock. Une partie du stock est remboursée chaque année. Le niveau de la dette dépend donc de la course entre les deux : ce qui entre et ce qui sort.</p>

  <figure class="figure">
    {baignoire}
    <figcaption>L'image de la baignoire : tant que le robinet du déficit coule plus fort que la bonde du remboursement, le niveau de la dette monte.<span class="src">[schéma, sans échelle]</span></figcaption>
  </figure>

  <p>Le graphique de la vidéo commence en 2004 : sur toute la période, les comptes publics sont en déficit chaque année, le robinet ne se ferme jamais, et la dette grossit. Ça ne dit pas encore si c'est grave. Une dette qui monte peut financer des dépenses utiles ; ce qui compte, c'est sa taille par rapport à l'économie, et c'est l'objet d'un prochain épisode.</p>''',
     ("Ce qu'elle montre, ce qu'elle ne montre pas",
      ["La différence entre le déficit, qui recommence chaque année, et la dette, qui s'accumule.", "Pourquoi la dette monte tant que le déficit dépasse ce qui est remboursé.", "Que la dette française augmente parce que les budgets sont en déficit chaque année."],
      ["Qu'une dette qui augmente serait forcément une catastrophe.", "À partir de quel niveau une dette devient un problème.", "Ce qui pourrait faire baisser la dette."],
      "Elle montre", "Elle ne montre pas"),
     liste_sources([
       f'<strong>Insee</strong>, la dette trimestrielle de Maastricht des administrations publiques, dernière publication. Le montant de la dette, en milliards d\'euros et en part du PIB. {a("insee_dette_trim")}',
       f'<strong>Insee</strong>, définition de la dette publique au sens de Maastricht. {a("insee_dette_def")}',
       '<span class="gris">Les graphiques de la vidéo (la dette et le déficit de la France depuis 2004, puis la dette dans la zone euro) ont été faits par Marin Ferry ; leurs sources et leurs données sont à ajouter ici.</span>',
     ]),
     tableau([
       ["Dette publique au sens de Maastricht, fin du deuxième trimestre 2026", "3 595,5 milliards €", "vérifié dans la source le 25 novembre 2026 : Insee, Informations rapides n° 239, 29 septembre 2026"],
       ["La même dette, rapportée au produit intérieur brut (PIB)", "119,0 %", "idem ; le PIB est la richesse produite en France en un an"],
     ]),
     rel_auteur("Marin Ferry"))

# =====================================================================================
# 5. Taille des classes (Hanna)
fc = F["classes"]
tennessee = barres_h("c1", "Project STAR, Tennessee : 43,7 % des élèves passés par une petite classe ont passé l'examen d'entrée à l'université, contre 40,0 % des élèves des classes normales.",
    [("Petites classes\n13 à 17 élèves", 43.7, "43,7 %", True), ("Classes normales\n22 à 25 élèves", 40.0, "40,0 %", False)],
    50, [0, 10, 20, 30, 40, 50], lambda v: f"{v} %", "part des élèves qui passent l'examen d'entrée à l'université", label_w=190)
cp = barres_h("c2", "CP dans les écoles les plus défavorisées : 22 élèves par classe avant 2017, 13 après le dédoublement.",
    [("CP avant 2017", 22, "22 élèves", False), ("CP dédoublé", 13, "13 élèves", True)],
    25, [0, 5, 10, 15, 20, 25], lambda v: str(v), "élèves par classe, éducation prioritaire renforcée (REP+)", label_w=150)

page("taille-des-classes.html", "Moins d'élèves par classe, ça marche ?",
     "Réduire la taille des classes aide les plus jeunes élèves ; au lycée, personne ne l'a mesuré. Résumé, graphiques et sources de la vidéo de Hanna Bony : Tennessee, et les CP dédoublés en France.",
     "Éducation · à paraître le mardi 1<sup>er</sup> décembre",
     "Au lycée général, en France, il y a en moyenne trente élèves par classe. En CP dans les quartiers les plus pauvres : treize. Est-ce que moins d'élèves, ça donne de meilleurs résultats ?",
     "à paraître le mardi 1<sup>er</sup> décembre 2026 · carrousel le samedi 5 décembre",
     [("La question", "Moins d'élèves par classe, est-ce que ça donne de meilleurs résultats ?"),
      ("La réponse", "Pour les plus jeunes, oui : deux expériences le montrent. Au lycée, personne ne l'a mesuré."),
      ("Résumé", "Au lycée général, en France, il y a en moyenne une trentaine d'élèves par classe ; en CP dans les écoles les plus défavorisées, treize. Est-ce que ça change les résultats ? Ça a été testé. Au Tennessee, à partir de 1985, 11 600 enfants ont été tirés au sort dans des classes d'environ quinze ou d'environ vingt-trois élèves : dans les petites classes, ils progressent plus, et à dix-huit ans, ils sont plus nombreux à passer l'examen d'entrée à l'université. En France, depuis 2017, les CP des écoles les plus défavorisées sont passés de vingt-deux à treize élèves : deux ans après, ces élèves avaient rattrapé une partie de leur retard ; pour la première génération, la différence n'était plus visible à l'entrée en sixième. Ces deux expériences portent sur l'école primaire. Au lycée, personne n'a fait le test."),
      ("Avec", HB),
      ("Source principale", f'<span class="crochet long">{a("krueger_whitmore", "Krueger et Whitmore, 2001, Economic Journal")}</span> <span class="crochet long">{a("depp_2026", "DEPP, Synthèse n° 8, 2026")}</span>'),
      ("La limite", "Les deux expériences portent sur l'école primaire. En France, l'effet est net en fin de CE1, puis s'estompe : à l'entrée en sixième, il a disparu en français et reste faible en maths. Pour une terminale à trente, la recherche ne sait pas encore répondre."),
      ("Thème", '<a href="education.html">Éducation</a>'),
      ("Légende publiée", '<span class="gris">Des classes moins chargées, ça marche ? Au primaire oui, surtout pour les élèves défavorisés ; au lycée, on ne sait presque rien. Avec Hanna Bony, doctorante en économie à l\'Université Gustave Eiffel. Les prises de position n\'engagent que leur auteur.</span>')],
     f'''<p class="chapeau">Réduire la taille des classes revient dans chaque débat sur l'école. C'est l'une des rares mesures éducatives qui ont été testées avec un vrai tirage au sort. Voici ce qu'on a trouvé, et où s'arrêtent les résultats.</p>

  <p><strong>Le Tennessee, 1985.</strong> L'expérience s'appelle Project STAR. Pendant leurs premières années d'école, 11 600 enfants sont répartis au hasard entre des petites classes, de 13 à 17 élèves, et des classes normales, de 22 à 25. Comme le hasard a fait les groupes, la seule différence entre eux, c'est la taille de la classe. Des années plus tard, les chercheurs regardent combien passent l'examen d'entrée à l'université.</p>

  <figure class="figure">
    {tennessee}
    <figcaption>Les élèves passés par une petite classe sont un peu plus nombreux à passer l'examen d'entrée à l'université. L'échelle part de zéro : l'écart est réel, mais modeste.<span class="src">[Krueger et Whitmore, 2001, Economic Journal · Project STAR]</span></figcaption>
  </figure>

  <p><strong>La France, 2017.</strong> Dans les écoles de l'éducation prioritaire renforcée, les classes de CP, puis de CE1, sont coupées en deux. Le ministère de l'Éducation nationale compare ces élèves à des élèves semblables d'écoles qui n'ont pas été dédoublées.</p>

  <figure class="figure">
    {cp}
    <figcaption>Le dédoublement des CP : de 22 à 13 élèves par classe dans les écoles les plus défavorisées.<span class="src">[DEPP · rentrée 2017]</span></figcaption>
  </figure>

  <div class="tuiles">
    <div class="tuile"><div class="chiffre">16 %</div><p class="quoi">du retard rattrapé, en français</p><p>En fin de CE1, l'effet du dédoublement équivaut à 16 % de l'écart qui séparait, à l'entrée en CP, ces élèves de ceux des écoles hors éducation prioritaire.</p></div>
    <div class="tuile"><div class="chiffre">38 %</div><p class="quoi">du retard rattrapé, en maths</p><p>Même mesure, en mathématiques.</p></div>
  </div>

  <p>Et ensuite ? Pour la première génération d'élèves des CP dédoublés, on ne mesure plus de différence à l'entrée en sixième. Une étude publiée par la DEPP en octobre 2026, sur les trois premières générations, trouve un petit effet positif en maths à l'entrée en sixième, qui grandit d'une génération à l'autre, et aucun effet durable en français.</p>

  <div class="adecider">
    <span class="etiquette">À CORRIGER DANS LE SCRIPT</span>
    <p>Deux phrases de la vidéo ne collent pas tout à fait aux études. « Le retard avait reculé de seize pour cent en français, de trente-huit pour cent en maths » : la DEPP dit que l'effet équivaut à 16 % et 38 % de l'écart de départ ; on peut dire « ces élèves avaient rattrapé un sixième de leur retard en français, plus d'un tiers en maths ». « En sixième, on ne mesure plus de différence » : c'est vrai pour la première génération seulement ; l'étude d'octobre 2026 trouve un petit effet en maths pour les suivantes. Cet encadré disparaîtra quand la vidéo sera corrigée.</p>
  </div>

  <p>Les deux expériences vont dans le même sens : pour les plus jeunes, et surtout pour les élèves défavorisés, des classes plus petites aident. Mais l'effet s'estompe avec le temps en France, et aucune expérience comparable n'a été menée au lycée. Pour une terminale à trente élèves, la recherche ne sait pas encore répondre.</p>''',
     ("Ce qu'elle montre, ce qu'elle ne montre pas",
      ["Que la taille des classes a été testée avec un vrai tirage au sort, au Tennessee.", "Qu'au primaire, des classes plus petites améliorent les résultats, surtout pour les élèves défavorisés.", "Qu'en France, l'effet du dédoublement des CP est net en fin de CE1, puis s'estompe."],
      ["Ce qui se passerait au lycée : personne ne l'a mesuré.", "Si réduire les classes est la meilleure façon de dépenser le même argent.", "Pourquoi l'effet s'estompe en France, ni s'il durera au-delà de la sixième."],
      "Elle montre", "Elle ne montre pas"),
     liste_sources([
       f'<strong>Krueger A. B. et Whitmore D. M.</strong>, « The Effect of Attending a Small Class in the Early Grades on College-Test Taking and Middle School Test Results: Evidence from Project STAR », <em>The Economic Journal</em>, 2001. Les 43,7 % contre 40,0 %. {a("krueger_whitmore")}',
       f'<strong>Krueger A. B.</strong>, « Experimental Estimates of Education Production Functions », <em>Quarterly Journal of Economics</em>, 1999. L\'analyse de référence de Project STAR. {a("krueger1999")}',
       f'<strong>DEPP</strong> (service statistique du ministère de l\'Éducation nationale), Charpentier A., « Réduction de la taille de classe en éducation prioritaire : que nous apprennent les données de la DEPP ? », <em>Synthèse</em> n° 8, février 2026. Les 16 % et 38 % en fin de CE1 (d\'après Andreu et co-auteurs, document de travail 2021.E04), et l\'absence de différence en sixième pour la première génération. Accès libre. {a("depp_2026")}',
       f'<strong>DEPP</strong>, El Bah, « Les effets à long terme de la réduction de la taille de classe en éducation prioritaire », document de travail n° 2026-E18, 13 octobre 2026 : les trois premières générations à l\'entrée en sixième. Accès libre. {a("depp_2026_oct")}',
       f'<strong>DEPP</strong>, <em>Note d\'information</em> n° 26.38, août 2026 : 30,2 élèves par classe en moyenne dans les formations générales et technologiques des lycées, à la rentrée 2025. Accès libre. {a("depp_lycee")}',
       f'<strong>Fredriksson P., Öckert B. et Oosterbeek H.</strong>, « Long-Term Effects of Class Size », <em>Quarterly Journal of Economics</em>, 2013. Les effets à long terme en Suède, présentés dans le carrousel. {a("fredriksson")}',
     ]),
     f'''<h3>Les bases de données utilisées</h3>

  <ul>
    <li><strong>Project STAR</strong> (Tennessee, 1985-1989) : les données de l'expérience sont publiques et ont été réanalysées par de nombreux chercheurs ; elles sont décrites dans les articles de Krueger.</li>
    <li><strong>Les évaluations nationales de CP et de CE1</strong> (DEPP), qui servent à comparer les élèves des classes dédoublées à des élèves comparables.</li>
  </ul>

  <h3>Nos calculs, à télécharger</h3>

  <ul>
    <li><a href="../donnees/taille-des-classes.csv" download>taille-des-classes.csv</a> : tous les chiffres de la vidéo, avec leur source et leur statut.</li>
  </ul>

  {tableau([
       ["Élèves de l'expérience Project STAR", "11 600", verif("star_eleves")],
       ["Taille des classes, Tennessee", "13-17 contre 22-25", verif("star_tailles")],
       ["Examen d'entrée à l'université, petites classes contre classes normales", "43,7 % contre 40,0 %", verif("star_examen")],
       ["CP en éducation prioritaire renforcée", "22 puis 13 élèves", verif("cp_taille")],
       ["Effet du dédoublement en fin de CE1, en part de l'écart de départ, français et maths", "16 % et 38 %", verif("cp_effet")],
       ["Élèves par classe au lycée général et technologique", fc["lycee_txt"], verif("lycee")],
     ])}''',
     [("Écriture du script", "Hanna Bony", "fait"), ("Relecture scientifique extérieure", "à compléter", "demandée"),
      ("Relecture par le comité", "à compléter", "en cours"), ("Validation technique (sous-titres, habillage, sources à l'écran)", "à compléter", "en cours"),
      ("Accord de la chercheuse sur la version montée", "Hanna Bony", "en cours")])

# =====================================================================================
# 6. Le Français « moyen » (Hanna) — remplace la page pilote
salaires = barres_h("m1", "Salaire net mensuel en équivalent temps plein, secteur privé, 2025 : moyenne 2 797 euros, médiane 2 238 euros.",
    [("Moyenne", 2797, "2 797 €", False), ("Médiane", 2238, "2 238 €", True)],
    3000, [0, 1000, 2000, 3000], lambda v: "0" if v == 0 else f"{v//1000} 000 €", "salaire net par mois, équivalent temps plein, secteur privé, 2025", label_w=120)

page("moyenne-mediane.html", "Le Français « moyen » existe-t-il ?",
     "Le salaire moyen dans le privé est de 2 797 euros net, le salaire médian de 2 238 euros : la moyenne n'est pas le milieu. Résumé, graphique et sources de la vidéo de Hanna Bony.",
     "Comprendre les chiffres · à paraître le dimanche 6 décembre",
     "L'Insee vient de publier le salaire moyen dans le privé : deux mille sept cent quatre-vingt-dix-sept euros net par mois. Vous gagnez moins ? Vous êtes comme la majorité des salariés.",
     "à paraître le dimanche 6 décembre 2026 · carrousel le lundi 7 décembre",
     [("La question", "Quand on dit « salaire moyen », est-ce que la moitié des gens gagnent moins ?"),
      ("La réponse", "Non. La moyenne n'est pas le milieu. Le milieu, c'est la médiane, et elle est nettement plus basse : plus de la moitié des salariés gagnent moins que le salaire moyen."),
      ("Résumé", "L'Insee a publié en octobre 2026 le salaire moyen dans le secteur privé en 2025 : 2 797 euros net par mois, en équivalent temps plein. Une moyenne, c'est tous les salaires additionnés, puis divisés par le nombre de salariés : les très hauts salaires tirent le résultat vers le haut. L'autre chiffre, c'est la médiane, le salaire du milieu : la moitié des salariés gagne moins, la moitié gagne plus. Elle est de 2 238 euros, soit 559 euros de moins que la moyenne. C'est la médiane qui dit où l'on se situe par rapport aux autres. Quand on vous parle du Français moyen, demandez : la moyenne, ou le milieu ?"),
      ("Avec", HB),
      ("Source principale", f'<span class="crochet long">{a("insee_salaires", "Insee Première n° 2132, octobre 2026")}</span>'),
      ("La limite", "Aucun des deux chiffres n'est faux : ils ne répondent pas à la même question. Et les deux portent sur les salariés du privé, en équivalent temps plein."),
      ("Thème", '<a href="comprendre-les-chiffres.html">Comprendre les chiffres</a>'),
      ("Notion", '<a href="../notions.html#moyenne-mediane">Moyenne et médiane</a>'),
      ("Légende publiée", '<span class="gris">Le salaire du « Français moyen » existe-t-il ? La moyenne (2 797 €) dépasse la médiane (2 238 €) : plus de la moitié des salariés du privé gagnent moins que la moyenne. Avec Hanna Bony, doctorante en économie à l\'Université Gustave Eiffel. Les prises de position n\'engagent que leur auteur.</span>')],
     f'''<p class="chapeau">Deux chiffres résument les salaires du privé en France. Ils sont tous les deux justes, et ils ne disent pas la même chose.</p>

  <p>La <strong>moyenne</strong>, c'est la somme de tous les salaires divisée par le nombre de salariés. Une poignée de très hauts salaires pèse donc très lourd dans l'addition, et tire la moyenne vers le haut.</p>

  <p>La <strong>médiane</strong>, c'est le milieu : on range tous les salariés du plus petit salaire au plus grand, et on prend celui du centre. La moitié gagne moins, la moitié gagne plus. Elle ne bouge pas quand les plus hauts salaires augmentent.</p>

  <figure class="figure">
    {salaires}
    <figcaption>En 2025, le salaire médian du privé est inférieur de 559 euros au salaire moyen. Plus de la moitié des salariés gagnent donc moins que la moyenne.<span class="src">[Insee Première n° 2132, octobre 2026 · salariés du privé, net, équivalent temps plein]</span></figcaption>
  </figure>

  <p>La prochaine fois qu'on vous parle du salaire « moyen », demandez lequel des deux on vous donne. Pour savoir où vous vous situez par rapport aux autres, c'est la médiane qu'il vous faut.</p>''',
     ("Ce qu'elle montre, ce qu'elle ne montre pas",
      ["Que la moyenne et la médiane des salaires sont deux chiffres différents, calculés différemment.", "Que la médiane est plus basse que la moyenne, parce que les très hauts salaires tirent la moyenne vers le haut.", "Que « gagner moins que la moyenne » ne veut pas dire « être dans la moitié basse »."],
      ["Ce que gagnent les fonctionnaires ou les indépendants : les chiffres portent sur les salariés du privé.", "Ce que gagnent les personnes à temps partiel : les salaires sont ramenés à un temps plein.", "Comment les salaires ont évolué : c'est une photographie d'une année."],
      "Elle montre", "Elle ne montre pas"),
     liste_sources([
       f'<strong>Insee</strong>, « Les salaires dans le secteur privé en 2025 », <em>Insee Première</em> n° 2132, 22 octobre 2026. Salaire net moyen (2 797 €) et médian (2 238 €) en équivalent temps plein. Accès libre. {a("insee_salaires")}',
     ]),
     f'''<h3>Les bases de données utilisées</h3>

  <ul>
    <li><strong>Insee, base Tous salariés</strong>, construite à partir des déclarations sociales des employeurs. C'est la base d'où viennent les deux chiffres. Champ : France, salariés du privé, y compris alternants, stagiaires et contrats aidés, hors agriculture et particuliers employeurs. {a("insee_salaires_xlsx", "Fichier des données de la publication")}.</li>
  </ul>

  <h3>Nos calculs, à télécharger</h3>

  <ul>
    <li><a href="../donnees/salaires-2025.csv" download>salaires-2025.csv</a> : les deux chiffres de l'Insee, leur champ, leur source, et l'écart calculé.</li>
  </ul>

  {tableau([
       ["Salaire net moyen, équivalent temps plein, secteur privé, 2025", "2 797 € / mois", verif("salaire_moyen")],
       ["Salaire net médian, équivalent temps plein, secteur privé, 2025", "2 238 € / mois", verif("salaire_median")],
       ["Écart entre la moyenne et la médiane", "559 €", "calcul : 2 797 − 2 238 ; l'Insee écrit que la médiane est inférieure de 20,0 % à la moyenne"],
       ["Part des salariés qui gagnent moins que la moyenne", "entre 60 % et 70 %", "notre calcul, d'après les déciles de l'Insee : 60 % gagnent moins de 2 497 €, 70 % moins de 2 850 €, et la moyenne (2 797 €) est entre les deux"],
     ])}''',
     REL_HANNA)

# =====================================================================================
# 7. Migrant ou réfugié (Marine)
fm = F["migr"]
cercles = svg("r1", "Un grand ensemble, les migrants, contient un ensemble plus petit, les réfugiés. L'étudiante espagnole, le jeune paysan chinois et la famille syrienne sont des migrants ; le journaliste menacé est un migrant et un réfugié.", 640, 330,
    f'<ellipse cx="320" cy="172" rx="300" ry="150" fill="{ENCRE}" fill-opacity="0.06" stroke="{ENCRE}" stroke-width="2.5"/>'
    f'<circle cx="470" cy="185" r="85" fill="{JAUNE}" fill-opacity="0.6" stroke="{ENCRE}" stroke-width="2.5"/>' +
    texte(320, 52, "MIGRANTS", 15, gras=True) + texte(320, 70, "toute personne qui part vivre ailleurs", 12, cls="gris") +
    texte(470, 150, "RÉFUGIÉS", 14, gras=True) + texte(470, 168, "un statut du", 12) + texte(470, 183, "droit international", 12) +
    texte(470, 215, "le journaliste", 12, gras=True) + texte(470, 230, "menacé", 12, gras=True) +
    texte(200, 115, "l'étudiante espagnole", 13, gras=True) + texte(200, 131, "venue étudier à Paris", 12, cls="gris") +
    texte(200, 180, "le jeune paysan chinois", 13, gras=True) + texte(200, 196, "parti travailler en ville", 12, cls="gris") +
    texte(200, 245, "la famille syrienne", 13, gras=True) + texte(200, 261, "qui fuit la guerre", 12, cls="gris"))

parcours = svg("r2", "Le parcours en France : on dépose une demande d'asile à l'Ofpra ; en attendant, on est demandeur d'asile ; si la réponse est oui, on est reconnu réfugié, ou on reçoit une autre protection.", 640, 170,
    boite(10, 45, 180, 70, [("Demande d'asile", True), ("déposée à l'Ofpra", False)], "noir") + fleche(194, 80, 226, 80) +
    boite(230, 45, 180, 70, [("Demandeur", True), ("d'asile, en attendant", False)], "noir") + fleche(414, 70, 446, 50) + fleche(414, 95, 446, 120) +
    boite(450, 20, 180, 55, [("Réfugié reconnu", True)], "jaune") +
    boite(450, 90, 180, 55, [("Autre protection", True), ("ou refus", False)], "clair") +
    texte(320, 165, "Ofpra : Office français de protection des réfugiés et apatrides", 12, cls="gris"))

page("migrant-ou-refugie.html", "Migrant ou réfugié : est-ce la même chose ?",
     "Migrant est un mot large, sans définition officielle ; réfugié est un statut défini par la Convention de Genève de 1951. Tous les migrants ne sont pas des réfugiés. Résumé, schémas et sources de la vidéo de Marine de Talancé.",
     "Immigration · épisode 2 · à paraître le lundi 7 décembre",
     "Crise des migrants ou crise des réfugiés ? Qui a raison ?",
     "à paraître le lundi 7 décembre 2026 · carrousel le mardi 8 décembre",
     [("La question", "Migrant et réfugié, est-ce la même chose ?"),
      ("La réponse", "Non. « Migrant » est un mot large, sans définition officielle : toute personne qui part vivre ailleurs. « Réfugié » est un statut précis, défini par la Convention de Genève de 1951. Tous les réfugiés sont des migrants ; tous les migrants ne sont pas des réfugiés."),
      ("Résumé", f"En 2015, {fm['arrivees_2015_phrase']} sont arrivées en Europe, beaucoup fuyant la guerre en Syrie. On a parlé de crise des migrants, ou de crise des réfugiés. Qui a raison ? « Migrant » désigne toute personne qui part vivre ailleurs, quelle qu'en soit la raison : une étudiante espagnole venue étudier à Paris, une famille syrienne qui fuit la guerre, un jeune paysan chinois parti travailler en ville. « Réfugié », au contraire, est un statut défini par le droit international : une personne qui a fui son pays parce qu'elle risque d'y être persécutée pour l'un de cinq motifs, et que son pays ne peut pas la protéger. En France, c'est l'Ofpra qui le reconnaît ; en attendant, on est demandeur d'asile. Fuir la guerre ou une sécheresse ne suffit pas : d'autres protections existent. En France, environ un immigré sur dix est venu chercher une protection. Les deux expressions ne sont pas fausses : elles ne mettent pas l'accent sur la même chose."),
      ("Avec", MT),
      ("Source principale", f'<span class="crochet long">{a("convention_1951", "Convention de Genève, 1951, article 1 A(2)")}</span>'),
      ("La limite", "La vidéo explique les mots, pas les chiffres : combien de migrants ou de réfugiés vivent en France dépend de qui compte, et de comment."),
      ("Thème", '<a href="immigration.html">Immigration</a> · épisode 2 · avant : <a href="immigre-ou-etranger.html">immigré ou étranger</a>')],
     f'''<p class="chapeau">« Crise des migrants » ou « crise des réfugiés » : en 2015, les deux expressions ont circulé pour parler des mêmes arrivées en Europe. Elles ne sont pas fausses, mais elles ne disent pas la même chose.</p>

  <p><strong>Migrant</strong> est un mot large, sans définition juridique : il désigne toute personne qui part vivre ailleurs, dans son pays ou dans un autre, quelle qu'en soit la raison. <strong>Réfugié</strong> est un statut précis, défini par la Convention de Genève de 1951. Le second est donc un cas particulier du premier.</p>

  <figure class="figure">
    {cercles}
    <figcaption>Tous les réfugiés sont des migrants ; tous les migrants ne sont pas des réfugiés. Seul le journaliste menacé pour ses articles peut être reconnu réfugié.<span class="src">[schéma · exemples de la vidéo]</span></figcaption>
  </figure>

  <p>Pour être reconnu réfugié, il faut avoir fui son pays parce qu'on risque d'y être persécuté pour l'un de ces cinq motifs, et que son pays ne peut pas, ou ne veut pas, vous protéger :</p>

  <ul>
    <li>sa « race », que le Haut-Commissariat des Nations unies pour les réfugiés (HCR) entend au sens large, y compris l'origine ethnique ;</li>
    <li>sa religion ;</li>
    <li>sa nationalité ;</li>
    <li>son appartenance à un groupe social ;</li>
    <li>ses opinions politiques.</li>
  </ul>

  <p>Fuir la guerre ne suffit donc pas, à lui seul : il faut un risque de persécution pour l'un de ces motifs. Sinon, d'autres protections existent en France et dans l'Union européenne, dites subsidiaire ou temporaire. Le droit international ne reconnaît pas non plus de « réfugié climatique ».</p>

  <figure class="figure">
    {parcours}
    <figcaption>En France, c'est l'Ofpra qui reconnaît le statut de réfugié. En attendant sa réponse, la personne est demandeuse d'asile.<span class="src">[service-public.gouv.fr · schéma]</span></figcaption>
  </figure>

  <div class="tuiles">
    <div class="tuile jaune"><div class="chiffre">{fm['protection_txt']}</div><p class="quoi">des immigrés arrivés en France après 15 ans</p><p>sont venus en France pour chercher une protection. Les autres sont surtout venus pour travailler, étudier ou rejoindre leur famille.</p></div>
    <div class="tuile"><div class="chiffre">5</div><p class="quoi">motifs de persécution</p><p>ouvrent droit au statut de réfugié, selon la Convention de Genève de 1951.</p></div>
  </div>

  <p>Alors, crise des migrants ou crise des réfugiés ? Aucune des deux expressions n'est fausse. La première parle de tous ceux qui sont partis ; la seconde met l'accent sur ceux qui fuyaient une persécution.</p>''',
     ("Ce qu'elle montre, ce qu'elle ne montre pas",
      ["Que « migrant » est un mot large et que « réfugié » est un statut juridique précis.", "Les cinq motifs de persécution qui ouvrent droit au statut de réfugié.", "Que fuir la guerre ou le climat ne suffit pas à être reconnu réfugié, mais que d'autres protections existent."],
      ["Combien de migrants ou de réfugiés vivent en France : ça dépend de qui compte.", "Combien de demandes d'asile sont acceptées.", "Ce que les politiques d'asile devraient être."],
      "Elle montre", "Elle ne montre pas"),
     liste_sources([
       f'<strong>Convention relative au statut des réfugiés</strong>, Genève, 28 juillet 1951, article 1 A(2) : la définition du réfugié. {a("convention_1951")}',
       f'<strong>HCR</strong> (Haut-Commissariat des Nations unies pour les réfugiés), <em>Guide des procédures et critères à appliquer pour déterminer le statut de réfugié</em>, 1979, réédité, paragraphes 28, 34, 68 et 164-165. {a("hcr_guide")}',
       f'<strong>Organisation internationale pour les migrations (OIM)</strong>, « Termes clés de la migration » : la définition de « migrant ». {a("oim_termes")}',
       f'<strong>OIM</strong>, les arrivées en Europe en 2015. {a("oim_2015")}',
       f'<strong>Service-public.gouv.fr</strong>, « Statut de réfugié » : qui peut l\'obtenir en France. {a("service_public_refugie")}',
       f'<strong>Insee</strong>, les raisons de l\'arrivée en France des immigrés arrivés à 15 ans ou plus. {a("insee_motifs")}',
       f'<strong>Ofpra</strong>, rapport d\'activité : les personnes placées sous sa protection. {a("ofpra")}',
       f'<strong>Unesco</strong>, « Migrants, réfugiés ou déplacés ? ». {a("unesco")}',
     ]),
     f'''{tableau([
       ["Arrivées en Europe en 2015", fm["arrivees_2015_txt"], verif("oim_2015")],
       ["Part des immigrés arrivés à 15 ans ou plus venus chercher une protection", fm["protection_txt"], verif("protection")],
       ["Personnes protégées par l'Ofpra", fm["ofpra_txt"], verif("ofpra")],
     ])}''',
     rel_auteur("Marine de Talancé", "de la chercheuse"))
