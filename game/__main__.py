from resources.states import max_number_of_tries, print_hangman_state
from resources.word_selection import get_word

import sys
import os


chosen_chars = []


def clear_console():
    os.system('cls')


def choose_char() -> str:
    possibilities = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n" "ñ", "o", "p", "q", "r", "s",
                     "t", "u", "v", "w", "x", "y", "z")
    user_input = str("Ingresa una de las letras de la palabra oculta: ")
    if user_input in chosen_chars:
        print("El carácter ingresado ya ha sido utilizado.")
    elif user_input not in chosen_chars and user_input in possibilities:
        return user_input
    else:
        print("El carácter ingresado no es permitido.")
    choose_char()


def choose_difficulty() -> str:
    possibilities = {"1": "easy", "2": "normal", "3": "hard"}
    user_input = str(input("Elige la dificultad:\n1. Fácil\n2. Normal\n3. Difícil\nRespuesta: "))
    if user_input in possibilities.keys():
        return possibilities[user_input]
    print("Debes ingresar como entrada: 1, 2 o 3. No se aceptan otras entradas.")
    choose_difficulty()


def close_app():
    clear_console()
    _ = input("Hasta la próxima, gracias por jugar.")
    sys.exit()


def draw_ui(tries: int, hidden_word: list):
    print_hangman_state(tries)
    for i in hidden_word:
        print(i, end=" ")


def run():
    clear_console()
    difficulty = choose_difficulty()
    word = get_word(difficulty)
    word_as_list = [i for i in word]
    hidden_word = ["_" for _ in word_as_list]
    tries = max_number_of_tries

    print(f"¡¡A jugar Hangman!!. Inicias con {tries} intentos.")
    while tries < max_number_of_tries:
        draw_ui(tries, hidden_word)
        chosen_char = choose_char()
        if chosen_char in word_as_list:
            chosen_chars.append(chosen_char)
        else:
            tries -= 1
    clear_console()

    while input("¿Quieres jugar de nuevo? (S/N) ").upper() == ("SI" or "S"):
        run()
    close_app()


if __name__ == "__main__":
    run()
