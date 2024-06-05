#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication)

from view.view import View

app = QApplication(sys.argv)
window = View()
window.show()

sys.exit(app.exec_())