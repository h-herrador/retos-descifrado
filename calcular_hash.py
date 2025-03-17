import sys
from hashlib import sha256

with open(sys.argv[1], 'r') as txt:
    dificultad = 'semidios'
    reader = sha256(txt.read().encode('utf8')).hexdigest()
    print(reader)

with open(f'hash_{dificultad}.txt', 'w') as txt:
    txt.write(reader)