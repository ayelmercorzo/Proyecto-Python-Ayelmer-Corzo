import json
import funciones.ingresoDatos.datosMedicos as fd
import funciones.ingresoDatos.datosPacientes as fp
import ui.uiMenuPrincipal as ui
import ui.uiPaciente as uiP
import ui.uiGestionCitas as uiG
import modules.movesJson as mj
import modules.gestionEspecialistas as ge
import funciones.globalesWindowsLinux as gb
import ui.menu as menu

DATABASE_MEDICOS = 'data/medicos.json'
DATABASE_PACIENTES = 'data/pacientes.json'
DATABASE_CONSULTAS = 'data/consultas.json'

CentroMedicoMedicos = {"datamedicos": {}}
CentroMedicoPacientes = {"datapacientes": {}}
CentroMedicoConsultas = {"dataConsultas": {}}
def iniciarCentroMedico():
    mj.checkfile(DATABASE_MEDICOS, CentroMedicoMedicos)
    mj.checkfile(DATABASE_PACIENTES, CentroMedicoPacientes)
    mj.checkfile(DATABASE_CONSULTAS, CentroMedicoConsultas)

def generarDiagnoastico():
    gb.borrar_pantalla()
    print("Generando diagnostico...")
    uiG.gestionCitas("op")
    
def consultarInformacionConsulta():
    gb.borrar_pantalla()  
    menu.tituloPacientes()
    
    try:
        Nroidentificacion = input("Digite su Identificación (sin puntos ni comas): ")
        gb.barra_de_carga()
    except ValueError:
        print("Error: Por favor ingrese un número de identificación válido.")
        return
    
    with open('data/consultas.json', 'r') as file:
        data = json.load(file)
        
        if Nroidentificacion in data["dataConsultas"]:
            consulta = data["dataConsultas"][Nroidentificacion]
            print("\nDetalles de la consulta:")
            print(f"Fecha: {consulta['Fecha']}")
            print(f"Médico: {consulta['Medico']}")
            print(f"Paciente: {consulta['Paciente']['Nombre']}")
            print(f"Diagnóstico: {consulta['Diagnostico']}")
            print(f"Correo del paciente: {consulta['Correo del paciente']}")
            print(f"Consultorio: {consulta['Consultorio']}")
        else:
            print(f"No se encontró información para el ID {Nroidentificacion}.")
    
    print("Para volver al menú anterior presiona enter...")
    gb.pausar_pantalla()
    uiP.mainMenuPacientes("op")


def revisarTratamiento():
    gb.borrar_pantalla()  
    menu.tituloPacientes()
    try:
        Nroidentificacion = input("Digite su Identificación (sin puntos ni comas): ")
        gb.barra_de_carga()
    except ValueError:
        print("Error: Por favor ingrese un número de identificación válido.")
        return
    
    with open('data/consultas.json', 'r') as file:
        data = json.load(file)
        
        if Nroidentificacion in data["dataConsultas"]:
            consulta = data["dataConsultas"][Nroidentificacion]
            print("\nDetalles de el tratamiento:")
            print(f"Nombre de medicamento: {consulta['Receta Medica']['Medicamentos']['Nombre']}")
            print(f"Dosis: {consulta['Receta Medica']['Medicamentos']['Dosis']}")
            print(f"Frecuencia: {consulta['Receta Medica']['Medicamentos']['Frecuencia']}")
            print(f"Duracion: {consulta['Receta Medica']['Medicamentos']['Duracion']}")
            print(f"Instrucciones: {consulta['Receta Medica']['Medicamentos']['Instrucciones']}")
        else:
            print(f"No se encontró información para el ID {Nroidentificacion}.")
    
    print("Para volver al menú anterior presiona enter...")
    gb.pausar_pantalla()
    uiP.mainMenuPacientes("op")

def agendarCitasPorPaciente():
    while True:
        gb.borrar_pantalla()
        menu.tituloEspecialistas()
        print("1. Agendar cita")
        print("2. Cancelar cita")
        print("3. Volver atrás")

        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            gb.borrar_pantalla()
            fp.ingresoDatosPaciente()
            gb.pausar_pantalla()

        elif opcion == "2":
            gb.borrar_pantalla()
            identificacion = int(input("Ingrese el Nro de documento del paciente a cancelar: "))
            fp.eliminarPacientePorIdentificacion(identificacion)
            gb.pausar_pantalla()

        elif opcion == "3":
            print("Volviendo atrás...")
            ui.mainMenu("op")

        else:
            print("Opción inválida. Por favor, seleccione una opción válida (1-3).")
            gb.pausar_pantalla()




def GestionarEspecialista():
    gb.borrar_pantalla()
    menu.tituloEspecialistas()
    print("1. Registrar Especialista")
    print("2. Modificar Especialista")
    print("3. Eliminar Especialista")
    print("4. Consultar Especialista")
    print("5. Salir")
    print("")
    op = int(input("|Ingrese una opcion: "))
    if op == 1:
        gb.borrar_pantalla()
        ge.RegistroEspecialista()
        gb.pausar_pantalla()
        GestionarEspecialista()
    elif op == 2:
        gb.borrar_pantalla()
        ge.modificarMedico()
        gb.pausar_pantalla()
        GestionarEspecialista()
    elif op == 3:
        gb.borrar_pantalla()
        ge.eliminarEspecialista()
        gb.pausar_pantalla()
        GestionarEspecialista()
    elif op == 4:
        gb.borrar_pantalla()
        ge.ConsultarEspecialista()
        gb.pausar_pantalla()
        GestionarEspecialista()
    elif op == 5:
        ui.mainMenu("op")
