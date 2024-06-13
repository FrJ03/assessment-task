"""Class that represents a criteria to evaluate
"""
class Criteria():
    def __init__(self, name):
        """Constructor
        Args:
            name (str): criteria name
        """
        self.name = name
    
    def eval(self, case, val=None):
        """Evaluate the criteria and return a list of values modified based in the new criteria

        Args:
            case (Array<(name, value)>): Case information
            eval (ResultValue): Current evaluation data
        Returns:
            Array<(key,value)>: new values based on the criteria
            str: decision message
        """
        pass