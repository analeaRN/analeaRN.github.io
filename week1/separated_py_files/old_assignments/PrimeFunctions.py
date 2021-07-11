

def primes(n):
    """
     Assignment 2.4

     takes a number n as an input, and outputs all prime numbers from 1 to n.  
     (Remember: a prime number is a whole number greater than 1 which is divisible only by 1 and itself.)  
     For instance, primes(10) should return the list [2,3,5,7]
    """
    result = []

    if n <= 1:
        return result
    
    for count in range (2, n):
        if is_prime(count):
            result.append(count)

    return result

def prime_factorization(n):
    """
     Assignment 2.5

     Probably better to have made this a class, if this was meant to be done multiple times.
     So I would have saved prime numbers encountered, to be easily retrieved.
    """
    if n < 0 :
        return []
    if is_prime(n):
        return [n]
    
    # how to find Prime Factorization 
    # https://www.mesacc.edu/~scotz47781/mat120/notes/radicals/simplify/images/examples/prime_factorization.html

    result = []
    list_primes = primes(n)
    def getA():
        return list_primes[a]
    
    a = 0  # holds the index of which prime we are at
    b = n
    while True:
        temp = b / getA()
        if getA() in list_primes and temp in list_primes:  # base case, recursion?
            result.append(getA())
            result.append(int(temp))
            break
        elif temp % int(temp) == 0:  
            # no remainder, keep dividing by the same prime
            result.append(getA())
            b = temp
        elif temp % int(temp) != 0: 
            # if there is a remainder, and b is not prime, find next prime to divide by
            a += 1

    return result

print("Is 7 prime?", is_prime(7))
print("What are the prime numbers from 1 to 10?", primes(10))
print("What is the prime factorization of 120?", prime_factorization(120))