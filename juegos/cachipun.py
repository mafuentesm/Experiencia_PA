import random
def cachipun():
    print('Elige piedra, papel o tijera')
    elecusu = input()
    opciones = ['piedra', 'papel', 'tijera']
    num = random.randint(0,2)
    eleccompu = opciones[num]
    mensaje = ''
    if eleccompu == elecusu:
        mensaje  = 'Oh oh, parece que han empatado, intentalo de nuevo'
    elif eleccompu == 'tijera' and elecusu == 'piedra':
        mensaje = 'Yeii, ganaste!!'
    elif eleccompu == 'tijera' and elecusu == 'papel':
        mensaje = 'Nooo, perdiste:('
    elif eleccompu == 'piedra' and elecusu == 'papel':
        mensaje = 'Yeii, ganaste!!'
    elif eleccompu == 'piedra' and elecusu == 'tijera':
        mensaje = 'Nooo, perdiste:('
    elif eleccompu == 'papel' and elecusu == 'tijera':
        mensaje = 'Yeii, ganaste!!'
    elif eleccompu == 'papel' and elecusu == 'piedra':
        mensaje = 'Nooo, perdiste:('
    return mensaje
    pass

print(cachipun())