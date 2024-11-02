import math
def prime_factors(number):
    n = abs(number)
    prime_factors = set()
    # if divides just by prime number, you can check for half only !!
    while n % 2 == 0:
        prime_factors.add(2)
        n = n // 2

    for x in range(3, int(math.sqrt(n)) + 1):
        while n % x == 0:
            prime_factors.add(x)
            print(f"Range {n} changed, after finding {x} factor")
            n = n // x


    # If n is a prime number greater than 2
    if n > 2:
        prime_factors.add(n)
    return prime_factors


def main():
    print(prime_factors(15))
    print(prime_factors(12))
    print(prime_factors(129))
    #print(prime_factors(-765999))
    #lst = [-29804, -4209, -28265, -72769, -31744]
    #unique_primes = set()
    #for x in lst:
    #    unique_primes = unique_primes.union(prime_factors(x))
    #print(unique_primes)
if __name__ == "__main__":
    main()