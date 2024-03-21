import random
import logging

logging.basicConfig(filename='number_guesser.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def get_user_input(prompt, input_type=int):
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print(f"Please enter a valid {input_type.__name__}.")

def choose_difficulty():
    levels = {'easy': (1, 10, 10), 'medium': (1, 50, 7), 'hard': (1, 100, 5), 'custom': None}
    choice = input("Choose difficulty (easy, medium, hard, custom): ").lower()
    if choice == 'custom':
        low = get_user_input("Enter the lower bound: ", int)
        high = get_user_input("Enter the upper bound: ", int)
        attempts = get_user_input("Enter the number of attempts: ", int)
        return (low, high, attempts)
    return levels.get(choice, levels['easy'])

def offer_hint(guesses, number):
    if len(guesses) >= 3:
        hint = "even" if number % 2 == 0 else "odd"
        print(f"Hint: The number is {hint}.")

def update_leaderboard(leaderboard, difficulty, attempts):
    if difficulty not in leaderboard or attempts < leaderboard[difficulty]:
        print("Congratulations! You've set a new high score for this difficulty!")
        leaderboard[difficulty] = attempts

def play_game(leaderboard):
    low, high, max_attempts = choose_difficulty()
    number = random.randint(low, high)
    attempts = 0
    guesses = []

    print(f"Guess the number between {low} and {high}. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        guess = get_user_input(f"Attempt {attempts + 1}/{max_attempts}. Enter your guess: ")
        attempts += 1
        guesses.append(guess)

        if guess == number:
            print(f"Congratulations! You've guessed the number in {attempts} attempts!")
            logging.info(f"Success - Attempts: {attempts}, Number: {number}, Guesses: {guesses}")
            update_leaderboard(leaderboard, f"{low}-{high}-{max_attempts}", attempts)
            break
        elif guess < number:
            print("Too low.")
        else:
            print("Too high.")

        if attempts % 3 == 0:
            offer_hint(guesses, number)

    if attempts == max_attempts:
        print(f"Out of attempts! The number was {number}.")
        logging.info(f"Fail - Number: {number}, Guesses: {guesses}")

def main():
    leaderboard = {}
    while get_user_input("Play Number Guesser? (yes=1/no=0): ", int) == 1:
        play_game(leaderboard)
        print("Current Leaderboard:", leaderboard)
        logging.info(f"Leaderboard: {leaderboard}")

if __name__ == "__main__":
    main()
