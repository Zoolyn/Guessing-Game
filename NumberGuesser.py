from random import *
import sys

while True:
    print("Welcome to the Number Guessing game!")
    while True:
        #minNum
        minNum = input("Please type the min of numbers you want to guess \n")
        try:
            minVal = int(minNum)
            break
        except ValueError:
            print("That's not an int!")

    while True:
        #maxNum
        maxNum = input("Please type the max of numbers you want to guess \n")
        try:
            maxVal = int(maxNum)
            break
        except ValueError:
            print("That's not an int!")

    answer = randint(minVal, maxVal)
    print(answer)
               
    game = input("Type 'endless' or 'number' to select game type \n")
    

    if game.lower() == 'endless':
        #ENDLESS MODE WHERE YOU CAN GUESS UNTIL YOU GET THE NUMBER
        print("ENDLESS MODE, you get an endless number of guesses!")

        while True:
            while True:
                guess = input("What is your guess? \n")
                try:
                   guessVal = int(guess)
                   break
                except ValueError:
                   print("That's not an int!")
            if guessVal < answer:
                print("Your guess was too low!")
            elif guessVal > answer:
                print("Your guess was too high!")
            else:
                print("THAT'S THE CORRECT GUESS")
                break

        #play-again
        end = input("Would you like to play again? yes/no \n")
        if end == 'no':
            sys.exit()
        elif end == 'yes':
            continue;
        else:
            print("Incorrect input!")
            x = input("Would you like to play again? yes/no \n")
            while True:
                if x == 'no':
                    sys.exit()
                elif x == 'yes':
                    break;
                else:
                    print("Incorrect input!")
                    x = input("Would you like to play again? yes/no \n")
                    
    #this is for only having a cetain amount of guesses    
    elif game.lower() == 'number':
        print("NUMBER MODE, you get a certain amount of guesses")
        
        while True:
            numOfGuess = input("How many guesses would you like?")
            try:
                numOfGuessVal = int(numOfGuess)
                break
            except ValueError:
                print("That's not an int!")
        for i in range(1,numOfGuessVal):
            while True:
                guess = input("What is your guess? \n")
                try:
                   guessVal = int(guess)
                   break
                except ValueError:
                   print("That's not an int!")
            if guessVal > answer:
                print("Your guess was too high")
                if (i+1) == numOfGuessVal:
                    print("YOU RAN OUT OF GUESSES, YOU LOSE!")
            elif guessVal < answer:
                print("Your guess was too low")
                if (i+1) == numOfGuessVal:
                    print("YOU RAN OUT OF GUESSES, YOU LOSE!")
            else:
                print("THAT'S THE CORRECT GUESS!")
                break
                
        #play-again
        end = input("Would you like to play again? yes/no \n")
        if end == 'no':
            break;
        elif end == 'yes':
            continue;
        else:
            print("Incorrect input!")
            x = input("Would you like to play again? yes/no \n")
            while True:
                if x == 'no':
                    sys.exit();
                elif x == 'yes':
                    break;
                else:
                    print("Incorrect input!")
                    x = input("Would you like to play again? yes/no \n")
        
    else:
        print("That is not a correct input!")
