VALUES = [200, 100, 50, 20, 10, 5, 2, 1]

def calcurate_price(coins):
    """receive numbers of coins, returns total value of them.
    coins = 200, 100, 50, 20, 10, 5, 2, 1
    >>> calcurate_price([1,0,1,0,1,0,1,0])
    262
    >>> calcurate_price([0,1,0,1,0,1,0,1])
    126
    """
    assert type(coins).__name__ == 'list'
    assert len(coins) == 8
    total_value = 0
    for i in range(len(coins)):
        total_value += VALUES[i] * coins[i]

    return total_value

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    TARGET = 200
    two_pound = 0

    for P2 in range(int(TARGET / VALUES[0] + 1)):
        for P1 in range(int(TARGET / VALUES[1] + 1)):
            for p50 in range(int(TARGET / VALUES[2] + 1)):
                for p20 in range(int(TARGET / VALUES[3] + 1)):
                    for p10 in range(int(TARGET / VALUES[4] + 1)):
                        for p5 in range(int(TARGET / VALUES[5] + 1)):
                            for p2 in range(int(TARGET / VALUES[6] + 1)):
                                for p1 in range(int(TARGET / VALUES[7] + 1)):
                                    if calcurate_price([P2,P1,p50,p20,p10,p5,p2,p1]) == 200:
                                        two_pound += 1
                                        break
                                    if calcurate_price([P2,P1,p50,p20,p10,p5,p2,p1]) > 200:
                                        break
                                if calcurate_price([P2,P1,p50,p20,p10,p5,p2,0]) > 200:
                                    break
                            if calcurate_price([P2,P1,p50,p20,p10,p5,0,0]) > 200:
                                break
                        if calcurate_price([P2,P1,p50,p20,p10,0,0,0]) > 200:
                            break
                    if calcurate_price([P2,P1,p50,p20,0,0,0,0]) > 200:
                        break
                if calcurate_price([P2,P1,p50,0,0,0,0,0]) > 200:
                    break
            if calcurate_price([P2,P1,0,0,0,0,0,0]) > 200:
                break
        if calcurate_price([P2,0,0,0,0,0,0,0]) > 200:
            break
    print(two_pound)

