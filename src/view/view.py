#!/usr/bin/env python3
# -*- coding: utf-8

from PyQt5.QtWidgets import ( QMainWindow )
from view.mainWindow.mainWindow import ( MainWindow )

class View(QMainWindow):
    def __init__(self):
        super(View, self).__init__()
        self.setWindowTitle(self.tr('Assessment-Task'))
        self.setMinimumSize(750,550)

        self.window = MainWindow()

        self.setCentralWidget(self.window)