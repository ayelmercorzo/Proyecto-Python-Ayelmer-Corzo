import modules.corefiles as cf
import modules.movesJson as mj
import funciones.globalesWindowsLinux as gb
import ui.uiPaciente as uiP
import ui.uiMenuPrincipal as uiM
import ui.menu as menu

def mainMenuEntrada(op : int):
    gb.borrar_pantalla()
    menuPrincipal = """1. ENTRAR COMO PACIENTE  \n2. ENTRAR COMO ESPECIALISTA\n3. Salir               """
    menu.tituloBienvenida()
    if (op != 3):
        ()
        print(menuPrincipal)
        print(" ")
        try:
            op = int(input("Ingrese la opcion: "))
        except ValueError:
                print("Ingrese una opcion correcta")
                gb.pausar_pantalla()
                mainMenuEntrada(0)
        else:
            match op:
                case 1:
                    uiP.mainMenuPacientes("op")
                case 2:
                    gb.verificar_contraseña()
                case 3:
                    gb.salir()
                case _: 
                    print("Error Ingrese otra opcion")

