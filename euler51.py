import util_euler
import re

def pattern_generator(length_of_number):
    if length_of_number - 1 < 1:
        return None
    pass

if __name__ == "__main__":
    maximum = 100
    while maximum <= 10000:
        gen = util_euler.prime_generator(maximum=maximum, minimum=int(maximum/10))
        primes = [n for n in gen]

        patterns = pattern_generator(len(str(maximum)) - 1)
        for p in patterns:
            match_cases = re.findall(p, str(primes))
            if len(match_cases) == 6:
                answer = "".join([d for d in match_cases[0]])
                break
        maximum *= 10

        print("answer: {0}".format(answer))
