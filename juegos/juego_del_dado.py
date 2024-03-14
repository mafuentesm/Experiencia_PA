import random
def juego_del_dado():
    puntusu = 0
    puntcompu = 0
    while puntusu <= 30 and puntcomp <= 30:
        print('Presiona enter para lanzar el dado')
        num1 = random.randint(1,6)
        puntusua += num1
        num2 = random.randint(1,6)
        puntcomp += num2
        if puntusu >= 30 or puntcompu >= 30:
            break

    pass