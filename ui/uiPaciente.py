import modules.corefiles as cf
import modules.movesJson as mj
import funciones.globalesWindowsLinux as gb
import ui.uiEntrada as uiE
import ui.menu as menu

def mainMenuPacientes(op : int):
    gb.borrar_pantalla()
    menu.tituloPacientes()
    menuPrincipal = """1. Consultar la información de la consulta médica.
2. Revisar el tratamiento recomendado para su enfermedad.
3. Salir.
"""
    if (op != 4):
        
        print(menuPrincipal)
        print(" ")
        try:
            op = int(input("Ingrese la opcion: "))
        except ValueError:
                print("Ingrese una opcion correcta")
                gb.pausar_pantalla()
                mainMenuPacientes(0)
        else:
            match op:
                case 1:
                    cf.consultarInformacionConsulta()
                case 2:
                    cf.revisarTratamiento()
                case 3:
                    uiE.mainMenuEntrada("op")
                case _: 
                    print("Error Ingrese otra opcion")
