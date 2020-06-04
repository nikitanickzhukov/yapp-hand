from typing import Sequence, Tuple, Type
import subprocess
import re
import logging

from domain.service.identifier import Identifier, IdentifierError
from domain.model.card import Card
from domain.model.game import (
    Game,
    Holdem, Omaha, OmahaHighLow,
    Razz, Stud, StudHighLow, StudNoQ,
    Draw, Badugi,
    LowballA5, Lowball27, TripleLowballA5, TripleLowball27,
)
from domain.model.hand import (
    Hand,
    HighCard, OnePair, TwoPair, Trips, Straight,
    Flush, FullHouse, Quads, StraightFlush,
)


logger = logging.getLogger(__name__)


class PokerstoveIdentifierError(IdentifierError):
    pass


class PokerstoveIdentifier(Identifier):
    encoding = 'utf-8'
    game_mapping = {
        Holdem: 'h',
        Omaha: 'O',
        OmahaHighLow: 'o',
        Razz: 'r',
        Stud: 's',
        StudHighLow: 'e',
        StudNoQ: 'q',
        Draw: 'd',
        Badugi: 'b',
        LowballA5: 'l',
        Lowball27: 'k',
        TripleLowballA5: 'T',
        TripleLowball27: 't',
    }
    hand_mapping = {
        HighCard: 'high card',
        OnePair: 'one pair',
        TwoPair: 'two pair',
        Trips: 'trips',
        Straight: 'straight',
        Flush: 'flush',
        FullHouse: 'full house',
        Quads: 'quads',
        StraightFlush: 'str8 flush',
    }

    @classmethod
    def identify(cls, game_class: Type[Game], pocket_cards: Sequence[Card], board_cards: Sequence[Card]) -> Tuple[Hand]:
        try:
            cls.check_params(game_class=game_class, pocket_cards=pocket_cards, board_cards=board_cards)
        except IdentifierError as e:
            raise PokerstoveIdentifierError(str(e)) from e

        game_code = cls._encode_game(game_class=game_class)

        args = [
            'ps-id',
            '--game',
            game_code,
        ]
        if pocket_cards:
            pocket_cards_code = cls._encode_cards(cards=pocket_cards)
            args.append('--hand')
            args.append(pocket_cards_code)
        if board_cards:
            board_cards_code = cls._encode_cards(cards=board_cards)
            args.append('--board')
            args.append(board_cards_code)

        try:
            output = cls._run_command(*args)
        except PokerstoveError as e:
            logger.exception('Cannot identify hand')
            raise PokerstoveIdentifierError('Cannot identify hand') from e

        return cls._parse_identify_output(game_class=game_class, output=output)

    @classmethod
    def _parse_identify_output(cls, game_class: Type[Game], output: str) -> Tuple[Hand]:
        lines = output.split('\n')
        i = 0
        hands = []
        try:
            while i < len(lines):
                if lines[i] == '':
                    i += 1
                    continue

                hand_line = lines[i]
                weight_line = lines[i + 1]
                res = re.search(r'^\s*([a-z0-9\s]+)\s*:\s*([A-Z0-9]+)\s*$', hand_line)
                if res:
                    code = res.group(1)
                    comment = res.group(2)
                    weight = int(weight_line)
                    hand_class = cls._decode_hand(code=code)
                    hands.append(hand_class(weight=weight, comment=comment))
                i += 2
        except Exception as e:
            logger.exception('Cannot identify hand')
            raise PokerstoveIdentifierError('Cannot identify hand') from e

        return tuple(hands)

    @classmethod
    def _encode_game(cls, game_class: Type[Game]) -> str:
        code = cls.game_mapping.get(game_class)
        if code is None:
            raise PokerstoveIdentifierError('Cannot encode game {}'.format(game_class))
        return code

    @classmethod
    def _encode_cards(cls, cards: Sequence[Card]) -> str:
        return ''.join(map(lambda x: x.code, cards))

    @classmethod
    def _decode_hand(cls, code: str) -> Type[Hand]:
        for hand_class in cls.hand_mapping:
            if cls.hand_mapping[hand_class] == code:
                return hand_class
        raise PokerstoveIdentifierError('Cannot decode hand {}'.format(code))

    @classmethod
    def _run_command(cls, command: str, *args) -> str:
        logger.debug('Running command {} with args {}'.format(command, args))

        result = subprocess.run([command, *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode:
            stderr = result.stderr.decode(cls.encoding)
            logger.exception(stderr)
            raise PokerstoveIdentifierError(stderr)

        stdout = result.stdout.decode(cls.encoding)
        logger.debug('Got result:\n{}'.format(stdout))

        return stdout


__all__ = ('PokerstoveIdentifier', 'PokerstoveIdentifierError')
