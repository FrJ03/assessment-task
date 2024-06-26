#!/usr/bin/env python3
# -*- coding: utf-8

'''
Class that represents the decision and its details
'''
class Decision():
    def __init__(self, decision: bool = False, details=[]):
        """Decision class construtor

        Args:
            decision (bool, optional): Value that represents the decision. Defaults to False.
            details (Array<(key, value)>, optional): Attributes for the decision. Defaults to [].
        """
        self._decision = decision
        self._decisionMade = False
        self._details = details
    def getDecision(self):
        """Returns the status of the decision

        Returns:
            bool: decision status
        """
        return self._decision
    def setDecision(self, decision: bool):
        """Set a new value to the desicion

        Args:
            decision (bool): new value
        """
        self._decision = decision
    def getDecisionMade(self):
        """Returns if the decision has been made

        Returns:
            bool: true if the decision has been made, false otherwise
        """
        return self._decisionMade
    def setDecisionMade(self, decision: bool):
        """Set if a decision has been made

        Args:
            decision (bool): true if the decision has been made, false otherwise
        """
        self._decisionMade = decision
    def toString(self):
        """Resume the decision info into an string

        Returns:
            str: decision info
        """
        pass
    def addDetail(self, key: str, value):
        """Add a new detail to a decision, or update it if exists

        Args:
            key (str): detail name
            value (any): detail value
        """

        for i in range(len(self._details)):
            if(self._details[i][0] == key):
                self._details[i] = (self._details[i][0], value)
                return

        self._details.append((key, value))
    
    def getDetail(self, key: str):
        """Get the detail value

        Args:
            key (str): detail name
        """
        for k, v in self._details:
            if(k == key):
                return v