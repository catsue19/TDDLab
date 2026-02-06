
class cipher:
    def __init__(self) -> None:
        self.LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖabcdefghijklmnopqrstuvwxyzåäö"

    def pattern_cipher(self, normal: str)-> str:
        '''
        Single-word pattern cipher
        Args:
            normal (str): Normal string
        Returns:
            (str) Ciphered String
        '''

        if normal is None:
            return None

        ciphered_word = normal
        string_list = []
        
        for char in normal:
            # only alphabetic words are transformed
            if char in self.LETTERS:

                # palindrome case -> leave unchanged
                if normal.lower() == normal.lower()[::-1]:
                    ciphered_word = normal

                # repeated letter case -> reverse the word
                # check duplicate letters case insensitive
                elif self.has_duplicates(normal.lower()):
                    ciphered_word = normal[::-1]
                    
                # if not duplicate letters, all letters must be unique case -> rotate left by one char
                else: 
                    ciphered_word = normal[1:] + normal[:1]

            # numbers, special characters, and punctuation remain unchanged
            else:
                string_list.append(char)
                ciphered_word = ''.join(string_list)
                
        return ciphered_word
        
    def has_duplicates(self, string):
        for i in range(0, len(string)): 
            for j in range(i+1, len(string)):
                if (string[i] == string[j]): 
                    # the character is a duplicate
                    return True
