
# 630 2
# 315 3
# 105 3
# 35  5
# 7   7

def get_prime_factors(number: int):
    factors = []
    divisor = 2

    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number = number // divisor
        else:
            divisor += 1
    return factors


print(get_prime_factors(630))
print(get_prime_factors(13))
print(get_prime_factors(3))

# quick test
print([2, 3, 3, 5, 7] == get_prime_factors(630))
print([13] == get_prime_factors(13))
