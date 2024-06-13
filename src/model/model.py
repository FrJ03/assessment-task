"""
Name: Model Class for the project
Description: This class is responsible for the model of the project
"""

# Libraries
from knowledgeBase.commons.decision import Decision
from knowledgeBase.commons.case import Case
from knowledgeBase.commons.criteria import Criteria

#Select domain
from knowledgeBase.loansDomain import loansDomain as dominio


class Inferencia():
    def __init__(self):
        pass
    def execute(self):
        pass

"""
Especificar inferencia
"""
class Especificar(Inferencia):
    def __init__(self, LHipotesis):
        self.LHipotesis = LHipotesis
    def execute(self):
        LHipotesis = self.LHipotesis
        if len(LHipotesis)> 0:
            return LHipotesis[0]
        

"""
Seleccionar inferencia
"""
class Seleccionar(Inferencia):
    def __init__(self, criterias):
        self.criterias = criterias
        self.contador = 0
    def execute(self):
        criterio = self.criterias[self.contador]
        self.contador += 1
        return criterio
        

"""
Evaluar inferencia
"""
class Evaluar(Inferencia):
    def __init__(self, caso, criterio):
        self.caso = caso
        self.criterio = criterio
    def execute(self):
        caso = self.caso
        criterio = self.criterio
        valor = 0
        explicacion = ''
        return valor, explicacion
        

"""
Equiparar inferencia
"""
class Equiparar(Inferencia, Decision):
    def __init__(self, valor):
        self.valor = valor
    def execute(self):
        valor = self.valor
        self.setDecision(valor)
        self.setDecisionMade(True)
     

"""
Function that return the cases of the domain
"""
def getCases():
    cases = []
    cases.append(dominio.LoanAmount())
    cases.append(dominio.LoanTerm())
    cases.append(dominio.LoanInterestRate())
    cases.append(dominio.LoanType())
    return cases


"""
Function that return the criteria of the domain
"""
def getCriteria():
    criteria = dominio.getCriterias()
    return criteria