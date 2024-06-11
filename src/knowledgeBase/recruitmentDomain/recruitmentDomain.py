from knowledgeBase.commons.case import Case
from knowledgeBase.commons.decision import Decision



"""Education level of the candidate
"""
class EducationLevel(Case):
    def __init__(self):
        super(EducationLevel, self).__init__('nivel de educación', 'selectable', ['primaria', 'secundaria', 'grado medio', 'grado superior', 'universitario'])

"""Language proficiency of the candidate
"""
class LanguageProficiency(Case):
    def __init__(self):
        super(LanguageProficiency, self).__init__('nivel de idioma', 'selectable', ['básico', 'intermedio', 'avanzado', 'nativo'])

"""Years of experience of the candidate in the relevant field
"""
class YearsOfExperience(Case):
    def __init__(self):
        super(YearsOfExperience, self).__init__('años de experiencia', 'natural')

"""Specific job required, e.g., Electrician
"""
class JobType(Case):
    def __init__(self):
        super(JobType, self).__init__('tipo de trabajo', 'selectable', ['electricista', 'ingeniero', 'administrativo', 'otro'])

class JobTimeIdea(Case):
    def __init__(self):
        super(JobType, self).__init__('tiempo en el que se quiere quedar en la empresa', 'selectable', ['poco', 'medio', 'indefinido'])



def getCases():
    """Function that returns the cases for the recruitment domain

        Returns:
            Array<Case>: List of cases
        """
    cases = []
    cases.append(EducationLevel())
    cases.append(LanguageProficiency())
    cases.append(YearsOfExperience())
    cases.append(JobType())
    cases.append(JobTimeIdea())


    return cases


"""Decision class for the recruitment domain
"""
class RecruitmentDecision(Decision):
    """Decision class constructor

    Args:
        decision (bool, optional): Value that represents the decision. Defaults to False.
    """
    def __init__(self, decision: bool = False):
        super(self, RecruitmentDecision).__init__(decision)
    """Overwrites toString method from Decision class
    """
    def toString(self):
        if self._decision:
            message = 'Decisión: Aprobado\n\n'
            for key, value in self._details.items():
                message += f'\t{key}: {value}\n'
        else:
            message = 'Decisión: Rechazado\n'
        return message