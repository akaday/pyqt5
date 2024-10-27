import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt Application")
        self.setGeometry(100, 100, 600, 400)

        label = QLabel("Hello, PyQt!", self)
        label.move(250, 200)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

sys.exit(app.exec_())
