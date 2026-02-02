'''
    Student shall write their names here
        1. Student 1: Sofie Friholm
        2. Student 2: Arissa Rakluea
        3. Student 3: Catherine Sue
'''

import unittest
from Cipher import cipher

class test_string(unittest.TestCase):
    '''
        Write your TCs based on the lab instructions.

        1. Palindrome Rule (highest priority)
            - If a word is a palindrome (reads the same forward and backward, case-insensitive), leave it unchanged.
        2. Repeated Letter Rule (medium priority)
            - If the word contains any repeated letters and is not a palindrome, reverse the word.
        3. Unique Letter Rule (lowest priority)
            - If all letters are unique, rotate the word left by one character.

        Some words may match multiple rules. Priority determines which rule is applied: Palindrome > Repeated Letter > Unique Letter

        4. Additional Rules
            - If the input is empty ("") or None, it is returned unchanged.
            - Only alphabetic words are transformed.
            - Special characters/punctuation remain unchanged.
            - Original casing is preserved.

        - Identify all distinct equivalence classes (categories) of single words based on the rules.
        - Include conflict cases where multiple rules could apply.
        - Include boundary cases such as single-letter words, two-letter words, empty string, numbers, and special characters.
        - For each equivalence class, design at least one representative test case.
    '''

    def setUp(self):
        '''
            Set up shared resources = Class instance to access cipher class methods
        '''
        self.cp = cipher()

        # Check non-empty string input
        # Rules in order of priority: Palindrome > Repeated Letter > Unique Letter
        # Need to check distinct rules as well as cases where multiple rules could apply to the same word

    # - uppercase
    def test_cipher_large_palidrome(self):
        self.assertEqual(self.cp.pattern_cipher('LEVEL'), 'LEVEL')

    def test_cipher_large_repeated(self):
        self.assertEqual(self.cp.pattern_cipher('HELLO'), 'OLLEH')
    
    def test_cipher_large_unique(self):
        self.assertEqual(self.cp.pattern_cipher('CAT'), 'ATC')
        
    # - lowercase
    def test_cipher_small_palidrome(self):
        self.assertEqual(self.cp.pattern_cipher('level'), 'level')

    def test_cipher_small_repeated(self):
        self.assertEqual(self.cp.pattern_cipher('hello'), 'olleh')

    def test_cipher_small_unique(self):
        self.assertEqual(self.cp.pattern_cipher('cat'), 'atc')
    
    # - boundary case
    # - single letter
    def test_cipher_single_letter(self):
        self.assertEqual(self.cp.pattern_cipher('a'), 'a')
    
    # - two letter
    def test_cipher_single_letter(self):
        self.assertEqual(self.cp.pattern_cipher('Bä'), 'Bä')

    # - multi-rule case (palidrome + repeated letter)
    def test_cipher_multi(self):
        self.assertEqual(self.cp.pattern_cipher('noon'), 'noon')

    # ADDITIONAL RULES 
    # - null input
    def test_cipher_null(self):
        self.assertEqual(self.cp.pattern_cipher(None), None)
    
    # - empty string input
    def test_cipher_empty_string(self):
        self.assertEqual(self.cp.pattern_cipher(''), '')
        
    # - numbers
    def test_cipher_numbers(self):
        self.assertEqual(self.cp.pattern_cipher("0123456789"), "0123456789")
    
    # - punctuation and special characters
    def test_cipher_special_characters(self):
        self.assertEqual(self.cp.pattern_cipher('!” #€%&/(),.'), '!” #€%&/(),.')

    # - original casing is preserved
    def test_cipher_casing_preserved(self):
        self.asserrEqual(self.cp.pattern_cipher('Python'), 'ythonP')


if __name__ == '__main__':
    print("***********START OF All TEST CASES RESULTS SHOWN BELOW**************")
    unittest.main(verbosity = 2)