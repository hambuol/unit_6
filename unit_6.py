#written by oliver hamburger
#program takes a max number and gereates all the prime numbers smaller than the max number

def get_list():
    n = int(input("give the max number"))
    original = list(range(2,n+1))
    return(original)


original = get_list()
print(original)

