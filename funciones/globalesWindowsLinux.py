from os import system
import sys
import ui.menu as menu
import ui.uiMenuPrincipal as uiM



CMCAL = {
  "data": {}
}

def barra_de_carga():
    ESC = '\x1b'
    RESET_COLOR = '\033[49m'

    GREEN_BG = ESC + '[42m'
    YELLOW_BG = ESC + '[43m'
    WHITE_BG = ESC + '[47m'

    colors = [GREEN_BG, YELLOW_BG, WHITE_BG]

    import time, sys, math

    for i in range(0, 100):
        time.sleep(0.02)
        width = (i + 1) // 4
        color_index = math.floor(i / 100.0 * len(colors))
        color = colors[color_index]
        loading_text = "Cargando... Espere      "
        padding = " " * (25 - len(loading_text))
        bar = "[" + color + loading_text + padding + RESET_COLOR + "]"
        sys.stdout.write(ESC + '[1000D' + bar)
        sys.stdout.flush()
    print("\n")
def verificar_contraseña():
    borrar_pantalla()
    menu.tituloEspecialistas()
    contraseñas_permitidas = ["pass123", "pass456", "pass789"]
    contraseña_ingresada = input("Ingrese la contraseña: ")

    if contraseña_ingresada in contraseñas_permitidas:
        print(" ")
        barra_de_carga()
        verde = "\033[92m"
        print(verde + "Contraseña correcta. Bienvenido.")
        pausar_pantalla()
        uiM.mainMenu("op")
    else:
        barra_de_carga()  
        rojo = "\033[91m"
        print(rojo + "Contraseña incorrecta. Acceso denegado.") 
        pausar_pantalla() 
        return verificar_contraseña() 

def borrar_pantalla():
  if sys.platform == "linux" or sys.platform == "darwin":
    system("clear")
  else:
    system("cls")

def pausar_pantalla():
  if sys.platform == "linux" or sys.platform == "darwin":
    x=input("Presione un tecla para continuar")
  else:
    system("pause")

def salir():
    print("Estas saliendo del programa...")
    sys.exit()