from falcon import HTTPBadRequest
from typing import Sequence, Type
import json

from domain.model.game import Game, games
from domain.model.card import Card, cards
from domain.model.hand import Hand
from infrastructure.service.pokerstove_identifier import PokerstoveIdentifier, PokerstoveIdentifierError


class IdentifierViewV1:
    game_mapping = {x.__name__: x for x in games}
    card_mapping = {x.code: x for x in cards}

    def on_get(self, req, resp) -> None:
        game_class = self._get_game_class(game_code=req.get_param(name='game', required=True))
        pocket_cards = self._get_cards(card_codes=req.get_param_as_list(name='pocket', required=True))
        board_cards = self._get_cards(card_codes=req.get_param_as_list(name='board', default=[]))

        try:
            hands = PokerstoveIdentifier.identify(
                game_class=game_class,
                pocket_cards=pocket_cards,
                board_cards=board_cards,
            )
        except PokerstoveIdentifierError as e:
            raise HTTPBadRequest(title=str(e)) from e

        result = {
            'high': self._serialize_hand(hand=hands[0])
        }
        if game_class.is_high_low:
            result['low'] = None

        if len(hands) > 1:
            result['low'] = self._serialize_hand(hand=hands[1])

        resp.body = json.dumps(result)

    def _get_game_class(self, game_code: str) -> Type[Game]:
        game_class = self.game_mapping.get(game_code)
        if game_class is None:
            raise HTTPBadRequest(title='Game {} is not found.'.format(game_code))
        return game_class

    def _get_cards(self, card_codes: Sequence[str]) -> Sequence[Card]:
        items = []
        for code in card_codes:
            card = self.card_mapping.get(code)
            if card is None:
                raise HTTPBadRequest(title='Card {} is not found.'.format(code))
            items.append(card)
        return items

    def _serialize_hand(self, hand: Hand) -> dict:
        return {
            'hand': hand.__class__.__name__,
            'weight': hand.weight,
            'comment': hand.comment,
        }


__all__ = ('IdentifierViewV1',)
