class ChainNumber:
    def __init__(self, start=1):
        self.start = start

    def __iter__(self):
        self.number = self.start

    def __next__(self):
        self.number = sum([int(i) ** 2 for i in str(self.number)])
        return self.number

if __name__ == "__main__":
    MAXIMUM = 10000000
    ones = 0
    eighty_niners = 0

    for i in range(1, MAXIMUM):
        chain_number = ChainNumber(i)
        chain_number.__iter__()
        while True:
            n = chain_number.__next__()
            if n == 89:
                eighty_niners += 1
                break
            if n == 1:
                ones += 1
                break
    print("answer: {0}".format(eighty_niners))
