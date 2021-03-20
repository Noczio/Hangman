class SelectedLetters:
    _selected: list = []
    _current_index: int = 0
    __instance = None

    @staticmethod
    def get_instance() -> "SelectedLetters":
        """Static access method."""
        if SelectedLetters.__instance is None:
            SelectedLetters()
        return SelectedLetters.__instance

    def __init__(self) -> None:
        """Virtually private constructor."""
        if SelectedLetters.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            SelectedLetters.__instance = self

    def __getitem__(self, key: int) -> any:
        if (key < len(self._selected)) and (key >= -len(self._selected)):
            return self._selected[key]
        raise KeyError

    def add(self, value: any) -> None:
        self.__setitem__(value)

    def __setitem__(self, value: any) -> any:
        self._selected.append(value)

    def __iter__(self) -> any:
        return iter(self._selected)

    def __next__(self) -> any:
        if len(self._selected) > 0:
            if self._current_index > len(self._selected):
                self._current_index = 0
                return self._selected[self._current_index]
            else:
                out_put = self._selected[self._current_index]
                self._current_index += 1
                return out_put

    @classmethod
    def reset(cls) -> None:
        cls._current_index = 0
        cls._selected = []
