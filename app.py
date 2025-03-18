from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import random
import string
from procesar import procesar
app = Flask(__name__)
app.secret_key = os.urandom(24)
from hashlib import sha256



def generar_sustitucion(clave: str):
    """
    Cifra un texto utilizando el algoritmo MHA
    La clave debe ser una cadena de texto de 26 caracteres (sin contar espacios, signos de puntuación o caracteres especiales).
    """
    clave = procesar(clave)
    while len(clave) < 26:
        clave *= 2
    
    clave = clave[:26]
    deltas = [ord(letra) - ord('A') + 1 for letra in clave]
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sustitucion = alfabeto
    
    for i in range(len(clave)):
        letra = alfabeto[i]
        posicion = (deltas[i] + i)%26
        sustitucion = sustitucion[:sustitucion.find(letra)] + sustitucion[sustitucion.find(letra)+1:] # quitamos la letra
        sustitucion = sustitucion[:posicion] + letra + sustitucion[posicion:] # la añadimos en la posicion que corresponde

    return sustitucion

def cifrar(texto: str, clave: str):
    texto = procesar(texto)
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sustitucion = generar_sustitucion(clave)
    return texto.translate(str.maketrans(alfabeto, sustitucion))


def descifrar(texto_cifrado: str, clave: str):
    """
    Descifra un texto usando MHA
    """
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sustitucion = generar_sustitucion(clave)
    return texto_cifrado.translate(str.maketrans(sustitucion, alfabeto))

# Rutas de la aplicación
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cifrar', methods=['GET', 'POST'])
def cifrar_texto():
    resultado = None
    if request.method == 'POST':
        texto = request.form.get('texto', '')
        clave = request.form.get('clave', '')
        
        try:
            resultado = cifrar(texto, clave)
        except ValueError as e:
            return render_template('cifrar.html', error=str(e))
        
    return render_template('cifrar.html', resultado=resultado)

@app.route('/descifrar', methods=['GET', 'POST'])
def descifrar_texto():
    resultado = None
    if request.method == 'POST':
        texto_cifrado = request.form.get('texto_cifrado', '')
        clave = request.form.get('clave', '')
        
        try:
            resultado = descifrar(texto_cifrado, clave)
        except ValueError as e:
            return render_template('descifrar.html', error=str(e))
        
    return render_template('descifrar.html', resultado=resultado)

@app.route('/reto', methods=['GET', 'POST'])
def reto():
    mensaje = None
    exito = None
    
    if request.method == 'POST':
        respuesta = request.form.get('respuesta', '')
        respuesta = procesar(respuesta)
        dificultad = request.form.get('dificultad')
        print(dificultad)
        with open(f'hash_{dificultad}.txt', 'r') as txt:
            hash_texto = txt.read()

        if sha256(respuesta.encode('utf8')).hexdigest() == hash_texto:
            mensaje = "¡Increíble! Has descifrado el texto."
            exito = True

        else:
            mensaje = "El texto descifrado no es correcto. Sigue intentándolo."
            exito = False
        
    return render_template('reto.html', mensaje=mensaje, exito=exito)

@app.route('/descargar_retos')
def descargar_reto():
    return send_file('retos.zip', as_attachment=True)

@app.route('/codigo_fuente')
def codigo_fuente():
    return render_template('codigo_fuente.html')

if __name__ == '__main__':
    app.run(debug=True)
