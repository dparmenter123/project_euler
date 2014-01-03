from utils import timeit
from collections import defaultdict

mapping = {
    'A' : 14,
    'K' : 13,
    'Q' : 12,
    'J' : 11,
    'T' : 10,
    '9' : 9,
    '8' : 8,
    '7' : 7,
    '6' : 6,
    '5' : 5,
    '4' : 4,
    '3' : 3,
    '2' : 2,
}

def noop(hand):
    return 0

def high_card(hand):
    return max([number for number, suit in hand])
#    return max([card[0] for card in hand])

def high_card_excluding_pairs(hand):
    numbers = defaultdict(int)
    singletons = set()
    for number, suit in hand:
        if number in singletons:
            singletons.remove(number)
        else:
            singletons.add(number)
    return max(singletons)


def low_pair(hand):
    numbers = defaultdict(int)
    pairs = []
    for number, suit in hand:
        numbers[number] += 1
        if numbers[number] == 2:
            pairs.append(number)
    return min(pairs)

def high_pair(hand):
    numbers = defaultdict(int)
    pairs = []
    for number, suit in hand:
        numbers[number] += 1
        if numbers[number] == 2:
            pairs.append(number)
    return max(pairs)

def high_triple(hand):
    numbers = defaultdict(int)
    for number, suit in hand:
        numbers[number] += 1
        if numbers[number] == 3:
            return number

################################################################

def one_pair(hand):
    numbers = defaultdict(int)
    for number, suit in hand:
        numbers[number] += 1
    lengths = sorted(numbers.values())
    return int(lengths == [1,1,1,2])

def two_pair(hand):
    numbers = defaultdict(int)
    for number, suit in hand:
        numbers[number] += 1
    lengths = sorted(numbers.values())
    return int(lengths == [1,2,2])

def three_of_a_kind(hand):
    numbers = defaultdict(int)
    for number, suit in hand:
        numbers[number] += 1
        if numbers[number] == 3:
            return 1
    return 0

def straight(hand):
    numbers = set([card[0] for card in hand])
    if len(numbers) != 5:
        return 0
    if max(numbers) - min(numbers) == 4:
        return 1
    return 0

def flush(hand):
    suits = set([card[1] for card in hand])
    return int(len(suits) == 1)

def full_house(hand):
    numbers = defaultdict(int)
    for number, suit in hand:
        numbers[number] += 1
    if len(numbers.keys()) != 2:
        return 0
    lengths = set(numbers.values())
    return int(lengths == {2,3})

def four_of_a_kind(hand):
    numbers = defaultdict(int)
    for number, suit in hand:
        numbers[number] += 1
        if numbers[number] == 4:
            return 1
    return 0

def straight_flush(hand):
    return int(flush(hand) and straight(hand))

def royal_flush(hand):
    return int(flush(hand) and straight(hand) and high_card(hand) == 14)

strategies = [
    (royal_flush, high_card),
    (straight_flush, high_card),
    (four_of_a_kind, high_card),
    (full_house, high_triple),
    (flush, noop),
    (straight, high_card),
    (three_of_a_kind, high_triple),
    (two_pair, high_pair, low_pair, high_card_excluding_pairs),
    (one_pair, high_pair, high_card_excluding_pairs),
    (high_card, noop)
]

def compare(p1, p2):
    for strategy in strategies:
        score = 0
        for func in strategy:
            s1 = func(p1)
            s2 = func(p2)
            if s1 == 0 and s2 == 0:
                break
            if s1 == s2:
                continue
            if s1 > s2:
                return True
            else:
                return False
    raise 'Error: identical hands!'
    return None

def deal():
    def prepare_card(card):
        number = mapping[card[0]]
        suit = card[1]
        return number, suit

    count = 0
    for game in open('poker.txt', 'r').readlines():
        cards = [prepare_card(hand) for hand in game.split()]
        p1 = cards[:5]
        p2 = cards[5:]
        yield p1, p2


@timeit
def solution():
    count = 0
    for p1, p2 in deal():
        if compare(p1, p2):
            count += 1
    return count
    

################################################################
#
################################################################
if __name__ == "__main__":
    print '\nsolution:', solution()
