import streamlit as st
from app.calculations import *
from app.bd_connection import *

# Diccionario de usuarios y contraseñas
CREDENTIALS = {
    "admin": "Numerologia11"
    #"user2": "password2",
}

# Función para autenticar
def authenticate(username, password):
    return CREDENTIALS.get(username) == password

# Crear el formulario de login
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Función principal
def main():
    if not st.session_state.authenticated:
        # Mostrar formulario de inicio de sesión
        st.title("Inicio de Sesión")
        username = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")
        if st.button("Iniciar sesión"):
            if authenticate(username, password):
                st.session_state.authenticated = True
                st.success("Inicio de sesión exitoso")
            else:
                st.error("Usuario o contraseña incorrectos")
    else:
        # Contenido de la aplicación principal
        st.title("Calculadora de Numerología Evolutiva")

        # Entrada para el nombre del paciente
        name = st.text_input("Nombre del paciente (todo en minúsculas y sin tildes):", "")
        date = st.text_input("Fecha de nacimiento (dd/mm/aaaa):", "")

        # Botón para calcular
        if st.button("Calcular"):
            if not name or not date:
                st.error("Por favor, ingresa un nombre y una fecha válida.")
            else:
                try:
                    # Generar resultados
                    result_text = (
                        f"Nombre completo: {name}\n"
                        f"Fecha de nacimiento: {date}\n\n"
                    )

                    total_sum_one_digit, month_sum_one_digit, day_sum_one_digit, year_sum_one_digit = sum_date_digits(date)

                    result_text += (
                        f"El número de destino o camino de vida es: {total_sum_one_digit}\n\n"
                        f"{search_destinity_number(total_sum_one_digit)}"
                        f"Interpretación de los ciclos de vida:\n\n"
                        f"El {month_sum_one_digit} marcaría su primer ciclo de vida, el de formación (desde el nacimiento hasta los 20 años)\n"
                        f"{search_cycle1(month_sum_one_digit)}\n"
                        f"El {day_sum_one_digit} marcaría su segundo ciclo de vida, los años de productividad\n"
                        f"{search_cycle2(day_sum_one_digit)}\n"
                        f"El {year_sum_one_digit} marcaría su tercer ciclo de vida, el de recolección o cosecha\n"
                        f"{search_cycle3(year_sum_one_digit)}\n"
                    )

                    result_text += determinate_karma_talent(df, name)
                    result_text += stages(total_sum_one_digit, date)
                    result_text += digits_governs_stages(date)

                    personal_year_value = personal_year(date)
                    result_text += search_personal_year_in_database(personal_year_value)

                    next_personal_year_value = next_personal_year(date)
                    result_text += search_next_personal_year_in_database(next_personal_year_value)

                    extern_personality_value = extern_personality(name)
                    result_text += search_extern_personality_in_database(extern_personality_value)

                    intern_personality_value = intern_personality(name)
                    result_text += search_intern_personality_in_database(intern_personality_value)

                    global_personality_value = global_personality(name)
                    result_text += search_global_personality_in_database(global_personality_value)

                    result_text += search_vocation_in_database(intern_personality_value)

                    # Mostrar los resultados en el área de texto
                    st.text_area("Resultados", result_text, height=800)

                    # Guardar los resultados globalmente para exportar
                    st.session_state["results"] = result_text

                except Exception as e:
                    st.error(f"Error en los cálculos: {e}")

        # Botón para exportar a PDF
        if st.button("Generar PDF"):
            if name and date and "results" in st.session_state:
                # Llamar a la función export_to_pdf
                pdf_buffer = export_to_pdf(name, date, st.session_state["results"])
                
                # Usar st.download_button para descargar el PDF
                st.download_button(
                    label="Descargar PDF",
                    data=pdf_buffer,
                    file_name=f"{name}_numerologia.pdf",
                    mime="application/pdf",
                )
            else:
                st.warning("Por favor, completa los cálculos antes de generar el PDF.")

if __name__ == '__main__':
    main()
