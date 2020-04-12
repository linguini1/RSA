# RSA
RSA encryption & decryption program written in python.

# Disclaimer
This program is NOT meant as a replacement for actual RSA encryption. It is most definitely not secure, and serves only as a proof of concept/experiment. Please do not encrypt any meaningful data with this program and assume it is safe.

# Instructions
In order to use the program, you must first create the lock and key using dataRSA.py.
The program will ask for two prime numbers; the larger your primes are the more difficult it will be to break your encryption.

Once you have your data, you may encrypt files with encrypterRSA.py by inputting the lock you were given.
These files can also be decrypted with decrpyterRSA.py, using the key as input.

# Notes
- The encryption and decryption programs make use of multiprocessing, so be ready for 100% CPU usage when using them.

- The lock and key are interchangeable, meaning you can encrypt files using the key and decrypt them using the lock. It is not a good idea though.

# Feedback?
If you have any feedback for me in regards to making the programs more efficient, please add an issue to the repository.
