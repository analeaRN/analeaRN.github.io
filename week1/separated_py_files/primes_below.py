import is_prime 

def primes_below(n):
    result = []

    if n <= 1:
        return result
    
    for count in range(2, n):
        if is_prime.is_prime(count):
            result.append(count)

    return result