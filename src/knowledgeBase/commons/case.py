"""Class that contains a case info
"""
class Case():
    def __init__(self, name, type, allowedValues=None):
        """_summary_

        Args:
            name (str): _description_
            type (str): Type of the attribute: natural, real, selectable
            allowedValues (array<str>, optional): Values allowed for selectable attributes. Defaults to None.
        """
        self.name = name
        self.type = type
        self.allowedValues = allowedValues