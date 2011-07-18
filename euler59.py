if __name__ == "__main__":
    with open('problem_euler59.txt', encoding='utf-8') as cipher:
        characters = cipher.read()
        characters_list = characters.split(",")
        characters_list = [int(c) for c in characters_list]
