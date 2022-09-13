from enum import Enum
from typing import List, Dict
import random

# DO NOT MODIFY THESE ENUMS/CONSTANTS; use them as is in your code
class GuessState(Enum):
    UNKNOWN = 0
    INVALID_WORD = 1
    GUESS_AGAIN = 2
    YOU_LOST = 3
    YOU_WON = 4

class LetterState(Enum):
    MATCH_LETTER = 0
    MATCH_PLACE = 1
    NOT_FOUND = 2

class TextColor:
    GREEN =  '\033[32m'
    YELLOW =  '\033[33m'
    RESET =  '\033[m'
# END CONSTANTS

# ********************
# Instructions:
# ********************
# Implement the class headers, constructors, and methods in the placeholder 
# spots (surrounded by """).  All variables and methods must use type hints.
# Use the APIs to determine how they should operate.  wordle_runner.py will
# handle running the game so that you can test out your functionality.
# ********************


# Class: GuessResult
# *************************
# An object that gets passed to the user (e.g. wordle_runner) about how a guess
# performed against the current word. 
# This object is meant to store related properties in a single object, 
# with a couple string helper functions. All attributes are public 
# and can be set from outside the class without getters and setters.
""" <Declare class header here> """

    # Constructor: 
    # ************************
    # Parameters: 
    #   guess: str: the guess string
    #   turns_remaining: int: the number of turns remaining after this guess
    # Return: None
    # ************************
    # Initialize the following attributes (names must be exact for test):
    #   user_guess: str: the guess that this object is storing state for (default: parameter val)  
    #   turns_remaining: int: the number of turns remaining after this one (default: parameter val)
    #   state: GuessState: the game result of this guess, e.g. if you won (default to GuessState.UNKNOWN)
    #   letter_state: List[LetterState]: LetterState of each letter in the current guess (default: empty list)
    #   current_word: str: set this to None until the user has lost the game to not give it away
""" <write constructor for GuessResult here>"""

    # get_state_string
    # ******************
    # Gets a string explaining the game state after the current guess
    # ****************** 
    # Parameters: None
    # Returns the following strings depending on the value of the state attribute:
    #   GUESS_AGAIN: "<NUMBER OF TURNS LEFT> turns left"
    #   YOU_WON: "You Won!!"
    #   YOU_LOST: "You lost.  Word was <THE WORD>"
    #   INVALID or UNKNOWN: "Not a word, try again."
""" <method for get_state_string> """
   
    # get_guess_string
    # *******************
    # Returns a string that has each letter of the guess color coded. If the guess
    # contains a letter that occurs more than once in the real word, only highlight
    # the first occurence of the letter that is not already highlighted.
    # *******************
    # Parameters: None
    # Return:
    # Concatenate the TextColor constants in front of each letter in the string to
    # make it a specific color:
    # GREEN: Letter is in the word at the correct position
    # YELLOW: Letter is in the word but at an incorrect position
    # RESET: Letter is not in the word
""" <method for get_guess_string> """


# class WordList
# ******************
# A "dictionary" of words that you can use for the game; selects
# and verifies whether words are words of the length being tracked
""" <Class Header for WordList> """

    # Constructor
    # ******************
    # Initialize the following attributes (make sure you include the beginning _):
    # - _word_length: int: the length of the words we want to track
    # - _active_words: List[str]: a list of words that are of the correct length
    def __init__(self) -> None:
        # load words from file; DO NOT MODIFY UNLESS YOU WANT TO DO YOUR OWN FILE I/O;)
        with open("words.txt", "r", encoding="utf-8") as file:
            self._words = [line.rstrip() for line in file]
        # init other attributes here
 

    # set_active_word_length
    # ************************
    # Sets the length of the words that we are looking for and adds all words 
    # of that length to _active_words
    # ************************
    # Parameters:
    #   length: int: the length of the words to track 
    # Return: None
""" <method for set_active_word_length> """

    # is_valid_word
    # ***************
    # Checks to see if word is a valid word of the length we are looking for.
    # ***************
    # Parameters:
    #   word: str: the word that we want to check is valid
    # Return: bool: true if the word is found, and false otherwise
""" <method for is_valid_word> """

    # pick_random_word
    # ******************
    # Picks a random word of the current active word length
    # ******************
    # Parameters: None
    # Return: str: a random word of the current active length 
""" <method for pick_random_word> """


MAX_GUESSES = 5

# class WordleGame
# ******************
# Manages the gameplay logic for Wordle.
""" <Class header for WordleGame> """
    
    # Constructor:
    # Initialize your choice of attributes needed for your logic
""" <Constructor for WordleGame> """

    # has_more_guesses
    # *****************
    # Checks to see if you can continue to guess words
    # *****************
    # Parameters: None
    # Return: bool: true if you have not reached MAX_GUESSES, and false 
    # if no guesses remain.
""" <method for has_more_guesses> """

    # start_new_game
    # *****************
    # Starts a new game of Wordle using words of the given length
    # *****************
    # Parameters:
    #   length: int: the length of the words you want to use for this game
    #   test_word: str: optional: specify a word to use for this game for testing purposes.  To make it optional,
    #        set it equal to a default value in the parameter, e.g. "test_word:str = None"
    # Return: None
""" <method for start_new_game> """

    # submit_guess_and_get_result
    # *****************
    # Creates a GuessResult object with the user's guess and how it did against
    # the target word. This method is responsible for setting the values
    # in the returned object. Remember that the current word should not be stored
    # in the object unless the user has lost the game with this guess.
    # *****************
    # Parameters:
    #   guess: str: the user's guess for the word
    # Return: GuessResult: object that contains the results of the current guess
""" <method for submit_guess_and_get_result> """

