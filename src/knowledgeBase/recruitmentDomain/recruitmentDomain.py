from knowledgeBase.commons.decision import Decision
from knowledgeBase.commons.case import Case
from knowledgeBase.commons.criteria import Criteria
from knowledgeBase.commons.resultValue import ResultValue

"""Nivel de estudios del candidato
"""
class EducationLevel(Case):
    def __init__(self):
        super(EducationLevel, self).__init__('nivel de estudios', 'selectable', ['secundaria', 'grado medio', 'grado superior', 'universitario'])

"""Nivel de idioma del candidato
"""
class LanguageLevel(Case):
    def __init__(self):
        super(LanguageLevel, self).__init__('nivel de idioma', 'selectable', ['básico', 'intermedio', 'avanzado'])

"""Experiencia laboral del candidato en años
"""
class WorkExperience(Case):
    def __init__(self):
        super(WorkExperience, self).__init__('experiencia laboral', 'selectable', ['SI', 'NO'])

def getCases():
    """Function that returns the cases for the recruitment domain

        Returns:
            Array<Case>: List of cases
        """
    cases=[]
    cases.append(EducationLevel())
    cases.append(LanguageLevel())
    cases.append(WorkExperience())
    
    return cases

"""Criteria for language level
"""
class LanguageLevelCriteria(Criteria):
    def __init__(self):
        """Constructor"""
        super(LanguageLevelCriteria, self).__init__('nivel de idioma')
    
    def eval(self, case, value):
        """Redefinition of eval method"""
        super(LanguageLevelCriteria, self).eval(case, value)

        languageLevel = ''
        message = f'evaluando {self.name}\n\t'
        values = []

        for i in range(len(case)):
            if(case[i][0] == 'nivel de idioma'):
                languageLevel = case[i][1]
        
        if(languageLevel == ''):
            values.append(('decisión', False))
            values.append(('puntuación', 0))
            message = f'{message}No se ha especificado el nivel de idioma\n'
        elif (languageLevel == 'básico'):
            values.append(('decisión', True))
            values.append(('puntuación', 1))
            message = f'{message}Nivel de idioma básico\n'
        elif (languageLevel == 'intermedio'):
            values.append(('decisión', True))
            values.append(('puntuación', 2))
            message = f'{message}Nivel de idioma intermedio\n'
        elif (languageLevel == 'avanzado'):
            values.append(('decisión', True))
            values.append(('puntuación', 3))
            message = f'{message}Nivel de idioma avanzado\n'
        
        return values, message

class EducationLevelCriteria(Criteria):
    def __init__(self):
        """Constructor"""
        super(EducationLevelCriteria, self).__init__('nivel de estudios')
    
    def eval(self, case, value):
        """Redefinition of eval method"""
        super(EducationLevelCriteria, self).eval(case, value)

        educationLevel = ''
        message = f'evaluando {self.name}\n\t'
        values = []

        for i in range(len(case)):
            if(case[i][0] == 'nivel de estudios'):
                educationLevel = case[i][1]
        
        if(educationLevel == ''):
            values.append(('decisión', False))
            values.append(('puntuación', 0))
            message = f'{message}No se ha especificado el nivel de estudios\n'
        elif (educationLevel == 'secundaria'):
            values.append(('decisión', True))
            values.append(('puntuación', 1))
            message = f'{message}Nivel de estudios: secundaria\n'
        elif (educationLevel == 'grado medio'):
            values.append(('decisión', True))
            values.append(('puntuación', 2))
            message = f'{message}Nivel de estudios: grado medio\n'
        elif (educationLevel == 'grado superior'):
            values.append(('decisión', True))
            values.append(('puntuación', 3))
            message = f'{message}Nivel de estudios: grado superior\n'
        elif (educationLevel == 'universitario'):
            values.append(('decisión', True))
            values.append(('puntuación', 4))
            message = f'{message}Nivel de estudios: universitario\n'
        
        return values, message

class WorkExperienceCriteria(Criteria):
    def __init__(self):
        """Constructor"""
        super(WorkExperienceCriteria, self).__init__('experiencia laboral')
    
    def eval(self, case, value):
        """Redefinition of eval method"""
        super(WorkExperienceCriteria, self).eval(case, value)

        workExperience = ''
        message = f'evaluando {self.name}\n\t'
        values = []

        for i in range(len(case)):
            if(case[i][0] == 'experiencia laboral'):
                workExperience = case[i][1]
        
        if(workExperience == ''):
            values.append(('decisión', False))
            values.append(('puntuación', 0))
            message = f'{message}No se ha especificado la experiencia laboral\n'
        elif (workExperience == 'SI'):
            values.append(('decisión', True))
            values.append(('puntuación', 1))
            message = f'{message}Experiencia laboral: SI\n'
        elif (workExperience == 'NO'):
            values.append(('decisión', True))
            values.append(('puntuación', 0))
            message = f'{message}Experiencia laboral: NO\n'
        
        return values, message


def getCriterias():
    """Function that returns all criterias
    
    Returns:
        Array<Criterias>: All criterias
    """
    criterias = []
    criterias.append(LanguageLevelCriteria())
    criterias.append(EducationLevelCriteria())
    criterias.append(WorkExperienceCriteria())

    return criterias

class RecruitmentResultValue(ResultValue):
    def __init__(self, values=[0, 0, 0]):
        """Constructor

        Args:
            values (Array<any>, optional): initial values of the attributes. The order is: nivel de estudios -> nivel de idioma -> experiencia laboral. Defaults to [0, 0, 0]
        """
        attributes = [('nivel de estudios', values[0]), ('nivel de idioma', values[1]), ('experiencia laboral', values[2]), ('decisión', True), ('decidido', False)]

        super(RecruitmentResultValue, self).__init__(attributes)
    
    def setValue(self, key, value):
        """Add or set the value. It depends of the key

        Args:
            key (str): Attribute key. Could be 'nivel de estudios', 'nivel de idioma', 'experiencia laboral', 'decisión' or 'decidido'
            value (any): Value to add or set
        """
        super().setValue(key, value)

        if key == 'nivel de estudios':
            self._attributes[0] = (self._attributes[0][0], value)
        elif key == 'nivel de idioma':
            self._attributes[1] = (self._attributes[1][0], value)
        elif key == 'experiencia laboral':
            self._attributes[2] = (self._attributes[2][0], value)
        elif key == 'decisión':
            self._attributes[3] = (self._attributes[3][0], value)
        elif key == 'decidido':
            self._attributes[4] = (self._attributes[4][0], value)

def setInitialResultValue(case):
    """Initialize a RecruitmentResultValue

    Args:
        case (Array<(key, values)>): Case info
    
    Return:
        RecruitmentResultValue: result value initialized
    """
    educationLevel = -1
    languageLevel = -1
    workExperience = -1

    for key, value in case:
        if key == 'nivel de estudios':
            if value == 'secundaria':
                educationLevel = 1
            elif value == 'grado medio':
                educationLevel = 2
            elif value == 'grado superior':
                educationLevel = 3
            elif value == 'universitario':
                educationLevel = 4
        elif key == 'nivel de idioma':
            if value == 'básico':
                languageLevel = 1
            elif value == 'intermedio':
                languageLevel = 2
            elif value == 'avanzado':
                languageLevel = 3
        elif key == 'experiencia laboral':
            if value == 'SI':
                workExperience = 1
            elif value == 'NO':
                workExperience = 0

    return RecruitmentResultValue([educationLevel, languageLevel, workExperience])


"""Decision class for recruitment domain
"""
class RecruitmentDecision(Decision):
    """Decision class constructor"""
    def __init__(self, decision: bool = False):
        super(RecruitmentDecision, self).__init__(decision, [('nivel de estudios', 0), ('nivel de idioma', 0), ('experiencia laboral', 0), ('puntuación total', 0)])

    def toString(self):
        if self._decision:
            message = 'Decisión: Aprobado\n\n'
        else:
            message = 'Decisión: Rechazado\n\n'
        for key, value in self._details:
            message += f'{key} : {value}\n'
        return message

def loadResultValue(value: ResultValue):
    decision = RecruitmentDecision()

    education_level = value.getValue('nivel de estudios')
    language_level = value.getValue('nivel de idioma')
    work_experience = value.getValue('experiencia laboral')

    total_score = education_level + language_level + work_experience

    decision.addDetail('nivel de estudios', education_level)
    decision.addDetail('nivel de idioma', language_level)
    decision.addDetail('experiencia laboral', work_experience)
    decision.addDetail('puntuación total', total_score)

    if total_score > 3:
        decision.setDecision(True)
    else:
        decision.setDecision(False)

    decision.setDecisionMade(True)

    return decision
