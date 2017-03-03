from math import gcd, sqrt, factorial, cos, sin, tan, exp, log
from nbu_decorators import *
from random import randint, random


pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406


def are_coprime(a: int, b: int) -> bool:
    """ Return True if a is coprime with b, False otherwise.
        a and b are said to be coprime, or mutually prime if
        the only positive integer that divide both of them is 1.
    """
    return gcd(a, b) == 1


# def cos(x: float) -> float:
#     """ Return the cosine of x radians. """
#     # The value of an angle can't be greater than 2*pi
#     angle = x % (2 * pi)

#     # Remarquable angles
#     if angle == 0:
#         return 1
#     elif angle == pi / 2:
#         return 0
#     elif angle == pi:
#         return -1
#     elif angle == (3 * pi) / 2:
#         return 0

#     if angle > pi:
#         angle = -angle

#     # Computation with the Taylor serie of cos(x)
#     result = 0
#     for n in range(16):
#         result += (((-1)**n) / factorial(2 * n)) * (angle**(2 * n))
#     return result


# def exp(x: float) -> float:
#     """ Return e**x. """
#     if x == 0:
#         return 1

#     # Computation with the Taylor serie of exp(x)
#     result = 0
#     for n in range((x + 15) * 2):
#         result += (x**n) / (factorial(n))
#     return result


# def factorial(n: int) -> int:
#     """ Return the factorial of a number.
#         Raises ValueError if n is not integral or is negative.
#     """
#     if (n < 0) or (type(n) is not int):
#         raise ValueError

#     if n == 0:
#         return 0

#     product = 1
#     while n != 1:
#         product *= n
#         n -= 1
#     return product


def fibonacci(n: int) -> int:
    """ Return the n-th value of the Fibonacci serie in constant time.
        The Fibonacci serie is defined as follow:
        fibonacci(0) = 0
        fibonacci(1) = 1
        fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
        This function use a formula to approximate the n-th value of the
        Fibonacci serie.
    """
    if n < 0:
        raise ValueError(("fibonacci takes a positive integer as input,"
                          " you passed {}.").format(n))
    sqrt_5 = sqrt(5)
    return round(
        (pow((1 + sqrt_5) / 2, n) -
         pow((1 - sqrt_5) / 2, n)) / sqrt_5)


# def gcd(a: int, b: int) -> int:
#     """ Return the greatest common divisor between a and b. """
#     while a % b != 0:
#         a, b = b, (a % b)
#     return b


def generate_primes(ceil: int) -> list:
    """ Returns a list of primes below ceil.
        Based from this SO post :
        http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """
    sieve = [True] * (ceil // 2)
    sqrt_n_plus_1 = int(sqrt(ceil) + 1)
    for i in range(3, sqrt_n_plus_1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * \
                ((ceil - i * i - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, ceil // 2) if sieve[i]]


def generate_primes_in_range(floor: int, ceil: int) -> list:
    """ Return a list of all primes in the range(floor, ceil).
        Written by PM 2Ring 2014.10.15
    """
    def potential_primes() -> iter:
        """ Make a generator for 2, 3, 5, & thence all
            numbers coprime to 30.
        """
        s = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
        for i in s:
            yield i
        s = (1,) + s[3:]
        j = 30
        while True:
            for i in s:
                yield j + i
            j += 30

    # Mark all numbers as prime
    primes = [True] * (ceil - floor)
    # Eliminate 0 and 1, if necessary
    for i in range(floor, min(2, ceil)):
        primes[i - floor] = False
    ihi = int(ceil ** 0.5)
    for i in potential_primes():
        if i > ihi:
            break
        # Find first multiple of i: i >= i*i and i >= floor
        ilo = max(i, 1 + (floor - 1) // i) * i
        # Determine how many multiples of i >= ilo are in range
        n = 1 + (ceil - ilo - 1) // i
        # Mark them as composite
        primes[ilo - floor:: i] = n * [False]
    return [i for i, v in enumerate(primes, floor) if v]


def get_divisors_of(n: int, proper: bool = True) -> list:
    """ Return a list containing all the divisors of n. """
    if (n <= 0):
        n = abs(n)
    if proper:
        divisors = [1]
    else:
        divisors = [1, n]
    ceil = int(sqrt(n))
    for i in range(ceil, 1, -1):
        if is_divisible_by(n, i):
            divisors.append(i)
            divisors.append(n // i)
    return divisors


def get_number_of_divisors_of(n: int) -> int:
    """ Return the number of divisors of n. """
    if (n <= 0):
        return 0
    numberOfDivisors = 2
    ceil = int(sqrt(n))
    for i in range(ceil, 1, -1):
        if is_divisible_by(n, i):
            numberOfDivisors += 2
    return numberOfDivisors


def get_random_float(floor: float, ceil: float) -> float:
    """ Return a random float between 'floor' inclusive and 'ceil'
        exclusive.
    """
    return (random() * (ceil - floor)) + floor


def get_random_integer(floor: int, ceil: int) -> int:
    """ Return a random integer between 'floor' inclusive and 'ceil'
        exclusive.
    """
    return randint(floor, ceil)


def is_a_palindrome(string: str) -> bool:
    """ Return True if string is a palindrome, False otherwise.
        A palindrome is a string who can be read the same both
        ways.
    """
    return string == ''.join(reversed(string))


def is_a_palindromic_number(n: int) -> bool:
    """ Return True if n is a palindromic number, False otherwise.
        A palindromic number is a number whose digits can be read
        the same both ways.
    """
    return is_a_palindrome(str(n))


def is_divisible_by(n: int, divisor: int) -> bool:
    """ Return True if n is divisible by divisor, False otherwise. """
    return n % divisor == 0


def is_divisor_of(potential_divisor: int, n: int) -> bool:
    """ Return True if n is divisible by potential_divisor,
        False otherwise.
    """
    return n % potential_divisor == 0


def is_even(n: int) -> bool:
    """ Return True if n is even, False otherwise. """
    return bin(n).endswith("0")


def is_odd(n: int) -> bool:
    """ Return True if n is odd, False otherwise. """
    return bin(n).endswith("1")


def is_prime(n: int) -> bool:
    """ Return True if n is a prime number, False otherwise.
        To optimize the program, we first check if n is even,
        and iterate only with odd numbers until the square root of n.
        We also store this square root on a variable, saving lot
        of CPU's power because the formula is not
        calculated for each iteration.
    """
    if (n <= 1 or (is_even(n) and n != 2)):
        return False
    divisor = 3
    floor = sqrt(n)
    while (divisor < floor):
        if is_divisible_by(n, divisor):
            return False
        divisor += 2
    return True


def lcm(a: int, b: int) -> int:
    """ Return the least common divisor between a and b. """
    return int((a * b) / gcd(a, b))


# def ln(x: float) -> float:
#     """ Return the value of the natural logarithm of x. """
#     if x <= 0:
#         raise ValueError
#     if x == 1:
#         return 0

#     # Computation with the Taylor serie of ln(x)
#     result = 0
#     for n in range((x + 15) * 2):
#         result += (((x - 1) / (x + 1))**((2 * n) + 1)) / ((2 * n) + 1)
#     return 2 * result


# def log(x: float, base: int) -> float:
#     """ Return the logarithm of x to the given base. """
#     if base == 1:
#         raise ValueError
#     return ln(x) / ln(base)


# def sin(x: float) -> float:
#     """ Return the sine of x radians. """
#     # The value of an angle can't be greater than 2*pi
#     angle = x % (2 * pi)

#     # Remarquable angles
#     if angle == 0:
#         return 0
#     elif angle == pi / 2:
#         return 1
#     elif angle == pi:
#         return 0
#     elif angle == (3 * pi) / 2:
#         return -1

#     if pi / 2 < angle < (3 * pi) / 2:
#         angle = -angle

#     # Computation with the Taylor serie of sin(x)
#     result = 0
#     for n in range(16):
#         result += (((-1)**n) / factorial(2 * n + 1)) * (angle**(2 * n + 1))
#     return result


# def tan(x: float) -> float:
#     """ Return the tangent of x radians. """
#     if (x % 2 * pi) == ((pi / 2) or ((3 * pi) / 2)):
#         raise ValueError
#     return sin(x) / cos(x)


@todo_implement
def get_all_coprime_with(n: int) -> list:
    """ Return a list containing all the positive
        integers who are coprime with b.
        a and b are said to be coprime, or mutually prime if
        the only positive integer that divide both of them is 1.
    """
    pass


@todo_implement
def get_the_number_of_coprime_with(n: int) -> int:
    """ This function use the Euler's totient function formula
        and return the number of integers coprime with n.
    """
    n_in_primes_factor = get_product_of_primes_factors_form_of(n)
    phi_n = n
    for prime in n_in_primes_factor.keys():
        phi_n *= (1 - (1 / prime))
    return int(phi_n)


@todo_implement
def get_product_of_primes_factors_form_of(n: int) -> list:
    """ Every integer n can be written in the form of an unique
        product of primes factors.
        Return a dict containing the decomposition of primes
        factors of the number n.
        Example :
        get_product_of_primes_factors_form_of(20) = 2^2 * 5^1
                                                  ={2:2,  5:1}
    """
    primes_factor = {}
    if (not n) or (n < 2):
        return primes_factor
    for i in range(2, n + 1):
        while (is_divisible_by(n, i)):
            if (i in primes_factor):
                primes_factor[i] += 1
            else:
                primes_factor[i] = 1
            n /= i
    return primes_factor


@todo_implement
def print_product_of_primes_factors_form_of(n: int) -> None:
    """ This function is meant to be used with the
        get_product_of_primes_factors_form_of function.
        It print the dictionary the previous function return as
        an argument and print it in a more readable form.
    """
    product_of_primes_factors = get_product_of_primes_factors_form_of(n)
    string = ""
    for prime in product_of_primes_factors.keys():
        string += str(prime) + "^" + \
            str(product_of_primes_factors[prime]) + " x "
    print(str(n), "=", string[:-3])


if __name__ == '__main__':
    pass
