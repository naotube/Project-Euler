class Triangle:
    def __init__(self, start=1, maximum=2100000000):
        self.start = start
        self.maximum = maximum

    def __iter__(self):
        self.number = self.start
        return self

    def __next__(self):
        triangle = int(self.number * (self.number + 1) / 2)
        if triangle > self.maximum:
            raise StopIteration
        self.number += 1
        return triangle

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

class Hexagonal:
    def __init__(self, start=1, maximum=2100000000):
        self.start = start
        self.maximum = maximum

    def __iter__(self):
        self.number = self.start
        return self

    def __next__(self):
        hexagonal = self.number * (2 * self.number - 1)
        if hexagonal > self.maximum:
            raise StopIteration
        self.number += 1
        return hexagonal

if __name__ == "__main__":
    VERIFIED_MAX = 40755

    tr = Triangle(start=285)
    pn = Pentagonal(start=165)
    hx = Hexagonal(start=143)
    tr.__iter__()
    pn.__iter__()
    hx.__iter__()
    T = tr.__next__()
    P = pn.__next__()
    H = hx.__next__()

    while True:
        if T == P == H:
            if T > VERIFIED_MAX:
                break
            else:
                T = tr.__next__()
                P = pn.__next__()
                H = hx.__next__()
        elif T > P and T > H:
            P = pn.__next__()
            H = hx.__next__()
            continue
        elif P > T and P > H:
            T = tr.__next__()
            H = hx.__next__()
            continue
        elif H > T and H > P:
            T = tr.__next__()
            P = pn.__next__()
            continue
        elif T == P and T > H:
            H = hx.__next__()
            continue
        elif P == H and P > T:
            T = tr.__next__()
            continue
        elif H == T and H > P:
            P = pn.__next__()
            continue
        else:
            print("something's weird XD")

    print(T)

