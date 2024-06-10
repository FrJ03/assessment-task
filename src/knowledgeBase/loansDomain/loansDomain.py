from knowledgeBase.commons.decision import Decision

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