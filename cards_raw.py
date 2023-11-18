from collections import namedtuple
from enum import Enum, auto

BasicSuit = namedtuple('BasicSuit', ['name', 'symbol'])


class SymbolMixin:

    def __str__(self):
        return self.symbol


class Suit(SymbolMixin, BasicSuit):
    pass


suits = {
    'spades': '\u2660',
    'hearts': '\u2665',
    'diamonds': '\u2666',
    'clubs': '\u2663'
}

_suitvals = {k: Suit(name=k, symbol=v) for k, v in suits.items()}
CardSuit = Enum('CardSuit', _suitvals)


class UpperRank(Enum):
    J = 11
    Q = 12
    K = 13
    A = 14


ranks = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']  # Додано список рангів

class Card:
    __slots__ = 'rank', 'suit'

    def __init__(self, rank, suit):
        if rank not in ranks or suit not in suits:
            raise ValueError("Invalid rank or suit")
        self.rank = rank
        self.suit = Suit(name=suit, symbol=suits[suit])  # Змінено на Suit

if __name__ == '__main__':
    # Створення об'єктів Suit
    spades = Suit(name='spades', symbol='\u2660')
    hearts = Suit(name='hearts', symbol='\u2665')
    diamonds = Suit(name='diamonds', symbol='\u2666')
    clubs = Suit(name='clubs', symbol='\u2663')

    # Створення об'єкта UpperRank
    king = UpperRank.K

    # Створення об'єкта CardSuit
    card_suit = CardSuit.spades

    # Створення об'єкта Card
    my_card = Card(rank=10, suit='hearts')

    # Виведення об'єктів на екран
    print(f"Suit: {spades.name}, Symbol: {spades}, Rank: {king.name}, CardSuit: {card_suit.name}")
    print(f"My Card: Rank - {my_card.rank}, Suit - {my_card.suit.name}, Symbol - {my_card.suit}")
