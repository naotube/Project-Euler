def count_coin_change(total=None, units=None, memo={}):
    assert not total == None
    assert not units == None

    if total == 0:
        return 1
    if total < 0:
        return 0
    if total >= 0 and len(units) <= 0:
        return 0
    key = "{0}-{1}".format(total, len(units))
    if key not in memo:
        memo[key] = count_coin_change(total, units[:-1]) + count_coin_change(total - units[-1], units)
    return memo[key]

if __name__ == "__main__":
    Coins = [1, 2, 5, 10, 20, 50, 100, 200]
    Total = 200
    Memo = {}
    print(count_coin_change(Total, Coins, Memo))
