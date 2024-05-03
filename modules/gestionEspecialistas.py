import json
import ui.uiMenuPrincipal as uiM
import funciones.globalesWindowsLinux as gb
import funciones.ingresoDatos.datosMedicos as fd
import ui.menu as menu 
def RegistroEspecialista():
    gb.borrar_pantalla()
    menu.tituloEspecialistas()
    opcionesAggEsp = """
    1. Pediatra                       
    2. Ginecologo                      
    3. Dermatologo                   
    4. Endocrinologo                 
    5. Optemetra                      
    6. Salir                          """
    
    print(opcionesAggEsp)
    print("")
    op = int(input("Ingrese una opcion: "))
    if op == 1:
        gb.borrar_pantalla()
        print("Ingrese los datos para el especialista en Pediatria")
        fd.ingresoDatosMedico()
    elif op == 2:
        gb.borrar_pantalla()
        print("Ingrese los datos para el especialista en Ginecologia")
        fd.ingresoDatosMedico()
    elif op == 3:
        gb.borrar_pantalla()
        print("Ingrese los datos para el especialista en Dermatologo")
        fd.ingresoDatosMedico()
    elif op == 4:
        gb.borrar_pantalla()
        print("Ingrese los datos para el especialista en Endocrinologo")
        fd.ingresoDatosMedico()
    elif op == 5:
        gb.borrar_pantalla()
        print("Ingrese los datos para el especialista en Optometra")
        fd.ingresoDatosMedico()
    gb.pausar_pantalla()
def modificarEspecialista(identificacion, nuevo_correo, nuevo_consultorio):
    with open('data/medicos.json', 'r') as file:
        medicos_data = json.load(file)
    for especialidad, medicos in medicos_data['datamedicos'].items():
        for medico in medicos:
            if medico['identificacion'] == identificacion:
                medico['correo electronico'] = nuevo_correo
                medico['consultorio'] = nuevo_consultorio
                with open('data/medicos.json', 'w') as file:
                    json.dump(medicos_data, file, indent=4)
                
                print(f"Datos modificados para el médico {medico['nombre']} {medico['apellidos']}")
                return uiM.mainMenu("op")
    
    print("No se encontró ningún médico con esa identificación.")

def modificarMedico():
    menu.titubloEspecialistas()
    identificacion = input("Ingrese la identificación del médico a modificar: ")
    nuevo_correo = input("Ingrese el nuevo correo electrónico del médico: ")
    nuevo_consultorio = input("Ingrese el nuevo consultorio del médico: ")

    modificarEspecialista(identificacion, nuevo_correo, nuevo_consultorio)

def consultarEspecialistaPorIdentificacion(identificacion):
    with open('data/medicos.json', 'r') as file:
        medicos_data = json.load(file)
    for especialidad, medicos in medicos_data['datamedicos'].items():
        for medico in medicos:
            if medico['identificacion'] == identificacion:
                print(f"Identificación: {medico['identificacion']}")
                print(f"Nombre: {medico['nombre']} {medico['apellidos']}")
                print(f"Correo Electrónico: {medico['correo electronico']}")
                print(f"Consultorio: {medico['consultorio']}")
                print(f"Especialidad: {medico['especialidad']}")
                print("Horarios:")
                for horario in medico['horarios']:
                    print(f"- {horario}")
                print("Citas:")
                if medico['citas']:
                    for cita in medico['citas']:
                        print(f"- Número de Identificación: {cita['numero de identificacion']}")
                        print(f"  Nombre: {cita['nombre, apellidos']}")
                        print(f"  Número Telefónico: {cita['numero telefonico']}")
                        print(f"  Número Celular: {cita['numero celular']}")
                        print(f"  Fecha de Nacimiento: {cita['fecha de nacimiento']}")
                        print(f"  Edad: {cita['edad']}")
                        print(f"  Género: {cita['genero']}")
                        print(f"  Consultorio: {cita['consultorio']}")
                        print(f"  Hora de Cita: {cita['hora de cita']}")
                else:
                    print("- Sin citas registradas.")
                return uiM.mainMenu("op")
    
    print("No se encontró ningún médico con esa identificación.")

def ConsultarEspecialista():
    menu.titubloEspecialistas()
    identificacion = input("Ingrese la identificación del médico a consultar: ")
    consultarEspecialistaPorIdentificacion(identificacion)

def eliminarEspecialistaPorIdentificacion(identificacion):
    with open('data/medicos.json', 'r') as file:
        medicos_data = json.load(file)
    for especialidad, medicos in medicos_data['datamedicos'].items():
        for medico in medicos:
            if medico['identificacion'] == identificacion:
                medicos.remove(medico)
                with open('data/medicos.json', 'w') as file:
                    json.dump(medicos_data, file, indent=4)
                
                print(f"Médico con identificación {identificacion} eliminado correctamente.")
                return uiM.mainMenu("op")
    
    print("No se encontró ningún médico con esa identificación.")

def eliminarEspecialista():
    ()
    identificacion = input("Ingrese la identificación del médico a eliminar: ")
    eliminarEspecialistaPorIdentificacion(identificacion)