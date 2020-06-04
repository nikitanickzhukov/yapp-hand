# Bounded context
Hand identifier

# Description
A service which allows consumers to identify a hand by giver pocket and board (optionally) cards, and a game type

# Ubiquitous language
- `Identifier` - a service which implements a task mentioned in description
- `Hand` - a combination of certain weight (depending on the game type) consisting of board and pocket cards
- `Card` - a playing card which can be identified by it's rank and suit (e.g. ace of spades, trey of diamonds)
- `Suit` - a card's suit (spades, hearts, diamonds, clubs)
- `Rank` - a card's rank (ace, king, ..., trey, deuce)
- `Board` - a set of community cards on the table (all cards are open)
- `Pocket` - a set of player's cards (can contain hole and open cards)
- `Game` - a type of poker game (e.g. Holdem, Omaha, ...)
