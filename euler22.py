def calcurate_character_score(character):
    """
    returns score of a character
    score of each characters are like this.
    A: 1, B:2, ... Z:26
    >>> calcurate_character_score('A')
    1
    >>> calcurate_character_score('a')
    1
    >>> calcurate_character_score('Z')
    26
    >>> calcurate_character_score('"')
    0
    """
    if not character.isalpha() == True:
        return 0
    scores="_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    character = character.capitalize()
    return scores.index(character)

def calcurate_name_score(name):
    """
    calcurates score of a name.
    >>> calcurate_name_score("ADAM")
    19
    >>> calcurate_name_score("EVE")
    32
    >>> calcurate_name_score(23)
    False
    """
    if not type(name).__name__ == 'str':
        return False
    score = 0
    for character in name:
        score = score + calcurate_character_score(character)
    return score

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    with open('problem_euler22.txt', encoding='utf-8') as names_file:
        names = names_file.read()
        names_list = names.split(",")
        names_list.sort()
        place = 1
        score = 0
        for name in names_list:
            name_score = place * calcurate_name_score(name)
            score = score + name_score
            place = place + 1
        print(score)
