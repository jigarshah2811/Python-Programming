"""
FIND ALL PRIME NUMBERS till n

https://www.geeksforgeeks.org/sieve-of-eratosthenes/

"""
n = 100


# Create a boolean array "prime[0..n]" and initialize
#  all entries it as true. A value in prime[i] will
# finally be false if i is Not a prime, else true.
primes = [True] * (n+1)

# All even numbers are NOT prime
for i in xrange(n):
    if i%2 == 0:
        primes[i] = False

# All numbers multiply by 3 and 5 and ongoing primes are NOT prime
p = 3
while p*p <= n:
    # If prime[p] is not changed, then it is a prime
    if primes[p] == True:

        # Update all multiples of P
        for multiplier in xrange(p*3, n+1, p):
            primes[multiplier] = False
    p += 1

for p in xrange(2, n):
    if primes[p]:
        print p,