import sys
import os
import random
import base64
import string
import hashlib
from passlib.hash import md5_crypt



#
import random

if not os.path.exists("Contraseñas"):
    os.mkdir("Contraseñas")
    os.mkdir("Contraseñas/a")
    os.mkdir("Contraseñas/b")
    os.mkdir("Contraseñas/c")
    os.mkdir("Contraseñas/d")
    os.mkdir("Contraseñas/e")
    os.mkdir("Contraseñas/a/md5crypt")
    os.mkdir("Contraseñas/a/sha512")
    os.mkdir("Contraseñas/b/md5crypt")
    os.mkdir("Contraseñas/b/sha512")
    os.mkdir("Contraseñas/c/md5crypt")
    os.mkdir("Contraseñas/c/sha512")
    os.mkdir("Contraseñas/d/md5crypt")
    os.mkdir("Contraseñas/d/sha512")
    os.mkdir("Contraseñas/e/md5crypt")
    os.mkdir("Contraseñas/e/sha512")
# Función para generar palabras aleatorias
def generar_palabra(longitud, solo_mins=False, solo_mayus=False,solo_nums=False, alfanum=False):
    caracteres=""
    if solo_mins:
        caracteres = string.ascii_lowercase
    elif solo_mayus:
        caracteres = string.ascii_uppercase
    elif solo_nums:
        caracteres = string.digits
    elif alfanum:
        caracteres = caracteres = string.ascii_lowercase + string.digits + string.ascii_uppercase + "!@#$%^&*()_-+=|;:,.<>?/\\"
    else:
        caracteres = string.ascii_lowercase + string.digits + string.ascii_uppercase
    return ''.join(random.choice(caracteres) for _ in range(random.choice(longitud)))

def random_capitalize(word):
    resultado = ""
    for letra in word:
        try: #Es un numero
            num=int(letra)
            resultado+=letra
        except: #Es una letra
            if random.choice([True, False]):  # Decidir aleatoriamente si convertir a mayúsculas
                resultado += letra.upper()
            else:
                resultado += letra.lower()
    return resultado

def tiene_numero(word):
    for letra in word:
        try:
            num=int(letra)
            return True
        except:
            pass
    return False

# a) sha512
for i in range(5):
    palabras_generadas = [generar_palabra([3,4,5,6,7], solo_mins=True) for _ in range(100)]
    random.shuffle(palabras_generadas)
    # Barajar la lista para que estén en orden aleatorio
    with open("contraseñas/a/sha512/"+str(i+1)+".txt", "w") as archivo:
        for palabra in palabras_generadas:
            archivo.write(palabra + "\n")
    with open("contraseñas/a/sha512/"+str(i+1)+"_hash.txt", "w") as archivo:
        for palabra in palabras_generadas:
            hash_obj = hashlib.sha512()
            hash_obj.update(palabra.encode())
            palabra=hash_obj.hexdigest()
            archivo.write(palabra + "\n")

## a) md5crypt
for i in range(5):
    palabras_generadas = [generar_palabra([3,4,5,6,7], solo_mins=True) for _ in range(100)]
    random.shuffle(palabras_generadas)
    # Barajar la lista para que estén en orden aleatorio
    with open("contraseñas/a/md5crypt/"+str(i+1)+".txt", "w") as archivo:
        for palabra in palabras_generadas:
            archivo.write(palabra + "\n")
    with open("contraseñas/a/md5crypt/"+str(i+1)+"_hash.txt", "w") as archivo:
        for palabra in palabras_generadas:
            palabra = md5_crypt.hash(palabra)
            archivo.write(palabra + "\n")


# b) sha512
for i in range(5):
    palabras_generadas = [generar_palabra([3,4,5,6,7], solo_mayus=True) for _ in range(100)]
    random.shuffle(palabras_generadas)
    # Barajar la lista para que estén en orden aleatorio
    with open("contraseñas/b/sha512/"+str(i+1)+".txt", "w") as archivo:
        for palabra in palabras_generadas:
            archivo.write(palabra + "\n")
    with open("contraseñas/b/sha512/"+str(i+1)+"_hash.txt", "w") as archivo:
        for palabra in palabras_generadas:
            hash_obj = hashlib.sha512()
            hash_obj.update(palabra.encode())
            palabra=hash_obj.hexdigest()
            archivo.write(palabra + "\n")

## b) md5crypt
for i in range(5):
    palabras_generadas = [generar_palabra([3,4,5,6,7], solo_mayus=True) for _ in range(100)]
    random.shuffle(palabras_generadas)
    # Barajar la lista para que estén en orden aleatorio
    with open("contraseñas/b/md5crypt/"+str(i+1)+".txt", "w") as archivo:
        for palabra in palabras_generadas:
            archivo.write(palabra + "\n")
    with open("contraseñas/b/md5crypt/"+str(i+1)+"_hash.txt", "w") as archivo:
        for palabra in palabras_generadas:
            palabra = md5_crypt.hash(palabra)
            archivo.write(palabra + "\n")

# c) sha512
for i in range(5):
    palabras_generadas = [generar_palabra([3,4,5,6,7], solo_nums=True) for _ in range(100)]
    random.shuffle(palabras_generadas)
    # Barajar la lista para que estén en orden aleatorio
    with open("contraseñas/c/sha512/"+str(i+1)+".txt", "w") as archivo:
        for palabra in palabras_generadas:
            archivo.write(palabra + "\n")
    with open("contraseñas/c/sha512/"+str(i+1)+"_hash.txt", "w") as archivo:
        for palabra in palabras_generadas:
            hash_obj = hashlib.sha512()
            hash_obj.update(palabra.encode())
            palabra=hash_obj.hexdigest()
            archivo.write(palabra + "\n")

## c) md5crypt
for i in range(5):
    palabras_generadas = [generar_palabra([3,4,5,6,7], solo_nums=True) for _ in range(100)]
    random.shuffle(palabras_generadas)
    # Barajar la lista para que estén en orden aleatorio
    with open("contraseñas/c/md5crypt/"+str(i+1)+".txt", "w") as archivo:
        for palabra in palabras_generadas:
            archivo.write(palabra + "\n")
    with open("contraseñas/c/md5crypt/"+str(i+1)+"_hash.txt", "w") as archivo:
        for palabra in palabras_generadas:
            palabra = md5_crypt.hash(palabra)
            archivo.write(palabra + "\n")


# d) sha512
for i in range(5):
    palabras_generadas = [generar_palabra([3,4,5,6,7], alfanum=True) for _ in range(100)]
    random.shuffle(palabras_generadas)
    # Barajar la lista para que estén en orden aleatorio
    with open("contraseñas/d/sha512/"+str(i+1)+".txt", "w") as archivo:
        for palabra in palabras_generadas:
            archivo.write(palabra + "\n")
    with open("contraseñas/d/sha512/"+str(i+1)+"_hash.txt", "w") as archivo:
        for palabra in palabras_generadas:
            hash_obj = hashlib.sha512()
            hash_obj.update(palabra.encode())
            palabra=hash_obj.hexdigest()
            archivo.write(palabra + "\n")

## d) md5crypt
for i in range(5):
    palabras_generadas = [generar_palabra([3,4,5,6,7], alfanum=True) for _ in range(100)]
    random.shuffle(palabras_generadas)
    # Barajar la lista para que estén en orden aleatorio
    with open("contraseñas/d/md5crypt/"+str(i+1)+".txt", "w") as archivo:
        for palabra in palabras_generadas:
            archivo.write(palabra + "\n")
    with open("contraseñas/d/md5crypt/"+str(i+1)+"_hash.txt", "w") as archivo:
        for palabra in palabras_generadas:
            palabra = md5_crypt.hash(palabra)
            archivo.write(palabra + "\n")

# Imprimir las palabras generadas



diccionario=datos="diccionario.txt"
diccionario_letras={'a': ["@", "4"], 'e':["3"], 's':["5", "$"], 'o':["0"], 'l':["1"]}

with open(datos, "r") as f:
    data = f.readlines()
    lengths = [3,4,5,6,7]

    #e) sha512 diccionario tipo 1
    for x in range (5):
        palabras_generadas = []
        for i in range(0,100):
            len_idx = random.randint(0,10) % len(lengths)
            word_idx = random.randint(0,10000) % len(data)
            pwd_txt = data[word_idx][:len_idx + 2].strip()
            for letra in pwd_txt:
                if letra in diccionario_letras.keys():
                    pwd_txt= pwd_txt.replace(letra, random.choice([letra, random.choice(diccionario_letras[letra])]))

            pwd1 = pwd_txt + str(random.randint(0,100))
            pwd2 = str(random.randint(0,100)) + pwd_txt


            if not tiene_numero(pwd_txt):
                pwd = pwd_txt
            else:
                pwd = random.choice([pwd1,pwd2])

            palabras_generadas.append(pwd)
        #print(palabras_generadas)
        with open("contraseñas/e/sha512/" + str(x + 1) + ".txt", "w") as archivo:
            for pwd in palabras_generadas:
                archivo.write(pwd + "\n")
        with open("contraseñas/e/sha512/" + str(x + 1) + "_hash.txt", "w") as archivo:
            for palabra in palabras_generadas:
                hash_obj = hashlib.sha512()
                hash_obj.update(palabra.encode())
                palabra = hash_obj.hexdigest()
                archivo.write(palabra + "\n")


        # e) md5crypt tipo 1
        for x in range(5):
            palabras_generadas = []
            for i in range(0, 100):
                len_idx = random.randint(0, 10) % len(lengths)
                word_idx = random.randint(0, 10000) % len(data)
                pwd_txt = data[word_idx][:len_idx + 2].strip()
                for letra in pwd_txt:
                    if letra in diccionario_letras.keys():
                        pwd_txt = pwd_txt.replace(letra,
                                                  random.choice([letra, random.choice(diccionario_letras[letra])]))

                pwd1 = pwd_txt + str(random.randint(0, 100))
                pwd2 = str(random.randint(0, 100)) + pwd_txt

                if not tiene_numero(pwd_txt):
                    pwd = pwd_txt
                else:
                    pwd = random.choice([pwd1, pwd2])

                palabras_generadas.append(pwd)
            # print(palabras_generadas)
            with open("contraseñas/e/md5crypt/" + str(x + 1) + ".txt", "w") as archivo:
                for pwd in palabras_generadas:
                    archivo.write(pwd + "\n")
            with open("contraseñas/e/md5crypt/" + str(x + 1) + "_hash.txt", "w") as archivo:
                for pwd in palabras_generadas:
                    pwd = md5_crypt.hash(pwd)
                    archivo.write(pwd + "\n")
