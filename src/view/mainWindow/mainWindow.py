#!/usr/bin/env python3
# -*- coding: utf-8

from PyQt5.QtWidgets import (
                                QWidget,
                                QVBoxLayout
                            )

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.layout = QVBoxLayout()

        self.setLayout(self.layout)