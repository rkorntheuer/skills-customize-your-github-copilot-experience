
# 📘 Assignment: Games in Python

## 🎯 Objective

Build a classic Hangman game in Python to practice loops, conditionals, string manipulation, and user input handling. By the end of this assignment, you will have a playable terminal game with clear game-state updates.

## 📝 Tasks

### 🛠️ Build the Hangman Game Loop

#### Description
Create the main game flow for Hangman. The program should choose a secret word, repeatedly ask the player for letter guesses, and stop when the player wins or runs out of attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list of words.
- Display the current progress using underscores for unknown letters (for example: `_ _ _ _`).
- Ask the player to enter one letter per turn.
- Track remaining incorrect guesses and display the count after each turn.
- End the game when the full word is guessed or remaining attempts reach `0`.

### 🛠️ Improve Input Handling and Feedback

#### Description
Add user-friendly checks and messages so the game behaves clearly and consistently for valid and invalid guesses.

#### Requirements
Completed program should:

- Accept only single alphabetic characters as valid guesses.
- Prevent duplicate guesses from reducing remaining attempts.
- Show a clear message for correct guesses, incorrect guesses, and repeated guesses.
- Display a win message when the player guesses the word.
- Display a lose message with the correct word when attempts are exhausted.
