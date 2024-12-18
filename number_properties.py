def getFactors(x):
    """Function that returns a list of factors of a given number x.
    Finds the numbers between 1 and the given integer that divide the number evenly.

    For example:
    - If we call getFactors(2), we'll get [1, 2] in return
    - If we call getFactors(12), we'll get [1, 2, 3, 4, 6, 12] in return
    """
    
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    return factors

def isPrime(x):
    """Function that returns whether or not the number x is prime. This function returns a boolean.

    A prime number is a natural number greater than 1 that cannot be formed by multiplying two
    smaller natural numbers.

    For example:
    - Calling isPrime(11) will return True
    - Calling isPrime(71) will return True
    - Calling isPrime(12) will return False
    - Calling isPrime(76) will return False
    """

    # Numbers less than 2 are not prime
    if x < 2:
        return False

    # Check for divisibility from 2 to the square root of x
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    
    return True

def isComposite(x):
    """Function that returns whether or not the given number x is composite. This function returns a
    boolean.

    A composite number has more than 2 factors.
    A natural number greater than 1 that is not prime is called a composite number.
    Note, the number 1 is neither prime nor composite.

    For example:
    - Calling isComposite(9) will return True
    - Calling isComposite(22) will return True
    - Calling isComposite(3) will return False
    - Calling isComposite(44) will return False
    """

    return x > 1 and not isPrime(x)

def isPerfect(x):
    """Function that returns whether or not the given number x is perfect. This function returns
    a boolean.

    A number is said to be perfect if it is equal to the sum of all its factors (for obvious
    reasons the list of factors being considered does not include the number itself).

    Example: 6 = 3 + 2 + 1, hence 6 is perfect.
    Example: 28 is another example since 1 + 2 + 4 + 7 + 14 is 28.
    Note, the number 1 is not a perfect number.
    """

    # Get all factors except the number itself
    factors = getFactors(x)[:-1]

    return sum(factors) == x

def isAbundant(x):
    """Function that returns whether or not a given number x is abundant. This function returns
    a boolean.

    A number is considered to be abundant if the sum of its factors (aside from the number) is
    greater than the number itself.

    Example: 12 is abundant since 1 + 2 + 3 + 4 + 6 = 16 > 12.
    However, a number like 15, where the sum of the factors is 1 + 3 + 5 = 9 is not abundant.
    """

    # Get all the factors except the number itself
    factors = getFactors(x)[:-1]

    # Check if sum of factors is greater than the number
    return sum(factors) > x

def isTriangular(x):
    """Function that returns whether or not a given number x is triangular. This function returns
    a boolean.

    The triangular number Tn is a number that can be represented in the form of a triangular grid
    of points where the first row contains a single element and each subsequent row contains one
    more element than the previous one.

    We can just use the fact that the nth triangular number can be found by using a formula:
    Tn = n(n + 1)/2.

    Example: 3 is triangular since 3 = 2(3) / 2
    3 --> 2nd position: (2 * 3 / 2)

    Example: 15 is triangular since 15 = 5(6) / 2
    15 --> 5th position: (5 * 6 / 2)
    """

    
    # Solve the quadratic equation: x = n(n+1)/2
    # Rearranged: n^2 + n - 2x = 0

    for n in range(1, x + 1):
        if n * (n + 1) // 2 == x:
            return True
    return False

def isNarcissistic(x):
    """"Function that returns whether or not a given number is narcissistic. This function returns
    a boolean.

    A positive integer is called a narcissistic number if it is equal to the sum of its own digits
    each raised to the power of the nymber of digits.

    Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
    Note that by this definition all single digit numbers are narcissistic.
    """

    # Convert number to string to easily iterate through digits
    str_x = str(x)
    num_digits = len(str_x)

    # Sum of each digit raised to the power of the number of digits
    narcissistic_sum = sum(int(digit) ** num_digits for digit in str_x)

    return narcissistic_sum == x

def main():
    playing = True
    while playing == True:
        num_input = input("Give me a number from 1 to 10000. Type -1 to exit.")
        try:
            num = int(num_input)
            if (num == -1):
                playing = False
                continue
            if (num <= 0 or num > 10000):
                continue
            factors = getFactors(num)
            print("The factors of ", num, " are ", factors)

            if isPrime(num):
                print(str(num) + " is prime")

            if isComposite(num):
                print(str(num) + " is composite")

            if isPerfect(num):
                print(str(num) + " is perfect")

            if isAbundant(num):
                print(str(num) + " is abundant")

            if isTriangular(num):
                print(str(num) + " is triangular")

            if isNarcissistic(num):
                print(str(num) + " is narcissistic")

        except ValueError:
            print("Invalidf input. Please enter a valid number.")

# Run the main function
if __name__ == "__main__":
    main()


    
