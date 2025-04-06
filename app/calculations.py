from datetime import datetime
from app.bd_connection import *
from app.inputs import *
from fpdf import FPDF
from io import BytesIO
import os
import streamlit as st
from googletrans import Translator


#from PyInstaller.utils.hooks import collect_data_files



def export_to_pdf(name, date, results):
    # Crear un objeto PDF
    pdf = FPDF()
    pdf.add_page()

    # Configurar márgenes personalizados
    pdf.set_margins(left=20, top=20, right=20)  # Márgenes de 20 mm
    pdf.set_auto_page_break(auto=True, margin=20)  # Configura márgenes inferiores
    
    # Agregar una fuente Unicode
    font_path = "fonts/DejaVuSans.ttf" # Agregar la fuente desde su ubicación
    pdf.add_font('DejaVu', '', font_path, uni=True)
    pdf.set_font('DejaVu', size=11) 


    # Título
    pdf.set_font('DejaVu', size=14)
    pdf.cell(0, 10, txt="Reporte de Numerología Evolutiva", ln=True, align='C')
    pdf.ln(15)  # Espaciado después del título
    
    # Resultados con interlineado ajustado
    pdf.set_font('DejaVu', size=11)
    
    #Ajustes para interlineado
    line_height = 5  # Interlineado ajustado
    page_width = pdf.w - 2 * pdf.l_margin  # Ancho de la página (restando márgenes)
    
    # Usar multi_cell con un ancho limitado
    pdf.multi_cell(page_width, line_height, txt="Resultados:", align='L')  # Título de la sección
    pdf.ln(5)  # Espacio extra después de la sección
    pdf.multi_cell(page_width, line_height, txt=results, align='J')  # Texto justificado
    
    # Guardar el PDF en un buffer en memoria
    pdf_buffer = BytesIO()
    pdf.output(pdf_buffer)
    pdf_buffer.seek(0)
    return pdf_buffer
#FIN NUEVO PDF

def extract_digits_and_sum(value):
     # Manejar números negativos convirtiéndolos a su representación positiva
    value = abs(int(value))

    # Define las excepciones: numeros maestros y karmicos 
    master_numbers = [11, 22, 33, 44]
    karmic_numbers = [13, 14, 16, 19]

    # Chequea si es numero maestro o karmico
    if value in master_numbers or value in karmic_numbers:
        return value

    # Convertir cada dígito a una lista de dígitos
    digit_list = [int(digit) for digit in str(value) if digit.isdigit()]
    # Suma los digitos
    digit_sum = sum(digit_list)
   
    # Si la suma de dígitos es mayor que 9, sumar los dígitos nuevamente
    while digit_sum > 9:
        digit_sum = sum(int(digit) for digit in str(digit_sum))

    return digit_sum


def extract_digits_and_sum_without_karmic(value):
     # Manejar números negativos convirtiéndolos a su representación positiva
    value = abs(int(value))

    # Define las excepciones: numeros maestros y karmicos 
    master_numbers = [11, 22, 33, 44]

    # Chequea si es numero maestro o karmico
    if value in master_numbers:
        return value

    # Convertir cada dígito a una lista de dígitos
    digit_list = [int(digit) for digit in str(value) if digit.isdigit()]
    # Suma los digitos
    digit_sum = sum(digit_list)
   
    # Si la suma de dígitos es mayor que 9, sumar los dígitos nuevamente
    while digit_sum > 9:
        digit_sum = sum(int(digit) for digit in str(digit_sum))

    return digit_sum


def extract_digits_and_sum_without_master_karmic(value):
     # Manejar números negativos convirtiéndolos a su representación positiva
    value = abs(int(value))

    # Convertir cada dígito a una lista de dígitos
    digit_list = [int(digit) for digit in str(value) if digit.isdigit()]
    # Suma los digitos
    digit_sum = sum(digit_list)
   
    # Si la suma de dígitos es mayor que 9, sumar los dígitos nuevamente
    while digit_sum > 9:
        digit_sum = sum(int(digit) for digit in str(digit_sum))

    return digit_sum



def sum_date_digits(validated_date):
    # Extraer día, mes y año como cadenas
    day, month, year = validated_date.split('/')

    # Calcular la suma de dígitos para cada componente
    month_sum_one_digit = extract_digits_and_sum_without_master_karmic(month)
    #print(f"el {day_sum_one_digit} marcaría su primer ciclo de vida, el de formación (desde el nacimiento hasta los 20 años)")
    day_sum_one_digit = extract_digits_and_sum_without_master_karmic(day)
    #print(f"el {month_sum_one_digit} marcaría su segundo ciclo de vida, los años de productividad (")
    year_sum_one_digit = extract_digits_and_sum_without_master_karmic(year)
    #print(f"el {year_sum_one_digit} marcaría su tercer ciclo de vida, el de recolección o cosecha")

    # Sumar las sumas parciales
    total_sum_one_digit = extract_digits_and_sum(str(day_sum_one_digit + month_sum_one_digit + year_sum_one_digit))
    #print(f"El número de destino o camino de vida es: {total_sum_one_digit}")
    return total_sum_one_digit, month_sum_one_digit, day_sum_one_digit, year_sum_one_digit


def count_letters_times(validated_name):
    # Definir el mapeo de letras a números
    map = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
    'h': 8, 'i': 9, 'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5,
    'ñ': 5 , 'o': 6, 'p': 7, 'q': 8, 'r': 9, 's': 1, 't': 2,
    'u': 3, 'v': 4, 'w': 5, 'x': 6, 'y': 7, 'z': 8
    }

    # Inicializar el conteo para cada número del 1 al 9
    count_numbers = {str(i): 0 for i in range(1, 10)}

    # Contar las ocurrencias de cada número en la entrada
    for letter in validated_name:
        if letter.lower() in map:
            valor_numerico = map[letter.lower()]
            count_numbers[str(valor_numerico)] += 1

    return count_numbers

#VER ESTOOO!!!! NO LO PUEDO HACER  ANDAR. Trae mal la info de la bd. Siempre dice que no hay resultados (EL ERROR ESTA ACÁ si o si, ya testee lo demas y esta de 10). Arreglado
def determinate_karma_talent(df, validated_name):
    # Obtener el conteo de ocurrencias de cada número
    count_numbers = count_letters_times(validated_name)

    # Inicializar la cadena de resultado
    result_string_talento_karma = "Números en carencia, en equilibrio y en exceso:"

    # Iterar sobre los elementos del diccionario
    for number, count in count_numbers.items():
        if count > 3:
            result_string_talento_karma += f"\nEl número {number} se encuentra en exceso. → "
            result_string_talento_karma += search_talento_in_database(df, int(number)) #faltaba poner int() renegue una banda
        elif count == 3:
            result_string_talento_karma += f"\nEl número {number} se encuentra en equilibrio. "
        else:
            result_string_talento_karma += f"\nEl número {number} se encuentra en carencia. → "
            result_string_talento_karma += search_karma_in_database(df, int(number)) #faltaba poner int() renegue una banda
    
    # Retornar las cadenas de resultado
    return result_string_talento_karma



def stages (total_sum_one_digit, validated_date):
    # Obtener el año en formato AAAA
    full_year = int(datetime.strptime(validated_date, '%d/%m/%Y').strftime('%Y'))
    first_stage_duration = 36-total_sum_one_digit
    first_stage_period =  f"1° etapa de oportunidades y desafíos: {full_year} a {full_year+int(first_stage_duration)}"
    #print (first_stage_period)
    second_stage_duration = int(first_stage_duration)+9
    second_stage_period =  f"2° etapa de oportunidades y desafíos: {full_year+int(first_stage_duration)+1} a {full_year+int(second_stage_duration)}"
    #print (second_stage_period)
    third_stage_duration = int(second_stage_duration)+9
    third_stage_period = f"3° etapa de oportunidades y desafíos: {full_year+int(second_stage_duration)+1} a {full_year+int(third_stage_duration)}"
    #print (third_stage_period)
    fourth_stage_period = f"4° etapa de oportunidades y desafíos: {full_year+int(third_stage_duration)+1} en adelante"
    #print (fourth_stage_period)
    
    # Concatenar todas las etapas en una sola cadena
    stage_period_string = f"\n\n{first_stage_period}\n{second_stage_period}\n{third_stage_period}\n{fourth_stage_period}\n\n"

    return stage_period_string


def digits_governs_stages(validated_date):
    # Llamar a sum_date_digits para obtener los resultados
    #total_sum_one_digit, month_sum_one_digit, day_sum_one_digit, year_sum_one_digit = sum_date_digits(validated_date)
    day_sum_one_digit, month_sum_one_digit, year_sum_one_digit = map(int, validated_date.split('/'))

    stage_oportunities_1 = extract_digits_and_sum_without_master_karmic(str(day_sum_one_digit + month_sum_one_digit))
    result_string = f"1° Etapa de Oportunidades = {stage_oportunities_1} → "
    result_string += search_oportunity_in_database(stage_oportunities_1)
    stage_oportunities_2 = extract_digits_and_sum_without_master_karmic(str(day_sum_one_digit + year_sum_one_digit))
    result_string += f"\n2° Etapa de Oportunidades = {stage_oportunities_2} → "
    result_string += search_oportunity_in_database(stage_oportunities_2)
    stage_oportunities_3 = extract_digits_and_sum_without_master_karmic(str(stage_oportunities_1 + stage_oportunities_2))
    result_string += f"\n3° Etapa de Oportunidades = {stage_oportunities_3} → "
    result_string += search_oportunity_in_database(stage_oportunities_3)
    stage_oportunities_4 = extract_digits_and_sum_without_master_karmic(str(month_sum_one_digit + year_sum_one_digit))
    result_string += f"\n4° Etapa de Oportunidades = {stage_oportunities_4} → "
    result_string += search_oportunity_in_database(stage_oportunities_4)


    # Calcular las etapas de desafíos
    stage_challenges_1 = abs(month_sum_one_digit - day_sum_one_digit)  # Asegurarse de que siempre restamos el número mayor al menor
    stage_challenges_1 = extract_digits_and_sum_without_master_karmic(str(stage_challenges_1))
    result_string += f"\n\n1° Etapa de Desafíos = {stage_challenges_1} → "
    result_string += search_challenge_in_database(stage_challenges_1)

    stage_challenges_2 = abs(day_sum_one_digit - year_sum_one_digit) # Asegurarse de que siempre restamos el número mayor al menor
    stage_challenges_2 = extract_digits_and_sum_without_master_karmic(str(stage_challenges_2))
    result_string += f"\n2° Etapa de Desafíos = {stage_challenges_2} → "
    result_string += search_challenge_in_database(stage_challenges_2)

    stage_challenges_3 = abs(stage_challenges_1 - stage_challenges_2) # Asegurarse de que siempre restamos el número mayor al menor
    stage_challenges_3 = extract_digits_and_sum_without_master_karmic(str(stage_challenges_3))
    result_string += f"\n3° Etapa de Desafíos = {stage_challenges_3} → "
    result_string += search_challenge_in_database(stage_challenges_3)

    stage_challenges_4 = abs(month_sum_one_digit - year_sum_one_digit) # Asegurarse de que siempre restamos el número mayor al menor
    stage_challenges_4 = extract_digits_and_sum_without_master_karmic(str(stage_challenges_4))
    result_string += f"\n4° Etapa de Desafíos = {stage_challenges_4} → "
    result_string += search_challenge_in_database(stage_challenges_4)

    # Retornar cadena
    return result_string


"""HACER ESTO, FALTA SUMAR LAS  CONSONANTES Y DEJARLAS COMO UN NUMERO.
def extern_personality(validated_name):
    # Definir el mapeo de letras a números
    map = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
    'h': 8, 'i': 9, 'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5,
    'ñ': 5, 'o': 6, 'p': 7, 'q': 8, 'r': 9, 's': 1, 't': 2,
    'u': 3, 'v': 4, 'w': 5, 'x': 6, 'y': 7, 'z': 8
    }

    # Inicializar el conteo para cada número del 1 al 9
    count_numbers = {str(i): 0 for i in range(1, 10)}

    # Inicializar la suma de las consonantes
    consonant_sum = 0

    # Contar las ocurrencias de cada número en las consonantes de la entrada
    for letter in validated_name:
        if letter.lower() in map and letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
            valor_numerico = map[letter.lower()]
            count_numbers[str(valor_numerico)] += 1
            consonant_sum += valor_numerico  # Sumar el valor numérico de la consonante

    return count_numbers, consonant_sum
"""

def extern_personality(validated_name):
    # Definir el mapeo de letras a números
    map = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
    'h': 8, 'i': 9, 'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5,
    'ñ': 5, 'o': 6, 'p': 7, 'q': 8, 'r': 9, 's': 1, 't': 2,
    'u': 3, 'v': 4, 'w': 5, 'x': 6, 'y': 7, 'z': 8}

    # Inicializar el conteo para cada número del 1 al 9
    count_numbers = {str(i): 0 for i in range(1, 10)}
    
    # Inicializar la suma de los valores numéricos de las consonantes
    consonant_sum = 0

    # Sumar los valores numéricos de las consonantes de la entrada
    for letter in validated_name:
        if letter.lower() in map and letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
            valor_numerico = map[letter.lower()]
            consonant_sum += valor_numerico  # Sumar el valor numérico de la consonant
    consonant_digit = extract_digits_and_sum_without_karmic(consonant_sum)
    return consonant_digit


def intern_personality(validated_name):
    # Definir el mapeo de letras a números
    map = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
    'h': 8, 'i': 9, 'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5,
    'ñ': 5, 'o': 6, 'p': 7, 'q': 8, 'r': 9, 's': 1, 't': 2,
    'u': 3, 'v': 4, 'w': 5, 'x': 6, 'y': 7, 'z': 8}

    # Inicializar el conteo para cada número del 1 al 9
    count_numbers = {str(i): 0 for i in range(1, 10)}
    
    # Inicializar la suma de los valores numéricos de las consonantes
    vowel_sum = 0

    # Sumar los valores numéricos de las consonantes de la entrada
    for letter in validated_name:
        if letter.lower() in map and letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            valor_numerico = map[letter.lower()]
            vowel_sum += valor_numerico  # Sumar el valor numérico de la vocal
    vowel_digit = extract_digits_and_sum_without_karmic(vowel_sum)
    return vowel_digit


def global_personality(validated_name):
    result_intern_personality = intern_personality(validated_name)
    result_extern_personality = extern_personality(validated_name)
    sum_intern_extern = result_intern_personality + result_extern_personality
    result_global_personality = extract_digits_and_sum_without_karmic(sum_intern_extern)
    return result_global_personality


def personal_year(validated_date):
    # Extraer día, mes y año como cadenas
    day, month, year = validated_date.split('/')

    # Calcular la suma de dígitos para cada componente
    day_sum_one_digit = extract_digits_and_sum_without_master_karmic(day)
    month_sum_one_digit = extract_digits_and_sum_without_master_karmic(month)
    year_sum_one_digit = extract_digits_and_sum_without_master_karmic(datetime.now().year)

    # Sumar las sumas parciales
    total_sum_one_digit = extract_digits_and_sum_without_master_karmic(str(day_sum_one_digit + month_sum_one_digit + year_sum_one_digit))
   
    return total_sum_one_digit

def next_personal_year(validated_date):
    # Extraer día, mes y año como cadenas
    day, month, year = validated_date.split('/')

    # Calcular la suma de dígitos para cada componente
    day_sum_one_digit = extract_digits_and_sum_without_master_karmic(day)
    month_sum_one_digit = extract_digits_and_sum_without_master_karmic(month)
    year_sum_one_digit = extract_digits_and_sum_without_master_karmic((datetime.now().year)+1)

    # Sumar las sumas parciales
    total_sum_one_digit = extract_digits_and_sum_without_master_karmic(str(day_sum_one_digit + month_sum_one_digit + year_sum_one_digit))
   
    return total_sum_one_digit


def translate_text(text, dest_lang='en'):
    try:
        translator = Translator()
        translation = translator.translate(text, dest=dest_lang)
        return translation.text
    except Exception as e:
        st.error(f"Error al traducir: {e}")
        return ""
