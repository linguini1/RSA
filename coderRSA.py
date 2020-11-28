# RSA Encryption Method

# Imports

# Default file name
name = "RSA_file.txt"


# Multiply & Square algorithm allowing for much faster encryption and decryption

def multiply_square_e(base, power, modulo):
    result = 1
    for binary in str(format(power, 'b')):

        # If the bit is zero, then it just gets set to the power of two, mod modulo
        if binary == "0":
            result = (result ** 2) % modulo

        # If the bit is one, then it gets multiplied by the base as well
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

    # Asks user if they want to encrypt their data or decrypt their data
    while True:
        encrypt = input("Do you want to encrypt or decrypt? (Type the word): ")
        if encrypt.lower() == "encrypt":
            encrypt = True
            break
        elif encrypt.lower() == "decrypt":
            encrypt = False
            break
        else:
            print("Invalid input.")

    # Asks user if they want to use data from a text file or just type within the console
    while True:
        file_or_no = input("Do you want to read from a text file (1) or write a small message in the console (2)? Type: ")

        # Reading from a text file
        if file_or_no == "1":

            # Gets a valid directory
            while True:
                directory = input("Which file do you want to use? Include the whole directory: ")

                # If the path is contained in quotation marks, they're removed so that the program works properly
                if '"' in directory:
                    directory = directory[1:-1]
                try:
                    message = open(directory, 'r')
                    # Gets the filename from the user
                    name = input("What filename do you want to save your new file under? Type: ")
                    name = name + ".txt"  # Adds the necessary .txt suffix
                    break

                # If the path is invalid the user is re-prompted
                except FileNotFoundError:
                    print("Invalid directory or file name, try again.")
            break

        # Reading from the console
        elif file_or_no == "2":
            # Getting user string to be converted
            message = input("Message to be encrypted or decrypted: ")
            break

        # If the user selects an option other than 1 or 2
        else:
            print("Invalid input.")
    print()  # Print a line break

    # Getting lock
    while True:
        lock_1 = input("Lock or key in format (x, y): ")
        try:
            lock = lock_1[1:-1].split(",")  # Removes the brackets and comma
            e = int(lock[0])  # Sets the x value as an integer for e
            n = int(lock[1])  # Sets the y value as an integer for n
            break

        # If the lock format is incorrect
        except ValueError:
            print("Invalid lock.")

    # Creating dictionary
    dictionary = {}
    characters = """abcdef1234567890"""
    characters = list(characters)

    # Gives each character its own index to be used for mathematical operations
    for index, character in enumerate(characters):
        dictionary[character] = index

    # Getting multiprocessing power
    from multiprocessing import Pool
    from itertools import repeat

    # If the user selected encryption:
    if encrypt:

        # If reading from a text file
        if file_or_no == "1":

            # Switching char to num, performing math
            with open(name, 'w') as new_file:

                # Making a list of the indexes
                for line in message:
                    char_nums = [dictionary[character] for character in line.encode("utf-8").hex()]

                    with Pool() as pool:  # Opening multithreading

                        # Passes in the indexes, e & n values to the multiply and square algorithm as iterables
                        new_nums = pool.starmap(multiply_square_e, zip(char_nums, repeat(e), repeat(n)))

                        # Saving the encrypted number to the file
                        for new_num in new_nums:
                            new_file.write(str(new_num) + " ")

            # Returning Info
            print(f"Your encrypted message has been saved to a file named '{name}'.")
            print(f"It has been locked with {lock_1}.")

        # If reading from console
        elif file_or_no == "2":
            new_message = ""  # Empty string variable to save the encrypted message
            char_numbers = [dictionary[character] for character in message.encode("utf-8").hex()]  # Getting list of indexes
            with Pool() as pool:  # Opening multithreading

                # Passes in the indexes, e & n values to the multiply and square algorithm as iterables
                new_char_numbers = pool.starmap(multiply_square_e, zip(char_numbers, repeat(e), repeat(n)))

                # Saving the encrypted message to the empty string variable
                for new_char_number in new_char_numbers:
                    new_message += str(new_char_number) + " "

            # Returning message encrypted
            print("The following is your encrypted message.")
            print(f"It has been locked with {lock_1}.")
            print()
            print(new_message)

    # If the user selected decryption
    elif not encrypt:

        # From a text file
        if file_or_no == "1":
            with open(name, 'w') as file:
                for row in message:
                    line = row.split(" ")[0:-1]  # Removes the spaces between numbers
                    with Pool() as pool:  # Opening multithreading

                        # Passes in the line of numbers, e & n values as iterables to the multiply and square algorithm
                        new_nums = pool.starmap(multiply_square_d, zip(line, repeat(e), repeat(n)))

                        # Decrypted index is matched to the dictionary character and then written into the hex list
                        hexed_line = ""  # Empty string for carrying a hexed line
                        for new_num in new_nums:
                            for label, value in dictionary.items():
                                if value == new_num:
                                    hexed_line += label

                        # Write to file
                        file.write(str(bytes.fromhex(hexed_line).decode("ASCII")))

            # Returning info
            print(f"Your message has been decoded and saved under filename '{name}'.")
            print()

        # From the console
        elif file_or_no == "2":
            d_message = ""  # Empty string variable to hold the decryption
            with Pool() as pool:  # Getting multithreading power

                # Passing in the message, the e & n values as iterables to the multiply and square algorithm
                new_nums = pool.starmap(multiply_square_d, zip(message.split(" "), repeat(e), repeat(n)))

                # Matches decrypted index to the dictionary character and then adds it to the empty string
                for new_num in new_nums:
                    for label, value in dictionary.items():
                        if value == new_num:
                            d_message += label

            # Returning info
            print("Your decoded message is as follows:")
            print()
            print(str(bytes.fromhex(d_message))[2:-1])  # Convert back from hex first
