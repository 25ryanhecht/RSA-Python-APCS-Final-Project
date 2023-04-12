Author: Ryan Hecht
Title: RSA Python

	This is an RSA implementation in python that attempts to be secure. It uses cryptographically secure random numbers to generate large prime numbers to use in the RSA encryption algorithm. It uses the Miller-Rabin primality test to find probable primes, decreasing the amount of time needed to find a large prime when compared to a deterministic algorithm. This should NEVER be trusted for any actual usage, as it is probably not secure.
