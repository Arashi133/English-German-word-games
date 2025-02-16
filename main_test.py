import random
import time
import string
from pprint import pprint
import json
from pathlib import Path
from datetime import datetime

def load_words_from_file():
    """Load words from file and create dictionaries for both languages"""
    words = {"english": {}, "german": {}}
    
    with open("input_german.txt", "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(": ")
            if len(parts) == 2:
                german_word, english_word = parts
                words["german"][english_word] = german_word  # German -> English
                words["english"][german_word] = english_word  # English -> German
    
    return words

def get_words_and_translations(language):
    """Get words and their translations for the given language"""
    words = load_words_from_file()
    if language.lower() == "german":
        return words["german"]  # German words -> English translations
    else:
        return words["english"]  # English words -> German translations

def insert_random_blank(word):
    """Insert a random blank in the word and return the modified word and correct letter"""
    if len(word) <= 1:
        return word, word
    blank_index = random.randint(0, len(word) - 1)
    return word[:blank_index] + "_" + word[blank_index + 1:], word[blank_index]

def fill_the_blanks(language):
    """Play fill in the blanks game in the selected language"""
    word_dict = get_words_and_translations(language)
    available_words = list(word_dict.keys())  # Words in selected language
    
    if language.lower() == "german":
        welcome_msg = "Willkommen zum Lückentext-Spiel!"
        fill_msg = "Fülle die Lücke aus:"
        your_answer_msg = "Deine Antwort:"
        correct_msg = "Richtig!\n"
        wrong_msg = "Falsch! Die richtige Antwort war"
        game_over_msg = "Spiel vorbei! Dein Endergebnis:"
    else:
        welcome_msg = "Welcome to the Fill in the Blanks Word Game!"
        fill_msg = "Fill in the blank:"
        your_answer_msg = "Your answer:"
        correct_msg = "Correct!\n"
        wrong_msg = "Wrong! The correct answer was"
        game_over_msg = "Game over! Your final score:"
    
    score = 0
    print(welcome_msg)
    
    for _ in range(5):
        word = random.choice(available_words)
        question, correct_answer = insert_random_blank(word)
        print(f"{fill_msg} {question}")
        player_answer = input(f"{your_answer_msg} ").strip().lower()
        
        if player_answer == correct_answer.lower():
            print(correct_msg)
            score += 1
        else:
            print(f"{wrong_msg} {correct_answer}\n")
    
    print(f"{game_over_msg} {score}/5")

def play_word_guess(language):
    """Play word guessing game in the selected language"""
    word_dict = get_words_and_translations(language)
    available_words = list(word_dict.keys())  # Words in selected language
    
    if language.lower() == "german":
        prompt = "Übersetze das deutsche Wort ins Englische"
        correct_msg = "Richtig!"
        wrong_msg = "Falsch. Die richtige Antwort ist:"
        play_again_msg = "Möchtest du weiterspielen? (ja/nein): "
        thanks_msg = "Danke fürs Spielen!"
        continue_word = "ja"
    else:
        prompt = "Translate the English word to German"
        correct_msg = "Correct!"
        wrong_msg = "Wrong. The correct answer is:"
        play_again_msg = "Do you want to play again? (yes/no): "
        thanks_msg = "Thanks for playing!"
        continue_word = "yes"
    
    print(f"Welcome to Word Guessing Game! {prompt}.")
    
    while True:
        word = random.choice(available_words)
        correct_translation = word_dict[word]
        
        user_guess = input(f"Translate: {word} -> ")
        
        if user_guess.lower() == correct_translation.lower():
            print(correct_msg)
        else:
            print(f"{wrong_msg} {correct_translation}")
        
        play_again = input(play_again_msg)
        if play_again.lower() != continue_word:
            print(thanks_msg)
            break

def play_word_chain(language):
    """Play word chain game in the selected language"""
    word_dict = get_words_and_translations(language)
    available_words = list(word_dict.keys())  # Words in selected language
    
    if language.lower() == "german":
        welcome_msg = "Willkommen zum Wortketten-Spiel! Jeder Spieler muss ein Wort finden, das mit dem letzten Buchstaben des vorherigen Wortes beginnt."
        current_word_msg = "Aktuelles Wort:"
        your_word_msg = "Dein Wort:"
        game_end_msg = "Spiel beendet."
        used_word_msg = "Dieses Wort wurde bereits verwendet!"
        must_begin_msg = "Das Wort muss mit"
        begin_msg_end = "beginnen!"
        not_in_list_msg = "Dieses Wort ist nicht in der Liste!"
    else:
        welcome_msg = "Welcome to Word Chain Game! Each player must find a word that begins with the last letter of the previous word."
        current_word_msg = "Current word:"
        your_word_msg = "Your word:"
        game_end_msg = "Game over."
        used_word_msg = "This word has already been used!"
        must_begin_msg = "The word must begin with"
        begin_msg_end = "!"
        not_in_list_msg = "This word is not in the list!"
    
    print(welcome_msg)
    
    used_words = set()
    current_word = random.choice(available_words)
    used_words.add(current_word)
    
    while True:
        print(f"{current_word_msg} {current_word}")
        user_input = input(f"{your_word_msg} ").strip().lower()
        
        if not user_input:
            print(game_end_msg)
            break
        
        if user_input in used_words:
            print(used_word_msg)
            continue
        
        if user_input[0].lower() != current_word[-1].lower():
            print(f"{must_begin_msg} '{current_word[-1]}' {begin_msg_end}")
            continue
        
        if user_input not in [word.lower() for word in available_words]:
            print(not_in_list_msg)
            continue
        
        used_words.add(user_input)
        current_word = random.choice([word for word in available_words if (word.lower() not in used_words) and (word[0].lower() == user_input[-1].lower())])

def hang_man(language):
    """Play hangman game in the selected language"""
    word_dict = get_words_and_translations(language)
    hang_man_art = {0: ("   ",
                        "   ",
                        "   "),
                    1: (" o ",
                        "   ",
                        "   "),
                    2: (" o ",
                        " | ",
                        "   "),
                    3: (" o ",
                        "/| ",
                        "   "),
                    4: (" o ",
                        "/|\\"
                        "   "),
                    5: (" o ",
                        "/|\\",
                        "/  "),
                    6: (" o ",
                        "/|\\",
                        "/ \\")}
    
    if language.lower() == "german":
        print("Willkommen zum Galgenmännchen-Spiel!")
        print("Errate das Wort, bevor das Galgenmännchen fertig ist!")
        guesses_left = "Verbleibende Versuche:"
        guess_prompt = "Rate einen Buchstaben:"
        already_guessed = "Bereits geratene Buchstaben:"
        win_msg = "Glückwunsch! Du hast gewonnen!"
        lose_msg = "Spiel vorbei! Das Wort war:"
    else:
        print("Welcome to Hangman Game!")
        print("Guess the word before the hangman is complete!")
        guesses_left = "Remaining guesses:"
        guess_prompt = "Guess a letter:"
        already_guessed = "Letters already guessed:"
        win_msg = "Congratulations! You won!"
        lose_msg = "Game over! The word was:"
    
    word = random.choice(list(word_dict.keys())).lower()
    word_letters = set(word)
    alphabet = set(string.ascii_lowercase)
    used_letters = set()
    
    lives = 6
    wrong = 0
    def display_hangman(wrong):
        for line in hang_man_art[wrong]:
            print(line)
    
    while len(word_letters) > 0 and lives > 0:
        print(f"\n{guesses_left} {lives}")
        print(f"{already_guessed} {' '.join(used_letters)}")
        
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print(' '.join(word_list))
        
        user_letter = input(f"{guess_prompt} ").lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                wrong = wrong + 1
                display_hangman(wrong)
        
    if lives == 0:
        print(f"{lose_msg} {word}")
    else:
        print(f"{win_msg}")

def word_search(language):
    """Create and play word search puzzle"""
    word_dict = get_words_and_translations(language)
    words = [random.choice(list(word_dict.keys())).upper().replace("'", '').strip() for _ in range(5)]
    
    grid_size = 20
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
    
    def print_grid():
        for row in grid:
            print('\t' * 5 + ' '.join(row))
    
    def word_search_bot(grid, words):
        found_words = {}
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for word in words:
            word_length = len(word)
            for x in range(len(grid)):
                for y in range(len(grid[x])):
                    for dx, dy in directions:
                        try:
                            check_word = ''.join(grid[x + i * dx][y + i * dy] for i in range(word_length))
                            if check_word == word:
                                found_words[word] = (x, y, dx, dy)
                        except IndexError:
                            continue
        return found_words
    
    orientations = ['leftright', 'updown', 'diagonalup', 'diagonaldown']
    
    for word in words:
        word_length = len(word)
        placed = False
        
        while not placed:
            orientation = random.choice(orientations)
            
            if orientation == 'leftright':
                step_x, step_y = 1, 0
            elif orientation == 'updown':
                step_x, step_y = 0, 1
            elif orientation == 'diagonalup':
                step_x, step_y = 1, 1
            elif orientation == 'diagonaldown':
                step_x, step_y = 1, -1
                
            x_position = random.randint(0, grid_size - word_length)
            y_position = random.randint(0, grid_size - word_length)
            
            failed = False
            
            for i in range(word_length):
                character = word[i]
                new_x = x_position + i * step_x
                new_y = y_position + i * step_y
                
                if new_x < 0 or new_x >= grid_size or new_y < 0 or new_y >= grid_size:
                    failed = True
                    break
                    
                character_at_location = grid[new_y][new_x]  # Note: Swapped x and y
                
                if character_at_location != ' ' and character_at_location != character:
                    failed = True
                    break
            
            if not failed:
                for i in range(word_length):
                    character = word[i]
                    new_x = x_position + i * step_x
                    new_y = y_position + i * step_y
                    grid[new_y][new_x] = character  # Note: Swapped x and y
                placed = True
    
    # Fill empty spaces with random letters
    for y in range(grid_size):
        for x in range(grid_size):
            if grid[y][x] == ' ':
                if language.lower() == "german":
                    grid[y][x] = random.choice(string.ascii_uppercase + 'ÄÖÜß')
                else:
                    grid[y][x] = random.choice(string.ascii_uppercase)
    
    if language.lower() == "german":
        print("Willkommen zum Wort-Suchspiel!")
        print("Finde die versteckten Wörter in diesem Rätsel:")
        print(", ".join(words))
        print("Die Wörter können horizontal, vertikal oder diagonal versteckt sein.")
        print("Viel Spaß!")
        print_grid()
        print("\nBot sucht nach Wörtern...")
        
        start_time = time.time()
        found = word_search_bot(grid, words)
        end_time = time.time()
        search_time = end_time - start_time
        
        for word, (x, y, dx, dy) in found.items():
            print(f"{word} gefunden bei ({x}, {y}) in Richtung ({dx}, {dy})")
        print(f"\nSuchzeit: {search_time:.2f} Sekunden")
        
    else:
        print("Welcome to the Word Search Game!")
        print("Find these hidden words in the puzzle:")
        print(", ".join(words))
        print("The words can be hidden horizontally, vertically, or diagonally.")
        print("Have fun!")
        print_grid()
        print("\nBot Searching for Words...")
        
        start_time = time.time()
        found = word_search_bot(grid, words)
        end_time = time.time()
        search_time = end_time - start_time
        
        for word, (x, y, dx, dy) in found.items():
            print(f"{word} found at ({x}, {y}) moving ({dx}, {dy})")
        print(f"\nSearch time: {search_time:.2f} seconds")

def menu():
    """Main menu for language and game selection"""
    while True:
        language = input("Choose language (English/German): ").lower()
        if language not in ["english", "german"]:
            print("Invalid language choice. Please try again.")
            continue
            
        if language == "german":
            print("\nWähle ein Spiel:")
            print("1. Lückentext")
            print("2. Wort-Ratespiel")
            print("3. Wortketten-Spiel")
            print("4. Galgenmännchen")
            print("5. Wort-Suche")
            print("6. Beenden")
        
            choice = input("\nEingabe: ")
        else:
            print("\nChoose a game:")
            print("1. Fill in the Blanks")
            print("2. Word Guess")
            print("3. Word Chain")
            print("4. Hangman")
            print("5. Word Search")
            print("6. Exit")
            
            choice = input("\nInput: ")
        
        if choice == "1":
            fill_the_blanks(language)
        elif choice == "2":
            play_word_guess(language)
        elif choice == "3":
            play_word_chain(language)
        elif choice == "4":
            hang_man(language)
        elif choice == "5":
            word_search(language)
        elif choice == "6":
            if language == "german":
                print("Auf Wiedersehen!")
            else:
                print("Goodbye!")
            break
        else:
            if language == "german":
                print("Ungültige Eingabe. Bitte erneut versuchen.")
            else:
                print("Invalid input. Please input again.") 

if __name__ == "__main__":
    menu()