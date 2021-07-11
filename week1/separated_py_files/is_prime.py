def is_prime(check_prime):
    for count in range(2, check_prime):
        if check_prime % count == 0:
            return False
    return True