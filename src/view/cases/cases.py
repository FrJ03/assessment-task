#!/usr/bin/env python3
# -*- coding: utf-8

from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QComboBox,
    QLineEdit,
    QVBoxLayout
)
from PyQt5.QtGui import (
    QIntValidator,
    QDoubleValidator
)

class Cases(QWidget):
    def __init__(self, cases):
        super(Cases, self).__init__()

        self.label = QLabel('Inserte la información del caso', self)

        header = ['Característica', 'Valor']

        self.table = QTableWidget(len(cases), 2)

        self.table.setColumnWidth(0, 349)
        self.table.setColumnWidth(1, 349)

        self.table.setHorizontalHeaderLabels(header)

        for i in range(len(cases)): 
            attr = QTableWidgetItem(cases[i].name)

            if cases[i].type == 'selectable':
                combobox = QComboBox()
                for j in cases[i].allowedValues:
                    combobox.addItem(j)
                self.table.setCellWidget(i, 1, combobox)
            elif cases[i].type == 'natural':
                input = QLineEdit()
                input.setValidator(QIntValidator())
                self.table.setCellWidget(i, 1, input)
            elif cases[i].type == 'real':
                input = QLineEdit()
                input.setValidator(QDoubleValidator())
                self.table.setCellWidget(i, 1, input)
            else:
                input = QLineEdit()
                self.table.setCellWidget(i, 1, input)
            self.table.setItem(i, 0, attr)
        
        layout = QVBoxLayout()

        layout.addWidget(self.label)
        layout.addWidget(self.table)

        self.setLayout(layout)