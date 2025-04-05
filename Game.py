import random

 

Easy_level_turns = 10

Hard_level_turns = 5

 

def game():

    print("Welcome to Number Guessing Game")

    print("I'm thinking a number between 1 and 100")

    answer = random.randint(1 , 100)

    turn = set_action()

    guess = 0

    while guess != answer:

        print(f"You have {turn} remaining")

        guess = int(input("Make a guess"))

        k = check_answer(guess , answer , turn)

        if k == 0:

            print("You you have reached the limit")

            return

        elif k!= 0:

            print("Guess again!")

 

def check_answer(user_guess, actual_answer, t):

    if user_guess > actual_answer:

        print("Too High")

        t -= 1

    elif user_guess < actual_answer:

        print("Too Low")

        t -= 1

    else:

        print(f"You got it! The answer was {actual_answer}")

       

def set_action ():

    level = input("Choose the difficulty level. Type 'Easy' or 'Hard':")

    if level == "Easy":

        return Easy_level_turns

    else:

        return Hard_level_turns

 

game()