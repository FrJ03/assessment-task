from knowledgeBase.commons.decision import Decision
from knowledgeBase.commons.case import Case

class Age(Case):
    def __init__(self):
        super(Age, self).__init__('edad', 'natural')

class Amount(Case):
    def __init__(self):
        super(Amount, self).__init__('cuantía del cliente', 'real')

class AnnualIncomes(Case):
    def __init__(self):
        super(AnnualIncomes, self).__init__('ingresos anuales', 'real')

class Defaults(Case):
    def __init__(self):
        super(Defaults, self).__init__('número de impagos', 'natural')

class Debt(Case):
    def __init__(self):
        super(Debt, self).__init__('deuda', 'real')

class EmploymentStatus(Case):
    def __init__(self):
        super(EmploymentStatus, self).__init__('situación laboral', 'selectable', ['desempleado', 'temporal', 'indefinido', 'fijo', 'autónomo/empresario'])

class LoanAmount(Case):
    def __init__(self):
        super(LoanAmount, self).__init__('cuantía del préstamo', 'real')

class LoanDuration(Case):
    def __init__(self):
        super(LoanDuration, self).__init__('duración del préstamo', 'natural')


def getCases():
    cases=[]
    cases.append(Age())
    cases.append(Amount())
    cases.append(AnnualIncomes())
    cases.append(EmploymentStatus())
    cases.append(Defaults())
    cases.append(Debt())
    cases.append(LoanAmount())
    cases.append(LoanDuration())
    return cases


"""Decision class for loans domain
"""
class LoanDecision(Decision):
    """Decision class construtor

    Args:
        decision (bool, optional): Value that represents the decision. Defaults to False.
    """
    def __init__(self, decision: bool = False):
        super(self, LoanDecision).__init__(decision)
    """Overwrites toString method from Decision class
    """
    def toString(self):
        if(self._decision):
            message = 'Decisión: Concedido\n\n'
            for key, value in self._details:
                message += f'\t{key}: {value}\n'
        else:
            return 'Decisión: Denegado'