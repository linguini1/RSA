# RSA Encryption Method


# Euclidean algorithm

def euclidAlg(e, n, character):
    original_num = 1
    for _ in range(e):
        original_num = (original_num * character) % n
    return original_num


if __name__ == '__main__':
    # Read from file or small message
    while True:
        file_or_no = input("Do you want to read from a file (1) or write a small message in the console (2)? Type: ")
        if file_or_no == "1":
            while True:
                directory = input("Which file do you want to use? Include the whole directory: ")
                if '"' in directory:
                    directory = directory[1:-1]
                try:
                    message = open(directory, 'r')
                    name = input("What filename do you want to save your encryption under? Type: ")
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
        lock_1 = input("Lock in format (x, y): ")
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

    # Switching char to num, performing math and then converting back to char
    if file_or_no == "1":
        with open(name, 'w') as new_file:
            for word in message:
                char_nums = [dictionary[character] for character in word]
                with Pool() as pool:
                    new_nums = pool.starmap(euclidAlg, zip(repeat(e), repeat(n), char_nums))
                    for new_num in new_nums:
                        new_file.write(str(new_num) + " ")

        # Returning Info
        print(f"Your encrypted message has been saved to a file named '{name}'.")
        print(f"It has been locked with {lock_1}.")

    elif file_or_no == "2":
        new_message = ""
        for character in message:
            char_number = dictionary[character]
            new_char_number = (char_number ** e) % n
            new_message += str(new_char_number) + " "

        # Returning message encrypted
        print("The following is your encrypted message.")
        print(f"It has been locked with {lock_1}.")
        print()
        print(new_message)
