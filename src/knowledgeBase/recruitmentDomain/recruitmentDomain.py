from knowledgeBase.commons.decision import Decision
from knowledgeBase.commons.case import Case
from knowledgeBase.commons.criteria import Criteria

"""Nivel de estudios del candidato
"""
class EducationLevel(Case):
    def __init__(self):
        super(EducationLevel, self).__init__('nivel de estudios', 'selectable', ['secundaria', 'grado superior', 'universitario'])

"""Nivel de idioma del candidato
"""
class LanguageProficiency(Case):
    def __init__(self):
        super(LanguageProficiency, self).__init__('nivel de idioma', 'selectable', ['básico', 'intermedio', 'avanzado', 'nativo'])

"""Experiencia laboral del candidato en años
"""
class WorkExperience(Case):
    def __init__(self):
        super(WorkExperience, self).__init__('experiencia laboral', 'natural')

"""Puesto solicitado por el candidato
"""
class JobPosition(Case):
    def __init__(self):
        super(JobPosition, self).__init__('puesto solicitado', 'selectable', ['electricista', 'ingeniero eléctrico', 'otro'])

def getCases():
    """Función que retorna los casos para el dominio de selección de personal

    Returns:
        Array<Case>: Lista de casos
    """
    cases = []
    cases.append(EducationLevel())
    cases.append(LanguageProficiency())
    cases.append(WorkExperience())
    cases.append(JobPosition())
    
    return cases

"""Criterio para evaluar el nivel de estudios del candidato
"""
class EducationCriteria(Criteria):
    def __init__(self):
        """Constructor
        """
        super(EducationCriteria, self).__init__('nivel de estudios')

    def eval(self, case, decision: Decision):
        """Redefinición del método eval

        Args:
            case (Array<(key,value)>): Información del caso
            decision (Decision): Decisión actual

        Returns:
            Decision: Nueva decisión
        """
        super(EducationCriteria, self).eval(case, decision)

        educationLevel = ''
        jobPosition = ''
        message = f'evaluando {self.name}\n\t'

        for i in range(len(case)):
            if case[i][0] == 'nivel de estudios':
                educationLevel = case[i][1]
            elif case[i][0] == 'puesto solicitado':
                jobPosition = case[i][1]

        if jobPosition == 'electricista':
            if educationLevel == 'universitario':
                decision.addDetail('puntuación', 10)
                message = f'{message}Nivel universitario para puesto de electricista, puntuación 10\n'
            elif educationLevel == 'grado superior':
                decision.addDetail('puntuación', 7)
                message = f'{message}Grado superior para puesto de electricista, puntuación 7\n'
            elif educationLevel == 'secundaria':
                decision.addDetail('puntuación', 4)
                message = f'{message}Secundaria para puesto de electricista, puntuación 4\n'
        else:
            if educationLevel == 'universitario':
                decision.addDetail('puntuación', 8)
                message = f'{message}Nivel universitario, puntuación 8\n'
            elif educationLevel == 'grado superior':
                decision.addDetail('puntuación', 5)
                message = f'{message}Grado superior, puntuación 5\n'
            elif educationLevel == 'secundaria':
                decision.addDetail('puntuación', 2)
                message = f'{message}Secundaria, puntuación 2\n'

        return decision, message

"""Criterio para evaluar el nivel de idioma del candidato
"""
class LanguageCriteria(Criteria):
    def __init__(self):
        """Constructor
        """
        super(LanguageCriteria, self).__init__('nivel de idioma')

    def eval(self, case, decision: Decision):
        """Redefinición del método eval

        Args:
            case (Array<(key,value)>): Información del caso
            decision (Decision): Decisión actual

        Returns:
            Decision: Nueva decisión
        """
        super(LanguageCriteria, self).eval(case, decision)

        languageProficiency = ''
        message = f'evaluando {self.name}\n\t'

        for i in range(len(case)):
            if case[i][0] == 'nivel de idioma':
                languageProficiency = case[i][1]

        if languageProficiency == 'nativo':
            decision.addDetail('puntuación', 10)
            message = f'{message}Nivel de idioma nativo, puntuación 10\n'
        elif languageProficiency == 'avanzado':
            decision.addDetail('puntuación', 7)
            message = f'{message}Nivel de idioma avanzado, puntuación 7\n'
        elif languageProficiency == 'intermedio':
            decision.addDetail('puntuación', 5)
            message = f'{message}Nivel de idioma intermedio, puntuación 5\n'
        elif languageProficiency == 'básico':
            decision.addDetail('puntuación', 2)
            message = f'{message}Nivel de idioma básico, puntuación 2\n'

        return decision, message

"""Criterio para evaluar la experiencia laboral del candidato
"""
class ExperienceCriteria(Criteria):
    def __init__(self):
        """Constructor
        """
        super(ExperienceCriteria, self).__init__('experiencia laboral')

    def eval(self, case, decision: Decision):
        """Redefinición del método eval

        Args:
            case (Array<(key,value)>): Información del caso
            decision (Decision): Decisión actual

        Returns:
            Decision: Nueva decisión
        """
        super(ExperienceCriteria, self).eval(case, decision)

        experience = -1
        message = f'evaluando {self.name}\n\t'

        for i in range(len(case)):
            if case[i][0] == 'experiencia laboral':
                experience = int(case[i][1])

        if experience < 0:
            decision.setDecision(False)
            decision.setDecisionMade(True)
            message = f'{message}No se ha especificado la experiencia laboral\n'
        else:
            decision.setDecision(True)
            decision.addDetail('puntuación', experience * 2)
            message = f'{message}Experiencia laboral evaluada, puntuación {experience * 2}\n'

        return decision, message

def getCriterias():
    """Función que retorna todos los criterios
    
    Returns:
        Array<Criterias>: Todos los criterios
    """
    criterias = []
    criterias.append(EducationCriteria())
    criterias.append(LanguageCriteria())
    criterias.append(ExperienceCriteria())

    return criterias

"""Clase de decisión para el dominio de selección de personal
"""
class RecruitmentDecision(Decision):
    """Constructor de la clase Decision

    Args:
        decision (bool, optional): Valor que representa la decisión. Defaults to False.
    """
    def __init__(self, decision: bool = False):
        super(RecruitmentDecision, self).__init__(decision, [('puntuación', 0)])
    
    """Sobrescribe el método toString de la clase Decision
    """
    def toString(self):
        if self._decision:
            message = 'Decisión: Aprobado\n\n'
            for key, value in self._details:
                message += f'\t{key}: {value}\n'
        else:
            message = 'Decisión: Rechazado\n'
        return message
    
    def addDetail(self, key: str, value):
        super().addDetail(key, value)

        self.recalcTotalScore()

    def recalcTotalScore(self):
        totalScore = 0

        for key, value in self._details:
            if key == 'puntuación':
                totalScore += value

        # Actualiza la puntuación total en los detalles
        for i in range(len(self._details)):
            if self._details[i][0] == 'puntuación':
                self._details[i][1] = totalScore
                break

