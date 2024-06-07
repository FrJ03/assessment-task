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