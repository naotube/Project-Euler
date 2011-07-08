class Pentagonal:
    def __init__(self, start=1, maximum=2100000000):
        self.start = start
        self.maximum = maximum

    def __iter__(self):
        self.number = self.start
        return self

    def __next__(self):
        pentagonal = int(self.number * (3 * self.number - 1) / 2)
        if pentagonal > self.maximum:
            raise StopIteration
        self.number += 1
        return pentagonal

if __name__ == "__main__":
    pentagonal_numbers = []
    pen = Pentagonal()
    answer = 0
    for i in pen:
        pentagonal_numbers.append(i)
        penta = Pentagonal(maximum=i)
        for n in penta:
            if (i-n) in pentagonal_numbers and (n - (i-n)) in pentagonal_numbers:
                answer = n - (i-n)
        if not answer == 0:
            break
    print("answer:{0}".format(answer))
