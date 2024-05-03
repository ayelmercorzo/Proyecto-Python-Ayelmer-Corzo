import json
import ui.uiMenuPrincipal as uiM
import funciones.globalesWindowsLinux as gb
def ingresoDatosMedico():
    identificacionMedico = input("Ingrese el Nro de documento: ")
    nombre_completo = input("Ingrese su nombre y apellido, separados por un espacio: ")
    nombre, apellidos = nombre_completo.split(maxsplit=1)
    correoElectronico = input("Ingrese su correo: ")
    numeroConsultorio = int(input("Ingrese el número del consultorio: "))
    especialidad = input("Ingrese la especialidad del médico: ")
    horarios = []

    while True:
        horario = input("Ingrese un horario disponible (ejemplo: '08:00 - 12:00'), o deje en blanco para terminar: ")
        if not horario:
            break
        horarios.append(horario)

    medico = {
        'identificacion': identificacionMedico,
        'nombre': nombre,
        'apellidos': apellidos,
        'correo electronico': correoElectronico,
        'consultorio': numeroConsultorio,
        'especialidad': especialidad,
        'horarios': horarios,
    }
    
    aggDataMedicos('datamedicos', especialidad, medico)
    print("¡Médico agregado correctamente!")
    gb.pausar_pantalla()
    uiM.mainMenu("op")

def aggDataMedicos(namespace, especialidad, medico):
    try:
        with open('data/medicos.json', 'r+') as file:
            data_medicos = json.load(file)
    except FileNotFoundError:
        data_medicos = {namespace: {}}

    if especialidad not in data_medicos[namespace]:
        data_medicos[namespace][especialidad] = []

    if 'citas' not in medico:
        medico['citas'] = []

    data_medicos[namespace][especialidad].append(medico)

    with open('data/medicos.json', 'w') as file:
        json.dump(data_medicos, file, indent=4)

