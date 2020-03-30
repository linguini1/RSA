# RSA Encryption software to just generate lock and key
from math import gcd as bltin_gcd

# Getting two valid primes
while True:
    p = input("First prime: ")
    q = input("Second prime: ")
    try:
        p = int(p)
        q = int(q)
        if p * q < 96 or p == 1 or q == 1 or p == q:
            print("The product of both primes must be larger than 96, they can't be equal, and no one can equal 1.")
        elif p * q > 96:
            break
    except ValueError:
        print("Invalid input. Primes must be integers.")


# Important numbers
n = p * q
coprimes = (p-1)*(q-1)


# Functions for finding coprimes of p and q
def coprime(num, n_or_num_of_coprimes):
    return bltin_gcd(num, n_or_num_of_coprimes) == 1


def finding_e():
    for num in range(2, n):
        if coprime(num, n) and coprime(num, coprimes):
            return num


# Getting coprimes to find e
e = finding_e()

# Making lock
lock = (e, n)


# Finding decryption key fxn
def find_d():
    for d_val in range(0, n):
        if (d_val * e) % coprimes == 1 and d_val != e:
            return d_val


# Making key
d = find_d()
key = (d, n)

# Returning data
print(f"The lock is: {lock}")
print(f"The key is: {key}")
