# Proyecto python - Centro Medico 🏥

## Descripción
El proyecto **Centro Médico** es una aplicación que gestiona la información de pacientes, especialistas y citas médicas. Permite a los pacientes consultar su información médica, revisar tratamientos recomendados y agendar citas. Los especialistas pueden registrar, modificar, eliminar y consultar otros especialistas. La aplicación tiene una interfaz basada en texto con menús interactivos.

## Estructura de carpetas 📁

- `modules`: Contiene los módulos para el manejo de datos y funcionalidades.
  - `corefiles.py`: Funciones centrales del sistema.
  - `movesJson.py`: Manejo de archivos JSON.
  - `gestionEspecialistas.py`: Gestión de especialistas médicos.
- `ui`: Interfaz de usuario.
  - `menu.py`: Funciones para mostrar títulos de bienvenida y menús.
  - `entrada.py`: Menú principal y navegación.
  - `uigestionCitas.py`: Gestión de citas médicas.
  - `uiMenuPrincipal.py`: Menú principal para especialistas.
  - `uiPaciente.py`: Menú principal para pacientes.
- `funciones`: Funciones auxiliares.
  - `globalesWindowsLinux.py`: Funciones comunes para diferentes sistemas operativos.
  - `ingresoDatos`: Manejo de datos médicos y pacientes.
    - `datosMedicos.py`: Funciones para ingreso de datos de médicos.
    - `datosPacientes.py`: Funciones para ingreso de datos de pacientes.
  - `consultas`: Consultas médicas.
    - `consultaPorEnfermedad.py`: Funciones relacionadas con consultas médicas.

## Lenguajes y Herramientas 🛠
<div align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="100" alt="python logo" />
</div>

## Instalación ⬇️

### Requisitos Previos
- Python 3.x
- Un editor de texto (por ejemplo, VSCode, PyCharm)
- Git (para clonar el repositorio)

### Pasos 👣
1. **Clonar el repositorio:**
    ```sh
    git clone https://github.com/ayelmercorzo/Proyecto-Python-Ayelmer-Corzo.git
    ```

2. **Navegar al directorio del proyecto:**
    ```sh
    cd Proyecto-Python-Ayelmer-Corzo
    ```

3. **Instalar las dependencias (si hay alguna):**
    ```sh
    pip install -r requirements.txt
    ```

4. **Ejecutar el archivo principal:**
    ```sh
    python main.py
    ```

## Uso
- **Para pacientes:**
  - Consulta la información de tus consultas médicas.
  - Revisa el tratamiento recomendado para tu enfermedad.
  - Agenda nuevas citas o cancela citas existentes.

- **Para especialistas:**
  - Registra nuevos especialistas.
  - Modifica o elimina especialistas existentes.
  - Consulta información sobre especialistas.

### Contraseñas para Especialistas
Cuando se te solicite una contraseña para acceder como especialista, puedes usar una de las siguientes contraseñas:
- `12345`
- `6789`
- `0000`

<h2 align="center">Desarrollado por:</h2>

- [@ayelmercorzo](https://www.github.com/ayelmercorzo)
