import os
import modulos.opciones as mo
import modulos.mensajes as mm
import modulos.utils as mu

if (__name__ == '__main__'):
    theCachipun = []
    isActive = True
    opMenu = 0
    
    while (isActive):
        try:
            os.system('cls')
            print(mm.tituloMenuPrincipal)
            print(mo.menuModoDeJuego)
            opMenu = int(input('=> '))
        except ValueError:
            print('Ingrese una opción valida')
            os.system('pause')
            continue
    pass