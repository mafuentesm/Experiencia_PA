import random

def adivinar_numero():
    num_random=random.randint(1,10)
    print("Adivina el numero entre 1 y 10...")
    user=int(input())
    if user==num_random:
        print("Correctoooo")
    else:
        print("Incorrecto :(, el numero era",num_random)
    pass

adivinar_numero()