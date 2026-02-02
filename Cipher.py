
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

        encoded = []
        for char in normal:
            # only alphabetic words are transformed
            if char in self.LETTERS:
                 # palindrome case -> leave unchanged
                if normal == normal[::-1]:
                    encoded.append(char)
                # repeated letter case -> reverse the word

                # unique letter case -> rotate the word left by one character

            # number, special characters/punctuation remain unchanged
            else:
                encoded.append(char)
        return ''.join(encoded)

    