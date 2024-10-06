import sys
import random  # Para generar valores aleatorios temporales
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QLineEdit,
    QPushButton, QFormLayout, QFrame, QHBoxLayout, QGroupBox, QMessageBox, QTabWidget,
    QScrollArea, QSizePolicy
)
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QFont, QRegExpValidator, QIcon, QPixmap


class Navbar(QFrame):
    """Clase para la barra de navegación superior."""
    def __init__(self):
        super().__init__()
        self.init_navbar()

    def init_navbar(self):
        self.setFixedHeight(70)
        self.setStyleSheet("""
            background-color: #2c3e50;
        """)
        navbar_layout = QHBoxLayout()
        navbar_layout.setContentsMargins(20, 10, 20, 10)
        self.setLayout(navbar_layout)

        # Logo
        logo = QLabel()
        pixmap = QPixmap("logo.png")
        if pixmap.isNull():
            logo.setText("🌾")
            logo.setFont(QFont('Helvetica Neue', 24))
        else:
            logo.setPixmap(pixmap.scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        logo.setStyleSheet("background-color: transparent;")
        logo.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        navbar_layout.addWidget(logo, alignment=Qt.AlignLeft)

        # Título
        title = QLabel("Modelo Predictivo de Cultivos")
        title.setFont(QFont('Helvetica Neue', 20, QFont.Bold))
        title.setStyleSheet("color: #ecf0f1; background-color: transparent;")
        title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        navbar_layout.addWidget(title)#, alignment=Qt.AlignVCenter | Qt.AlignLeft)

        # Botones de navegación adicionales
        home_button = QPushButton("Inicio")
        home_button.setFont(QFont('Helvetica Neue', 14))
        home_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #ecf0f1;
                border: none;
                padding: 10px 15px;
                font-size: 16px;
                cursor: pointer;
                transition: background-color 0.3s, color 0.3s;
            }
            QPushButton:hover {
                background-color: #34495e;
                color: #ffffff;
                border-radius: 5px;
            }
        """)
        navbar_layout.addWidget(home_button, alignment=Qt.AlignRight)

        about_button = QPushButton("Acerca de")
        about_button.setFont(QFont('Helvetica Neue', 14))
        about_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #ecf0f1;
                border: none;
                padding: 10px 15px;
                font-size: 16px;
                cursor: pointer;
                transition: background-color 0.3s, color 0.3s;
            }
            QPushButton:hover {
                background-color: #34495e;
                color: #ffffff;
                border-radius: 5px;
            }
        """)
        navbar_layout.addWidget(about_button, alignment=Qt.AlignRight)


class PredefinedInputForm(QGroupBox):
    """Formulario de selección por zona predefinida."""
    def __init__(self):
        super().__init__("Selección por Zona Predefinida")
        self.init_form()

    def init_form(self):
        self.setStyleSheet("""
            QGroupBox {
                border: 3px solid #2c3e50;
                border-radius: 10px;
                margin-top: 20px;
                background-color: #f0f4f7;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 15px;
                padding: 0 5px 0 5px;
                background-color: white;
                color: #2c3e50;
                font-size: 18px;
                font-weight: bold;
            }
            QLabel {
                color: #2c3e50;
                font-size: 16px;
                background-color: #f0f4f7;
            }
        """)
        form_layout = QFormLayout()
        form_layout.setLabelAlignment(Qt.AlignRight)
        form_layout.setFormAlignment(Qt.AlignLeft | Qt.AlignTop)
        form_layout.setContentsMargins(30, 30, 30, 30)
        self.setLayout(form_layout)


                # Selección de País
        self.pais_combo = QComboBox()
        self.pais_combo.addItems(["Seleccionar un exo/planeta", "Tierra","Marte","AU Mic b" ])
        self.pais_combo.setFont(QFont('Helvetica Neue', 14))
        self.pais_combo.currentIndexChanged.connect(self.load_states)
        self.pais_combo.setStyleSheet("""
            QComboBox {
                background-color:  #ffffff;
                border: 2px solid #2c3e50;
                border-radius: 5px;
                padding: 8px;
                font-size: 14px;
                color: #2c3e50;
                transition: border-color 0.3s;
            }
            QComboBox:hover {
                border-color: #2980b9;
            }
            QComboBox::drop-down {
                border-left: none;
            }
        """)
        form_layout.addRow(QLabel("Planeta:"), self.pais_combo)

        # Selección de País
        self.pais_combo = QComboBox()
        self.pais_combo.addItems(["Seleccione un país", "México", "Estados Unidos", "Canadá"])
        self.pais_combo.setFont(QFont('Helvetica Neue', 14))
        self.pais_combo.currentIndexChanged.connect(self.load_states)
        self.pais_combo.setStyleSheet("""
            QComboBox {
                background-color:  #ffffff;
                border: 2px solid #2c3e50;
                border-radius: 5px;
                padding: 8px;
                font-size: 14px;
                color: #2c3e50;
                transition: border-color 0.3s;
            }
            QComboBox:hover {
                border-color: #2980b9;
            }
            QComboBox::drop-down {
                border-left: none;
            }
        """)
        form_layout.addRow(QLabel("País:"), self.pais_combo)

        # Selección de Estado/Región
        self.estado_combo = QComboBox()
        self.estado_combo.addItem("Seleccione primero un país")
        self.estado_combo.setFont(QFont('Helvetica Neue', 14))
        self.estado_combo.setStyleSheet("""
            QComboBox {
                background-color: #ffffff;
                border: 2px solid #2c3e50;
                border-radius: 5px;
                padding: 8px;
                font-size: 14px;
                color: #2c3e50;
                transition: border-color 0.3s;
            }
            QComboBox:hover {
                border-color: #2980b9;
            }
            QComboBox::drop-down {
                border-left: none;
            }
        """)
        form_layout.addRow(QLabel("Estado/Región:"), self.estado_combo)

        # Tipo de Suelo
        self.tipo_suelo_combo = QComboBox()
        self.tipo_suelo_combo.addItems([
            "Seleccione tipo de suelo", "Arenoso", "Arcilloso", "Limoso", "Mixto", "Calcáreo"
        ])
        self.tipo_suelo_combo.setFont(QFont('Helvetica Neue', 14))
        self.tipo_suelo_combo.currentIndexChanged.connect(self.validate_form)
        self.tipo_suelo_combo.setStyleSheet("""
            QComboBox {
                background-color: #ffffff;
                border: 2px solid #2c3e50;
                border-radius: 5px;
                padding: 8px;
                font-size: 14px;
                color: #2c3e50;
                transition: border-color 0.3s;
            }
            QComboBox:hover {
                border-color: #2980b9;
            }
            QComboBox::drop-down {
                border-left: none;
            }
        """)
        form_layout.addRow(QLabel("Tipo de suelo:"), self.tipo_suelo_combo)

        # Botón de Envío
        self.submit_button = QPushButton("Generar predicción")
        self.submit_button.setEnabled(False)
        self.submit_button.setFixedHeight(45)
        self.submit_button.setFont(QFont('Helvetica Neue', 16))
        self.submit_button.setStyleSheet("""
            QPushButton {
                background-color: #2980b9;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 10px 25px;
                font-size: 16px;
                cursor: pointer;
                transition: background-color 0.3s, transform 0.2s;
            }
            QPushButton:enabled {
                background-color: #95a5a6;
                cursor: not-allowed;
            }
            QPushButton:hover:enabled {
                background-color: #3498db;
                transform: scale(1.05);
            }
        """)
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.submit_button)
        button_layout.addStretch()
        form_layout.addRow(button_layout)
    

    def load_states(self):
        """Actualiza la lista de estados/regiones según el país seleccionado."""
        country = self.pais_combo.currentText()
        self.estado_combo.clear()

        states = {
            "México": ["Seleccione un estado", "Jalisco", "Nuevo León", "Ciudad de México", "Yucatán", "Veracruz"],
            "Estados Unidos": ["Seleccione un estado", "California", "Texas", "Nueva York", "Florida", "Illinois"],
            "Canadá": ["Seleccione una provincia", "Ontario", "Quebec", "Columbia Británica", "Alberta", "Manitoba"]
        }

        if country in states:
            self.estado_combo.addItems(states[country])
        else:
            self.estado_combo.addItem("Seleccione primero un país")
        self.validate_form()

    def validate_form(self):
        """Valida las selecciones del formulario."""
        country_valid = self.pais_combo.currentIndex() > 0
        state_valid = self.estado_combo.currentIndex() > 0
        soil_valid = self.tipo_suelo_combo.currentIndex() > 0
        form_valid = all([country_valid, state_valid, soil_valid])
        self.submit_button.setEnabled(form_valid)


class ManualInputForm(QGroupBox):
    """Formulario de ingreso manual de datos."""
    def __init__(self):
        super().__init__("Ingreso Manual de Datos")
        self.init_form()

    def init_form(self):
        self.setStyleSheet("""
            QGroupBox {
                border: 3px solid #2c3e50;
                border-radius: 10px;
                margin-top: 20px;
                background-color: #f0f4f7;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 15px;
                padding: 0 5px 0 5px;
                background-color: white;
                color: #2c3e50;
                font-size: 18px;
                font-weight: bold;
            }
            QLabel {
                color: #2c3e50;
                font-size: 16px;
            }
        """)
        form_layout = QFormLayout()
        form_layout.setLabelAlignment(Qt.AlignRight)
        form_layout.setFormAlignment(Qt.AlignLeft | Qt.AlignTop)
        form_layout.setContentsMargins(30, 30, 30, 30)
        self.setLayout(form_layout)

        # Campos de entrada
        self.inputs = {}
        fields = {
            "Humedad del suelo (%)": r"^\d{1,3}(\.\d{1,2})?$",
            "Temperatura promedio (°C)": r"^-?\d{1,3}(\.\d{1,2})?$",
            "Precipitación (mm)": r"^\d{1,4}(\.\d{1,2})?$",
            "Altitud (msnm)": r"^-?\d{1,4}(\.\d{1,2})?$",
            "pH del suelo": r"^\d{1,2}(\.\d{1,2})?$"
        }

        for label, regex in fields.items():
            line_edit = QLineEdit()
            line_edit.setPlaceholderText(f"Ingrese {label.lower()}")
            line_edit.setFont(QFont('Helvetica Neue', 14))
            validator = QRegExpValidator(QRegExp(regex))
            line_edit.setValidator(validator)
            line_edit.textChanged.connect(self.validate_form)
            line_edit.setStyleSheet("""
                QLineEdit {
                    background-color: #ffffff;
                    border: 2px solid #2c3e50;
                    border-radius: 5px;
                    padding: 8px;
                    font-size: 14px;
                    color: #2c3e50;
                    transition: border-color 0.3s;
                }
                QLineEdit:hover {
                    border-color: #2980b9;
                }
            """)
            form_layout.addRow(QLabel(f"{label}:"), line_edit)
            self.inputs[label] = line_edit

        # Botón de Envío
        self.submit_button = QPushButton("Generar predicción")
        self.submit_button.setEnabled(False)
        self.submit_button.setFixedHeight(45)
        self.submit_button.setFont(QFont('Helvetica Neue', 16))
        self.submit_button.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 10px 25px;
                font-size: 16px;
                cursor: pointer;
                transition: background-color 0.3s, transform 0.2s;
            }
            QPushButton:enabled {
                background-color: #95a5a6;
                cursor: not-allowed;
            }
            QPushButton:hover:enabled {
                background-color: #2ecc71;
                transform: scale(1.05);
            }
        """)
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.submit_button)
        button_layout.addStretch()
        form_layout.addRow(button_layout)

    def validate_form(self):
        """Valida las entradas del formulario."""
        form_valid = all(
            input_field.hasAcceptableInput() and input_field.text() != ""
            for input_field in self.inputs.values()
        )
        self.submit_button.setEnabled(form_valid)


class ResultsDisplay(QGroupBox):
    """Muestra los resultados de la predicción."""
    def __init__(self):
        super().__init__("Resultados de la Predicción")
        self.init_results()

    def init_results(self):
        self.setStyleSheet("""
            QGroupBox {
                border: 3px solid #2c3e50;
                border-radius: 10px;
                margin-top: 20px;
                background-color: #f0f4f7;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 15px;
                padding: 0 5px 0 5px;
                background-color: white;
                color: #2c3e50;
                font-size: 18px;
                font-weight: bold;
            }
            QLabel {
                color: #2c3e50;
                font-size: 16px;
                background-color: transparent;
            }
            
        
        """)
        results_layout = QVBoxLayout()
        results_layout.setContentsMargins(30, 30, 30, 30)
        self.setLayout(results_layout)

        # Título de Resultados
        results_title = QLabel("Resultados de la predicción")
        results_title.setFont(QFont('Helvetica Neue', 18, QFont.Bold))
        results_title.setStyleSheet("color: #2c3e50;")
        results_layout.addWidget(results_title)

        # Espaciador
        results_layout.addSpacing(20)

        # Widgets de resultados
        self.result_widgets = []

        for label_text in [
            "Probabilidad de éxito del cultivo",
            "Probabilidad de fenómeno natural que afecte",
            "Recomendación de tipo de cultivo",
            "Sugerencias de manejo agronómico"
        ]:
            label = QLabel(f"{label_text}: -")
            label.setFont(QFont('Helvetica Neue', 16))
            label.setStyleSheet("color: #2c3e50;")
            results_layout.addWidget(label)
            self.result_widgets.append(label)


class PredictiveModelApp(QWidget):
    """Clase principal de la aplicación."""
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Modelo Predictivo de Cultivos")
        self.setGeometry(100, 100, 1600, 1000)
        self.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
            }
        """)
        # self.setWindowIcon(QIcon("app_icon.png"))  # Descomenta si tienes el icono

        # Layout principal
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Barra de navegación
        navbar = Navbar()
        main_layout.addWidget(navbar)

        # Área central con scroll
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("background-color: #ffffff;")
        main_content = QWidget()
        scroll_area.setWidget(main_content)
        main_layout.addWidget(scroll_area)

        content_layout = QVBoxLayout(main_content)
        content_layout.setSpacing(20)
        content_layout.setContentsMargins(40, 40, 40, 40)

        # Pestañas
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.North)
        self.tabs.setTabShape(QTabWidget.Rounded)
        # No es necesario usar objectName si no utilizas CSS externo
        self.tabs.setStyleSheet("""
            QTabBar::tab {
            background: #BDC3C7;
            border: 2px solid #C4C4C3;
            border-bottom-color: #C2C7CB; /* same as pane color */
            border-top-left-radius: 4px;
            border-top-right-radius: 4px;
            min-width: 150px; /* Aumentar el ancho mínimo para evitar corte de texto */
            padding: 10px;
            font: bold 14px;
            color: #2C3E50;
            }
            QTabBar::tab:selected {
                background: #3498db;
                color: white;
                font-weight: bold;
            }
            QTabBar::tab:hover {
                background: #bdc3c7;
            }
        """)

        # Agregar pestañas
        self.predefined_tab = PredefinedInputForm()
        self.manual_tab = ManualInputForm()
        self.tabs.addTab(self.predefined_tab, "Proceso Predefinido")
        self.tabs.addTab(self.manual_tab, "Manual")

        content_layout.addWidget(self.tabs)

        # Resultados de la predicción
        self.results_display = ResultsDisplay()
        content_layout.addWidget(self.results_display, stretch=1)

        # Conectar botones
        self.manual_tab.submit_button.clicked.connect(self.generate_prediction_manual)
        self.predefined_tab.submit_button.clicked.connect(self.generate_prediction_predefined)

    def generate_prediction_manual(self):
        """Genera y muestra los resultados para ingreso manual."""
        try:
            data = {label: float(input_field.text()) for label, input_field in self.manual_tab.inputs.items()}
        except ValueError:
            QMessageBox.warning(self, "Entrada inválida", "Por favor, verifica las entradas numéricas.")
            return

        # Simulación de predicción con valores aleatorios
        cultivo_probabilidad = random.uniform(50, 100)
        fenomeno_probabilidad = random.uniform(0, 50)
        tipo_cultivo = random.choice(["Maíz", "Trigo", "Soja", "Arroz"])
        manejo = random.choice([
            "Rotación de cultivos",
            "Uso de fertilizantes orgánicos",
            "Control biológico de plagas",
            "Riego por goteo"
        ])

        # Actualizar resultados
        self.results_display.result_widgets[0].setText(
            f"Probabilidad de éxito del cultivo: {round(cultivo_probabilidad, 2)} %"
        )
        self.results_display.result_widgets[1].setText(
            f"Probabilidad de fenómeno natural que afecte: {round(fenomeno_probabilidad, 2)} %"
        )
        self.results_display.result_widgets[2].setText(
            f"Recomendación de tipo de cultivo: {tipo_cultivo}"
        )
        self.results_display.result_widgets[3].setText(
            f"Sugerencias de manejo agronómico: {manejo}"
        )

    def generate_prediction_predefined(self):
        """Genera y muestra los resultados para selección predefinida."""
        pais = self.predefined_tab.pais_combo.currentText()
        estado = self.predefined_tab.estado_combo.currentText()
        tipo_suelo = self.predefined_tab.tipo_suelo_combo.currentText()

        # Validar selecciones
        if pais == "Seleccione un país" or estado.startswith("Seleccione") or tipo_suelo == "Seleccione tipo de suelo":
            QMessageBox.warning(self, "Selección inválida", "Por favor, verifica las selecciones realizadas.")
            return

        # Simulación de predicción con valores aleatorios
        cultivo_probabilidad = random.uniform(50, 100)
        fenomeno_probabilidad = random.uniform(0, 50)
        tipo_cultivo = random.choice(["Maíz", "Trigo", "Soja", "Arroz"])
        manejo = random.choice([
            "Rotación de cultivos",
            "Uso de fertilizantes orgánicos",
            "Control biológico de plagas",
            "Riego por goteo"
        ])

        # Actualizar resultados
        self.results_display.result_widgets[0].setText(
            f"Probabilidad de éxito del cultivo: {round(cultivo_probabilidad, 2)} %"
        )
        self.results_display.result_widgets[1].setText(
            f"Probabilidad de fenómeno natural que afecte: {round(fenomeno_probabilidad, 2)} %"
        )
        self.results_display.result_widgets[2].setText(
            f"Recomendación de tipo de cultivo: {tipo_cultivo}"
        )
        self.results_display.result_widgets[3].setText(
            f"Sugerencias de manejo agronómico: {manejo}"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PredictiveModelApp()
    window.show()
    sys.exit(app.exec_())