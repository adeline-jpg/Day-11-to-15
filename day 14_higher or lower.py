#print art
from day_14_game_data import data
import random
print(logo)
score = 0

def format_data(account):
    """Takes the account data and returns the printable format"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(user_answer, a_followers, b_followers):
    """Take a user's guess and the followers count and returns if they got it right"""
    if a_followers > b_followers:
        if user_answer == "a":
            return True
        else:
            return False
    if a_followers < b_followers:
        if user_answer == "b":
            return True
        else:
            return False
                               

account_b = random.choice(data)
game_should_continue = True
while game_should_continue: # make the game repeatable.
    #generate random accounts
    # making account position B become the next account at position A
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    #ask user for a guess
    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    #clear the screen
    print("\n" *20)
    print(logo)

    #check the answer if the user is correct
    ## get follow account of each account
    a_follower = account_a["follower_count"]
    b_follower = account_b["follower_count"]
    is_correct = check_answer (user_answer, a_follower, b_follower)


    # give user feedback of their guess
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry that's wrong. Final score: {score}")
        game_should_continue = False

    # track user score
