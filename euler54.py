def number_of_card(number):
    """
    >>> number_of_card('7')
    7
    >>> number_of_card('J')
    11
    >>> number_of_card('A')
    14
    """
    try:
        number = int(number)
        return number
    except ValueError:
        if number == 'T':
            return 10
        elif number == 'J':
            return 11
        elif number == 'Q':
            return 12
        elif number == 'K':
            return 13
        elif number == 'A':
            return 14
        else:
            raise ValueError

def poker_score(cards):
    """returns score of Poker
    one pair       : 100
    two pairs      : 200
    3 of a kind    : 300
    straight       : 400
    flush          : 500
    full house     : 600
    4 of a kind    : 700
    straight flush : 800
    royal flush    : 900
    2-9: 2-9, T: 10, J: 11, Q:12, K: 13, A: 14
    >>> poker_score(['7C','8C','5C','QD','6C'])
    12.08070605
    >>> poker_score(['5H','5C','6S','7S','KD'])
    105.130706
    >>> poker_score(['4H','4D','8C','8S','AC'])
    208.0414
    >>> poker_score(['2D','9C','AS','AH','AC'])
    314.0902
    >>> poker_score(['7C','8D','9H','TC','JD'])
    411.10090807
    >>> poker_score(['2D','6D','4D','AD','KD'])
    514.13060402
    >>> poker_score(['2H','2D','4C','4D','4S'])
    604.02
    >>> poker_score(['7H','4C','4H','4S','4D'])
    704.07
    >>> poker_score(['4D','5D','6D','7D','8D'])
    808.07060504
    >>> poker_score(['TS','JS','QS','KS','AS'])
    900
    """
    RoyalFlush = 900
    StraightFlush = 800
    FourOfAKind = 700
    FullHouse = 600
    Flush = 500
    Straight = 400
    ThreeOfAKind = 300
    TwoPairs = 200
    OnePair = 100

    isFlush = False
    suits = set([n[1:] for n in cards])
    if len(suits) == 1:
        isFlush = True

    numbers = [number_of_card(n[:1]) for n in cards]
    numbers = sorted(numbers)
    differences = [numbers[i+1] - numbers[i] for i in range(4)]

    if all(d == 1 for d in differences):
        if isFlush:
            if numbers[0] == 10:
                score = RoyalFlush
            else:
                score = StraightFlush + numbers[4]\
                        + numbers[3]/100 + numbers[2]/10000\
                        + numbers[1]/1000000 + numbers[0]/100000000
        else:
            score = Straight + numbers[4]\
                    + numbers[3]/100 + numbers[2]/10000\
                    + numbers[1]/1000000 + numbers[0]/100000000
    elif isFlush:
        score = Flush + numbers[4]\
                + numbers[3]/100 + numbers[2]/10000\
                + numbers[1]/1000000 + numbers[0]/100000000
    else:
        numbers_set = set(numbers)
        if len(numbers_set) == 2:
            for n in numbers_set:
                if numbers.count(n) == 4:
                    while n in numbers:
                        numbers.remove(n)
                    score = FourOfAKind + n + numbers[0]/100
                if numbers.count(n) == 3:
                    while n in numbers:
                        numbers.remove(n)
                    score = FullHouse + n + numbers[0]/100
        elif len(numbers_set) == 3:
            for n in numbers_set:
                if numbers.count(n) == 3:
                    while n in numbers:
                        numbers.remove(n)
                    score = ThreeOfAKind + n + numbers[1]/100 + numbers[0]/10000
                if numbers.count(n) == 2:
                    pairA = n
                    while n in numbers:
                        numbers.remove(n)
                    for m in numbers_set:
                        if numbers.count(m) == 2:
                            pairB = m
                            while m in numbers:
                                numbers.remove(m)
                    if pairA < pairB:
                        pairA, pairB = pairB, pairA
                    score = TwoPairs + pairA + pairB/100 + numbers[0]/10000
        elif len(numbers_set) == 4:
            for n in numbers_set:
                if numbers.count(n) == 2:
                    while n in numbers:
                        numbers.remove(n)
                    score = OnePair + n\
                            + numbers[2]/100 + numbers[1]/10000\
                            + numbers[0]/1000000
        else:
            score = numbers[4]\
                    + numbers[3]/100 + numbers[2]/10000\
                    + numbers[1]/1000000 + numbers[0]/100000000
    return round(score,8)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    with open('problem_euler54.txt', encoding='utf-8') as poker:
        player1wins = 0
        for line in poker:
            cards = line.rsplit()
            player1 = cards[0:5]
            player2 = cards[5:10]
            if poker_score(player1) > poker_score(player2):
                player1wins += 1
    print("player 1 wins {0} times.".format(player1wins))
