import modules.corefiles as cf
import modules.movesJson as mj
import funciones.globalesWindowsLinux as gb
import ui.uiEntrada as uiE
import ui.menu as menu

def mainMenu(op : int):
    gb.borrar_pantalla()
    menu.tituloEspecialistas()
    menuPrincipal = """1. Generar Diagnostico  \n2. Agendamiento de citas  \n3. Gestionar Especialistas \n4. Salir               """

    if (op != 4):
        
        print(menuPrincipal)
        print(" ")
        try:
            op = int(input("Ingrese la opcion: "))
        except ValueError:
                print("Ingrese una opcion correcta")
                gb.pausar_pantalla()
                mainMenu(0)
        else:
            match op:
                case 1:
                    cf.generarDiagnoastico()
                case 2:
                    cf.agendarCitasPorPaciente()
                case 3:
                    cf.GestionarEspecialista()
                case 4:
                    uiE.mainMenuEntrada("op")
                case _: 
                    print("Error Ingrese otra opcion")

