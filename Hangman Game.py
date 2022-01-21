#Hangman Game
#Thomas Vaughan
#2022

words = ('ant badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

hangman_stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def is_word_guessed(word, letters_guessed):
    # TODO: Fill in your the code here
    import copy
    _letters_guessed = copy.copy(letters_guessed)
    # Check each letter in the current game word
    for letter in word:
        try:
            # Remove guessed letter that has been check to be in the game word
            _letters_guessed.pop(_letters_guessed.index(letter))
            # Remove letter from array
        except Exception:
            # Game letter was not in letters_guessed
            # to return False (word hasn't been guessed)
            return False
    # All letters checked successfully and are
    # presnt so return True (word has been guessed)
    return True

def get_guessed_word(word, letters_guessed):
    # TODO: Fill in your code here
    # String to store displayed hangman letter list
    game_string = ""
    import copy
    _letters_guessed = copy.copy(letters_guessed)
    # Check each letter in the game word
    for i in range(len(word)):
        # Letter was guessed
        if word[i] in _letters_guessed:
            # Add the correct guessed word to the displayed hangman word list
            game_string += word[i].upper()
            # Remove the guessed letter from the copied
            # letters_guessed list so     we can check multiple occurances
            _letters_guessed.pop(_letters_guessed.index(word[i]))
        # Letter want guessed
        else:
            game_string += "_"
    return game_string

def get_remaining_letters(letters_guessed):
    # TODO: Fill in your code here
    from string import ascii_uppercase
    remaining = ascii_uppercase  # Store alphabet string
    # Remove the letter that have been guessed
    for letter in letters_guessed:
        remaining = remaining.replace(letter, "")
    return remaining

def check_guess(letter, word, letters_guessed):
    if letter in word:
        if word.count(letter) > letters_guessed.count(letter):
            return True
        else:
            print("You have used up all of letter", letter, "for this word.")
            return False
    else:
        print("That letter is not in this word.")
        return False

def display_hangman(remaining_guesses, word, letters_guessed):
    print(hangman_stages[6 - remaining_guesses], "\n", get_guessed_word(word, letters_guessed))

def main():
    print("Welcome to hangman!")
    usr_input = "yes"
    while usr_input == "yes":
        print("[New Game Started!]")
        from random import randint
        word = words[randint(0, len(words) - 1)].upper()
        print(word)
        guesses = 6
        letters_guessed = []
        #  Loop while guesses haven't run out
        # and the word hasn't been guessed
        while guesses > 0 and is_word_guessed(
            word, letters_guessed) is False:
            display_hangman(guesses, word, letters_guessed)
            print("Available letters: ", get_remaining_letters(letters_guessed).upper())
            guess = input("Please guess a letter: ")
            from string import ascii_uppercase
            guess = guess.upper()
            # Check if the user has entered a alphabetical letter
            if guess in ascii_uppercase and guess != "":
                # Check  if user hass entered the same previously
                if check_guess(guess, word, letters_guessed):
                    print("You have guessed a correct letter!")
                    letters_guessed.append(guess)
                    display_hangman(guesses, word, letters_guessed)
                else:
                    guesses -= 1
                    display_hangman(guesses, word, letters_guessed)
            else:
                guesses -= 1
                print("Please only guess a alphabetical character")
            print("-------------")
        #  Check if game ended from running out of guessed
        if guesses == 0:
            print("Sorry, you ran out of guesses. The word was:", word, "\n[GAME OVER]")
        # Word was guessed correctly
        else:
            print("Congratulations, you won! The word is", word)
        usr_input = input("Play again? (yes/no): ")   
    print("Thank for playing. Goodbye!")





main()