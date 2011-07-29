ord_a = 97
ord_z = 122

if __name__ == "__main__":
    with open('problem_euler59.txt', encoding='utf-8') as cipher:
        characters = cipher.read()
        characters_list = characters.split(",")
        characters_list = [int(c) for c in characters_list]
        decrypted_message = None

        for x in range(ord_a, ord_z + 1):
            for y in range(ord_a, ord_z + 1):
                for z in range(ord_a, ord_z + 1):
                    count = 0
                    suggested_list = []
                    for c in characters_list:
                        if count % 3 == 0:
                            suggested_list.append(chr(c^x))
                        if count % 3 == 1:
                            suggested_list.append(chr(c^y))
                        if count % 3 == 2:
                            suggested_list.append(chr(c^z))
                        count += 1
                    suggested_message = "".join(suggested_list)
                    # I tried only with one word 'the' at first.
                    # and found out the readable message, then added another word 'God'.
                    if 'the' in suggested_message and 'God' in suggested_message:
                        decrypted_message = suggested_message
                    count = 0
                    if not decrypted_message == None:
                        break
                if not decrypted_message == None:
                    break
            if not decrypted_message == None:
                break

        print("password: {0}{1}{2}".format(chr(x), chr(y), chr(z)))
        print(decrypted_message)
        sum_of_ASCII_values = 0
        for c in decrypted_message:
            sum_of_ASCII_values += ord(c)
        print("the answer: {0}".format(sum_of_ASCII_values))
