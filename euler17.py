ONE_THOUSAND = 11
HUNDRED = 7
AND = 3

NINETY = 6
EIGHTY = 6
SEVENTY = 7
SIXTY = 5
FIFTY = 5
FORTY = 5
THIRTY = 6
TWENTY = 6

NINETEEN = 8
EIGHTEEN = 8
SEVENTEEN = 9
SIXTEEN = 7
FIFTEEN = 7
FOURTEEN = 8
THIRTEEN = 8
TWELVE = 6
ELEVEN = 6

TEN = 3
NINE = 4
EIGHT = 5
SEVEN = 5
SIX = 3
FIVE = 4
FOUR = 4
THREE = 5
TWO = 3
ONE = 3

def count_letters_of_number(number):
    """counts letters of a number, only for 1 to 1000.
    342(three hundred and forty-two) : 23
    115(one hundred and fifteen)     : 20
    >>> count_letters_of_number(342)
    23
    >>> count_letters_of_number(115)
    20
    """
    letters = 0
    if number == 1000:
        letters = ONE_THOUSAND
    elif number > 99:
        hundreds = 0
        while True:
            number = number - 100
            hundreds = hundreds + 1
            if number < 100:
                break
        if not number == 0:
            letters = count_letters_of_number(hundreds) + HUNDRED + AND + count_letters_of_number(number) 
        else:
            letters = count_letters_of_number(hundreds) + HUNDRED
    elif number > 89:
        number = number - 90
        letters = NINETY + count_letters_of_number(number)
    elif number > 79:
        number = number - 80
        letters = EIGHTY + count_letters_of_number(number)
    elif number > 69:
        number = number - 70
        letters = SEVENTY + count_letters_of_number(number)
    elif number > 59:
        number = number - 60
        letters = SIXTY + count_letters_of_number(number)
    elif number > 49:
        number = number - 50
        letters = FIFTY + count_letters_of_number(number)
    elif number > 39:
        number = number - 40
        letters = FORTY + count_letters_of_number(number)
    elif number > 29:
        number = number - 30
        letters = THIRTY + count_letters_of_number(number)
    elif number > 19:
        number = number - 20
        letters = TWENTY + count_letters_of_number(number)
    elif number == 19:
        letters = NINETEEN
    elif number == 18:
        letters = EIGHTEEN
    elif number == 17:
        letters = SEVENTEEN
    elif number == 16:
        letters = SIXTEEN
    elif number == 15:
        letters = FIFTEEN
    elif number == 14:
        letters = FOURTEEN
    elif number == 13:
        letters = THIRTEEN
    elif number == 12:
        letters = TWELVE
    elif number == 11:
        letters = ELEVEN
    elif number == 10:
        letters = TEN
    elif number == 9:
        letters = NINE
    elif number == 8:
        letters = EIGHT
    elif number == 7:
        letters = SEVEN
    elif number == 6:
        letters = SIX
    elif number == 5:
        letters = FIVE
    elif number == 4:
        letters = FOUR
    elif number == 3:
        letters = THREE
    elif number == 2:
        letters = TWO
    elif number == 1:
        letters = ONE
    elif number == 0:
        letters = 0
    return letters

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    sum_of_letters = 0
    for i in range(1,1001):
        sum_of_letters = sum_of_letters + count_letters_of_number(i)
    print(sum_of_letters)
