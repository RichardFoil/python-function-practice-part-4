#Write a Python function called max_num()to find the maximum of three numbers.
def max_num(*args):
    print(max(args))

max_num(12,55,32,83)

#Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(list):

    product = 1
    for x in list:
        product = product * x
    print(product)

list1 = [2, 3, 4]

mult_list(list1)

#Write a Python function called rev_string() to reverse a string.
def rev_string(str):
    print(str[::-1])

rev_string("My Name is Rich")

#Write a Python function called num_within() to check whether a number falls in a given range.
#The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
def num_within(x,a,b):
    print( x in range(a,b+1))

num_within(5,3,10)

#Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
#The function accepts the number n, the number of rows to print

def pascal(n):
    for i in range(1, n+1):
        for x in range(0, n-i+1):
            print('', end='')
        
        C = 1 
        for x in range(1, i+1):
            print('',C,sep='',end='')
            C= C * (i-x) // x
        print()
pascal(5)