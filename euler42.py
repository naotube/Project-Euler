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

def calcurate_word_score(word):
    """
    calcurates score of a name.
    >>> calcurate_word_score("ADAM")
    19
    >>> calcurate_word_score("EVE")
    32
    >>> calcurate_word_score(23)
    False
    """
    if not type(word).__name__ == 'str':
        return False
    score = 0
    for character in word:
        score = score + calcurate_character_score(character)
    return score

def triangle_number_generator(maximum):
    """generate numbers can be described as n(n+1)/2
    """
    triangle_number = 0
    number = 1
    while triangle_number < maximum:
        triangle_number = int(number * (number + 1) / 2)
        number += 1
        yield triangle_number

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    with open('problem_euler42.txt', encoding='utf-8') as words_file:
        words = words_file.read()
        words_list = words.split(",")
        score_list = []
        for word in words_list:
            score_list.append(calcurate_word_score(word))

        triangle_number_gen = triangle_number_generator(max(score_list))
        triangle_numbers = []
        for n in triangle_number_gen:
            triangle_numbers.append(n)

        how_many_triangle_number = 0
        for score in score_list:
            if score in triangle_numbers:
                how_many_triangle_number += 1
        print(how_many_triangle_number)
