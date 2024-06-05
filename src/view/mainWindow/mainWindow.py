#!/usr/bin/env python3
# -*- coding: utf-8

from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout
)
from view.footer.footer import ( Footer )

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        layout = QVBoxLayout()
        
        self.footer = Footer()

        layout.addStretch(1)
        layout.addWidget(self.footer)

        self.setLayout(layout)