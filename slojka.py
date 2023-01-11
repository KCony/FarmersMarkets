from enum import Enum


class States(Enum):
    Easy = 'Easy'
    Normal = 'Noraml'
    Difficult = 'Difficult'




class StateMacine():
    def __init__(self):
        self._state = None
    def set_state(self, state):
        if not isinstance(state, States):
            print("Выбранная неверная сложность")
            return
        self._state = state
        print(self._state)
    def get_state(self):
        return self._state