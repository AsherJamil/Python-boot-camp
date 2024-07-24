import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QLabel
from PyQt6.QtCore import QTimer, Qt


class DangerousWritingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dangerous Writing App")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)  # type: ignore

        self.timer_label = QLabel("Time remaining: 5")
        self.layout.addWidget(self.timer_label)

        self.text_edit = QTextEdit()
        self.layout.addWidget(self.text_edit)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.reset_timer()

        self.text_edit.textChanged.connect(self.reset_timer)

    def reset_timer(self):
        self.timer.stop()
        self.timer.start(1000)  # Timer ticks every 1000 ms (1 second)
        self.countdown = 5
        self.timer_label.setText(f"Time remaining: {self.countdown}")

    def update_timer(self):
        self.countdown -= 1
        self.timer_label.setText(f"Time remaining: {self.countdown}")

        if self.countdown <= 0:
            self.text_edit.clear()
            self.reset_timer()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DangerousWritingApp()
    window.show()
    sys.exit(app.exec())
