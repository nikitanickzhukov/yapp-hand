from abc import ABC

from domain.exception import CoreError


class CardError(CoreError):
    pass


class Prop(ABC):
    __slots__ = ('_code', '_name')

    def __init__(self, code: str, name: str) -> None:
        self._code = code
        self._name = name

    def __str__(self) -> str:
        return self._code

    def __repr__(self) -> str:
        return '<{}: {}>'.format(self.__class__.__name__, self._name)

    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name


class Rank(Prop):
    pass


class Suit(Prop):
    pass


class Card:
    __slots__ = ('_rank', '_suit')

    def __init__(self, rank: Rank, suit: Suit) -> None:
        self._rank = rank
        self._suit = suit

    def __str__(self) -> str:
        return self.code

    def __repr__(self) -> str:
        return '<{}: {}>'.format(self.__class__.__name__, self.code)

    @property
    def rank(self) -> Rank:
        return self._rank

    @property
    def suit(self) -> Suit:
        return self._suit

    @property
    def code(self) -> str:
        return self._rank.code + self._suit.code

    @property
    def name(self) -> str:
        return '{} of {}'.format(self._rank.name, self._suit.name)


ranks = (
    Rank(code='A', name='ace'),
    Rank(code='2', name='deuce'),
    Rank(code='3', name='trey'),
    Rank(code='4', name='four'),
    Rank(code='5', name='five'),
    Rank(code='6', name='six'),
    Rank(code='7', name='seven'),
    Rank(code='8', name='eight'),
    Rank(code='9', name='nine'),
    Rank(code='T', name='ten'),
    Rank(code='J', name='jack'),
    Rank(code='Q', name='queen'),
    Rank(code='K', name='king'),
)
suits = (
    Suit(code='s', name='spades'),
    Suit(code='h', name='hearts'),
    Suit(code='d', name='diamonds'),
    Suit(code='c', name='clubs'),
)
cards = tuple(
    Card(rank=r, suit=s) for s in suits for r in ranks
)


__all__ = ('CardError', 'Rank', 'Suit', 'Card', 'ranks', 'suits', 'cards')
