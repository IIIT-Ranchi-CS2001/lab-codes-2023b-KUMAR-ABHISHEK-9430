# #  WAP to write square of n natural numbers

# user_input = int(input("Enter the number"))

# n=1
# print("Number ", " Square")
# while(n<=user_input):
#     print(n ,"        ",n**2)
#     n+=1


# # WAP to display sum of digits of a n kvhh6umber

# user_input_num = int(input("Enter the number"))
# sum =0

# while(user_input_num > 0):
#     rem = user_input_num%10
#     sum+=rem
#     user_input_num = user_input_num//10
# print(sum)

# # WAP to write n terms of fibonnaci series

# # Function to print Fibonacci series up to n terms
# def fibonacci(n):
#     # First two terms
#     a, b = 0, 1
#     if n <= 0:
#         print("Please enter a positive integer.")
#     elif n == 1:
#         print("Fibonacci sequence up to", n, "is:")
#         print(a)
#     else:
#         print("Fibonacci sequence:")
#         for i in range(n):
#             print(a, end=" ")
#             # Update the values of a and b
#             a, b = b, a + b

# # Input number of terms
# n = int(input("Enter the number of terms: "))
# fibonacci(n)

#WAP to write table of a number
print("Enter the number and till when in single line")
table,upto = map(int,input().split())

for i in range(upto):
    print(f"table X {i+1} = ",table*(i+1))


#  Wap to check alpha numeric

string = input("Enter any input")

flag = True

for i in string:
    if not i.isalnum():
        flag = False

if not flag:
    print("not a alphanumeric input")
else:
    print("Input is alphanumeric")


#  WAP to count occurance in string

def count_occurrences(input_string, target_char):
    
    count = 0

   
    for char in input_string:
        
        if char == target_char:
            count += 1

    return count


input_string = "hello world"
target_char = 'o'
result = count_occurrences(input_string, target_char)
print(f"The character '{target_char}' appears {result} time(s) in the string.")
