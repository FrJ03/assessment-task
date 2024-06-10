#!/usr/bin/env python3
# -*- coding: utf-8

class Decision():
    def __init__(self, decision: bool = False):
        self._decision = decision
    def get(self):
        return self._decision
    def set(self, decision: bool):
        self._decision = decision
    def toString(self):
        pass