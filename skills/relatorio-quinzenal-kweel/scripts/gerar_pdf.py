#!/usr/bin/env python3
"""Gera o PDF do relatório no padrão Kweel, com cabeçalho e rodapé paginados.

Uso: gerar_pdf.py <entrada.html> <saida.pdf> "<CLIENTE>" "<email>"
Requer: pip install playwright && playwright install chromium
A capa (primeira página) sai sem cabeçalho e rodapé.
"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROXO = "#8a6d9e"


def main(entrada, saida, cliente, email):
    cliente = cliente.upper()
    estilo = "font-family:Arial,sans-serif;font-size:7.5pt;color:#6b6b6b;width:100%;padding:0 18mm;"
    header = (
        f'<div style="{estilo}display:flex;justify-content:space-between;">'
        f'<span style="color:{ROXO};font-weight:700;letter-spacing:.5px;">{cliente}</span>'
        '<span>RESULTADOS &amp; ESTRATÉGIA</span><span>CONFIDENCIAL KWEEL</span></div>'
    )
    footer = (
        f'<div style="{estilo}text-align:center;">Agência Kweel · {email} · '
        'Pág. <span class="pageNumber"></span></div>'
    )
    url = Path(entrada).resolve().as_uri()
    with sync_playwright() as p:
        nav = p.chromium.launch()
        pag = nav.new_page()
        pag.goto(url, wait_until="networkidle")
        capa = saida + ".capa.pdf"
        miolo = saida + ".miolo.pdf"
        comum = dict(format="A4", print_background=True,
                     margin={"top": "22mm", "bottom": "20mm", "left": "18mm", "right": "18mm"})
        pag.pdf(path=capa, page_ranges="1", **comum)
        pag.pdf(path=miolo, page_ranges="2-", display_header_footer=True,
                header_template=header, footer_template=footer, **comum)
        nav.close()
    try:
        from pypdf import PdfWriter
        w = PdfWriter()
        for f in (capa, miolo):
            w.append(f)
        w.write(saida)
        Path(capa).unlink(); Path(miolo).unlink()
    except ImportError:
        print("pypdf não instalado: capa e miolo ficaram em arquivos separados.", file=sys.stderr)
        return 1
    print(saida)
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(__doc__)
        sys.exit(1)
    sys.exit(main(*sys.argv[1:]))
