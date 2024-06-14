#!/usr/bin/env python3
# -*- coding: utf-8

from knowledgeBase.commons.decision import Decision
from model import model

class Controller():
    def __init__(self):
        return
    
    def cases(self):
        return model.getCases()
    
    def eventEvaluar(self, caseData):
        """event that evaluates the case

        Args:
            caseData (Array<pair>): Case information

        Returns:
            str: decision
            str: explanation
        """
        especificar = model.Especificar(caseData)
        criterias = especificar.execute()
        seleccionar = model.Seleccionar(criterias)
        decision: Decision = None
        explanations = ''
        results = model.inicializateResultValue(caseData)
        i = 0

        for i in range(len(criterias)):
            criteria= seleccionar.execute()
            evaluar = model.Evaluar(caseData, criteria, results)
            valor, explanation = evaluar.execute()

            for i in range(len(valor)):
                results.setValue(valor[i][0], valor[i][1])

            explanations += f'{explanation}\n'

            equiparar = model.Equiparar(results)
            decision = equiparar.execute()

            if(decision.getDecisionMade() == True):
                break

        if(decision.getDecisionMade() == False):
            decision.setDecision(True)
            decision.setDecisionMade(True)
        
        return decision.toString(), explanations
