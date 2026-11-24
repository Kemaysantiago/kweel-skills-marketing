#!/usr/bin/env python3
"""Monta e valida nomes no padrão de nomenclatura Kweel.

Uso:
  nomear.py campanha <nome> <etapa> <tipo>
  nomear.py grupo <tipo> <etapa> <publico> <idade-persona-local> <objetivo>
  nomear.py anuncio <objetivo> <sobre> <cta> <numero>
  nomear.py validar "<nome>"
  nomear.py utm <campanha> <grupo> [<anuncio>]   (gera sufixo para Google Ads)
"""
import re
import sys
import unicodedata
from urllib.parse import quote

ETAPAS = {"topo", "meio", "fundo"}
PUBLICOS = {"pi", "pp", "ll", "rmkt", "lista", "adv"}
TIPOS = {"pesquisa", "pmax", "display", "video", "conversao", "trafego",
         "engajamento", "whatsapp", "mensagens", "cadastro"}
OBJETIVOS = {"lead", "agendamento", "whatsapp", "ligacao", "venda",
             "cadastro", "posicionamento"}


def slug(txt: str) -> str:
    txt = unicodedata.normalize("NFKD", txt).encode("ascii", "ignore").decode()
    txt = re.sub(r"[^a-zA-Z0-9]+", "-", txt.lower()).strip("-")
    return txt


def bloco(*partes: str) -> str:
    return "".join(f"[{slug(p)}]" for p in partes)


def blocos(nome: str):
    if not re.fullmatch(r"(\[[^\[\]]+\])+", nome):
        return None
    return re.findall(r"\[([^\[\]]+)\]", nome)


def validar(nome: str) -> list:
    erros = []
    partes = blocos(nome)
    if partes is None:
        return ["formato inválido: use blocos [assim][sem][espaco-entre-blocos]"]
    for p in partes:
        if p != slug(p):
            erros.append(f"bloco [{p}] fora do padrão; sugestão: [{slug(p)}]")
    norm = [slug(p) for p in partes]
    if norm[0] == "kweel":
        if len(norm) != 4:
            erros.append("campanha deve ter 4 blocos: [kweel][nome][etapa][tipo]")
        else:
            if norm[2] not in ETAPAS:
                erros.append(f"etapa '{norm[2]}' inválida ({', '.join(sorted(ETAPAS))})")
            if norm[3] not in TIPOS:
                erros.append(f"tipo '{norm[3]}' fora da lista ({', '.join(sorted(TIPOS))})")
    elif norm[0] == "cpc":
        if len(norm) != 6:
            erros.append("grupo deve ter 6 blocos: [cpc][tipo][etapa][publico][idade-persona-local][objetivo]")
        else:
            if norm[1] not in TIPOS:
                erros.append(f"tipo '{norm[1]}' fora da lista")
            if norm[2] not in ETAPAS:
                erros.append(f"etapa '{norm[2]}' inválida")
            if norm[3] not in PUBLICOS:
                erros.append(f"público '{norm[3]}' inválido ({', '.join(sorted(PUBLICOS))})")
            if not re.match(r"^\d{2}-\d{2}-", norm[4]):
                erros.append(f"'{norm[4]}' deve começar com idade mín-máx, ex.: 25-60-tema-praca")
            if norm[5] not in OBJETIVOS:
                erros.append(f"objetivo '{norm[5]}' fora da lista ({', '.join(sorted(OBJETIVOS))})")
    else:
        if len(norm) != 4:
            erros.append("anúncio deve ter 4 blocos: [objetivo][sobre][cta][01]")
        else:
            if norm[0] not in OBJETIVOS:
                erros.append(f"objetivo '{norm[0]}' fora da lista")
            if not re.fullmatch(r"\d{2}", norm[3]):
                erros.append("identificador deve ter 2 dígitos, ex.: [01]")
    return erros


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    cmd, args = argv[1], argv[2:]
    if cmd == "campanha" and len(args) == 3:
        nome = bloco("kweel", *args)
    elif cmd == "grupo" and len(args) == 5:
        nome = bloco("cpc", *args)
    elif cmd == "anuncio" and len(args) == 4:
        nome = bloco(args[0], args[1], args[2], f"{int(args[3]):02d}")
    elif cmd == "validar" and len(args) == 1:
        erros = validar(args[0])
        print("OK" if not erros else "\n".join("✗ " + e for e in erros))
        return 0 if not erros else 2
    elif cmd == "utm" and len(args) in (2, 3):
        partes = [("utm_source", "google"), ("utm_medium", args[1]),
                  ("utm_campaign", args[0]),
                  ("utm_content", args[2] if len(args) == 3 else "{adgroupid}-{creative}")]
        print("&".join(f"{k}={quote(v, safe='[]-{}')}" for k, v in partes))
        return 0
    else:
        print(__doc__)
        return 1
    print(nome)
    erros = validar(nome)
    for e in erros:
        print("✗ " + e, file=sys.stderr)
    return 0 if not erros else 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
