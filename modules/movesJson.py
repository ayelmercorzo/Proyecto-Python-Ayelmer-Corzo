import os
import modules.corefiles as mc
import json
import funciones.globalesWindowsLinux as gb
import ui.uiMenuPrincipal as uiM
def checkfile(databaseFile, datachek):
    if os.path.isfile(databaseFile):
        return  
    with open(databaseFile, "w") as file:
        json.dump(datachek, file, indent=4)

def aggDataMedicos(*param):
    dataMedicos = list(param)
    with open(mc.DATABASE_MEDICOS, "r+") as rwf:
        dataMedicos_file = json.load(rwf)
        if len(param) > 1:
            dataMedicos_file[dataMedicos[0]].update({dataMedicos[1]: dataMedicos[2]})
        else:
            dataMedicos_file.update({param[0]})
        rwf.seek(0)
        json.dump(dataMedicos_file, rwf, indent=4)

def aggDataPacientes(*param):
    dataPacientes = list(param)
    with open(mc.DATABASE_PACIENTES, "r+") as rwf:
        dataPacientes_file = json.load(rwf)
        if (len(param) > 1):
            dataPacientes_file[dataPacientes[0]].update({dataPacientes[1]:dataPacientes[2]})
        else:
            dataPacientes_file.update({param[0]})
        rwf.seek(0)
        json.dump(dataPacientes_file,rwf,indent=4)

def aggDataConsultas(*param):
    dataConsultas = list(param)
    with open(mc.DATABASE_CONSULTAS, "r+") as rwf:
        dataConsultas_file = json.load(rwf)
        if (len(param) > 1):
            dataConsultas_file[dataConsultas[0]].update({dataConsultas[1]:dataConsultas[2]})
        else:
            dataConsultas_file.update({param[0]})
        rwf.seek(0)
        json.dump(dataConsultas_file,rwf,indent=4)
        