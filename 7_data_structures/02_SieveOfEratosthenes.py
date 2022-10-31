# 3.1 - Sieve of Eratosthenes

# The sieve of Eratosthenes is a simple ancient method for finding all
# prime numbers up to any given limit.

# To implement the sieve, a list that stores whether a number is prime
# is created and initially filled with True for all values, except for
# indices 0 and 1. Starting from 2 (the first prime number), set all
# its multiples to False since they are non-prime (with 2as the
# divisor). Move on to the next available prime, 3, and set all
# its multiples  as non-prime. This is repeated until the last
# prime number is found.

# Create a function that returns all the prime numbers that are
# less than or equal to an input integer.

##### HOW TO DEFINE A PRIME NUMBER #####

def prime_num(num):
    if num > 1:
        for i in range(2, num // 2):
            if num % i == 0:
                print(num, 'is not a prime number')
                break
            else:
                print(num, 'is a prime number')
    elif num == 1:
        print(num, 'is not a prime number')
    elif num <= 3:
        print(num, 'is a prime number')

print(prime_num(7))

# https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/#:~:text=Sieve%20of%20Eratosthenes%20is%20a,to%20is%20prime%20or%20composite.

# Sieve of Eratosthenes is a method for finding all primes up to
# (and possibly including) a given natural. This method works well
# when is relatively small, allowing us to determine whether any
# natural number less than or equal to is prime or composite.

# Given a number n, print all primes smaller than or equal to n.
# It is also given that n is a small number. For instance here
# if n is 10, the output should be “2, 3, 5, 7”. If n is 20,
# the output should be “2, 3, 5, 7, 11, 13, 17, 19”.

# Python program to print all Primes Smaller
# than or equal to N using Sieve of Eratosthenes

def SieveOfEratosthenes(num):
    if num == 0 or num == 1:
        return False
    else:
        prime = [True for i in range(num+1)]
    #     boolean array
        p = 2
        while (p * p <= num):
    #   if prime[p] is not changed,
    #   then it is a prime

            if (prime[p] == True):
        #   updating all multiples of p
                for i in range(p * p, num+1, p):
                    prime[i] = False

            p += 1

    #     Print all prime numbers
        for p in range(2, num+1):
            if prime[p]:
                print(p)

print(SieveOfEratosthenes(7))

# Time Complexity: O(n*log(log(n)))
# Auxiliary Space: O(n)


##### OPTION 2 #####
def sieve_of_eratosthenes(n):
    #  this function must return a list of prime numbers that are below or equal to an input integer n.
    limitn = n+1
    primes = dict()
    for i in range(2, limitn):
        primes[i] = True

    for i in primes:
        factors = range(i, limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i] == True]

print(sieve_of_eratosthenes(14))