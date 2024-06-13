"""
Name: Model Class for the project
Description: This class is responsible for the model of the project
"""

# Libraries
from knowledgeBase.commons.decision import Decision
from knowledgeBase.commons.case import Case
from knowledgeBase.commons.criteria import Criteria
from knowledgeBase.commons.resultValue import ResultValue
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
#se la pasa como parametro value
class Evaluar(Inferencia):
    def __init__(self, caso, criterio, value=None):
        self.caso = caso
        self.criterio = criterio
        self.value = value
    def execute(self):
        #llamar a funcion eval de criteria (caso, value)
        caso = self.caso
        criterio = self.criterio
        value = self.value
        valor, mensaje = criterio.eval(caso, value)
        return valor, mensaje


"""
Equiparar inferencia
"""
#recibe el conjunto de valores de valor y en base a eso devuelve una decision
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
#terminar getcases
def getCases():
    cases = dominio.getCases()
    return cases


"""
Function that return the criteria of the domain
"""
def getCriteria():
    criteria = dominio.getCriterias()
    return criteria


#Funcion que devuielva el resultValue del dominio seleccionado
def inicializateResultValue(caso):
    RV = dominio.setInitialResultValue(caso)
    return RV
