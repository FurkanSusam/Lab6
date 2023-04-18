import math
#Question 1 :
n = int(input("Please enter a number for solve this e^n = 1 + n/1! + n^2/2! + ... + n^x/x! \n"))
x = int(input("Please enter a number for solve this e^n = 1 + n/1! + n^2/2! + ... + n^x/x! \n"))
result = 1
temp = lambda k,l : \
    int(k)**int(l) / math.factorial(l)
for k in range(1,int(x)+1):
    result = result + temp(n,k)
print(result)

#Question 2 :
print("________________Question 2_______________")

sum = 0

def function(n):
    ''' These functions sum the numbers up to the given step size'''
    global sum
    while (n > 0):

        temp = lambda j:  (-1) ** (j+1) / j
        sum = sum + temp(n)
        n = n - 1

print(function.__doc__)

x = int(input("Please enter the step size of the function \n"))
function(x)
print(sum)