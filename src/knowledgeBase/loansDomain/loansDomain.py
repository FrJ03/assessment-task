from knowledgeBase.commons.decision import Decision
from knowledgeBase.commons.case import Case
from knowledgeBase.commons.criteria import Criteria
from knowledgeBase.commons.resultValue import ResultValue

"""Client age
"""
class Age(Case):
    def __init__(self):
        super(Age, self).__init__('edad del cliente', 'natural')

"""Amount of money that the client has in the bank
"""
class Amount(Case):
    def __init__(self):
        super(Amount, self).__init__('cuantía del cliente', 'real')

"""Annual incomes of the client
"""
class AnnualIncomes(Case):
    def __init__(self):
        super(AnnualIncomes, self).__init__('ingresos anuales', 'real')

"""Number of times that the client have not paid their debts
"""
class Defaults(Case):
    def __init__(self):
        super(Defaults, self).__init__('número de impagos', 'natural')

"""Current debt of the client
"""
class Debt(Case):
    def __init__(self):
        super(Debt, self).__init__('deuda', 'real')

"""Employment situation of the client
"""
class EmploymentStatus(Case):
    def __init__(self):
        super(EmploymentStatus, self).__init__('situación laboral', 'selectable', ['desempleado', 'temporal', 'indefinido', 'fijo', 'autónomo/empresario'])

"""Amount of money requested
"""
class LoanAmount(Case):
    def __init__(self):
        super(LoanAmount, self).__init__('cuantía del préstamo', 'real')

"""Loan duration in years
"""
class LoanDuration(Case):
    def __init__(self):
        super(LoanDuration, self).__init__('duración del préstamo', 'natural')

def getCases():
    """Function that returns the cases for the loan domain

        Returns:
            Array<Case>: List of cases
        """
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

"""Criteria for age of the client when the loan have been paid
"""
class EndLoanCriteria(Criteria):
    def __init__(self):
        """Constructor
        """
        super(EndLoanCriteria, self).__init__('edad de finalizanción del préstamo')

    def eval(self, case, value):
        """Redefinition of eval method

        Args:
            case (Array<(key,value)>): Case information
            value (LoanResultValue): Current evaluation data

        Returns:
            Array<(key, values>: Result values
            str: evaluation message
        """
        super(EndLoanCriteria, self).eval(case, value)

        clientAge = -1
        loanDuration = -1
        message = f'evaluando {self.name}\n\t'

        values = []


        for i in range(len(case)):
            if(case[i][0] == 'edad del cliente'):
                clientAge = int(case[i][1])
            elif(case[i][0] == 'duración del préstamo'):
                loanDuration = int(case[i][1])
        
        if(clientAge < 0 or loanDuration < 0):
            values.append(('decisión', False))
            values.append(('decidido', True))
            message = f'{message}No se ha especificado la edad del cliente o la duración del préstamo\n'
        elif (clientAge + loanDuration > 80):
            values.append(('decisión', False))
            values.append(('decidido', True))
            message = f'{message}Denegado debido a que la edad de finalización del préstamo es mayor a 80 años\n'
        else:
            values.append(('decisión', True))
            message = f'{message}Edad de finalización del préstamo válida\n'
        
        return values, message

"""Criteria for employment status
"""
class EmploymentStatusCriteria(Criteria):
    def __init__(self):
        """Constructor
        """
        super(EmploymentStatusCriteria, self).__init__('situación laboral del cliente')
    
    def eval(self, case, value):
        """Redefinition of eval method

        Args:
            case (Array<(key,value)>): Case information
            value (LoanResultValue): Current evaluation data

        Returns:
            Array<(key, values>: Result values
            str: evaluation message
        """
        super(EmploymentStatusCriteria, self).eval(case, value)

        employmentStatus = ''
        message = f'evaluando {self.name}\n\t'

        values = []

        for i in range(len(case)):
            if(case[i][0] == 'situación laboral'):
                employmentStatus = case[i][1]
        
        if(employmentStatus == ''):
            values.append(('decisión', False))
            values.append(('decidido', True))
            message = f'{message}No se ha especificado la situación laboral del cliente\n'
        elif (employmentStatus == 'desempleado'):
            values.append(('decisión', False))
            values.append(('decidido', True))
            message = f'{message}Denegado debido a que el cliente se encuentra en situación de desempleo\n'
        elif(employmentStatus == 'fijo'):
            values.append(('decisión', True))
            values.append(('interés', 0.02))
            message = f'{message}Situación laboral válida\n'
        elif(employmentStatus == 'indefinido' or employmentStatus == 'autónomo/empresario'):
            values.append(('decisión', True))
            values.append(('interés', 0.025))
            message = f'{message}Situación laboral válida\n'
        elif(employmentStatus == 'temporal'):
            values.append(('decisión', True))
            values.append(('interés', 0.035))
            message = f'{message}Situación laboral válida\n'
        else:
            values.append(('decisión', False))
            values.append(('decidido', True))
            message = f'{message}Situación laboral incorrecta\n'
     
        return values, message

"""Criteria for the number of times that the client has not paid his debts
"""
class DefaultsCriteria(Criteria):
    def __init__(self):
        """Constructor
        """
        super(DefaultsCriteria, self).__init__('número de impagos')
    
    def eval(self, case, value):
        """Redefinition of eval method

        Args:
            case (Array<(key,value)>): Case information
            value (LoanResultValue): Current evaluation data

        Returns:
            Array<(key, values>: Result values
            str: evaluation message
        """
        super(DefaultsCriteria, self).eval(case, value)

        defaults = -1
        message = f'evaluando {self.name}\n\t'

        values = []

        for i in range(len(case)):
            if(case[i][0] == 'número de impagos'):
                defaults = int(case[i][1])
        
        if(defaults == -1):
            values.append(('decisión', False))
            values.append(('decidido', True))
            message = f'{message}No se ha especificado el número de impagos\n'
        else:
            values.append(('decisión', True))
            values.append(('interés', defaults * 0.003))
            message = f'{message}Número de impagos evaluado\n'

        return values, message

"""Criteria for the amount of money the client could request
"""
class AmountCriteria(Criteria):
    def __init__(self):
        """Constructor
        """
        super(AmountCriteria, self).__init__('cuantía solicitada')
    
    def eval(self, case, value):
        """Redefinition of eval method

        Args:
            case (Array<(key,value)>): Case information
            eval (LoanResultValue): Current evaluation data

        Returns:
            Array<(key, values>: Result values
            str: evaluation message
        """
        super(AmountCriteria, self).eval(case, value)

        message = f'evaluando {self.name}\n\t'

        duration = -1
        debts = -1
        annualIncomes = -1
        amount = -1
        interest = value.getValue('interés')

        values = []

        for i in range(len(case)):
            if(case[i][0] == 'ingresos anuales'):
                annualIncomes = float(case[i][1])
            elif(case[i][0] == 'deuda'):
                debts = float(case[i][1])
            elif(case[i][0] == 'duración del préstamo'):
                duration = int(case[i][1])
            elif(case[i][0] == 'cuantía del préstamo'):
                amount = float(case[i][1])

            if(debts != -1 and annualIncomes != -1 and duration != -1 and amount != -1):
                break

        monthyPayment = (amount + (amount * ((interest) + 1) ** duration)) / 12 * duration
        
        if(debts == -1 or annualIncomes == -1):
            values.append(('decisión', False))
            values.append(('decidido', True))
            message = f'{message}No se ha especificado el salario anual o la deuda actual\n'
        elif (monthyPayment * 12 * duration > 0.5 * ((annualIncomes * duration) - debts)):
            values.append(('decisión', False))
            values.append(('decidido', True))

            message = f'{message}Se ha solicitado demasiado dinero para sus posibilidades\n'
        else:
            values.append(('decisión', True))

            message = f'{message}El préstamo entra dentro de sus posibilidades\n'

        return values, message
    
def getCriterias():
    """Function that returns all criterias
    
    Returns:
        Array<Criterias>: All criterias
    """
    criterias = []
    criterias.append(EndLoanCriteria())
    criterias.append(EmploymentStatusCriteria())
    criterias.append(DefaultsCriteria())
    criterias.append(AmountCriteria())

    return criterias


class LoanResultValue(ResultValue):
    def __init__(self, values=[0, 0, 0, 0]):
        """Constructor

        Args:
            values (Array<any>, optional): initial values of the attributes. The order is: cantidad -> duración -> interés -> cuantía mensual. Defaults to [0, 0, 0, 0]
        """
        attributes = [('cantidad', values[0]), ('duración', values[1]), ('interés', values[2]), ('cuantía mensual', values[3]), ('decisión', True), ('decidido', False)]

        super(LoanResultValue, self).__init__(attributes)
    
    def setValue(self, key, value):
        """Add or set the value. It depends of the key

        Args:
            key (str): Attribute key. Could be 'cantidad', 'duración', 'interés', 'decisión' or 'decidido'. The 'cuantía mensual' attribute can not be seted
            value (any): Value to add or set
        """
        super().setValue(key, value)

        if key == 'cantidad':
            self._attributes[0] = (self._attributes[0][0], value)
        elif key == 'duración':
            self._attributes[1] = (self._attributes[1][0], value)
        elif key == 'interés':
            self._attributes[2] = (self._attributes[1][0], self._attributes[1][1] + value)
        elif key == 'decisión':
            self._attributes[4] = (self._attributes[4][0], value)
        elif key == 'decidido':
            self._attributes[5] = (self._attributes[5][0], value)
        else:
            return
        
        self.recalcMonthyPayment()
        
    def recalcMonthyPayment(self):
        interest = self._attributes[2][1]
        amount = self._attributes[0][1]
        duration = self._attributes[1][1]

        monthlyPayment = (amount + (amount * ((interest) + 1) ** duration)) / 12 * duration
        
        self._attributes[3] = (self._attributes[3][0], monthlyPayment)

def setInitialResultValue(case):
    """Initialize a LoanResultValue

    Args:
        case (Array<(key, values)>): Case info
    
    Return:
        LoanResultValue: result value initizalized
    """
    duration = -1
    amount = -1

    for i in range(len(case)):
        if(case[i][0] == 'duración del préstamo'):
            duration = int(case[i][1])
        elif(case[i][0] == 'cuantía del préstamo'):
            amount = float(case[i][1])
        
        if(duration != -1 and amount != -1):
            break
    
    return LoanResultValue([amount, duration, 0, 0])


"""Decision class for loans domain
"""
class LoanDecision(Decision):
    """Decision class construtor

    Args:
        decision (bool, optional): Value that represents the decision. Defaults to False.
    """
    def __init__(self, decision: bool = False):
        super(LoanDecision, self).__init__(decision, [('cantidad', 0), ('duración', 0), ('interés', 0), ('cuantía mensual', 0)])
    """Overwrites toString method from Decision class
    """
    def toString(self):
        if(self._decision):
            message = 'Decisión: Concedido\n\n'
            for key, value in self._details:
                message += f'\t{key}: {value}\n'
            return message
        else:
            return 'Decisión: Denegado'
    
def loadResultValue(value: LoanResultValue):
    decision = LoanDecision()

    decision.addDetail('cantidad', value.getValue('cantidad'))
    decision.addDetail('duración', value.getValue('duración'))
    decision.addDetail('interés', value.getValue('interés'))
    decision.addDetail('cuantía mensual', value.getValue('cuantía mensual'))

    decision.setDecision(value.getValue('decisión'))
    decision.setDecisionMade(value.getValue('decidido'))

    return decision
        