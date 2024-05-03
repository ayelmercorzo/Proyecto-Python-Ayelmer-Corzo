import os
import ui.uiMenuPrincipal as uiPrincipal
import funciones.consultas.consultaPorEnfermedad as co
import funciones.globalesWindowsLinux as gb
import ui.menu as  menu

def gestionCitas(op : int):
    gb.borrar_pantalla()
    menu.tituloEspecialistas()
    menuPrincipal = """1. Consulta Pediatria  \n2. Consulta Ginecologia   \n3. Consulta Dermatologia \n4. Consulta Endocrinologia  \n5. Consulta Optometria \n6. VOLVER AL MENU PRINCIPAL"""

    if (op != 6):
        print(menuPrincipal)
        print("")
        try:
            op = int(input("Ingrese la opcion:) "))
        except ValueError:
                print("Ingrese una opcion correcta")
                gb.pausar_pantalla()
                gestionCitas(0)
        else:
            match op:
                case 1:
                    co.ingresoConsultasPediatria()
                case 2:
                    co.ingresoConsultasGinecologia()
                case 3:
                    co.ingresoConsultasDermatologia()
                case 4:
                    co.ingresoConsultasEndocrinologia()
                case 5:
                    co.ingresoConsultasOptometria()
                case 6:
                    uiPrincipal.mainMenu("op")
                case _: 
                    print("Error Ingrese otra opcion")

    
        