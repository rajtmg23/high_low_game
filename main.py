import random
import replit
from game_data import data, vs, logo

def random_data():
    """Get data from random account"""
    return random.choice(data)

def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_follower_count(a, b):
    """Check followers count between two accounts"""
    if a>b:
        return "a"
    else:
        return "b"
    
def game():
    print(logo)
    game_is_on = True
    score = 0
    account_a = random_data()
    account_b = random_data()

    while game_is_on:
        account_a = account_b
        account_b = random_data()

        while account_a == account_b:
            account_b = random_data()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Compare B: {format_data(account_b)}.")

        user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_follower = account_a["follower_count"]
        b_follower = account_b["follower_count"]
        
        replit.clear()
        print(logo)

        answer = check_follower_count(a_follower, b_follower)
        if answer == user_input:
            score += 1
            print(f"You're right! Your current score is {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_is_on = False

game()
