import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QFormLayout,
    QLineEdit, QPushButton, QLabel, QFileDialog, QMessageBox
)
from PyQt6.QtCore import QProcess


class ModelLauncherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("OpenModelica Executable Launcher")
        self.setGeometry(200, 200, 400, 200)

        # Layouts
        self.layout = QVBoxLayout()
        self.form_layout = QFormLayout()

        # Input fields
        self.exe_path_input = QLineEdit()
        self.exe_path_input.setPlaceholderText("Select executable file")
        self.start_time_input = QLineEdit()
        self.start_time_input.setPlaceholderText("Enter start time (Integer)")
        self.stop_time_input = QLineEdit()
        self.stop_time_input.setPlaceholderText("Enter stop time (Integer)")

        # Button to browse for executable
        self.browse_button = QPushButton("Browse")
        self.browse_button.clicked.connect(self.browse_executable)

        # Submit button
        self.run_button = QPushButton("Run")
        self.run_button.clicked.connect(self.run_executable)

        # Form layout
        self.form_layout.addRow("Executable:", self.exe_path_input)
        self.form_layout.addRow("", self.browse_button)
        self.form_layout.addRow("Start Time:", self.start_time_input)
        self.form_layout.addRow("Stop Time:", self.stop_time_input)

        # Adding layouts
        self.layout.addLayout(self.form_layout)
        self.layout.addWidget(self.run_button)
        self.setLayout(self.layout)

    def browse_executable(self):
        exe_file, _ = QFileDialog.getOpenFileName(self, "Select Executable", "", "Executable Files (*.exe)")
        if exe_file:
            self.exe_path_input.setText(exe_file)

    def validate_inputs(self):
        # Validate start and stop times
        try:
            start_time = int(self.start_time_input.text())
            stop_time = int(self.stop_time_input.text())
        except ValueError:
            QMessageBox.critical(self, "Error", "Start and Stop times must be integers.")
            return False, None, None

        if not (0 <= start_time < stop_time < 5):
            QMessageBox.critical(self, "Error", "Ensure: 0 <= Start Time < Stop Time < 5")
            return False, None, None

        exe_path = self.exe_path_input.text()
        if not exe_path:
            QMessageBox.critical(self, "Error", "Please select an executable file.")
            return False, None, None

        return True, exe_path, (start_time, stop_time)

    def run_executable(self):
        is_valid, exe_path, times = self.validate_inputs()
        if not is_valid:
            return

        start_time, stop_time = times
        process = QProcess(self)
        process.setProgram(exe_path)
        process.setArguments([str(start_time), str(stop_time)])
        process.start()

        if process.waitForStarted():
            QMessageBox.information(self, "Success", "Executable started successfully!")
        else:
            QMessageBox.critical(self, "Error", "Failed to start the executable.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModelLauncherApp()
    window.show()
    sys.exit(app.exec())