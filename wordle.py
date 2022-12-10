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
class GuessResult:
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
    def __init__(self, user_guess: str, turns_remaining: int):
        self.user_guess = user_guess
        self.turns_remaining = turns_remaining
        self.state = GuessState.UNKNOWN
        self.letter_state = []
        self.current_word = None
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
    def get_state_string(self):
        #very straight forward, check the state for the specific GuessState and give the appropiate return val
        if self.state == GuessState.GUESS_AGAIN:
            return self.turns_remaining + " turns left"
        elif self.state == GuessState.YOU_WON:
            return "You Won!!"
        elif self.state == GuessState.YOU_LOST:
            return "You lost. Word was " + self.current_word
        elif self.state == GuessState.INVALID_WORD or self.state == GuessState.UNKNOWN:
            return "Not a word, try again."
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
    def get_guess_string(self):
        #
        ##check for any Greens
        #for x in range(len(self.user_guess)):
        #    if self.current_word[x] == self.user_guess[x]:
        #        #if the letter is in the same spot then all is great return that green
        #        return 
        ##check for reset, if the letter isnt in the word at all
        #for x in range(len(self.user_guess)):
        #    letter_in_word = False
        #    for y in range(len(self.user_guess)):
        #        if self.current_word[x] == self.user_guess[y] and self.current_word[x] != self.user_guess[x]:
        #            letter_in_word = True
        #    if letter_in_word == False:
        #        #in the case that the letter is not in the word, it needs to be greyed out w the reset color
        #        return
        #    else:
        #        #if the code reaches this point, the letter is in the word but the letter is not in the same place (to not overlap with the green )
        #       return
        
        #This ^ is going to remain here as my mark of shame I didn't realize that it was specifically for LetterState
        #I thought I had to manually code it this was embarassing.

        #actually that was rather useful i needed that later

        char_str = ""
        index = 0
        for x in self.letter_state:
            if x == LetterState.MATCH_LETTER:
                char_str = char_str +TextColor.YELLOW + self.user_guess[index] + TextColor.RESET
            elif x == LetterState.MATCH_PLACE:
                char_str = char_str +TextColor.GREEN + self.user_guess[index] + TextColor.RESET
            elif x == LetterState.NOT_FOUND:
                char_str = char_str +TextColor.RESET + self.user_guess[index] + TextColor.RESET
            index = index + 1
        return char_str

# class WordList
# ******************
# A "dictionary" of words that you can use for the game; selects
# and verifies whether words are words of the length being tracked
""" <Class Header for WordList> """
class WordList:
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
        self._active_words = []
        self._word_length = 0

    # set_active_word_length
    # ************************
    # Sets the length of the words that we are looking for and adds all words 
    # of that length to _active_words
    # ************************
    # Parameters:
    #   length: int: the length of the words to track 
    # Return: None
    """ <method for set_active_word_length> """
    def set_active_word_length(self, length: int) -> None:
        self._active_words = []
        self.length = length
        self._word_length = self.length
        for x in self._words:
            if len(x) == self.length:
                self._active_words.append(x)

    # is_valid_word
    # ***************
    # Checks to see if word is a valid word of the length we are looking for.
    # ***************
    # Parameters:
    #   word: str: the word that we want to check is valid
    # Return: bool: true if the word is found, and false otherwise
    """ <method for is_valid_word> """
    def is_valid_word(self, word: str) -> bool:
        
        if len(word) != self._word_length:
            return False
        for x in self._active_words:
            if x == word:
                return True
        return False
    # pick_random_word
    # ******************
    # Picks a random word of the current active word length
    # ******************
    # Parameters: None
    # Return: str: a random word of the current active length 
    """ <method for pick_random_word> """
    def pick_random_word(self) -> str:
        return random.choice(self._active_words)

MAX_GUESSES = 5

# class WordleGame
# ******************
# Manages the gameplay logic for Wordle.
""" <Class header for WordleGame> """
class WordleGame:
    # Constructor:
    # Initialize your choice of attributes needed for your logic
    """ <Constructor for WordleGame> """
    def __init__(self):
        #gotta determine how many guess to give them
        self.total_guesses = 0
        self.length = 5
        self.start_list = WordList()
        self.test_word = ""
        self.current_word =""
        
        
    # has_more_guesses
    # *****************
    # Checks to see if you can continue to guess words
    # *****************
    # Parameters: None
    # Return: bool: true if you have not reached MAX_GUESSES, and false 
    # if no guesses remain.
    """ <method for has_more_guesses> """
    def has_more_guesses(self) -> bool:
        #total guesses is going to be changing per submitted guess
        return self.total_guesses == MAX_GUESSES
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
    def start_new_game(self, length:int, test_word:str):
        self.length = length
        self.start_list = WordList()
        self.start_list.set_active_word_length(self.length)
        self.test_word = test_word

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
    def submit_guess_and_get_result(self, guess:str) ->GuessResult:
        self.guess = guess
        g = GuessResult(self.guess, MAX_GUESSES-self.total_guesses)
        #GuessResult object initialized, and WordList is the self.start_list since that started the game
        # code go brrrrr imagine not doing your homework - Chris Lynn
        
        #case of if the guess isn't valid
        if self.start_list.is_valid_word(self.guess) == False:
            g = GuessState.INVALID_WORD
            #if its not a valid word, change the guessstate of it and return the guessresult
            return g
            #letter state wouldn't matter, or maybe i'll have to set it to all grey
        self.total_guesses+=1
        #each time the code runs that should be adding on a guess, but it shouldn't include invalid words

        #if it gets to here, then the guess if a valid word
        #what should be done to determine that the guess is correct
        if self.total_guesses <= MAX_GUESSES:
            #as long as all the guesses arent used, check the word
            if self.guess == self.test_word:
                g = GuessState.YOU_WON
                return g
                #might set the entire letter state to correct (MATCH_PLACE)

        #you only lose in one case, when all guesses are used and the word isnt a the final word
        #if it gets to here, that means the guess was confirmed to not be correct.
        if self.total_guesses == MAX_GUESSES:
            if self.guess != self.test_word:
                g = GuessState.YOU_LOST
                return g
                #if a letterstate is needed then i can move the code below to above this

        #if it gets past that, it means that not all guesses were used but the guess was incorrect

        #check for any Greens
        for x in range(len(self.guess)):
            if self.current_word[x] == self.guess[x]:
                #if the letter is in the same spot then all is great slap a green on that letter state
                g.letter_state.append(LetterState.MATCH_PLACE)
        #check for RESET, if the letter isnt in the word at all
        for x in range(len(self.guess)):
            letter_in_word = False
            for y in range(len(self.guess)):
                if self.current_word[x] == self.guess[y] and self.current_word[x] != self.guess[x]:
                    letter_in_word = True
            if letter_in_word == False:
                #in the case that the letter is not in the word, it needs to be greyed out w the reset color
                g.letter_state.append(LetterState.NOT_FOUND)
            else:
                #if the code reaches this point, the letter is in the word but the letter is not in the same place (to not overlap with the green )
                g.letter_state.append(LetterState.MATCH_LETTER)
        #The loop gets the letter state situation for the guess sorted out, but what use is that

        #Well the case im looking for is that the guess was incorrect, but that they still have a change to guess again
        #the letter state helps determine which letters were in the correct spot or at least in the word
        #now the code for the submit guess should return that along with the GuessState GUESS_AGAIN

        # the code already determined the letter state for the GuessResult, so its what i should do with that info now
        #theres already a method that deals with that in GuessResult, get_guess_string (returns a string)
        print(g.get_guess_string())
        #that'll print out a string of the characters that should be color coded
        #but whats the use of that

        #in the GuessResult by this point, letter state is taken care of. state will be determined when i drop the GUESS_AGAIN
        #that leaves current_word to be set to the correct word, but should be done earlier
        #theres nothing other than that i think
        if self.total_guesses < MAX_GUESSES:
            #as long as all the guesses arent used, check the word
            g = GuessState.GUESS_AGAIN
            return g


