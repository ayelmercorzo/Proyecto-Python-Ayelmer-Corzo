import json
import modules.movesJson as mj
import modules.corefiles as mc
import ui.uiGestionCitas as ui
import ui.uiMenuPrincipal as uiM
import funciones.globalesWindowsLinux as gb

def ingresar_consulta(especialidad):
    gb.borrar_pantalla()
    
    while True:
        nombre_medico = input("Nombre del médico encargado: ")
        
        with open('data/medicos.json', 'r') as file:
            data = json.load(file)
        
        medico_encontrado = None
        
        for especialidad_medico, detalles_medicos in data["datamedicos"].items():
            for detalles_medico in detalles_medicos:
                if detalles_medico["nombre"] == nombre_medico:
                    medico_encontrado = detalles_medico
                    break
            if medico_encontrado:
                break
        
        if medico_encontrado is not None:
            fecha = input("Ingrese la fecha del día de hoy: ")
            identidad = input("Ingrese el número de documento: ")
            paciente = input("Ingrese el nombre del paciente: ")
            edad = int(input("Ingrese la edad del paciente: "))
            genero = input("Ingrese el género del paciente (F o M): ")
            direccion_paciente = input("Ingrese la dirección del paciente: ")
            telefono_paciente = input("Ingrese el número telefónico del paciente: ")
            diagnostico = input("¿Cuál es el diagnóstico de la consulta?: ")
            receta_medica = input("Ingrese la receta médica: ")
            nombre_medicamento = input("Nombre del medicamento: ")
            dosis_medicamento = input("Dosis del medicamento: ")
            frecuencia_medicamento = input("Frecuencia del medicamento: ")
            duracion_medicamento = input("Duración del tratamiento: ")
            instrucciones_medicamento = input("Instrucciones de uso del medicamento: ")
            consultorio = input(f"¿El consultorio es {especialidad}? (S/N): ").upper()
            
            if consultorio == 'S':
                consultorio_especialidad = especialidad
                correo = input("Ingrese el correo del paciente: ")

                consulta = {
                    'Fecha': fecha,
                    'ID': identidad,
                    'Medico': medico_encontrado["nombre"],
                    'Paciente': {
                        'Nombre': paciente,
                        'Edad': edad,
                        'Genero': genero,
                        'Direccion': direccion_paciente,
                        'Telefono': telefono_paciente,
                    },
                    'Diagnostico': diagnostico,
                    'Receta Medica': {
                        'Receta': receta_medica,
                        'Medicamentos': {
                            'Nombre': nombre_medicamento,
                            'Dosis': dosis_medicamento,
                            'Frecuencia': frecuencia_medicamento,
                            'Duracion': duracion_medicamento,
                            'Instrucciones': instrucciones_medicamento,
                        }
                    },
                    'Consultorio': consultorio_especialidad,
                    'Correo del paciente': correo
                }
                
                mj.aggDataConsultas('dataConsultas', identidad, consulta)
                mc.CentroMedicoConsultas['dataConsultas'].update({identidad: consulta})
                uiM.mainMenu("op")
                break
            
            elif consultorio == 'N':
                uiM.mainMenu("op")
                break
            
            else:
                print("Error: Por favor responda con 'S' o 'N'.")
        
        else:
            print("Error: El médico ingresado no está registrado en la base de datos. Intente de nuevo.")

def ingresoConsultasPediatria():
    ingresar_consulta("Pediatria")

def ingresoConsultasGinecologia():
    ingresar_consulta("Ginecologia")

def ingresoConsultasDermatologia():
    ingresar_consulta("Dermatologia")

def ingresoConsultasEndocrinologia():
    ingresar_consulta("Endocrinologia")

def ingresoConsultasOptometria():
    ingresar_consulta("Optometria")