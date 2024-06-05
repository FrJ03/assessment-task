#!/usr/bin/env python3
# -*- coding: utf-8

from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout
)
from view.footer.footer import ( Footer )
from view.cases.cases import ( Cases )

class MainWindow(QWidget):
    def __init__(self, cases):
        super(MainWindow, self).__init__()
        
        layout = QVBoxLayout()
        
        self.cases = Cases(cases)
        self.footer = Footer()

        layout.addWidget(self.cases)
        layout.addStretch(1)
        layout.addWidget(self.footer)

        self.setLayout(layout)