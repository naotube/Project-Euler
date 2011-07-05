if __name__ == "__main__":
    P = 1000

    max_count = 0
    for i in range(1,P+1):
        count = 0
        for c in range(i,0,-1):
            for a in range(1,i-c):
                b = i-c-a
                if a > b:
                    break
                if c ** 2 == a ** 2 + b ** 2:
                    count += 1
        if count > max_count:
            max_count = count
            answer = i
    print("answer: {0}".format(answer))

