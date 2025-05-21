import random

EASYLIVES = 10
HARDLIVES = 5
def lives():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASYLIVES
    else:
        return HARDLIVES

chosen_number = random.randint(1, 100)

def check_answer(guess, chosen_number, attempts): #needed the inputs otherwise it would not be defined within the function

    if guess > chosen_number:
        print("Too High")
        return attempts - 1
    if guess < chosen_number:
        print("Too Low")
        return attempts - 1
    if guess == chosen_number:
        print("you're right!")


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    game_over = False
    attempts = lives() # why did I have to store it in a variable, so that you can grab the number. 
    while not game_over:
        print(f"You have {attempts} remaining to guess the number")
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, chosen_number,attempts)  ## why did I have to store it in a different variable?, because when you got back into the loop it's -1
        if guess != chosen_number:
            print("Guess again.")
        if attempts == 0:
            print(f"You've lost, the answer was {chosen_number}")
            game_over = True
        if guess == chosen_number:
            game_over = True


game()