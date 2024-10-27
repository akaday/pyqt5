import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt Application")
        self.setGeometry(100, 100, 600, 400)

        self.label = QLabel("Hello, PyQt!", self)
        self.label.move(250, 150)

        self.button = QPushButton("Click Me", self)
        self.button.move(250, 200)
        self.button.clicked.connect(self.show_message)

    def show_message(self):
        QMessageBox.information(self, "Message", "Button Clicked!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()

sys.exit(app.exec_())
