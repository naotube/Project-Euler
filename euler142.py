from itertools import count

def main():
    squares = set()
    for x in count(3,1):
        squares.add(x ** 2)
        for y in range(x-1, 0, -1):
            if x+y in squares and x-y in squares:
                for z in range(y-1, 0, -1):
                    p = (x+z, x-z, y+z, y-z)
                    if all(n in squares for n in p):
                        return(x+y+z)

if __name__ == "__main__":
    print(main())
