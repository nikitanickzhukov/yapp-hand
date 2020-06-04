from abc import ABC

from domain.exception import CoreError


class GameError(CoreError):
    pass


class Game(ABC):
    min_pocket_size = 0
    max_pocket_size = 0
    min_board_size = 0
    max_board_size = 0
    hand_size = 0
    is_high_low = False


class Holdem(Game):
    min_pocket_size = 2
    max_pocket_size = 2
    min_board_size = 3
    max_board_size = 5
    hand_size = 5


class Omaha(Game):
    min_pocket_size = 4
    max_pocket_size = 4
    min_board_size = 3
    max_board_size = 5
    hand_size = 5


class OmahaHighLow(Game):
    min_pocket_size = 4
    max_pocket_size = 4
    min_board_size = 3
    max_board_size = 5
    hand_size = 5
    is_high_low = True


class Razz(Game):
    min_pocket_size = 5
    max_pocket_size = 7
    hand_size = 5


class Stud(Game):
    min_pocket_size = 5
    max_pocket_size = 7
    hand_size = 5


class StudHighLow(Game):
    min_pocket_size = 5
    max_pocket_size = 7
    hand_size = 5
    is_high_low = True


class StudNoQ(Game):
    min_pocket_size = 5
    max_pocket_size = 7
    hand_size = 5
    is_high_low = True


class Draw(Game):
    min_pocket_size = 5
    max_pocket_size = 5
    hand_size = 5


class Badugi(Game):
    min_pocket_size = 4
    max_pocket_size = 4
    hand_size = 4


class LowballA5(Game):
    min_pocket_size = 5
    max_pocket_size = 5
    hand_size = 5


class Lowball27(Game):
    min_pocket_size = 5
    max_pocket_size = 5
    hand_size = 5


class TripleLowballA5(Game):
    min_pocket_size = 5
    max_pocket_size = 5
    hand_size = 5


class TripleLowball27(Game):
    min_pocket_size = 5
    max_pocket_size = 5
    hand_size = 5


games = (
    Holdem, Omaha, OmahaHighLow, Razz,
    Stud, StudHighLow, StudNoQ, Draw, Badugi,
    LowballA5, Lowball27, TripleLowballA5, TripleLowball27,
)


__all__ = (
    'GameError', 'Game', 'games',
    'Holdem', 'Omaha', 'OmahaHighLow', 'Razz',
    'Stud', 'StudHighLow', 'StudNoQ', 'Draw', 'Badugi',
    'LowballA5', 'Lowball27', 'TripleLowballA5', 'TripleLowball27',
)
