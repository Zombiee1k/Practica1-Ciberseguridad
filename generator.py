import sys
import os
import random
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
    return ''.join(random.choice(caracteres) for _ in range(longitud))

# a) sha512
for i in range(5):
    # Generar 7 palabras solo con letras minúsculas
    palabras_min = [generar_palabra(3, solo_mins=True) for _ in range(7)]
    # Generar 93 palabras aleatorias con letras y números
    palabras_aleatorias = [generar_palabra(3) for _ in range(93)]
    # Unir las palabras
    palabras_generadas = palabras_min + palabras_aleatorias
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
    # Generar 7 palabras solo con letras minúsculas
    palabras_min = [generar_palabra(3, solo_mins=True) for _ in range(7)]
    # Generar 93 palabras aleatorias con letras y números
    palabras_aleatorias = [generar_palabra(3) for _ in range(93)]
    # Unir las palabras
    palabras_generadas = palabras_min + palabras_aleatorias
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
    # Generar 7 palabras solo con letras minúsculas
    palabras_min = [generar_palabra(3, solo_mayus=True) for _ in range(7)]
    # Generar 93 palabras aleatorias con letras y números
    palabras_aleatorias = [generar_palabra(3) for _ in range(93)]
    # Unir las palabras
    palabras_generadas = palabras_min + palabras_aleatorias
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
    # Generar 7 palabras solo con letras minúsculas
    palabras_min = [generar_palabra(3, solo_mayus=True) for _ in range(7)]
    # Generar 93 palabras aleatorias con letras y números
    palabras_aleatorias = [generar_palabra(3) for _ in range(93)]
    # Unir las palabras
    palabras_generadas = palabras_min + palabras_aleatorias
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
    # Generar 7 palabras solo con letras minúsculas
    palabras_min = [generar_palabra(3, solo_nums=True) for _ in range(7)]
    # Generar 93 palabras aleatorias con letras y números
    palabras_aleatorias = [generar_palabra(3) for _ in range(93)]
    # Unir las palabras
    palabras_generadas = palabras_min + palabras_aleatorias
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
    # Generar 7 palabras solo con letras minúsculas
    palabras_min = [generar_palabra(3, solo_nums=True) for _ in range(7)]
    # Generar 93 palabras aleatorias con letras y números
    palabras_aleatorias = [generar_palabra(3) for _ in range(93)]
    # Unir las palabras
    palabras_generadas = palabras_min + palabras_aleatorias
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
    # Generar 7 palabras solo con letras minúsculas
    palabras_min = [generar_palabra(3, alfanum=True) for _ in range(7)]
    # Generar 93 palabras aleatorias con letras y números
    palabras_aleatorias = [generar_palabra(3) for _ in range(93)]
    # Unir las palabras
    palabras_generadas = palabras_min + palabras_aleatorias
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
    # Generar 7 palabras solo con letras minúsculas
    palabras_min = [generar_palabra(3, alfanum=True) for _ in range(7)]
    # Generar 93 palabras aleatorias con letras y números
    palabras_aleatorias = [generar_palabra(3) for _ in range(93)]
    # Unir las palabras
    palabras_generadas = palabras_min + palabras_aleatorias
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


with open(datos, "r") as f:
    data = f.readlines()
    lengths = [3,4,5,6,7]

    #e) sha512
    for x in range (5):
        palabras_generadas = []
        for i in range(0,100):
            len_idx = random.randint(0,10) % len(lengths)
            word_idx = random.randint(0,10000) % len(data)
            pwd = data[word_idx][:len_idx+1].strip()+str(random.randint(0,100))
            palabras_generadas.append(pwd)
        #print(palabras_generadas)
        with open("contraseñas/e/sha512/" + str(x + 1) + ".txt", "w") as archivo:
            for pwd in palabras_generadas:
                archivo.write(pwd + "\n")
        with open("contraseñas/e/sha512/" + str(x + 1) + "_hash.txt", "w") as archivo:
            for pwd in palabras_generadas:
                hash_obj = hashlib.sha512()
                hash_obj.update(pwd.encode())
                pwd = hash_obj.hexdigest()
                archivo.write(pwd + "\n")


        # e) md5crypt
        for x in range(5):
            palabras_generadas = []
            for i in range(0, 100):
                len_idx = random.randint(0, 10) % len(lengths)
                word_idx = random.randint(0, 10000) % len(data)
                pwd = data[word_idx][:len_idx + 1].strip() + str(random.randint(0, 100))
                palabras_generadas.append(pwd)
            # print(palabras_generadas)
            with open("contraseñas/e/md5crypt/" + str(x + 1) + ".txt", "w") as archivo:
                for pwd in palabras_generadas:
                    archivo.write(pwd + "\n")
            with open("contraseñas/e/md5crypt/" + str(x + 1) + "_hash.txt", "w") as archivo:
                for pwd in palabras_generadas:
                    pwd = md5_crypt.hash(pwd)
                    archivo.write(pwd + "\n")