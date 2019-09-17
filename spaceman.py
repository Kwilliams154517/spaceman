
import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    
    for letter in secret_word:
        if letter in letters_guessed:
            pass
        else:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    result = ""
    
    for letter in secret_word:
        if letter in letters_guessed:
            result += letter
        else:
            result += "_"
    return result


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word

    if guess in secret_word:
        return True
    else:
        return False


def is_valid(guess, letters_guessed):
    if guess.isalpha():
        if len(guess) == 1:
            if guess not in letters_guessed:
                return True
    return False


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    letters_guessed = []
    guess_limit = len(secret_word)
    guess_number= 0
    
    print("WELCOME TO SPACEMAN")
    print("guess the correct letters if you dont you lose\n")
    
    print("Guesses: " + str(guess_limit - guess_number))
    print("_"*len(secret_word))

    while True:
        guess = input("Guess a letter: ")
        if is_valid(guess, letters_guessed):
            letters_guessed.extend(guess)
            guess_number+=1
            if is_guess_in_word(guess, secret_word):
                print("you're right! :)")
            else:
                print("You're wrong move on :(")
        else:
            print("you screwed up")
        
        print("Guesses left: " + str(guess_limit - guess_number))
        print(get_guessed_word(secret_word, letters_guessed))
        
        if is_word_guessed(secret_word, letters_guessed):
            print("Happy birthday you win")
            break
        if guess_number >= guess_limit:
            print("Youre a LoSeR")
            break


#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
while True:
    play_again = input("Would you like to play again? (yes, y): ")
    play_again = play_again.lower()
    if play_again == 'y' or play_again == 'yes':
        secret_word = load_word()
        spaceman(secret_word)
    else:
        break
