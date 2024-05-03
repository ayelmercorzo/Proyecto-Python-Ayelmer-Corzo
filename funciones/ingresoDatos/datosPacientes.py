import json
from datetime import datetime, timedelta
import ui.menu as menu
import ui.uiMenuPrincipal as uiM
import funciones.globalesWindowsLinux as gb
import modules.movesJson as mj
import modules.corefiles as mc

def ingresoDatosPaciente():
    with open('data/medicos.json', 'r') as file:
        medicos_data = json.load(file)
    
    menu.tituloEspecialistas()
    especialidad = input("Digite a qué consultorio es la cita: ")

    if especialidad in medicos_data['datamedicos']:
        medicos_disponibles = medicos_data['datamedicos'][especialidad]

        print(f"Horarios disponibles para el consultorio {especialidad}:")
        for medico in medicos_disponibles:
            print(f"Nombre: {medico['nombre']} {medico['apellidos']}")
            print("Horarios:", ", ".join(medico['horarios']))
            print()

        medico_elegido = input("Ingrese el nombre completo del médico: ")
        hora_elegida = input("¿A qué hora desea la cita (en formato HH:MM)?: ")

        #busca un médico específico entre una lista de médicos disponibles,
        #verifica si un horario de cita dado está disponible según las citas previas del médico y,
        #si está disponible, formatea la hora de la cita en un intervalo de 20 minutos.
        for medico in medicos_disponibles:
            if f"{medico['nombre']} {medico['apellidos']}" == medico_elegido:
                horarios_ocupados = [datetime.strptime(cita['hora de cita'].split(' - ')[0], '%H:%M') for cita in medico.get('citas', [])]
                hora_cita = datetime.strptime(hora_elegida, '%H:%M')

                if all(not (hc <= hora_cita < hc + timedelta(minutes=20)) for hc in horarios_ocupados):
                    cita_hora_fin = hora_cita + timedelta(minutes=20)
                    hora_cita_str = hora_cita.strftime('%H:%M') + ' - ' + cita_hora_fin.strftime('%H:%M')

                    
                    paciente = {
                        'numero de identificacion': input("Ingrese el Nro de documento: "),
                        'nombre, apellidos': input("Ingrese el nombre completo del paciente: "),
                        'numero telefonico': input("Ingrese su numero telefonico: "),
                        'numero celular': input("Ingrese su numero de celular: "),
                        'fecha de nacimiento': input("Ingrese su fecha de nacimiento (dia/mes/año): "),
                        'edad': int(input("Ingrese su edad: ")),
                        'genero': input("Ingrese su genero (F o M): "),
                        'consultorio': especialidad,
                        'hora de cita': hora_cita_str
                    }

                    
                    medico.setdefault('citas', []).append(paciente)

                    with open('data/medicos.json', 'w') as file:
                        json.dump(medicos_data, file, indent=4)
                    
                    print(f"Cita registrada para {medico_elegido} a las {hora_cita_str}")
                    gb.pausar_pantalla()
                    return uiM.mainMenu("op")

                else:
                    print("El médico no está disponible en ese horario.")
                    gb.pausar_pantalla()
                    return ingresoDatosPaciente()

        print("Médico no encontrado.")
        gb.pausar_pantalla()
        return ingresoDatosPaciente()

    else:
        print("Consultorio no disponible")
        gb.pausar_pantalla()
        return ingresoDatosPaciente()

def paciente_existe(identificacion):
    centroMedicoPaciente = mc.CentroMedicoPacientes.get('datapacientes', {})
    return identificacion in centroMedicoPaciente

def eliminarPacientePorIdentificacion(identificacion):
    with open('data/pacientes.json', 'r') as file:
        pacientes_data = json.load(file)
    
    pacientes = pacientes_data.get('datapacientes', {})
    pacientes_actualizados = {}
    paciente_encontrado = False
    
    for key, paciente in pacientes.items():
        if isinstance(paciente, dict) and paciente.get('numero de identificacion') == identificacion:
            paciente_encontrado = True
            print(f"Eliminando paciente con identificación {identificacion}...")
        else:
            pacientes_actualizados[key] = paciente
    
    if paciente_encontrado:
        pacientes_data['datapacientes'] = pacientes_actualizados

        with open('data/pacientes.json', 'w') as file:
            json.dump(pacientes_data, file, indent=4)
        
        print(f"Paciente con identificación {identificacion} eliminado correctamente.")
        return True
    else:
        print(f"No se encontró ningún paciente con identificación {identificacion}.")
        return False
