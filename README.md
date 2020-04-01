# RSA
RSA encryption program written in python.

# Instructions
In order to use the program, you must first create the lock and key using dataRSA.py.
The program will ask for two prime numbers; the larger your primes are the more difficult it will be to break your encryption.

Once you have your data, you may encrypt files with encrypterRSA.py by inputting the lock you were given.
These files can also be decrypted with decrpyterRSA.py, using the key as input.

# Notes
- The encryption and decryption programs make use of multiprocessing, so be ready for 100% CPU usage when using them.

- The lock and key are interchangeable, meaning you can encrypt files using the key and decrypt them using the lock.

- The time for encryption or decryption is proportional to the size of the x value in the lock or key of format (x, y).

- So, if you have lots of time to encrypt but you want decryption to be faster, use the set with the LARGER x value as the lock and the SMALLER x value as the key. This works vice versa. Just note that using a smaller x value for decryption makes the prime factors more apparent and makes your encryption LESS SECURE.

# Feedback?
If you have any feedback for me in regards to making the programs more efficient, please add an issue to the repository.
