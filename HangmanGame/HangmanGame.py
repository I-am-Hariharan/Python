import random


def welcome():
    name = input("\nEnter your name : ").capitalize()

    if name.isalpha() == True:
        print("\n>> Hi ", name,
              "<<\nWelcome to the Hangman Game! "
              "\n The computer will randomly choose a word...."
              "\n You will have to find what word it is ! "
              "\n Enjoy the Game !!!!!")

    else:
        print("Please type a valid name!")
        name = input("Enter your name : ")


def play_again():
    response = input('\nWould you like to play again? (y/n) : ').lower()

    if response == 'y':
        game_run()

    else:
        print('Hope you had fun playing the game!')


def get_word():
    words = ["apple", "plane", "table", "sky", "monitor", "book", "king"]
    return random.choice(words).lower()


def game_run():
    welcome()

    alphabets = ('abcdefghijklmnopqrstuvwxyz')

    word = get_word()

    letters_guessed = []

    tries = 7

    guessed = False

    print()

    print("The word contains ", len(word), "letters.")
    print('\n', len(word) * '_')

    while guessed == False and tries > 0:
        print('You have ', str(tries), 'tries')
        guess = input('Guess the letter in the word or the entire word : ')

        if len(guess) == 1:
            if guess not in alphabets:
                print('Please type a letter !')

            elif guess in letters_guessed:
                print('You have already guessed this letter'
                      '\nTry another one')

            elif guess not in word:
                print('Sorry the letter is not in the word :(')
                tries -= 1
                letters_guessed.append(guess)

            elif guess in word:
                print('Great! The letter exists in the word ')
                letters_guessed.append(guess)

        elif len(guess) == word:
            if guess not in word:
                print('Sorry.. You have guessed the worng word \n Try again!')
                tries -= 1

            if guess in word:
                print('Great! You have guessed the word correctly')

        else:
            print('The length of your guess is not as same as the length of the word')
            tries -= 1

        status = ''
        if guessed == False:
            for letters in word:
                if letters in letters_guessed:
                    status += letters
                else:
                    status += '_'

            print(status)

        if status == word:
            print('Congratulations YOU have guessed the word ')
            guessed = True

        elif tries == 0:
            print('Oops! You ran out of tries ...And You have not guessed the word ')

    play_again()


game_run()
