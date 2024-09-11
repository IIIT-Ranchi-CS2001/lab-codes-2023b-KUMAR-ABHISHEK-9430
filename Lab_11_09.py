#  WAP to write square of n natural numbers

user_input = int(input("Enter the number"))

n=1
print("Number ", " Square")
while(n<=user_input):
    print(n ,"        ",n**2)
    n+=1


# WAP to display sum of digits of a n kvhh6umber

user_input_num = int(input("Enter the number"))
sum =0

while(user_input_num > 0):
    rem = user_input_num%10
    sum+=rem
    user_input_num = user_input_num//10
print(sum)

# WAP to write n terms of fibonnaci series

# Function to print Fibonacci series up to n terms
def fibonacci(n):
    # First two terms
    a, b = 0, 1
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print("Fibonacci sequence up to", n, "is:")
        print(a)
    else:
        print("Fibonacci sequence:")
        for i in range(n):
            print(a, end=" ")
            # Update the values of a and b
            a, b = b, a + b

# Input number of terms
n = int(input("Enter the number of terms: "))
fibonacci(n)

