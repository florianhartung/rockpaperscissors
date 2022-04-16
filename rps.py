from enum import Enum


class RPSOutcome(Enum):
    WIN = 1
    LOSS = 2
    TIE = 3


class RPSObject:
    def __init__(self, name: str):
        self.name = name
        self.wins_against = []
        self.looses_against = []

    def __gt__(self, other) -> RPSOutcome:
        if other.name in self.wins_against:
            return RPSOutcome.WIN
        elif other.name in self.looses_against:
            return RPSOutcome.LOSS
        else:
            return RPSOutcome.TIE

    def __rshift__(self, other):
        self.wins_against.append(other.name)
        other.looses_against.append(self.name)
