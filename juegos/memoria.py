import random

def memoria():
    num_random=random.randint(1,100000)
    print("El numero a repetir es",num_random)
    repe=int(input())
    if repe==num_random:
        print("Acertaste!")
    else:
        print("Erroneo :(")
    pass

