import modules.corefiles as cf
import ui.uiEntrada as uiE
import funciones.globalesWindowsLinux as gb

gb.borrar_pantalla()
if __name__ == '__main__':
        cf.iniciarCentroMedico()
print(uiE.mainMenuEntrada("op"))

