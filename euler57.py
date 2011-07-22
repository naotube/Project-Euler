class root2:
    def __init__(self, max_count=1000):
        self.numerator = 1
        self.denominator = 1
        self.max_count = max_count
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.numerator += self.denominator
        self.numerator, self.denominator = self.denominator, self.numerator
        self.numerator += self.denominator
        self.count += 1
        if self.count > self.max_count:
            raise StopIteration
        return self.numerator, self.denominator

if __name__ == "__main__":
    root_two = root2(1000)
    print(len([i for i in root_two if len(str(i[0])) > len(str(i[1]))]))
