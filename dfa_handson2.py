# ===============================
# FECHA: 03 de octubre del 2025
# TEMA: Validación de un JSON de empleados
# ALUMNO: Jesus Vidrio Perez
# ===============================

import re

def validar_json(cadena_json):
    """
    Función que valida si un JSON cumple con la siguiente estructura:

    {
      "employees": [
        {"firstName":"Nombre","lastName":"Apellido"},
        {"firstName":"Nombre","lastName":"Apellido"},
        ...
      ]
    }

    - El objeto raíz debe llamarse "employees"
    - Cada objeto dentro del arreglo debe tener "firstName" y "lastName"
    - Los valores deben empezar con letra y pueden incluir números
    """

    # 1. Eliminamos espacios innecesarios (para evitar errores por formato)
    s = cadena_json.strip()

    # 2. Expresión regular que representa la estructura válida
    patron = r'''
    ^\{\s*                                    # empieza con {
    "employees"\s*:\s*                        # debe tener la clave "employees":
    \[\s*                                     # empieza el arreglo [

      (                                       # grupo que representa a los objetos
        \{\s*                                 # empieza un objeto {
          "firstName"\s*:\s*"([A-Za-z][A-Za-z0-9]*)"\s*,\s*  # clave "firstName" con valor válido
          "lastName"\s*:\s*"([A-Za-z][A-Za-z0-9]*)"\s*       # clave "lastName" con valor válido
        \}\s*                                 # cierra el objeto }

        (                                     # opcional: pueden venir más objetos
          ,\s*                                # separados por coma
          \{\s*
            "firstName"\s*:\s*"([A-Za-z][A-Za-z0-9]*)"\s*,\s*
            "lastName"\s*:\s*"([A-Za-z][A-Za-z0-9]*)"\s*
          \}\s*
        )*                                    # fin de repetición de objetos
      )?                                      # puede ser vacío

    \]\s*                                     # cierra el arreglo ]
    \}\s*$                                    # cierra el objeto raíz }
    '''

    # 3. Usamos la expresión regular para validar
    return re.fullmatch(patron, s, re.VERBOSE) is not None


# ================= PRUEBAS =================

ejemplo_valido = '''
{
    "employees": [
        {"firstName":"John","lastName":"Doe"},
        {"firstName":"Anna","lastName":"Smith"},
        {"firstName":"Peter","lastName":"Jones"}
    ]
}
'''

ejemplo_invalido = '''
{
    "employees": [
        {"firstName":"123John","lastName":"Doe"}
    ]
}
'''

print("Ejemplo válido:", validar_json(ejemplo_valido))   # True
print("Ejemplo inválido:", validar_json(ejemplo_invalido)) # False