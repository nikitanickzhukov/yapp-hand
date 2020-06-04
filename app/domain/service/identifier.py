from abc import ABC, abstractmethod
from typing import Sequence, Type

from domain.model.game import Game
from domain.model.hand import Hand
from domain.model.card import Card
from domain.exception import CoreError


class IdentifierError(CoreError):
    pass


class Identifier(ABC):
    @classmethod
    @abstractmethod
    def identify(cls, game_class: Type[Game], pocket_cards: Sequence[Card], board_cards: Sequence[Card]) -> Hand:
        pass

    @classmethod
    def check_params(cls, game_class: Type[Game], pocket_cards: Sequence[Card], board_cards: Sequence[Card]) -> None:
        if len(pocket_cards) < game_class.min_pocket_size:
            raise IdentifierError('Pocket cards count is less than {}'.format(game_class.min_pocket_size))
        if len(pocket_cards) > game_class.max_pocket_size:
            raise IdentifierError('Pocket cards count is greater than {}'.format(game_class.max_pocket_size))
        if len(board_cards) < game_class.min_board_size:
            raise IdentifierError('Board cards count is less than {}'.format(game_class.min_board_size))
        if len(board_cards) > game_class.max_board_size:
            raise IdentifierError('Board cards count is greater than {}'.format(game_class.max_board_size))
        if len(pocket_cards) + len(board_cards) < game_class.hand_size:
            raise IdentifierError('Not enough cards to identify hand')


__all__ = ('Identifier', 'IdentifierError')
