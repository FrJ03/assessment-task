from PyQt5.QtWidgets import (
    QWidget,
    QTextEdit,
    QVBoxLayout,
    QLabel
)

class TextBlock(QWidget):
    def __init__(self, header):
        super(TextBlock, self).__init__()

        self.label = QLabel(header)

        self.content = QTextEdit()
        self.content.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.content)

        self.setLayout(layout)
    
    def setContent(self, content):
        self.content.setText(content)