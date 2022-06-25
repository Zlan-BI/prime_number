# Buring question about how to get the prime numbers that are less than a certain target number


def prime_number(num):
    if num <= 1:
        return False
    if num >= 2:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True


def prime_number_list(num):
    lst = [num for num in range(2, num) if prime_number(num) == True]
    return lst


print(prime_number(49))
print(prime_number_list(101))
