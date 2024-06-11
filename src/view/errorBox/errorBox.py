from PyQt5.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QLabel,
    QVBoxLayout
)

class ErrorBox(QDialog):
    def __init__(self, message):
        super().__init__()

        self.setWindowTitle("ERROR!")

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(self.accept)

        self.layout = QVBoxLayout()
        label = QLabel(message)
        self.layout.addWidget(label)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)