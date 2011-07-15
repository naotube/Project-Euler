class ChainNumber:
    def __init__(self, start=1):
        self.start = start

    def __iter__(self):
        self.number = self.start

    def __next__(self):
        self.number = sum([int(i) ** 2 for i in str(self.number)])
        return self.number

if __name__ == "__main__":
    pass
