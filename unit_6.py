# written by oliver hamburger

# program takes a max number and gereates all the prime numbers smaller than the max number


def get_list():
    """function takes max number from user and makes a list from 2 to the max number"""
    n = int(input("give the max number: "))
    original = list(range(2, n+1))
    return original


def put_in_prime(original):
    """function creats blank list and runs algorithm to find prime numbers. then it puts the
    primes in the primes list and removes the primes from the original list"""
    primes = []
    while len(original) > 0:
        temp = original[0]
        primes.append(temp)
        original.pop(0)
        for x in original:
            if x % temp == 0:
                original.remove(x)
    return primes


# function runs all other functions in order
def main():
    original = get_list()
    primes = put_in_prime(original)
    print("the list of primes is: " + str(primes))

main()
