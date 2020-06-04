from abc import ABC
from functools import total_ordering

from domain.exception import CoreError


class HandError(CoreError):
    pass


@total_ordering
class Hand(ABC):
    __slots__ = ('_weight', '_comment')

    def __init__(self, weight: int, comment: str) -> None:
        self._weight = weight
        self._comment = comment

    def __repr__(self) -> str:
        return '<{}: {}>'.format(self.__class__.__name__, str(self))

    def __str__(self) -> str:
        return self._comment

    def __eq__(self, other: 'Hand') -> bool:
        if isinstance(other, self.__class__):
            return self._weight == other._weight
        return NotImplemented

    def __gt__(self, other: 'Hand') -> bool:
        if isinstance(other, self.__class__):
            return self._weight > other._weight
        return NotImplemented

    @property
    def weight(self) -> int:
        return self._weight

    @property
    def comment(self) -> str:
        return self._comment


class HighCard(Hand):
    pass


class OnePair(Hand):
    pass


class TwoPair(Hand):
    pass


class Trips(Hand):
    pass


class Straight(Hand):
    pass


class Flush(Hand):
    pass


class FullHouse(Hand):
    pass


class Quads(Hand):
    pass


class StraightFlush(Hand):
    pass


hands = (
    HighCard, OnePair, TwoPair, Trips, Straight,
    Flush, FullHouse, Quads, StraightFlush,
)


__all__ = (
    'HandError', 'Hand', 'hands',
    'HighCard', 'OnePair', 'TwoPair', 'Trips', 'Straight',
    'Flush', 'FullHouse', 'Quads', 'StraightFlush',
)
