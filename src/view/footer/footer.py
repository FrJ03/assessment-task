#!/usr/bin/env python3
# -*- coding: utf-8

from PyQt5.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QPushButton
)
import sys

class Footer(QWidget):
    def __init__(self, evaluarHandler):
        super(Footer, self).__init__()

        layout = QHBoxLayout()

        self.exitButton = QPushButton('Exit', self)
        self.exitButton.clicked.connect(sys.exit)
        self.evalButton = QPushButton('Evaluar', self)
        self.evalButton.clicked.connect(evaluarHandler)
        
        layout.addStretch(1)
        layout.addWidget(self.evalButton)
        layout.addWidget(self.exitButton)
        layout.addStretch(1)

        self.setLayout(layout)