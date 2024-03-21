# Number-Guesser

The Number Guesser game is a simple console application written in Python that challenges players to guess a randomly selected number within a specified range and number of attempts. Players can choose from predefined difficulty levels or create a custom game setting.

## Features

- **Multiple Difficulty Levels**: Players can choose from easy, medium, hard, or custom difficulty levels.
- **Hints**: After every three incorrect guesses, the game provides a hint indicating whether the target number is odd or even.
- **Leaderboard**: Records and updates high scores for each difficulty setting.
- **Logging**: The game logs all attempts, including successful guesses and failures, to a file for future reference.

## Requirements

- Python 3.x
- No external libraries are required.

## Usage

1. **Start the Game**: Run the script in a Python 3 environment.
2. **Select Difficulty**: Choose between easy, medium, hard, or custom difficulty levels. For custom levels, you will be prompted to enter the range and number of attempts.
3. **Guess the Number**: Enter your guesses based on the game's prompts. The game will inform you if your guess is too high or too low.
4. **Hints**: Use the hints provided after every three wrong guesses to narrow down your target.
5. **Leaderboard and Logging**: Achieve a high score to be featured on the leaderboard. All game sessions are logged for review.

## Customizing Difficulty

- **Easy**: Range 1-10 with 10 attempts.
- **Medium**: Range 1-50 with 7 attempts.
- **Hard**: Range 1-100 with 5 attempts.
- **Custom**: Set your own range and number of attempts.

## Logging

All game outcomes, including the number of attempts, the target number, and the guesses, are logged to `number_guesser.log`.

## Leaderboard

The game maintains a leaderboard for the lowest number of attempts needed to guess the number for each difficulty setting. Setting a new high score will update the leaderboard accordingly.

---

Enjoy the Number Guesser game and challenge yourself to set new high scores across all difficulty levels!
