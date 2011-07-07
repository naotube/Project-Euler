from math import factorial

if __name__ == "__main__":
    LIMIT = 100

    answer = 0
    for n in range(1,LIMIT + 1):
        for r in range(1,n):
            if factorial(n) / factorial(r) / factorial(n-r) > 1000000:
                answer += n - 1 - ((r - 1) * 2)
                break
    print(answer)
