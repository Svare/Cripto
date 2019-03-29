#!/usr/bin/python
#-*- coding: utf-8 -*-
# CIFRADO VIGENERE. 
#
abc = "abcdefghijklmnñopqrstuvwxyz0123456789"

def cifrar(cadena, clave):  # FUNCION CIFRADO
    text_cifrar = ""
    i = 0
    for letra in cadena: 
        suma = abc.find(letra) + abc.find(clave[i % len(clave)])
        modulo = int(suma) % len(abc)
        text_cifrar = text_cifrar + str(abc[modulo]) 
        i = i + 1
    return text_cifrar

def descifrar(cadena, clave):  # FUNCION DESCIFRADO
    text_cifrar = ""
    i = 0
    for letra in cadena:
        suma = abc.find(letra) - abc.find(clave[i % len(clave)])   # LO UNICO QUE CAMBIA ES EL SIGNO -
        modulo = int(suma) % len(abc)
        text_cifrar = text_cifrar + str(abc[modulo])  
        i = i + 1
    return text_cifrar

if __name__ == "__main__":

    print (cifrar("araña89", "pecesit"))
    print (descifrar("pvcrsgs", "pecesit")) 

    