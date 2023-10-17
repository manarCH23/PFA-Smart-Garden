import sys
import requests
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from interface import Ui_MainWindow


class RegistrationPage(QDialog):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #F7A400;")
        self.setWindowTitle('Registration')
        self.resize(300, 200)
        # Create widgets
        name_label = QLabel('Name:')
        name_label.setFont(QtGui.QFont('Arial'))  # Set font
        name_label.setStyleSheet('color: #333')  # Set color using CSS
        font = QtGui.QFont()
        font.setBold(True)
        name_label.setFont(font)
        self.password_edit = QLineEdit()

        self.password_edit.setStyleSheet(
    "border: 2px solid #3A9Efd;\
     border-radius: 10px;\
     padding: 5px;\
     background-color: #FFFFFF;"
)
        self.name_edit = QLineEdit()
        self.name_edit.setStyleSheet(
    "border: 2px solid #3A9Efd;\
     border-radius: 10px;\
     padding: 5px;\
     background-color: #FFFFFF;"
     
)
        email_label = QLabel('Email:')
        email_label.setFont(QtGui.QFont('Arial'))  # Set font
        email_label.setStyleSheet('color: #333')  # Set color using CSS
        font = QtGui.QFont()
        font.setBold(True)
        email_label.setFont(font)
        self.password_edit = QLineEdit()

        self.password_edit.setStyleSheet(
    "border: 2px solid #3A9Efd;\
     border-radius: 10px;\
     padding: 5px;\
     background-color: #FFFFFF;"
)
        self.email_edit = QLineEdit()
        self.email_edit.setStyleSheet(
    "border: 2px solid #3A9Efd;\
     border-radius: 10px;\
     padding: 5px;\
     background-color: #FFFFFF;"
     
)
        password_label = QLabel('Password:')
        password_label.setFont(QtGui.QFont('Arial'))  # Set font
        password_label.setStyleSheet('color: #333')  # Set color using CSS
        font = QtGui.QFont()
        font.setBold(True)
        password_label.setFont(font)
        self.password_edit = QLineEdit()

        self.password_edit.setStyleSheet(
    "border: 2px solid #3A9Efd;\
     border-radius: 10px;\
     padding: 5px;\
     background-color: #FFFFFF;"
)
        self.password_edit = QLineEdit()
        self.password_edit.setStyleSheet(
    "border: 2px solid #3A9Efd;\
     border-radius: 10px;\
     padding: 5px;\
     background-color: #FFFFFF;"
     
)
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        confirm_password_label = QLabel('Confirm Password:')
        confirm_password_label.setFont(QtGui.QFont('Arial'))  # Set font
        confirm_password_label.setStyleSheet('color: #333')  # Set color using CSS
        font = QtGui.QFont()
        font.setBold(True)
        confirm_password_label.setFont(font)
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)

        self.password_edit.setStyleSheet(
    "border: 2px solid #3A9Efd;\
     border-radius: 10px;\
     padding: 5px;\
     background-color: #FFFFFF;"
)
        self.confirm_password_edit = QLineEdit()
        self.confirm_password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_password_edit.setStyleSheet(
    "border: 2px solid #3A9Efd;\
     border-radius: 10px;\
     padding: 5px;\
     background-color: #FFFFFF;"
     
)
        self.confirm_password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        register_button = QPushButton('Register')
        register_button.setStyleSheet(
    "background-color: #3A9Efd; /* Green */ \
                                border: none;\
                                color: white;\
                                padding: 5px 10px;\
                                font-size: 16px;"
)
        login_button = QPushButton('Login')
        login_button.setStyleSheet(
    "background-color: #3A9Efd; /* Green */ \
                                border: none;\
                                color: white;\
                                padding: 5px 10px;\
                                font-size: 16px;\
                                margin: 4px 2px;"
)
        

        # Layout widgets
        layout = QVBoxLayout()
        layout.addWidget(name_label)
        layout.addWidget(self.name_edit)
        layout.addWidget(email_label)
        layout.addWidget(self.email_edit)
        layout.addWidget(password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(confirm_password_label)
        layout.addWidget(self.confirm_password_edit)
        layout.addWidget(register_button)
        layout.addWidget(login_button)
        self.setLayout(layout)

        # Connect signals to slots
        register_button.clicked.connect(self.register)
        login_button.clicked.connect(self.go_to_login_page)

    def register(self):
        # Check if the name, email, password, and confirm password fields are not empty
        # Check if the password and confirm password fields match
        # Display a message if the registration is successful or not
        username = self.name_edit.text()
        email = self.email_edit.text()
        password = self.password_edit.text()
        confirm_password = self.confirm_password_edit.text()

        if not all([username, email, password, confirm_password]):
            QMessageBox.warning(self, 'Error', 'All fields are required!')
        elif password != confirm_password:
            QMessageBox.warning(self, 'Error', 'Passwords do not match!')
        else:
            url = 'http://127.0.0.1:8000/register/'
            data = {'username': username, 'email': email, 'password': password}
            response = requests.post(url, data=data)
            if response.status_code == 201:
                self.go_to_interface()
            else:
                QMessageBox.warning(self, 'Error', 'Registration failed!')

    def go_to_login_page(self):
        self.close()
        login_page = LoginPage()
        login_page.exec()
    def go_to_interface(self):
        self.close()
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

class LoginPage(QDialog):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #F7A400;")
        self.setWindowTitle('Login')
        self.resize(300, 150)
        # Create widgets
        
        Username_label = QLabel('Username')
        Username_label = QLabel('Username')
        Username_label.setFont(QtGui.QFont('Arial'))  # Set font
        Username_label.setStyleSheet('color: #333')  # Set color using CSS
        font = QtGui.QFont()
        font.setBold(True)
        Username_label.setFont(font)


        self.Username_edit = QLineEdit()
        self.Username_edit = QLineEdit()
        self.Username_edit.setStyleSheet(
    "border: 2px solid #3A9Efd;\
     border-radius: 10px;\
     padding: 5px;\
     background-color: #FFFFFF;"
     
)

        password_label = QLabel('Password:')
        password_label.setFont(QtGui.QFont('Arial'))  # Set font
        password_label.setStyleSheet('color: #333')  # Set color using CSS
        font = QtGui.QFont()
        font.setBold(True)
        password_label.setFont(font)
        self.password_edit = QLineEdit()
        self.password_edit.setStyleSheet(
    "border: 2px solid #3A9Efd;\
     border-radius: 10px;\
     padding: 5px;\
     background-color: #FFFFFF;"
)
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        login_button = QPushButton('Login')
        registration_button = QPushButton('Registration')
        login_button.setStyleSheet(
    "background-color: #3A9Efd; /* Green */ \
                                border: none;\
                                color: white;\
                                padding: 5px 10px;\
                                text-align: center;\
                                text-decoration: none;\
                                display: inline-block;\
                                font-size: 16px;\
                                margin: 4px 2px;\
                                cursor: pointer;"
)
        registration_button.setStyleSheet(
    "background-color: #3A9Efd; /* Green */ \
                                border: none;\
                                color: white;\
                                padding: 5px 10px;\
                                text-align: center;\
                                font-size: 16px;\
                                margin: 4px 2px;"
)
        # Layout widgets
        layout = QVBoxLayout()
        layout.addWidget(Username_label)
        layout.addWidget(self.Username_edit )

        layout.addWidget(password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(login_button)
        layout.addWidget(registration_button)
        self.setLayout(layout)

        # Connect signals to slots
        login_button.clicked.connect(self.login)
        registration_button.clicked.connect(self.go_to_registration_page)

    def login(self):
        # Send a POST request to the REST API with the email and password
        username = self.Username_edit.text()
        password = self.password_edit.text()
        response = requests.post('http://127.0.0.1:8000/login/', json={'username': username, 'password': password})

        # Check if the login was successful and store the auth token
        if response.status_code == 200:
            self.auth_token = response.json()['token']
            self.go_to_interface()
        else:
            QMessageBox.warning(self, 'Error', 'Login failed!')

    def go_to_interface(self):
        self.close()
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def go_to_registration_page(self):
        self.close()
        registration_page = RegistrationPage()
        registration_page.exec()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_page = LoginPage()
    login_page.show()
    sys.exit(app.exec())
