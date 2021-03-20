import sys
import os

from resources.states import print_hangman_state
from resources.states import max_number_of_tries
from resources.word_selection import get_word

chosen_chars = []


def clear_console() -> None:
    os.system('cls')


def choose_char() -> str:
    possibilities = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                     "t", "u", "v", "w", "x", "y", "z")
    user_input = input("Type down a letter: ")
    if user_input in chosen_chars:
        print("Selected character has been previously used")
    elif user_input not in chosen_chars and user_input in possibilities:
        return user_input
    else:
        print("Input is not valid")
    choose_char()


def choose_difficulty() -> str:
    possibilities = {"1": "easy", "2": "normal", "3": "hard"}
    user_input = input("Choose the game's difficulty:\n1. Easy\n2. Normal\n3. Hard\nAnswer: ")
    if user_input.lower() in possibilities.keys():
        return possibilities[user_input]
    elif user_input.lower() in possibilities.values():
        return user_input.lower()
    print("\nInput must be: 1, 2, 3, easy, normal or hard\n")
    choose_difficulty()


def close_app() -> None:
    clear_console()
    _ = input("See you next time, thanks for playing!.")
    sys.exit()


def draw_ui(tries: int, hidden_word: list) -> None:
    clear_console()
    print_hangman_state(tries)
    for i in hidden_word:
        print(i, end=" ")
    print(f"\nYou've got {tries} tries.")


def run() -> None:
    clear_console()
    difficulty = choose_difficulty()
    word = get_word(difficulty, ".\\resources\\words.json")
    word_as_list = [i for i in word]
    hidden_word = ["_" for _ in word_as_list]
    tries = max_number_of_tries
    player_win = False

    print(f"Let's play Hangman!!")
    while tries > 0:
        draw_ui(tries-1, hidden_word)
        chosen_char = choose_char()
        if chosen_char in word_as_list:
            chosen_chars.append(chosen_char)
            # update hidden_word
            # check if player won
            player_win = True if hidden_word == word_as_list else False
        else:
            tries -= 1

    adaptive_final_msg = "won" if player_win else "lost"
    while input(f"You {adaptive_final_msg} ¿Do you want to play again? (Y/N) ").lower() == ("yes" or "y"):
        run()
    close_app()


if __name__ == "__main__":
    run()
