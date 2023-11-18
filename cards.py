from enum import Enum
import itertools
import random

_ranks = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
_suits = {
    'spades': '\u2660',
    'hearts': '\u2665',
    'diamonds': '\u2666',
    'clubs': '\u2663'
}

class SuitEnum(Enum):
    def __str__(cls):
        return cls.value

Suit = SuitEnum('Suit', _suits)

class Card:
    __slots__ = 'rank', 'suit'

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

class CardDeckBase:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank, suit in itertools.product(_ranks, _suits.values())]

    def display_deck(self):
        for card in self.cards:
            print(f"{card.rank} of {card.suit}")

class FrenchDeck(CardDeckBase):
    def shuffle_deck(self):
        random.shuffle(self.cards)

if __name__ == '__main__':
    deck = FrenchDeck()
    
    # Display the initial deck
    print("Initial Deck:")
    deck.display_deck()

    # Shuffle the deck
    deck.shuffle_deck()

    # Display the shuffled deck
    print("\nShuffled Deck:")
    deck.display_deck()
