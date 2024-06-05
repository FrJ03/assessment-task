#!/usr/bin/env python3
# -*- coding: utf-8

from PyQt5.QtWidgets import ( QMainWindow )
from view.mainWindow.mainWindow import ( MainWindow )

class CaseTest:
    def __init__(self, name, type, allowedValues=None):
        self.name = name
        self.type = type
        self.allowedValues = allowedValues

cases = []
cases.append(CaseTest('selectable', 'selectable', ['yes', 'no']))
cases.append(CaseTest('int', 'natural'))
cases.append(CaseTest('float', 'real'))

class View(QMainWindow):
    cases = []
    cases.append(CaseTest('selectable', 'selectable', ['yes', 'no']))
    cases.append(CaseTest('int', 'natural'))
    cases.append(CaseTest('float', 'real'))

    def __init__(self):
        super(View, self).__init__()
        self.setWindowTitle(self.tr('Assessment-Task'))
        self.setMinimumSize(750,550)

        self.window = MainWindow(cases)

        self.setCentralWidget(self.window)