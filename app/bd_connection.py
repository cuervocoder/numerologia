import pandas as pd
import os
import sys
from datetime import datetime


def get_excel_path():
    # Verificar si estamos dentro de un ejecutable de PyInstaller
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, 'base_de_datos2.xlsx')
    else:
        return 'base_de_datos2.xlsx'

# Lee el archivo Excel desde la ubicación correcta
df = pd.read_excel(get_excel_path(), header=1)


def search_karma_in_database (df, numero_objetivo):
    # Filtra el DataFrame para las filas donde 'numero' sea igual a numero_objetivo
    filtro = df['Numero'] == numero_objetivo
    fila_resultado = df.loc[filtro]
    # Asegura de que haya al menos una fila que cumple con el filtro
    if not fila_resultado.empty:
        # Aquí puedes acceder al valor de la celda en la columna 'karma'
        valor_respectiva_celda = fila_resultado['Karma'].iloc[0]
        return f" Karma del número {numero_objetivo}: {valor_respectiva_celda}"
    else:
        return f" No hay datos cargados sobre el karma del número {numero_objetivo}"

#search_karma_in_database(5) --> esto está bien (cambie los return por print arriba y me imprime el karma 5)

def search_talento_in_database (df, numero_objetivo):
    # Filtra el DataFrame para las filas donde 'numero' sea igual a numero_objetivo
    filtro = df['Numero'] == numero_objetivo
    fila_resultado = df.loc[filtro]
    # Asegura de que haya al menos una fila que cumple con el filtro
    if not fila_resultado.empty:
        # Aquí puedes acceder al valor de la celda en la columna 'talento'
        valor_respectiva_celda = fila_resultado['Talento'].iloc[0]
        return f" Talento del número {numero_objetivo}: {valor_respectiva_celda}"
    else:
        return f" No hay datos cargados sobre el talento del número {numero_objetivo}"

    

def search_oportunity_in_database (numero_objetivo):
    # Filtra el DataFrame para las filas donde 'numero' sea igual a numero_objetivo
    filtro = df['Numero'] == numero_objetivo
    fila_resultado = df.loc[filtro]
    # Asegura de que haya al menos una fila que cumple con el filtro
    if not fila_resultado.empty:
        # Acceder al valor de la celda en la columna requerida
        valor_respectiva_celda = fila_resultado['Oportunidad'].iloc[0]
        return f" Oportunidad del número {numero_objetivo}: {valor_respectiva_celda}"
    else:
        return f" No hay datos cargados sobre la oportunidad del número {numero_objetivo}"


def search_challenge_in_database (numero_objetivo):
    # Filtra el DataFrame para las filas donde 'numero' sea igual a numero_objetivo
    filtro = df['Numero'] == numero_objetivo
    fila_resultado = df.loc[filtro]
    # Asegura de que haya al menos una fila que cumple con el filtro
    if not fila_resultado.empty:
        # Acceder al valor de la celda en la columna requerida
        valor_respectiva_celda = fila_resultado['Desafio'].iloc[0]
        return f" Desafío del número {numero_objetivo}: {valor_respectiva_celda}"
    else:
        return f" No hay datos cargados sobre el desafío del número {numero_objetivo}"

def search_destinity_number(numero_objetivo):
    # Filtra el DataFrame para las filas donde 'numero' sea igual a numero_objetivo
    filtro = df['Numero'] == numero_objetivo
    fila_resultado = df.loc[filtro]

    # Inicializar la cadena de resultados
    result_string = ""

    # Verificar si hay datos y acumular resultados
    if not fila_resultado.empty:
        # Acceder al valor de la celda en la columna requerida
        valor_sendero_natal = fila_resultado['Sendero natal'].iloc[0]
        valor_aspecto_positivo = fila_resultado['Aspecto positivo'].iloc[0]
        valor_aspecto_negativo = fila_resultado['Aspecto negativo'].iloc[0]

        # Concatenar los resultados en la cadena
        result_string += (
            f"Interpretación del número de destino:\n"
            f"• Sendero natal del número {numero_objetivo}: {valor_sendero_natal}\n"
            f"• Aspecto positivo del número {numero_objetivo}: {valor_aspecto_positivo}\n"
            f"• Aspecto negativo del número {numero_objetivo}: {valor_aspecto_negativo}\n\n"
        )
    else:
        # Si no hay datos, agregar un mensaje indicando la falta de información
        result_string += f"No hay datos cargados sobre el número {numero_objetivo}\n"

    # Retornar la cadena de resultados
    return result_string



def search_cycle1(numero_objetivo):
    # Filtra el DataFrame para obtener la fila donde 'Numero' es igual a numero_objetivo
    filtro = df['Numero'] == numero_objetivo
    fila_resultado = df.loc[filtro]

    # Verificar si hay datos y devolver el resultado del ciclo formativo
    if not fila_resultado.empty:
        valor_ciclo1 = fila_resultado['Ciclo1'].iloc[0]
        return f"• Ciclo formativo regido por el número {numero_objetivo}: {valor_ciclo1}\n"
    else:
        return f"No hay datos cargados sobre el ciclo formativo del número {numero_objetivo}\n"


def search_cycle2(numero_objetivo):
    # Filtra el DataFrame para obtener la fila donde 'Numero' es igual a numero_objetivo
    filtro = df['Numero'] == numero_objetivo
    fila_resultado = df.loc[filtro]

    # Verificar si hay datos y devolver el resultado del ciclo productivo
    if not fila_resultado.empty:
        valor_ciclo2 = fila_resultado['Ciclo2'].iloc[0]
        return f"• Ciclo productivo regido por el número {numero_objetivo}: {valor_ciclo2}\n"
    else:
        return f"No hay datos cargados sobre el ciclo productivo del número {numero_objetivo}\n"    

def search_cycle3(numero_objetivo):
    # Filtra el DataFrame para obtener la fila donde 'Numero' es igual a numero_objetivo
    filtro = df['Numero'] == numero_objetivo
    fila_resultado = df.loc[filtro]

    # Verificar si hay datos y devolver el resultado del ciclo de recolección
    if not fila_resultado.empty:
        valor_ciclo3 = fila_resultado['Ciclo3'].iloc[0]
        return f"• Ciclo de recolección o cosecha regido por el número {numero_objetivo}: {valor_ciclo3}\n"
    else:
        return f"No hay datos cargados sobre el ciclo de recolección del número {numero_objetivo}\n"


def search_personal_year_in_database (numero_objetivo):
    # Filtra el DataFrame para las filas donde 'numero' sea igual a numero_objetivo
    filtro = df['Numero'] == numero_objetivo
    fila_resultado = df.loc[filtro]
    # Asegura de que haya al menos una fila que cumple con el filtro
    if not fila_resultado.empty:
        # Acceder al valor de la celda en la columna requerida
        valor_respectiva_celda = fila_resultado['Años personales'].iloc[0]
        return f"\n\nEn {(datetime.now().year)} vivirá el año personal número {numero_objetivo}: {valor_respectiva_celda}"
    else:
        return f" No hay datos cargados sobre el año personal {numero_objetivo}"


def search_next_personal_year_in_database (numero_objetivo):
    # Filtra el DataFrame para las filas donde 'numero' sea igual a numero_objetivo
    filtro = df['Numero'] == numero_objetivo
    fila_resultado = df.loc[filtro]
    # Asegura de que haya al menos una fila que cumple con el filtro
    if not fila_resultado.empty:
        # Acceder al valor de la celda en la columna requerida
        valor_respectiva_celda = fila_resultado['Años personales'].iloc[0]
        return f"\n\nEn {((datetime.now().year)+1)} vivirá el año personal número {numero_objetivo}: {valor_respectiva_celda}"
    else:
        return f" No hay datos cargados sobre el año personal {numero_objetivo}"



def search_vocation_in_database (numero_objetivo):
    # Filtra el DataFrame para las filas donde 'numero' sea igual a numero_objetivo
    filtro = df['Numero'] == numero_objetivo
    fila_resultado = df.loc[filtro]
    # Asegura de que haya al menos una fila que cumple con el filtro
    if not fila_resultado.empty:
        # Acceder al valor de la celda en la columna requerida
        valor_respectiva_celda = fila_resultado['Vocacion'].iloc[0]
        return f"\n\nEl número de vocación es {numero_objetivo} (coincide con el número del alma): {valor_respectiva_celda}"
    else:
        return f"\n\nNo hay datos cargados sobre la vocación del número {numero_objetivo}"

def search_extern_personality_in_database (numero_objetivo):
    # Filtra el DataFrame para las filas donde 'numero' sea igual a numero_objetivo
    filtro = df['Numero'] == numero_objetivo
    fila_resultado = df.loc[filtro]
    # Asegura de que haya al menos una fila que cumple con el filtro
    if not fila_resultado.empty:
        # Acceder al valor de la celda en la columna requerida
        valor_respectiva_celda = fila_resultado['Personalidad externa'].iloc[0]
        return f"\n\n• El número de proyección externa o yo externo (personalidad externa) es {numero_objetivo}: {valor_respectiva_celda}"
    else:
        return f"\n\nNo hay datos cargados sobre la personalidad externa del número {numero_objetivo}"


def search_intern_personality_in_database (numero_objetivo):
    # Filtra el DataFrame para las filas donde 'numero' sea igual a numero_objetivo
    filtro = df['Numero'] == numero_objetivo
    fila_resultado = df.loc[filtro]
    # Asegura de que haya al menos una fila que cumple con el filtro
    if not fila_resultado.empty:
        # Acceder al valor de la celda en la columna requerida
        valor_respectiva_celda = fila_resultado['Personalidad interna'].iloc[0]
        return f"\n• El número del alma o vibración interna (personalidad interna) es {numero_objetivo}: {valor_respectiva_celda}"
    else:
        return f"\nNo hay datos cargados sobre la personalidad interna del número {numero_objetivo}"

def search_global_personality_in_database (numero_objetivo):
    # Filtra el DataFrame para las filas donde 'numero' sea igual a numero_objetivo
    filtro = df['Numero'] == numero_objetivo
    fila_resultado = df.loc[filtro]
    # Asegura de que haya al menos una fila que cumple con el filtro
    if not fila_resultado.empty:
        # Acceder al valor de la celda en la columna requerida
        valor_respectiva_celda = fila_resultado['Personalidad global'].iloc[0]
        return f"\n• El número de personalidad global y misión de vida es {numero_objetivo}: {valor_respectiva_celda}"
    else:
        return f"\nNo hay datos cargados sobre la personalidad global del número {numero_objetivo}"