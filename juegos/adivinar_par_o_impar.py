def adivinar_par_o_impar():
    que_es=""
    ingresa=input()
    num_adivinar=random.randint(1,1000000000000000000000000000000000000)
    if num_adivinar%2==0:
        que_es="par"
    else:
        que_es="impar"
    ingresa_min=ingresa.lower()
    if ingresa_min==que_es:
        print("Correcto!")
    else:
        print("Incorrecto")

    #Esta función representa el juego de adivinar si un número es par o impar.
    #Tienes que permitir que el usuario ingrese una de las dos opciones y
    #generar un número aleatorio para ver si es par o impar.
    #Se debe mostrar si el usuario adivina correctamente o no.
    pass
