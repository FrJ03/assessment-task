#!/usr/bin/env python3
# -*- coding: utf-8

from PyQt5.QtWidgets import ( QMainWindow )
from view.mainWindow.mainWindow import ( MainWindow )
from controller.controller import ( Controller )

class View(QMainWindow):
    def __init__(self):
        super(View, self).__init__()
        self.setWindowTitle(self.tr('Assessment-Task'))
        self.setMinimumSize(750,550)

        controller = Controller()

        self.window = MainWindow(controller.cases())

        self.setCentralWidget(self.window)