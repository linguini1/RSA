# RSA Decryption Software


# Euclidean algorithm

def multiplySquare(base, power, modulo):
    result = 1
    base = int(base)
    for binary in str(format(power, 'b')):
        if binary == "0":
            result = (result ** 2) % modulo
        elif binary == "1":
            result = ((result ** 2) * base) % modulo
    return result


if __name__ == '__main__':
    # Read from file or small message
    while True:
        file_or_no = input("Do you want to read from a file (1) or read a small message through the console (2)? Type: ")
        if file_or_no == "1":
            while True:
                directory = input("Which file do you want to use? Include the whole directory: ")
                if '"' in directory:
                    directory = directory[1:-1]
                try:
                    message = open(directory, 'r')
                    name = input("What filename do you want to save your decryption under? Type: ")
                    name = name + ".txt"
                    break
                except FileNotFoundError:
                    print("Invalid directory or file name, try again.")
            break
        elif file_or_no == "2":
            # Getting user string to be converted
            message = input("Message to be decrypted: ")
            message = message.split(" ")[0:-1]
            break
        else:
            print("Invalid input.")
    print()

    # Getting lock
    while True:
        key = input("Key in format (x, y): ")
        try:
            key = key[1:-1].split(",")
            e = int(key[0])
            n = int(key[1])
            break
        except ValueError:
            print("Invalid key.")

    # Dictionary
    dictionary = {}
    characters = """QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()\x00\x1a_\xad+-=[]\{}\n|;:'<,>.?\t/`~ \""""
    characters = list(characters)
    for index, character in enumerate(characters):
        dictionary[character] = index

    # Getting multiprocessing power
    from multiprocessing import Pool
    from itertools import repeat

    # Decryption
    if file_or_no == "1":
        with open(name, 'w') as file:
            for row in message:
                line = row.split(" ")[0:-1]
                with Pool() as pool:
                    new_nums = pool.starmap(multiplySquare, zip(line, repeat(e), repeat(n)))
                    for new_num in new_nums:
                        for label, value in dictionary.items():
                            if value == new_num:
                                file.write(label)

        # Returning info
        print(f"Your message has been decoded and saved under filename '{name}'.")
        print()

    elif file_or_no == "2":
        d_message = ""
        with Pool() as pool:
            new_nums = pool.starmap(multiplySquare, zip(message, repeat(e), repeat(n)))
            for new_num in new_nums:
                for label, value in dictionary.items():
                    if value == new_num:
                        d_message += label

        # Returning info
        print("Your decoded message is as follows:")
        print()
        print(d_message)
