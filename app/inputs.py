from datetime import datetime

def validate_date(date_str):
    try:
        # Try to convert the date string to a datetime object
        date_obj = datetime.strptime(date_str, '%d/%m/%Y')
        return True, date_obj
    except ValueError:
        # If there's an error, the date is not valid
        return False, None

"""# Inputs
name_input = input("Ingrese el nombre del paciente, todo en minúsculas y sin tildes: ")
date_input = input("Ingrese la fecha de nacimiento (dd/mm/aaaa): ")"""

def validate_and_store_name (name_input):
    # Comprobar si hay tildes o letras mayúsculas en el nombre
    if any(char.isupper() or ord(char) >= 128 for char in name_input):
        raise ValueError("Error: El nombre no debe contener tildes o letras mayúsculas.")
    else:
       return name_input

"""# Validar y almacenar el nombre solo si cumple con los requisitos
validated_name = validate_and_store_name(name_input)

is_date_valid, date_datetime = validate_date(date_input)
# La función devuelve una tupla con dos elementos: is_date_valid (booleano) y date_datetime (objeto datetime)


def validate_and_store_date (date_datetime):
    if is_date_valid:
        formatted_date = date_datetime.strftime('%d/%m/%Y')
        return formatted_date
    else:
        print("Fecha inválida. Por favor ingrese una fecha con el formato dd/mm/aaaa.")

# Validar y almacenar la fecha solo si cumple con los requisitos
validated_date = validate_and_store_date(date_datetime)"""

def format_date(date_datetime):
    """Devuelve la fecha en formato dd/mm/yyyy."""
    return date_datetime.strftime('%d/%m/%Y')