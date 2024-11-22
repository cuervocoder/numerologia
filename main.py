from unittest import result
from app.inputs import *
from app.calculations import *
from app.bd_connection import *
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QTextEdit, QLineEdit


class NumerologyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Configuración de la ventana principal
        self.setWindowTitle('Numerología Evolutiva')
        self.setGeometry(100, 100, 600, 400)  # (x, y, ancho, alto)

        self.label_name = QLabel('Nombre del paciente (todo en minúsculas y sin tildes):', self)
        self.edit_name = QLineEdit(self)

        # Crear y configurar elementos de la interfaz
        self.label_date = QLabel('Fecha de nacimiento (dd/mm/aaaa):', self)
        self.edit_date = QLineEdit(self)

        self.label_result = QLabel('Resultados:', self)
        self.text_result = QTextEdit(self)
        self.btn_calculate = QPushButton('Calcular', self)
        self.btn_calculate.clicked.connect(self.calculate_numerology)


        #NUEVO PDF
        # Botón para exportar
        self.btn_export = QPushButton('Exportar a PDF', self)
        self.btn_export.clicked.connect(self.export_pdf)   
        #FIN NUEVO PDF

        # Configuración de la disposición
        layout = QVBoxLayout()
        layout.addWidget(self.label_name)
        layout.addWidget(self.edit_name)

        layout.addWidget(self.label_date)
        layout.addWidget(self.edit_date)

        layout.addWidget(self.label_result)
        layout.addWidget(self.text_result)
        layout.addWidget(self.btn_calculate)
        #PFD
        layout.addWidget(self.btn_export) 
        #FIN PDF

        # Configurar la disposición de la ventana principal
        self.setLayout(layout)

        # Mostrar la ventana
        self.show()

    def calculate_numerology(self):
        # Obtener la fecha y el nombre validados
        validated_date = self.edit_date.text()
        validated_name = self.edit_name.text()

        result_text = (
            f"Nombre completo: {validated_name}\n"
            f"Fecha de nacimiento: {validated_date}\n\n"
        )

        # Llamar a la función sum_date_digits para obtener la suma total de dígitos
        total_sum_one_digit, month_sum_one_digit, day_sum_one_digit, year_sum_one_digit = sum_date_digits(validated_date)

        # Construir el texto de resultado
        result_text += (
            f"El número de destino o camino de vida es: {total_sum_one_digit}\n\n"
            f"{search_destinity_number(total_sum_one_digit)}"
            f"Interpretación de los ciclos de vida:\n\nEl {month_sum_one_digit} marcaría su primer ciclo de vida, el de formación (desde el nacimiento hasta los 20 años)\n"
            f"{search_cycle1(month_sum_one_digit)}\n"
            f"El {day_sum_one_digit} marcaría su segundo ciclo de vida, los años de productividad\n"
            f"{search_cycle2(day_sum_one_digit)}\n"
            f"El {year_sum_one_digit} marcaría su tercer ciclo de vida, el de recolección o cosecha\n"
            f"{search_cycle3(year_sum_one_digit)}\n"
        )

        result_text += determinate_karma_talent(df, validated_name)

        result_text += stages (total_sum_one_digit, validated_date)

        result_text += digits_governs_stages(validated_date)

        personal_year_value = personal_year(validated_date)
        result_text += search_personal_year_in_database(personal_year_value)

        next_personal_year_value = next_personal_year(validated_date)
        result_text += search_next_personal_year_in_database(next_personal_year_value)

        extern_personality_value = extern_personality(validated_name)
        result_text += search_extern_personality_in_database(extern_personality_value)

        intern_personality_value = intern_personality(validated_name)
        result_text += search_intern_personality_in_database(intern_personality_value)

        global_personality_value = global_personality(validated_name)
        result_text += search_global_personality_in_database(global_personality_value)

        result_text += search_vocation_in_database(intern_personality_value)

        # Mostrar los resultados en el cuadro de texto
        self.text_result.setPlainText(result_text)

#PDF
    def export_pdf(self):
        name = self.edit_name.text()
        date = self.edit_date.text()
        results = self.text_result.toPlainText()
        export_to_pdf(name, date, results)
#FIN PDF


if __name__ == '__main__':
    app = QApplication(sys.argv)
    numerology_app = NumerologyApp()
    sys.exit(app.exec_())


"""
print (validated_date)
print (validated_name)


# Llamar a la función sum_date_digits para obtener la suma total de dígitos
total_sum_one_digit, year_sum_one_digit, month_sum_one_digit, day_sum_one_digit = sum_date_digits(date_input)
# Mostrar resultados
print(f"El número de destino o camino de vida es: {total_sum_one_digit}")
print(f"el {day_sum_one_digit} marcaría su primer ciclo de vida")
print(f"el {month_sum_one_digit} marcaría su segundo ciclo de vida")
print(f"el {year_sum_one_digit} marcaría su tercer ciclo de vida")

#total_sum_one_digit, year_sum_one_digit, month_sum_one_digit, day_sum_one_digit = sum_date_digits(validated_date)


results = count_letters_times(validated_name)
# Mostrar los resultados
for number, quantity in results.items():
    print(f"Número {number}: {quantity} ocurrencias")

stages (total_sum_one_digit, validated_date)

digits_governs_stages(validated_date)
"""