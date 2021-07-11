import primes_below

def palindrome_primes(n=100000):
    # make this method using the methods we used in
    # our last assignment. It would be better to cashe primes for future use.
    primes = primes_below.primes_below(n)
    # print(f'{primes=}')

    result = []
    
    index = len(primes) - 1
    
    while True:
        string_current = str(primes[index])
        if len(string_current) != len(str(n - 1)):
            break
        if is_palindrome(str(string_current)):
            result.append(primes[index])
        index -= 1
    
    print(result[::-1])
    
    
def is_palindrome(string):
    left = 0
    right = len(string) - 1
    
    while left <= right:
        if string[left] != string[right]:
            return False
        right -= 1
        left += 1
    
    return True

palindrome_primes()