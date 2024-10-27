import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QLabel, QVBoxLayout, QWidget, QPushButton, QMessageBox

class CalendarApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Family Calendar")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()
        self.calendar = QCalendarWidget(self)
        self.calendar.clicked.connect(self.date_selected)

        self.label = QLabel("Select a date to add events.", self)

        self.button = QPushButton("Click Me", self)
        self.button.move(250, 200)
        self.button.clicked.connect(self.show_message)

        layout.addWidget(self.calendar)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def date_selected(self, date):
        self.label.setText(f"Selected Date: {date.toString()}")

    def show_message(self):
        QMessageBox.information(self, "Message", "Button Clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalendarApp()
    window.show()
    sys.exit(app.exec_())
