import random
def juego_del_dado():
    puntusu = 0
    puntcomp = 0
    while puntusu <= 30 and puntcomp <= 30:
        num1 = random.randint(1,6)
        puntusu += num1
        mensaje = ''
        if puntusu >= 30:
            mensaje = 'Ganasteee!!'
            break
        num2 = random.randint(1,6)
        puntcomp += num2
        if puntcomp >= 30:
            mensaje = 'Noo, perdiste:(('
            break
    return mensaje
    pass
print(juego_del_dado())