# RSA Encryption software to just generate lock and key

# Imports
from math import gcd as bltin_gcd  # For finding the co-primes

# Getting two valid primes
while True:
    p = input("First prime: ")
    q = input("Second prime: ")
    try:
        p = int(p)
        q = int(q)

        # The factor of the primes must be at least 96
        # Neither of the primes can be 1
        # The primes can't form a perfect square
        if p * q < 96 or p == 1 or q == 1 or p == q:
            print("The product of both primes must be larger than 96, they can't be equal, and no one can equal 1.")
        elif p * q > 96:
            break

    # Catches non-integer inputs
    except ValueError:
        print("Invalid input. Primes must be integers.")


# Important numbers
n = p * q  # The actual product of the primes
coprimes = (p-1)*(q-1)  # The number of coprimes


# Function for finding co-prime of a number
def co_prime(num, n_or_num_of_coprimes):
    return bltin_gcd(num, n_or_num_of_coprimes) == 1


# Finds a number which is both co-prime with n and the number of coprimes
def finding_e():
    for num in range(2, n):
        if co_prime(num, n) and co_prime(num, coprimes):
            return num


# Getting co-primes to find e
e = finding_e()

# Making lock
lock = (e, n)


# Finding decryption key using the formula for RSA
def find_d():
    for k in range(e):
        if (1 + k * coprimes) % e == 0:
            d = (1 + k * coprimes) / e
            return int(d)
        else:
            pass


# Making key
d = find_d()
key = (d, n)

# Returning data
print(f"The lock is: {lock}")
print(f"The key is: {key}")
