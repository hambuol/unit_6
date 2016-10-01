#written by oliver hamburger
#program takes a max number and gereates all the prime numbers smaller than the max number

def get_list():
    n = int(input("give the max number"))
    my_list = list(range(2,n+1))
    return(my_list)

my_list = get_list()

print(my_list)