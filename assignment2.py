def check_prime(x):
    if x > 2 and x % 2 == 0:
        return False
    elif x < 2:
        return False
    else:
        for i in range(2, int(sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

print(check_prime(12000))