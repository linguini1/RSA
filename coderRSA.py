# RSA Encryption Method


# Multiply & Square algorithm

def multiply_square_e(base, power, modulo):
    result = 1
    for binary in str(format(power, 'b')):
        if binary == "0":
            result = (result ** 2) % modulo
        elif binary == "1":
            result = ((result ** 2) * base) % modulo
    return result


def multiply_square_d(base, power, modulo):
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
        encrypt = input("Do you want to encrypt or decrypt? (Type the word): ")
        if encrypt == "encrypt":
            encrypt = True
            break
        elif encrypt == "decrypt":
            encrypt = False
            break
        else:
            print("Invalid input.")
    while True:
        file_or_no = input("Do you want to read from a file (1) or write a small message in the console (2)? Type: ")
        if file_or_no == "1":
            while True:
                directory = input("Which file do you want to use? Include the whole directory: ")
                if '"' in directory:
                    directory = directory[1:-1]
                try:
                    message = open(directory, 'r')
                    name = input("What filename do you want to save your new file under? Type: ")
                    name = name + ".txt"
                    break
                except FileNotFoundError:
                    print("Invalid directory or file name, try again.")
            break
        elif file_or_no == "2":
            # Getting user string to be converted
            message = input("Message to be encrypted: ")
            break
        else:
            print("Invalid input.")
    print()

    # Getting lock
    while True:
        lock_1 = input("Lock or key in format (x, y): ")
        try:
            lock = lock_1[1:-1].split(",")
            e = int(lock[0])
            n = int(lock[1])
            break
        except ValueError:
            print("Invalid lock.")

    # Creating dictionary
    dictionary = {}
    characters = """QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()\x00\x1a_\xad+-=[]\{}\n|;:'<,>.?\t/`~ \""""
    characters = list(characters)
    for index, character in enumerate(characters):
        dictionary[character] = index

    # Getting multiprocessing power
    from multiprocessing import Pool
    from itertools import repeat

    if encrypt:
        # Switching char to num, performing math and then converting back to char
        if file_or_no == "1":
            with open(name, 'w') as new_file:
                for word in message:
                    char_nums = [dictionary[character] for character in word]
                    with Pool() as pool:
                        new_nums = pool.starmap(multiply_square_e, zip(char_nums, repeat(e), repeat(n)))
                        for new_num in new_nums:
                            new_file.write(str(new_num) + " ")

            # Returning Info
            print(f"Your encrypted message has been saved to a file named '{name}'.")
            print(f"It has been locked with {lock_1}.")

        elif file_or_no == "2":
            new_message = ""
            char_numbers = [dictionary[character] for character in message]
            with Pool() as pool:
                new_char_numbers = pool.starmap(multiply_square_e, zip(char_numbers, repeat(e), repeat(n)))
                for new_char_number in new_char_numbers:
                    new_message += str(new_char_number) + " "

            # Returning message encrypted
            print("The following is your encrypted message.")
            print(f"It has been locked with {lock_1}.")
            print()
            print(new_message)

    elif not encrypt:
        if file_or_no == "1":
            with open(name, 'w') as file:
                for row in message:
                    line = row.split(" ")[0:-1]
                    with Pool() as pool:
                        new_nums = pool.starmap(multiply_square_d, zip(line, repeat(e), repeat(n)))
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
                new_nums = pool.starmap(multiply_square_d, zip(message, repeat(e), repeat(n)))
                for new_num in new_nums:
                    for label, value in dictionary.items():
                        if value == new_num:
                            d_message += label

            # Returning info
            print("Your decoded message is as follows:")
            print()
            print(d_message)
