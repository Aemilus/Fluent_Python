import collections
from random import choice


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def spades_high(card: Card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':
    deck = FrenchDeck()
    print(f"This deck has {len(deck)} cards.")

    print(f"First card in the deck is:\n{deck[0]}")
    print(f"Last card in the deck is:\n{deck[-1]}")
    print(f"Pick a random card from deck:\n{choice(deck)}")

    print(f"First three cards from deck:\n{deck[:3]}")
    print(f"All aces in the deck (every 13th card in the deck):\n{deck[12::13]}")

    print("All cards in the deck:")
    for card in deck:
        print(card)

    print("All cards in deck in reverse order:")
    for card in reversed(deck):
        print(card)

    print(f"Is card Q of hearts in the deck?")
    print(Card('Q', 'hearts') in deck)
    print(f"Is card 7 of beasts in the deck?")
    print(Card('7', 'beasts') in deck)

    print(f"Sorted deck by {suit_values}:")
    for card in sorted(deck, key=spades_high):
        print(f"{spades_high(card)}: {card}")
