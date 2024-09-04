import sys
import random
import string
import re
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QHBoxLayout,
    QCheckBox, QGridLayout
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPalette, QColor, QIntValidator, QClipboard


class PasswordGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.is_dark_mode = True

        self.setWindowTitle("Password & Number Generator with Validators")
        self.setGeometry(100, 100, 600, 600)

        # Main layout
        layout = QVBoxLayout()

        # Top layout for mode button and exit button
        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(0, 0, 0, 0)

        # Dark/Light Mode Button
        self.mode_button = QPushButton("Light")
        self.mode_button.setFont(QFont("Arial", 14))
        self.mode_button.setStyleSheet("background-color: #5555ff; color: white; padding: 15px; border-radius: 75px;")
        self.mode_button.clicked.connect(self.toggle_mode)
        top_layout.addWidget(self.mode_button, alignment=Qt.AlignLeft)

        # Exit Button
        self.exit_button = QPushButton("Exit")
        self.exit_button.setFont(QFont("Arial", 14))
        self.exit_button.setStyleSheet("background-color: #ff5555; color: white; padding: 15px; border-radius: 75px;")
        self.exit_button.clicked.connect(self.close)
        top_layout.addWidget(self.exit_button, alignment=Qt.AlignRight)

        layout.addLayout(top_layout)

        # Password Section
        self.password_label = QLabel("Generated Password: ")
        self.password_label.setFont(QFont("Arial", 14))
        layout.addWidget(self.password_label, alignment=Qt.AlignCenter)

        self.password_input = QLineEdit()
        self.password_input.setFont(QFont("Arial", 18))
        self.password_input.setReadOnly(True)
        self.password_input.setAlignment(Qt.AlignCenter)
        self.password_input.setStyleSheet("background-color: #333333; color: white; padding: 10px; border-radius: 15px;")
        layout.addWidget(self.password_input, alignment=Qt.AlignCenter)

        # Password Options Section
        options_layout = QGridLayout()

        # Password Length
        self.length_label = QLabel("Length:")
        self.length_label.setFont(QFont("Arial", 14))
        options_layout.addWidget(self.length_label, 0, 0, alignment=Qt.AlignCenter)

        self.length_input = QLineEdit()
        self.length_input.setFont(QFont("Arial", 14))
        self.length_input.setValidator(QIntValidator(1, 100))
        self.length_input.setText("12")
        self.length_input.setAlignment(Qt.AlignCenter)
        self.length_input.setStyleSheet("background-color: #333333; color: white; padding: 10px; border-radius: 15px;")
        options_layout.addWidget(self.length_input, 0, 1, alignment=Qt.AlignCenter)

        # Checkboxes for password options
        self.uppercase_checkbox = QCheckBox("Uppercase")
        self.uppercase_checkbox.setFont(QFont("Arial", 14))
        self.uppercase_checkbox.setStyleSheet("color: green;")
        self.uppercase_checkbox.setChecked(True)
        options_layout.addWidget(self.uppercase_checkbox, 1, 0, alignment=Qt.AlignCenter)

        self.lowercase_checkbox = QCheckBox("Lowercase")
        self.lowercase_checkbox.setFont(QFont("Arial", 14))
        self.lowercase_checkbox.setStyleSheet("color: green;")
        self.lowercase_checkbox.setChecked(True)
        options_layout.addWidget(self.lowercase_checkbox, 1, 1, alignment=Qt.AlignCenter)

        self.numbers_checkbox = QCheckBox("Numbers")
        self.numbers_checkbox.setFont(QFont("Arial", 14))
        self.numbers_checkbox.setStyleSheet("color: green;")
        self.numbers_checkbox.setChecked(True)
        options_layout.addWidget(self.numbers_checkbox, 2, 0, alignment=Qt.AlignCenter)

        self.special_checkbox = QCheckBox("Special Characters")
        self.special_checkbox.setFont(QFont("Arial", 14))
        self.special_checkbox.setStyleSheet("color: green;")
        self.special_checkbox.setChecked(True)
        options_layout.addWidget(self.special_checkbox, 2, 1, alignment=Qt.AlignCenter)

        self.symbols_checkbox = QCheckBox("Symbols")
        self.symbols_checkbox.setFont(QFont("Arial", 14))
        self.symbols_checkbox.setStyleSheet("color: green;")
        self.symbols_checkbox.setChecked(True)
        options_layout.addWidget(self.symbols_checkbox, 3, 0, alignment=Qt.AlignCenter)

        self.spaces_checkbox = QCheckBox("Spaces")
        self.spaces_checkbox.setFont(QFont("Arial", 14))
        self.spaces_checkbox.setStyleSheet("color: green;")
        self.spaces_checkbox.setChecked(False)
        options_layout.addWidget(self.spaces_checkbox, 3, 1, alignment=Qt.AlignCenter)

        layout.addLayout(options_layout)

        password_buttons_layout = QHBoxLayout()
        self.generate_password_button = QPushButton("Generate")
        self.generate_password_button.setFont(QFont("Arial", 14))
        self.generate_password_button.setStyleSheet("background-color: #ff5555; color: white; padding: 15px; border-radius: 75px;")
        self.generate_password_button.clicked.connect(self.generate_password)
        password_buttons_layout.addWidget(self.generate_password_button, alignment=Qt.AlignCenter)

        self.copy_password_button = QPushButton("Copy")
        self.copy_password_button.setFont(QFont("Arial", 14))
        self.copy_password_button.setStyleSheet("background-color: #5555ff; color: white; padding: 15px; border-radius: 75px;")
        self.copy_password_button.clicked.connect(self.copy_password)
        password_buttons_layout.addWidget(self.copy_password_button, alignment=Qt.AlignCenter)

        layout.addLayout(password_buttons_layout)

        # Number Section
        self.number_label = QLabel("Generated Number:")
        self.number_label.setFont(QFont("Arial", 14))
        layout.addWidget(self.number_label, alignment=Qt.AlignCenter)

        self.number_input = QLineEdit()
        self.number_input.setFont(QFont("Arial", 18))
        self.number_input.setReadOnly(True)
        self.number_input.setAlignment(Qt.AlignCenter)
        self.number_input.setStyleSheet("background-color: #333333; color: white; padding: 10px; border-radius: 40px;")
        layout.addWidget(self.number_input, alignment=Qt.AlignCenter)

        number_buttons_layout = QHBoxLayout()
        self.generate_number_button = QPushButton("Generate")
        self.generate_number_button.setFont(QFont("Arial", 14))
        self.generate_number_button.setStyleSheet("background-color: #55ff55; color: white; padding: 40px; border-radius: 75px;")
        self.generate_number_button.clicked.connect(self.generate_number)
        number_buttons_layout.addWidget(self.generate_number_button, alignment=Qt.AlignCenter)

        self.copy_number_button = QPushButton("Copy")
        self.copy_number_button.setFont(QFont("Arial", 14))
        self.copy_number_button.setStyleSheet("background-color: #5555ff; color: white; padding: 15px; border-radius: 75px;")
        self.copy_number_button.clicked.connect(self.copy_number)
        number_buttons_layout.addWidget(self.copy_number_button, alignment=Qt.AlignCenter)

        # Range input boxes
        self.min_input = QLineEdit()
        self.min_input.setFont(QFont("Arial", 14))
        self.min_input.setAlignment(Qt.AlignCenter)
        self.min_input.setValidator(QIntValidator())
        self.min_input.setText("1")
        self.min_input.setStyleSheet("background-color: #333333; color: white; padding: 10px; border-radius: 15px;")
        number_buttons_layout.addWidget(self.min_input, alignment=Qt.AlignCenter)

        self.max_input = QLineEdit()
        self.max_input.setFont(QFont("Arial", 14))
        self.max_input.setAlignment(Qt.AlignCenter)
        self.max_input.setValidator(QIntValidator())
        self.max_input.setText("100")
        self.max_input.setStyleSheet("background-color: #333333; color: white; padding: 10px; border-radius: 15px;")
        number_buttons_layout.addWidget(self.max_input, alignment=Qt.AlignCenter)

        layout.addLayout(number_buttons_layout)

        # Email Validation Section
        self.email_label = QLabel("Email Validator:")
        self.email_label.setFont(QFont("Arial", 14))
        layout.addWidget(self.email_label, alignment=Qt.AlignCenter)

        self.email_input = QLineEdit()
        self.email_input.setFont(QFont("Arial", 14))
        self.email_input.setAlignment(Qt.AlignCenter)
        self.email_input.setStyleSheet("background-color: #333333; color: white; padding: 10px; border-radius: 15px;")
        layout.addWidget(self.email_input, alignment=Qt.AlignCenter)

        self.validate_email_button = QPushButton("Validate Email")
        self.validate_email_button.setFont(QFont("Arial", 14))
        self.validate_email_button.setStyleSheet("background-color: #ffaa00; color: white; padding: 15px; border-radius: 75px;")
        self.validate_email_button.clicked.connect(self.validate_email)
        layout.addWidget(self.validate_email_button, alignment=Qt.AlignCenter)

        self.email_validation_result = QLabel("")
        self.email_validation_result.setFont(QFont("Arial", 14))
        layout.addWidget(self.email_validation_result, alignment=Qt.AlignCenter)

        # URL Validation Section
        self.url_label = QLabel("URL Validator:")
        self.url_label.setFont(QFont("Arial", 14))
        layout.addWidget(self.url_label, alignment=Qt.AlignCenter)

        self.url_input = QLineEdit()
        self.url_input.setFont(QFont("Arial", 14))
        self.url_input.setAlignment(Qt.AlignCenter)
        self.url_input.setStyleSheet("background-color: #333333; color: white; padding: 10px; border-radius: 15px;")
        layout.addWidget(self.url_input, alignment=Qt.AlignCenter)

        self.validate_url_button = QPushButton("Validate URL")
        self.validate_url_button.setFont(QFont("Arial", 14))
        self.validate_url_button.setStyleSheet("background-color: #ffaa00; color: white; padding: 15px; border-radius: 75px;")
        self.validate_url_button.clicked.connect(self.validate_url)
        layout.addWidget(self.validate_url_button, alignment=Qt.AlignCenter)

        self.url_validation_result = QLabel("")
        self.url_validation_result.setFont(QFont("Arial", 14))
        layout.addWidget(self.url_validation_result, alignment=Qt.AlignCenter)

        self.setLayout(layout)

        self.apply_dark_mode()

    def toggle_mode(self):
        if self.is_dark_mode:
            self.apply_light_mode()
        else:
            self.apply_dark_mode()
        self.is_dark_mode = not self.is_dark_mode

    def apply_dark_mode(self):
        self.setStyleSheet("background-color: #1e1e1e; color: white;")
        self.mode_button.setText("Light")
        self.exit_button.setStyleSheet("background-color: #ff5555; color: white; padding: 15px; border-radius: 75px;")
        self.mode_button.setStyleSheet("background-color: #5555ff; color: white; padding: 15px; border-radius: 75px;")
        self.apply_common_styles()

    def apply_light_mode(self):
        self.setStyleSheet("background-color: #f5f5f5; color: black;")
        self.mode_button.setText("Dark")
        self.exit_button.setStyleSheet("background-color: #ff5555; color: white; padding: 15px; border-radius: 75px;")
        self.mode_button.setStyleSheet("background-color: #5555ff; color: white; padding: 15px; border-radius: 75px;")
        self.apply_common_styles()

    def apply_common_styles(self):
        # Update all input fields and buttons to match the new mode
        for widget in self.findChildren(QLineEdit):
            widget.setStyleSheet(f"background-color: {'#333333' if self.is_dark_mode else '#ffffff'}; color: {'white' if self.is_dark_mode else 'black'}; padding: 10px; border-radius: 15px;")
        for widget in self.findChildren(QPushButton):
            widget.setStyleSheet(f"padding: 15px; border-radius: 75px; color: white; background-color: {'#5555ff' if widget.text() == 'Dark' else '#ff5555' if widget.text() == 'Exit' else '#ffaa00'};")
        for widget in self.findChildren(QCheckBox):
            widget.setStyleSheet(f"color: green;")

    def generate_password(self):
        length = int(self.length_input.text())
        char_pool = ''
        if self.uppercase_checkbox.isChecked():
            char_pool += string.ascii_uppercase
        if self.lowercase_checkbox.isChecked():
            char_pool += string.ascii_lowercase
        if self.numbers_checkbox.isChecked():
            char_pool += string.digits
        if self.special_checkbox.isChecked():
            char_pool += "!@#$%^&*()"
        if self.symbols_checkbox.isChecked():
            char_pool += string.punctuation
        if self.spaces_checkbox.isChecked():
            char_pool += ' '

        if not char_pool:
            self.password_input.setText("Please select at least one option.")
            return

        password = ''.join(random.choice(char_pool) for _ in range(length))
        self.password_input.setText(password)

    def generate_number(self):
        min_val = int(self.min_input.text())
        max_val = int(self.max_input.text())
        number = random.randint(min_val, max_val)
        self.number_input.setText(str(number))

    def copy_password(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.password_input.text())

    def copy_number(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.number_input.text())

    def validate_email(self):
        email = self.email_input.text()
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(regex, email):
            self.email_validation_result.setText("Valid Email")
            self.email_validation_result.setStyleSheet("color: green;")
        else:
            self.email_validation_result.setText("Invalid Email")
            self.email_validation_result.setStyleSheet("color: red;")

    def validate_url(self):
        url = self.url_input.text()
        regex = r'^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$'
        if re.match(regex, url):
            self.url_validation_result.setText("Valid URL")
            self.url_validation_result.setStyleSheet("color: green;")
        else:
            self.url_validation_result.setText("Invalid URL")
            self.url_validation_result.setStyleSheet("color: red;")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = PasswordGeneratorApp()
    mainWin.show()
    sys.exit(app.exec())
  
