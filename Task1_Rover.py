
class rovar:

    def __init__(self) -> None:
        #“g” was missing from the lower consonants
        self._LOWER_CONSTANTS = "bcdfghjklmnpqrstvwxz"
        
        #“D” was missing from the upper consonants
        self._UPPER_CONSTANTS = "BCDFGHJKLMNPQRSTVWXZ"
 
    def enrove(self, normal: str)-> str:
        '''
        Encode the string in rovarspraket.
        Args:
            normal (str): Normal string
        Returns:
            (str) Encoded String
        '''
        if normal is None:
            return None
        
        encoded = []
        for char in normal:
            if char in self._LOWER_CONSTANTS:
                encoded.append(char + 'o' + char)
            elif char in self._UPPER_CONSTANTS:
                encoded.append(char + 'o' + char)
            else:
                encoded.append(char)
        return ''.join(encoded)
 
    def derove(self, rov:str)->str:
        """ 
            Decode a string from rovarspraket.
            Args:
                normal (str): Encoded string
            Returns:
                (str) Normal string
        """
        if rov is None:
            return None
       
        for c in self._LOWER_CONSTANTS:
            find = c+'o'+c
            rov = rov.replace(find, c)
       
        for c in self._UPPER_CONSTANTS:
            # “o” must be lower case
            find = c+'o'+c
            rov = rov.replace(find, c)
 
        return rov
