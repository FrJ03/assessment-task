#!/usr/bin/env python3
# -*- coding: utf-8

from knowledgeBase.commons.decision import Decision

class CaseTest:
    def __init__(self, name, type, allowedValues=None):
        self.name = name
        self.type = type
        self.allowedValues = allowedValues

cases = []
cases.append(CaseTest('selectable', 'selectable', ['yes', 'no']))
cases.append(CaseTest('int', 'natural'))
cases.append(CaseTest('float', 'real'))

class Controller():
    def __init__(self):
        return
    
    def cases(self):
        return cases
    
    def eventEvaluar(self, caseData):
        """event that evaluates the case

        Args:
            caseData (Array<pair>): Case information

        Returns:
            str: decision
            str: explanation
        """
        criterios = [] #obtener criterios del caso (caso)
        decision: Decision = Decision()#decision vacía
        explanations = ''
        i = 0

        while(decision.getDecisionMade() == False and len(criterios) < i):
            criterio= ''#seleccionar criterio(criterios, i)
            valor, explanation = 0 #evaluar criterio (caso, criterio)
            explanations += f'{explanation}\n'
            decision = Decision()#equiparar (valor)
            i += 1
        
        #If the case has pass the loop without a decision made, the decision is true
        if(decision.getDecisionMade() == False):
            decision.setDecision(True)
            decision.setDecisionMade(True)
        
        return decision.toString(), explanations
