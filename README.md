# English-German-word-games

## Description
Word Search Bot is a Python-based program that generates and solves word search puzzles in both English and German. It creates a randomized word search grid and automatically detects hidden words using an algorithmic search method.

## Features
- Generates word search grids of customizable size
- Supports English and German language words
- Searches for words using a bot-powered algorithm
- Interactive menu for selecting language and game mode

## Requirements
- Python 3.x

## Installation
1. Clone this repository or download the script.
   ```sh
   git clone https://github.com/your-repo/English-German-word-games.git
   ```
2. Navigate to the project directory.
   ```sh
   cd English-German-word-games
   ```
3. Run the script.
   ```sh
   python English-German-word-games.py
   ```

## Game Menu

1. Fill in the Blanks: A missing letter is removed from a word, and you must guess the correct letter.
2. Word Guess: Translate a word from one language to another.
3. Word Chain: Provide a word that starts with the last letter of the previous word.
4. Hangman: Guess the letters of a hidden word before running out of attempts.
5. Word Search: Find hidden words in a generated grid.
6. Exit: Quit the game.

## How to Play
1. Run the script and choose your preferred language (English or German).
2. Choose the game from the menu.

## Example Output
```
Choose language (English/German): English
Choose a game:
1. Fill in the Blanks
2. Word Guess
3. Word Chain
4. Hangman
5. Word Search
6. Exit

Input: 1
Welcome to the Fill in the Blanks Word Game!
Fill in the blank: h_llo

Input: 2
Welcome to Word Guessing Game! Translate the English word to German.
Translate: out of date ->

Input: 3
Welcome to Word Chain Game! Each player must find a word that begins with the last letter of the previous word.
Current word: heat
Your word:

Input: 4
Welcome to Hangman Game!
Guess the word before the hangman is complete!
_ _ _ _ _

Input: 5
Generated Word Search Grid:
T O P A
E X A M
S E A R
C H B O

Bot Searching for Words...
SEARCH found at (1, 2) moving (1, 0)

Input: 6
Goodbye!
```

## Contributions
Feel free to contribute by submitting pull requests or reporting issues.


