import os
import copy
import modulos.core as mc

jugadores = {
    'nombre' : "",
    'alias' : "",
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
    



    