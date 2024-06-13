#!/usr/bin/env python3
# -*- coding: utf-8

from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QDialog
)
from view.footer.footer import ( Footer )
from view.cases.cases import ( Cases )
from view.textBlock.textBlock import ( TextBlock )
from view.errorBox.errorBox import ( ErrorBox )

class MainWindow(QWidget):
    def __init__(self, cases, evaluarEvent):
        super(MainWindow, self).__init__()
        
        layout = QVBoxLayout()
        
        self.cases = Cases(cases)
        self.decision = TextBlock('Decisión')
        self.reasoner = TextBlock('Razonamiento')
        self.footer = Footer(self.evaluarHandler)
        self.evaluarEvent = evaluarEvent

        layout.addWidget(self.cases)
        layout.addWidget(self.decision)
        layout.addWidget(self.reasoner)
        layout.addWidget(self.footer)

        self.setLayout(layout)

    def evaluarHandler(self):
        cases = self.cases.getCases()

        allIntroduced = True

        for i in range(len(cases)):
            if(cases[i][1] == ''):
                allIntroduced = False
                break

        if allIntroduced:
            self.decision.clearContent()
            self.reasoner.clearContent()

            decision, explanation = self.evaluarEvent(cases)

            self.decision.setContent(decision)
            self.reasoner.setContent(explanation)
        else:
            error = ErrorBox('Please insert all data')
            error.exec()