'''
    Student shall write their names here
        1. Student 1: Sofie Friholm
        2. Student 2: Arissa Rakluea
        3. Student 3: Catherine Sue
'''

import unittest
from Task1_Rover import rovar

class test_string(unittest.TestCase):
    '''
        _LOWER_CONSTANTS = "bcdfghjklmnpqrstvwxz"
        _UPPER_CONSTANTS = "BCDFGHJKLMNPQRSTVWXZ" 
        Swedish vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'å', 'ä', 'ö']

        Write your TCs based on the lab instructions. One TC has been written below as an example
        
    '''

    def setUp(self):
        '''
            Set up shared resources = Class instance to access rover class methods
        '''
        self.rv = rovar()

    # START ENROVE TEST CASES
    # Check lower case rover - consonants
    def test_enrove_small(self):
       self.assertEqual(self.rv.enrove('bcdfghjklmnpqrstvwxz'), 'bobcocdodfofgoghohjojkoklolmomnonpopqoqrorsostotvovwowxoxzoz')

    # Check null input
    def test_enrove_null(self):
        self.assertEqual(self.rv.enrove(None), None)

    # Check empty string
    def test_enrove_empty_string(self):
        self.assertEqual(self.rv.enrove(""), "")
    
    # Check upper case rover - consonants
    def test_enrove_large(self):
       self.assertEqual(self.rv.enrove('BCDFGHJKLMNPQRSTVWXZ'), 'BoBCoCDoDFoFGoGHoHJoJKoKLoLMoMNoNPoPQoQRoRSoSToTVoVWoWXoXZoZ')

    # Check lower case rover - vowels
    def test_enrove_small_vowel(self):
       self.assertEqual(self.rv.enrove('aeiouyåäö'), 'aeiouyåäö')
       
    # Check upper case rover - vowels
    def test_enrove_large_vowel(self):
       self.assertEqual(self.rv.enrove('AEIOUYÅÄÖ'), 'AEIOUYÅÄÖ')

    # Check string of numbers
    def test_enrove_numbers(self):
       self.assertEqual(self.rv.enrove("0123456789"), "0123456789")

    # Check punctuation and special characters
    def test_enrove_special_characters(self):
       self.assertEqual(self.rv.enrove('!” #€%&/(),.'), '!” #€%&/(),.')
    ####### END OF ENROVE TEST CASES

    # DEROVE TEST CASES
    # Check lower case rover - consonants
    def test_derove_small(self):
       self.assertEqual(self.rv.derove('bobcocdodfofgoghohjojkoklolmomnonpopqoqrorsostotvovwowxoxzoz'), 'bcdfghjklmnpqrstvwxz')

    # Check null input
    def test_derove_null(self):
        self.assertEqual(self.rv.derove(None), None)

    # Check empty string
    def test_derove_empty_string(self):
        self.assertEqual(self.rv.derove(""), "")
    
    # Check upper case rover - consonants
    def test_derove_large(self):
       self.assertEqual(self.rv.derove('BoBCoCDoDFoFGoGHoHJoJKoKLoLMoMNoNPoPQoQRoRSoSToTVoVWoWXoXZoZ'), 'BCDFGHJKLMNPQRSTVWXZ')

    # Check lower case rover - vowels
    def test_derove_small_vowel(self):
       self.assertEqual(self.rv.derove('aeiouyåäö'), 'aeiouyåäö')
       
    # Check upper case rover - vowels
    def test_derove_large_vowel(self):
       self.assertEqual(self.rv.derove('AEIOUYÅÄÖ'), 'AEIOUYÅÄÖ')

    # Check string of numbers
    def test_derove_numbers(self):
       self.assertEqual(self.rv.derove("0123456789"), "0123456789")

    # Check punctuation and special characters
    def test_derove_special_characters(self):
       self.assertEqual(self.rv.derove('!” #€%&/(),.'), '!” #€%&/(),.')
    ####### END OF DEROVE TEST CASES


if __name__ == '__main__':
    print("***********START OF All TEST CASES RESULTS SHOWN BELOW**************")
    unittest.main(verbosity = 2)