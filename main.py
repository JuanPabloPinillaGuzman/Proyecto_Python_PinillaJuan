import os
import modulos.opciones as mo
import modulos.mensajes as mm
import modulos.usuarios as mu
import modulos.core as mc

if (__name__ == '__main__'):
    thechachipun = {}
    mc.MY_DATABASE = 'data/thechachipun.json'
    mc.checkFile(thechachipun)
    isActive = True
    opMenu = 0
    
    while (isActive):
        try:
            os.system('cls')
            print(mm.tituloMenuPrincipal)
            print(mm.menuModoDeJuego)
            opMenu = int(input('=> '))
            match opMenu:
                case 1 :
                    mu.crearUsuario(thechachipun)
                    mu.crearUsuario2(thechachipun)
                case 2 :
                    pass
                case _:
                    pass
        except ValueError:
            print('Ingrese una opción valida')
            os.system('pause')
            continue
    pass