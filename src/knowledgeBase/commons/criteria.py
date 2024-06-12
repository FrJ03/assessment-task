"""Class that represents a criteria to evaluate
"""
class Criteria():
    def __init__(self, name):
        """Constructor
        Args:
            name (str): criteria name
        """
        self.name = name
    
    def eval(self, case, decision):
        """Evaluate the criteria and return a decision based in the new criteria and the current decision

        Args:
            case (Array<(name, value)>): Case information
            decision (Decision): Current decision
        Returns:
            Decision: new decision based on the criteria
            str: decision message
        """
        pass