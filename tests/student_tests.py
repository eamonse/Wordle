import unittest
from wordle import WordList, GuessResult, GuessState, LetterState, WordleGame

"""
Instructions:
Write a test case for any function that you implemented
"""
class StudentTestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.game: WordleGame = WordleGame()
        return super().setUp()

    def test_student_case(self) -> None:
        #asserting the state of the GuessResult state
        correct_word = "wolf"
        self.game.start_new_game(4, correct_word)
        self.g = GuessResult("bllb", 5)
        self.assertEqual(GuessState.UNKNOWN, self.g.state)
        #with no submitted guess and result, the state should be an unknown (default) value.



        self.g = self.game.submit_guess_and_get_result("bllb")
        self.assertEqual(GuessState.INVALID_WORD, self.g.state)
        #as bllb isnt actually a word, it should return invalid word



        self.g = self.game.submit_guess_and_get_result("bond")
        self.assertEqual(GuessState.GUESS_AGAIN, self.g.state)
        self.assertEqual(self.g.turns_remaining, 4)
        #in the case that it does work, it should return a regular guess again, and one guess should be taken off



        #self.g = self.game.submit_guess_and_get_result("wolf")
        #self.assertEqual(GuessState.YOU_WON, self.g.state)
        #self.assertEqual(self.g.turns_remaining, 3)
        #if the word that was guessed was correct, then it should end it with YOU_WON and with only 3 guesses remaining


        self.g = self.game.submit_guess_and_get_result("long")
        self.g = self.game.submit_guess_and_get_result("song")
        self.g = self.game.submit_guess_and_get_result("song")
        self.g = self.game.submit_guess_and_get_result("song")
        self.assertEqual(GuessState.YOU_LOST, self.g.state)

        
        

    
    

        

        


