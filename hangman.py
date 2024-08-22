import random
hangman_words = ["PYTHON","ALGORITHM","FUNCTION","VARIABLE","LOOP","CONDITION","RECURSION","LIST","DICTIONARY","STRING","TUPLE","OBJECT","INHERITENCE","MODULE","EXCEPTION"]
def hangman_drawings(wrong_guess):
    if wrong_guess == 0:
        print("+---+")
        print("|   |")
        print("    |")
        print("    |")
        print("    |")
        print("    |")
        print("=========")
    elif wrong_guess == 1:
        print("+---+")
        print("|   |")
        print("O   |")
        print("    |")
        print("    |")
        print("    |")
        print("=========")
    elif wrong_guess == 2:
        print("+---+")
        print("|   |")
        print("O   |")
        print("|   |")
        print("    |")
        print("    |")
        print("=========")
    elif wrong_guess == 3:
        print("+---+")
        print("|   |")
        print("O   |")
        print("/|   |")
        print("    |")
        print("    |")
        print("=========")
    elif wrong_guess == 4:
        print("+---+")
        print("|   |")
        print("O   |")
        print("/|\\  |")
        print("/    |")
        print("    |")
        print("=========")
    elif wrong_guess == 5:
        print("+---+")
        print("|   |")
        print("O   |")
        print("/|\\  |")
        print("/ \\  |")
        print("    |")
        print("=========")
    elif wrong_guess == 6:
        print("+---+")
        print("|   |")
        print("O   |")
        print("/|\\  |")
        print("/ \\  |")
        print("    |")
        print("=========")
        print("Game Over!")
    else:
        print("Invalid stage number.")
def hangman():
    print("Welcome To Hangman!!")
    print("RULES OF GAME!!")
    print("1.Try to guess the hidden word by suggesting one letter at a time.")
    print("2. If your guessed letter is not in the word, a part of the hangman figure will be drawn.")
    print("3.You win if you guess all the letters in the word before the hangman figure is completely drawn.")
    print("4.You lose if the hangman figure is fully drawn before you guess the word.")
    print("5.You can only guess one letter at a time, and each letter can only be guessed once.")
    print("6.If your guessed letter is in the word, it will be revealed in its correct position(s).")
    print("7. A to Z are allowed as valid inputs!!")
    print("8. Duplicate Letters Will Be Revealed All At Once")
    print("9. Don't Enter Duplicate Letters")
    print("10. Don't Enter A Single Letter More Than 1 Times.")
    req_word = random.choice(hangman_words)
    user_word = []
    for i in range(0,(len(req_word))):
        user_word.append("_")
    wrong_guess = 0
    while ((''.join(user_word))!=req_word):
        if(wrong_guess==6):
            print("\nYou Lost!!")
            print("Hangman: ")
            hangman_drawings(6)
            return
        user_input = input("\nEnter Letter: ")
        if(req_word.find(user_input)==(-1)):
            print("\nIncorrect Guess")
            print("A Part Will be added to Hangman")
            wrong_guess+=1
            print("Hangman: ")
            hangman_drawings(wrong_guess)
            print("Current Word ->",(''.join(user_word)))
        elif(req_word.find(user_input)!=(-1)):
            print("\nCorrect Guess")
            for i in range(0,(len(user_word))):
                if(user_input==req_word[i]):
                    user_word[i]=req_word[i]
            print("Current Word:",(''.join(user_word)))
        if((''.join(user_word))==req_word):
            print("You Win!!")
            print("Yes!!,You are right!")
            print("Correct Word Is",req_word)
            return
hangman()