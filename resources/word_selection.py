import json
import random


def get_word(difficulty: str, file_path: str = ".\\resources\\words.json") -> str:
    file = load_file(file_path)
    if difficulty in file.keys():
        possible_words = file[difficulty]
        word = random.choice(possible_words)
        return word
    raise KeyError


def get_valid_input(file_path: str = ".\\resources\\valid_input.json") -> tuple:
    data = load_file(file_path)
    return tuple(data)


def load_file(file_path: str) -> any:
    # try to load file and set data, if error raise FileNotFoundError
    try:
        with open(file_path, 'r', encoding="utf-8") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        raise FileNotFoundError("Path to JSON file was not found")
    except ValueError:
        raise ValueError("Data does not meet requirements to be considered a json file")
    except OSError:
        raise OSError("Invalid file. It needs a text extension")
    except Exception as e:
        raise Exception(str(e))
