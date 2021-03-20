import os
import sys

from game.global_var import SelectedLetters
from resources.states import max_number_of_tries
from resources.states import print_hangman_state
from resources.word_selection import get_word, get_valid_input


def clear_console() -> None:
    os.system('cls')


def choose_char() -> str:
    selected_letters = SelectedLetters.get_instance()
    possibilities = get_valid_input()
    user_input = input("Type down a letter: ").lower()
    if user_input in selected_letters:
        print("Selected character has been previously used")
    elif user_input not in selected_letters and user_input in possibilities:
        return user_input
    else:
        print("Input is not valid")


def choose_difficulty() -> str:
    clear_console()
    possibilities = {"1": "easy", "2": "normal", "3": "hard"}
    user_input = input("Choose the game's difficulty:\n1. Easy\n2. Normal\n3. Hard\n\nAnswer: ").lower()
    if user_input in possibilities.keys():
        return possibilities[user_input]
    elif user_input in possibilities.values():
        return user_input
    print("\nInput must be: 1, 2, 3, easy, normal or hard\n")


def close_app() -> None:
    clear_console()
    _ = input("See you next time, thanks for playing!.")
    sys.exit()


def draw_ui(tries: int, hidden_word: list) -> None:
    clear_console()
    print_hangman_state(tries)
    for counter, i in enumerate(hidden_word):
        if counter == 0:
            print(f"\t\t{i}", end=" ")
        else:
            print(i, end=" ")
    print(f"\n\nYou've got {tries} tries left.")


def update_hidden_word(character: str, hidden_word: list, word: list) -> list:
    for counter, char in enumerate(word):
        if char == character:
            hidden_word[counter] = char
    return hidden_word


def run() -> None:
    # load global var
    selected_letters = SelectedLetters.get_instance()
    # choose a difficulty. Easy, normal or hard
    while True:
        difficulty = choose_difficulty()
        if difficulty is not None:
            break
    # get random word from json file by difficulty
    word = get_word(difficulty)
    # initialize word as a list, hidden_word, total tries and win condition var
    word_as_list = [char for char in word]
    hidden_word = ["_" for i in word_as_list]
    tries = max_number_of_tries
    player_win = False

    # game logic
    print(f"Let's play Hangman!!")
    while tries - 1 > 0:
        # if there are enough tries keep playing
        draw_ui(tries - 1, hidden_word)
        # get user input if tries are still greater than 0
        while True:
            chosen_char = choose_char()
            if chosen_char is not None:
                break
        # is user input one or more of the hidden letters?
        if chosen_char in word_as_list:
            # add letter as previously used, so it cannot be entered again
            selected_letters.add(chosen_char)
            # update hidden_word with last input
            hidden_word = update_hidden_word(chosen_char, hidden_word, word_as_list)
            # check if player won
            if hidden_word == word_as_list:
                # player won the game. Break while condition and set player_win to True
                player_win = True
                draw_ui(tries - 1, hidden_word)
                break
        else:
            # player missed a hidden letter. number of tries decreases by one
            selected_letters.add(chosen_char)  # add letter as previously used, so it cannot be entered again
            tries -= 1

    # if player won game set adaptive_final_msg to "won" else to "lost"
    if player_win:
        adaptive_final_msg = "won"
    else:
        # show one last time the hangman ui
        draw_ui(0, hidden_word)
        adaptive_final_msg = "lost"
        print(f"\nThe word was {word}.")

    while True:
        continue_game = input(f"\nYou {adaptive_final_msg} ¿Do you want to play again? (Y/N): ").lower()
        if continue_game == "yes" or continue_game == "y":
            # game will continue. Reset selected_letters to default and run the game again
            selected_letters.reset()
            run()
        elif continue_game == "no" or continue_game == "n":
            # user confirmed that they want to stop playing. Close app
            break
        else:
            print("Wrong input. It must be: yes, no, y or n")
    close_app()


if __name__ == "__main__":
    run()
