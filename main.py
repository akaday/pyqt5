import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QLabel, QVBoxLayout, QWidget, QPushButton, QMessageBox, QInputDialog

class CalendarApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Family Calendar")
        self.setGeometry(100, 100, 800, 600)

        self.events = {}

        layout = QVBoxLayout()
        self.calendar = QCalendarWidget(self)
        self.calendar.clicked.connect(self.date_selected)

        self.label = QLabel("Select a date to add events.", self)

        self.add_button = QPushButton("Add Event", self)
        self.add_button.clicked.connect(self.add_event)

        layout.addWidget(self.calendar)
        layout.addWidget(self.label)
        layout.addWidget(self.add_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def date_selected(self, date):
        date_str = date.toString()
        self.label.setText(f"Selected Date: {date_str}")
        if date_str in self.events:
            self.label.setText(f"Selected Date: {date_str}\nEvents: {', '.join(self.events[date_str])}")
        else:
            self.label.setText(f"Selected Date: {date_str}\nNo events.")

    def add_event(self):
        date = self.calendar.selectedDate().toString()
