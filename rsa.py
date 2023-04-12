#!/usr/bin/env python3
import random

# TODO: change to use 4096bit
# TODO: find d

def gcd(a, b):
    # find gcd of a & b
    # uses the euclidean algorithm
    while b: # b != 0
        a, b = b, a % b
    return a

def millerRabin(n, k):
    """
    Based on:
    https://rosettacode.org/wiki/Miller–Rabin_primality_test
    """

    # use the Miller-Rabin Primality Test to return True if n is probably prime, or False if n is definitely composite
    # uses k rounds

    # find s and d so that: n - 1 = (2^s) * d
    # s must be a positive int
    # d must be an odd positive int
    s = 0
    d = n - 1
    while d % 2 == 0: # while d is even
        d>>=1 # bitwise right shift to divide d by 2
        s+=1 # increment s by 1

    def testComposite(a):
        # test if n is composite with base a, by testing following conditions:
        # a^d === 1 (mod n)
        # a^((2^r) * d) === -1 (mod n) for some 0<=r<s
        if pow(a, d, n) == 1: # if a^d % n == 1
            return False # n is strong probable prime to base a
        for r in range(s):
            if pow(a, 2**r * d, n) == n - 1: # if a^((2^r) * d) % n == - 1
                return False # n is strong probable prime to base a
        return True # n failed the tests, so n is definitely composite

    for r in range(k): # k being the number of trials
        a = random.randrange(2, n) # in range of 2, n-1
        if testComposite(a):
            return False # n is deemed composite by the tests

    return True # n passed all tests, so it is probably prime

def isPrime(n, k):
    # return true if n is probably prime, and false if n is definitely composite
    # use k rounds in miller rabin test

    # all primes < 1000
    primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    if n in primeList: # if n is in primeList
        return True # n is definitely prime

    for prime in primeList:
        if n % prime == 0:
            return False # n is composite

    if not millerRabin(n, k):
        return False # n is definitely composite

    return True # n passed tests, it is probably prime

def primeFinder(b, k):
    # find a prime of b bits using the miller rabin primality test with k rounds


    while True:
        n = random.SystemRandom().getrandbits(b) # random num of b bits
        if isPrime(n, k):
            return n # n is probably prime, so return n

def encrypt(plaintext, pubKey):
    # encrypt the given plaintext with the public key
    e, n = pubKey # derive e and n from the public key

    ciphertext = [] # encrypted text stored as a list of integers (representing characters)

    for char in plaintext:
        ciphertext.append(pow(ord(char), e, n)) # calculate the new value of the character as (char^e) % n

    return ciphertext # return the encrypted message

def decrypt(ciphertext, privKey):
    # decrypt the given ciphertext using the private key
    d, n = privKey # derive d and n from the private key

    plaintext = [] # plaintext stored as a list of integers (representing characters)

    for char in ciphertext:
        plaintext.append(chr(pow(char, d, n))) # calculate the new value of the character as (char^d) % n

    return ''.join(plaintext)

if __name__ == "__main__":
    p = primeFinder(1024, 40) # find a prime
    q = primeFinder(1024, 40) # find a prime

    n = p * q # compute n

    phi = (p - 1) * (q - 1)

    while True:
        e = random.randrange(3, phi)
        if gcd(e, phi) == 1:
            break

    d = pow(e, -1, phi) # compute d as the modular multiplicitive inverse of e % phi

    pubKey = [e, n] # set the public key
    privKey = [d, n] # set the private key

    plaintext = input("Enter the plaintext to be encrypted: ")

    # print("p: {0}\nq: {1}\nn:{2}\nphi: {3}\ne: {4}\nd: {5}".format(p, q, n, phi, e, d))
    print("pubKey: {0}\nprivKey: {1}".format(pubKey, privKey))

    ciphertext = encrypt(plaintext, pubKey)

    print("ciphertext: {}".format(ciphertext))

    print("decrypted: {}".format(decrypt(ciphertext, privKey)))
