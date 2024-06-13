#!/usr/bin/env python3
# -*- coding: utf-8

from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QComboBox,
    QLineEdit,
    QVBoxLayout,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import (
    QIntValidator,
    QDoubleValidator,
)

import re

class Cases(QWidget):
    def __init__(self, cases):
        super(Cases, self).__init__()

        self.label = QLabel('Inserte la información del caso', self)

        header = ['Característica', 'Valor']

        self.table = QTableWidget(len(cases), 2)

        self.table.setColumnWidth(0, 340)
        self.table.setColumnWidth(1, 340)

        self.table.setHorizontalHeaderLabels(header)

        for i in range(len(cases)): 
            attr = QTableWidgetItem(cases[i].name)
            attr.setFlags(attr.flags() & ~Qt.ItemFlag.ItemIsEditable)

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
    
    def getCases(self):
        cases = []
        for i in range (self.table.rowCount()):
            key = self.table.item(i, 0).text()
            valueCell = self.table.cellWidget(i, 1)
            value = ''
            if hasattr(valueCell, 'text'):
                value = valueCell.text()
            else:
                value = valueCell.currentText()

            cases.append((key, value))

        return cases