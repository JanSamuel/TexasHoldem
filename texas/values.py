from functools import partial

from .cards import figures

def is_pair(figure, hand):
    """
    >>> is_pair("3", ["3a", "3a", "6a", "4a"])     
    True
    >>> is_pair("2", ["3a", "3a", "6a", "4a"])     
    False
    >>> is_pair("3", ["Ka", "4a", "6a", "3b"])     
    False
    """
    return len([x for x in hand if x[:-1] == figure]) >=2

def is_two_pair(figure1, figure2, hand):
    """
    >>> is_two_pair("3","2", ["3a", "3a", "2a", "2a"])     
    True
    >>> is_two_pair("4","5", ["3a", "3a", "2a", "2a"])     
    False
    >>> is_two_pair("3","2", ["4a", "3a", "2a", "2a"])     
    False
    """
    if(figure1==figure2):
        return False
    return (is_pair(figure1, hand) and is_pair(figure2, hand))

def is_three(figure, hand):
    """
    >>> is_three("3", ["3a", "3a", "6a", "4a"])     
    False
    >>> is_three("2", ["3a", "3a", "6a", "4a"])     
    False
    >>> is_three("3", ["3a", "3a", "6a", "3b"])     
    True
    """
    return len([x for x in hand if x[:-1] == figure]) >=3

def is_straight(figure, hand):
    """
    >>> is_straight("6", ["2a", "3a", "4a", "5b", "6a"])     
    True
    >>> is_straight("3", ["2a", "3a", "8a", "5b", "6a"])     
    False
    >>> is_straight("6", ["6a", "3a", "4a", "5b", "2a"])     
    True
    >>> is_straight("A", ["Aa", "2a", "3a", "4b", "5a"])     
    True
    >>> is_straight("A", ["Aa", "10a", "Ja", "Qb", "Ka"])     
    True
    >>> is_straight("K", ["Aa", "10a", "Ja", "Qb", "Ka"])     
    False
    """
    hand_value = sorted([figures.index(cards[:-1]) for cards in hand])
    if hand_value == [0,1,2,3,12] and figure == figures[max(hand_value)]: #special case As can be lowest and highst card
        return True
    return (hand_value == list(range(min(hand_value), max(hand_value)+1))) and figure == figures[max(hand_value)]

def is_flush(figure, hand):
    """
    >>> is_flush("6", ["3a", "3a", "6a", "4a"])     
    True
    >>> is_flush("6", ["3a", "3b", "6a", "4a"])     
    False
    >>> is_flush("3", ["3a", "3a", "6a", "4a"])     
    False
    """
    hand_value = sorted([figures.index(cards[:-1]) for cards in hand])
    return all(kolor[-1] == hand[0][-1] for kolor in hand) and  figure == figures[max(hand_value)]

def is_full(figure1, figure2, hand):
    """
    >>> is_full("2","3", ["2a", "3a", "2a", "3b", "3c"])     
    True
    >>> is_full("2","3", ["2a", "3a", "2a", "3b", "4c"])     
    False
    >>> is_full("2","3", ["2a", "3a", "5a", "3b", "3c"])     
    False
    >>> is_full("2","5", ["2a", "3a", "5a", "3b", "3c"])     
    False
    >>> is_full("2","6", ["2a", "3a", "2a", "3b", "3c"])      
    False
    """
    return (is_pair(figure1, hand) and is_three(figure2, hand))

def is_four(figure, hand):
    """
    >>> is_pair("3", ["3a", "3a", "3a", "3a"])     
    True
    >>> is_pair("2", ["3a", "3a", "3a", "3b"])     
    False
    >>> is_pair("3", ["Ka", "Ka", "6a", "6b"])     
    False
    """
    return len([x for x in hand if x[:-1] == figure]) >=4

def is_poker(figure, hand):
    """
    >>> is_poker("K", ["10a", "Ja", "Qa", "Ka", "9a"])     
    True
    >>> is_poker("A", ["10a", "Ja", "Qa", "Ka", "9a"])     
    False
    >>> is_poker("K", ["10a", "Ja", "Qb", "Ka", "9a"])     
    False
    """
    hand_value = sorted([figures.index(cards[:-1]) for cards in hand])
    return is_flush(figure, hand) and is_straight(figure, hand) and figure == figures[max(hand_value)]

def is_royal_poker(hand):
    """
    >>> is_royal_poker(["10a", "Ja", "Qa", "Ka", "9a"])
    False
    >>> is_royal_poker(["Aa", "Ka", "Qa", "Ja", "10a"])
    True
    """
    hand_value = sorted([figures.index(cards[:-1]) for cards in hand])
    
    return is_flush("A", hand) and hand_value == [8,9,10,11,12]

pair = [partial(is_pair, figure=f)for f in figures[::-1]]
two_pair = [partial(is_two_pair, figure1=f1, figure2=f2)for f1 in figures[::-1] for f2 in figures[::-1]]
three = [partial(is_three, figure=f)for f in figures[::-1]]
straight = [partial(is_straight, figure=f)for f in figures[::-1]]
kolor = [partial(is_flush, figure=f)for f in figures[::-1]]
full = [partial(is_full, figure1=f1, figure2=f2)for f1 in figures[::-1] for f2 in figures[::-1]]
four = [partial(is_four, figure=f)for f in figures[::-1]]
poker = [partial(is_poker, figure=f)for f in figures[::-1]]
royal_poker = [partial(is_royal_poker)]
strength = royal_poker + poker + four + full + kolor + straight + three + two_pair + pair

def hand_value(cards):
    """
    >>> hand_value(["3z", "3a", "6q", "4w"]) > hand_value(["2z", "2a", "6q", "4w"]) 
    True
    >>> hand_value(["3z", "3a", "6q", "4w"]) < hand_value(["2z", "2a", "4q", "4w"])
    True
    >>> hand_value(["3z", "3a", "6q", "4w"]) < hand_value(["2z", "2a", "2q", "2w"])
    True
    >>> hand_value(["2z", "3a", "4q", "5w"]) < hand_value(["2a", "4a", "5a", "2a"])
    True
    >>> hand_value(["2z", "2a", "3q", "3w", "3a"]) > hand_value(["2a", "4a", "5a", "2a"])
    True
    >>> hand_value(["2z", "2a", "3q", "3w", "3a"]) < hand_value(["2a", "2a", "2b", "2a"])
    True
    >>> hand_value(["2a", "3a", "4a", "5a", "6a"]) > hand_value(["2a", "2a", "2b", "2a"])
    True
    >>> hand_value(["2a", "3a", "4a", "5a", "6a"]) < hand_value(["Aa", "Ka", "Ja", "Qa", "10a"])
    True
    """
    for strength_value, check in enumerate(strength):
        if check(hand = cards):
            return len(strength) - strength_value