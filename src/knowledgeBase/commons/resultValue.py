""" Resulting value of the evaluation
"""
class ResultValue():
    def __init__(self, attributes):
        """Constructor

        Args:
            attributes (Array<(key, value)>): List of attributes for the result value
        """
        self._attributes = attributes

    def setInitialData(self, case):
        pass

    def getAttributes(self):
        """Return all the attributes of the result

        Returns:
            Array<(key, value)>: Result data
        """
        return self._attributes
    
    def setAttributes(self, attributes):
        """Set all attributes for the result

        Args:
            attributes (Array<(key, value)>): Result data
        """
        self._attributes = attributes

    def getValues(self):
        """Get all values

        Returns:
            Array<any>: Values
        """
        values = []

        for i in range(len(self._attributes)):
            values.append(self._attributes[i])

        return values

    def getValue(self, key):
        """Get the value of an attribute

        Args:
            key (str): attribute value

        Returns:
            any: attribute value
        """
        for i in range(len(self._attributes)):
            if(self._attributes[i][0] == key):
                return self._attributes[i][1]
        
        return -1
    
    def setValue(self, key, value):
        """Add or set the value. It depends of the key

        Args:
            key (str): Attribute key
            value (any): Value to add or set
        """
        pass
