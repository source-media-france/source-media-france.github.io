# Petites fonctions SVG aux couleurs de la charte SOURCE ?
ENCRE, JAUNE, PAPIER, GRIS, GRISCLAIR, BLANC = "#111111", "#FFE500", "#F4F0E6", "#6B6B6B", "#DDDAD0", "#FFFFFF"

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def fr(n, dec=0):
    s = f"{n:,.{dec}f}".replace(",", " ").replace(".", ",")
    return s

DEFS = ('<defs><marker id="fl" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        '<path d="M0,0 L10,5 L0,10 z" fill="#111111"/></marker></defs>')

def barres_h(uid, titre_access, rows, vmax, ticks, fmt_tick, unite_axe=None, w=640, label_w=170):
    """rows = [(étiquette, valeur, texte_valeur, jaune?)] ; axe à partir de 0."""
    n = len(rows); bar_h = 40; gap = 22; top = 24
    plot_x0 = label_w; plot_x1 = w - 90
    h = top + n * (bar_h + gap) + 40 + (18 if unite_axe else 0)
    def X(v): return plot_x0 + v / vmax * (plot_x1 - plot_x0)
    s = [f'<svg viewBox="0 0 {w} {h}" role="img" aria-labelledby="{uid}" xmlns="http://www.w3.org/2000/svg">',
         f'<title id="{uid}">{esc(titre_access)}</title>']
    y_axis = top + n * (bar_h + gap) - gap + 8
    for v in ticks:
        x = X(v)
        s.append(f'<line x1="{x:.1f}" y1="{top-6}" x2="{x:.1f}" y2="{y_axis}" stroke="{GRISCLAIR}"/>')
        s.append(f'<text x="{x:.1f}" y="{y_axis+18}" font-size="13" text-anchor="middle" class="gris">{esc(fmt_tick(v))}</text>')
    if unite_axe:
        s.append(f'<text x="{(plot_x0+plot_x1)/2:.1f}" y="{y_axis+38}" font-size="13" text-anchor="middle" class="gris">{esc(unite_axe)}</text>')
    for i, (lab, v, txt, jaune) in enumerate(rows):
        y = top + i * (bar_h + gap)
        lines = lab.split("\n")
        for j, l in enumerate(lines):
            yy = y + bar_h / 2 + 5 + (j - (len(lines) - 1) / 2) * 17
            s.append(f'<text x="{label_w-12}" y="{yy:.1f}" font-size="15" text-anchor="end" class="gras">{esc(l)}</text>')
        fill = JAUNE if jaune else ENCRE
        s.append(f'<rect x="{plot_x0}" y="{y}" width="{X(v)-plot_x0:.1f}" height="{bar_h}" fill="{fill}"><title>{esc(lab.replace(chr(10)," "))} : {esc(txt)}</title></rect>')
        s.append(f'<text x="{X(v)+8:.1f}" y="{y+bar_h/2+6:.1f}" font-size="16" class="gras">{esc(txt)}</text>')
    s.append('</svg>')
    return "\n".join(s)

def boite(x, y, w, h, lignes, style="noir", fs=15):
    fill, col = {"noir": (ENCRE, BLANC), "jaune": (JAUNE, ENCRE), "clair": (BLANC, ENCRE)}[style]
    stroke = f' stroke="{ENCRE}" stroke-width="1.5"' if style == "clair" else ""
    s = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"{stroke}/>']
    n = len(lignes)
    for j, (txt, gras) in enumerate(lignes):
        yy = y + h / 2 + 5 + (j - (n - 1) / 2) * (fs + 4)
        fw = ' font-weight="700"' if gras else ''
        size = fs if gras else fs - 2
        cls = ' class="blanc"' if style == "noir" else ''
        s.append(f'<text x="{x+w/2}" y="{yy:.1f}" font-size="{size}" text-anchor="middle"{fw}{cls}>{esc(txt)}</text>')
    return "\n".join(s)

def fleche(x0, y0, x1, y1, w=3):
    return f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" stroke="{ENCRE}" stroke-width="{w}" marker-end="url(#fl)"/>'

def svg(uid, titre, w, h, body):
    return (f'<svg viewBox="0 0 {w} {h}" role="img" aria-labelledby="{uid}" xmlns="http://www.w3.org/2000/svg">' + DEFS +
            f'<title id="{uid}">{esc(titre)}</title>' + body + '</svg>')

def texte(x, y, txt, fs=14, anchor="middle", cls="", gras=False):
    fw = ' font-weight="700"' if gras else ''
    c = f' class="{cls}"' if cls else ''
    return f'<text x="{x}" y="{y}" font-size="{fs}" text-anchor="{anchor}"{fw}{c}>{esc(txt)}</text>'
