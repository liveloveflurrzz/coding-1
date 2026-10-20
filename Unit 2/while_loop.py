# loop - a loop is a construct (special function) that repeats itself.
# in programming, a loop allows to repeat code instructions.

# there are two types of loops: for loop and while loop

# while loop - a type of loop where so long as a condition is equal
# to true it will keep running "forever."

# the keyboard is while --> do while

# syntax

#num = 4
#while 2+2 == num: # Condition --> Operations - must be TRUE
    #print("the program is running...") 
    #num = int(input("Please type in any number but 4 to stop the program"))

    # While loops will ALWAYS run unless you change the condition!
    # we can do this by writing instructions to manually change it.
    # the computer must ALWAYS complete their tasks before moving to the
    # next step

def guessingGame():
    correctAnswer=  8 
    attempts = 0
    print("WELCOME TO THE GUESSING GAME")
    print("Please type in a number between 1 and 10")
    userGuess = int(input("Please type in a number: "))
    while userGuess != correctAnswer:
        print("Sorry, incorrect. Guess again.")
        attempts+= 1
    print(attempts)
    userGuess =int(input("please try another number. "))
    print("Congrats! you guessed correctly. game over")

guessingGame()