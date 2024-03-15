import random
def juego_del_dado():
    puntusu = 0
    puntcomp = 0
    while puntusu <= 30 and puntcomp <= 30:
        print("Presiona Enter para lanzar")
        press=input()
        num1 = random.randint(1,6)
        print("Tu numero fue un",num1)
        puntusu += num1
        mensaje = ''
        if puntusu >= 30:
            mensaje = 'Llegaste a 30; Ganasteee!!'
            break
        num2 = random.randint(1,6)
        puntcomp += num2
        print("El numero de la computadora fue un",num2)
        if puntcomp >= 30:
            mensaje = 'Noo, la maquina llegó a 30, perdiste:(('
            break
    return mensaje
    pass
print(juego_del_dado())