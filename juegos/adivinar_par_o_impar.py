import random

def adivinar_par_o_impar():
    que_es=""
    print("Adivina si el numero que estoy pensando es par o impar...")
    ingresa=input()
    num_adivinar=random.randint(1,10000)
    if num_adivinar%2==0:
        que_es="par"
    else:
        que_es="impar"
    ingresa_min=ingresa.lower()
    if ingresa_min==que_es:
        print("Correcto!")
    else:
        print("Incorrecto")
    pass

adivinar_par_o_impar()