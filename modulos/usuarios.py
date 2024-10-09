import os
import copy
import modulos.core as mc

jugadores = {
    'nombre' : "",
    'alias' : "",
    'partidasJ' : 0,
    'victoriasJ' : 0,
    'derrotasJ' : 0,
    'victoriasIa' : 0,
    'derrotasIa' : 0,
    'puntajeJ' : 0 
}
def crearUsuario(thechachipun):
    nuevoJugador = copy.deepcopy(jugadores)
    usuario = input('Ingrese el nombre del primer jugador:')
    while True:
        alias = input('Ingrese el alias: ')
        if alias in thechachipun:
            print("El alias ya existe. Por favor, ingrese un alias diferente.")
            os.system('pause')
        else:
            break
    nuevoJugador['nombre'] = usuario
    nuevoJugador['alias'] = alias

    thechachipun[alias] = nuevoJugador
    mc.AddData(thechachipun)

def ingreso(thechachipun):
    nuevoJugador = copy.deepcopy(jugadores)
    alias = input("Introduce tu alias: ")
    if alias in nuevoJugador:
        print(f"Bienvenido {alias}.")
        return alias
    else:
        print("Alias no encontrado.")
        return None

jugadores2 = {
    'nombre' : "",
    'alias' : "",
    'partidasJ' : 0,
    'victoriasJ' : 0,
    'derrotasJ' : 0,
    'victoriasIa' : 0,
    'derrotasIa' : 0,
    'puntajeJ' : 0 
}
def crearUsuario2(thechachipun):
    nuevoJugador2 = copy.deepcopy(jugadores2)
    usuario2 = input('Ingrese el nombre del segundo jugador:')
    while True:
        alias2 = input('Ingrese el alias: ')
        if alias2 in thechachipun:
            print("El alias ya existe. Por favor, ingrese un alias diferente.")
            os.system('pause')
        else:
            break
    nuevoJugador2['nombre'] = usuario2
    nuevoJugador2['alias'] = alias2

    thechachipun[alias2] = nuevoJugador2
    mc.AddData(thechachipun)
    



    