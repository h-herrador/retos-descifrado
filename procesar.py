import sys
import re
from unicodedata import normalize


def procesar(s):
    s = re.sub(
            r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
            normalize( "NFD", s), 0, re.I
        )
    s = normalize('NFC', s)
    s = s.replace("ñ", "n").replace("Ñ", "N")
    texto = ""
    for i in s:
        if i.isalpha():
            texto += i.upper()
    return texto

if __name__ == "__main__":
    with open(sys.argv[1], "r") as s:
        s = s.read()
        texto = procesar(s)

    with open("resultados.txt", "w") as txt:
        txt.write(texto)