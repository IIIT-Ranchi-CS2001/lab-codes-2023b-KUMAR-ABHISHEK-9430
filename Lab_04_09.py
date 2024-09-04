#  lab 2 STRING   MANIPULATUION

'''Question 1 = If the given string S1= “Maha Bharat”, generate the following strings by manipulating S1.
“mAHA bHARAT”
“Bharat”
“BharatBharatBharat”
“Mera Bharat”
“Mera Bharat Mahan”'''
#  Answer 1
S1 = "Maha Bharat"

# use swapcase to change case of string 
 
print(S1.swapcase())
print(S1[5:])
print(S1[5:]*3)
third = "Mera"+" " + S1[5:]
print(third)
print(third +' '+ "Mahan")



#   QUEStion  2

'''
For the given string S=”Ba Ba Black Sheep”, determine the following using built in functions:
The length of the string S
The first occurrence of the letter ‘e’
The total number of occurrences of ‘a’
Generate “Ta Ta Black Sheep”

'''

# Answer 2

S = 'Ba Ba Black Sheep'

print(len(S))

for index,i in enumerate(S):
    if i == "e":
        print(index)
        break

count =0
for i in S:
    if i =="a":
        count +=1
print(count)        

S_modi=S.replace("Ba","Ta")
print(S_modi)

# Question 3 

'''
Write a python script to enter any string at run time and check whether it is a palindrome or not.
'''
#  Answer

word = input("Enter the word: ")

size = len(word)

i = 0
j = size - 1

is_palindrome = True  

while i <= j:
    if word[i] == word[j]:
        i += 1
        j -= 1
    else:
        is_palindrome = False
        break

if is_palindrome:
    print("It's a palindrome")
else:
    print("Not a palindrome")
  


#  Question 4

'''

Enter the following details of a student at run time: - Name, Roll number and marks secured for Mathematics Examination out of 100. Write a python script to display student details as shown:
Name:
Roll Number:
Marks:
Grade Point:
Remark:


'''

#  Answer

print("Name : ",input("Enter name "))
print(" Roll no. :", input("Enter roll number "))
marks = int(input("Enter marks "))
print(marks)

if( marks>= 90):
    print("Grade Point : 10\n","Remarks = OUTSTANDING")
elif (80<=marks<90):
    print("Grade Point : 9\n","Remarks = VERY GOOD") 
elif (70<=marks<80):
    print("Grade Point : 8\n","Remarks =  GOOD") 
elif (60<=marks<70):
    print("Grade Point : 7\n","Remarks = AVERAGE") 
elif (50<=marks<60):
    print("Grade Point : 6\n","Remarks = PASS")             
elif (marks<50):
    print("Grade Point : 0", "Remarks = FAIL")


#Question 5

'''Write a program to find the roots of a quadratic equation when the coefficients a, b and c are given ( assume that a, b and c are integers)
Hint: find the discriminant d= b2 − 4ac
If d = 0, the equation has one real repeated root (both roots are the same: 
R1= R2 = -b/(2a)

If d > 0, the equation has two distinct real roots.
	R1= (-b + sqrt(d))/2a
R2= (-b - sqrt(d))/2a
 
If d < 0, the equation has two complex roots.
real_part = -b / (2 * a) 
imaginary_part = math.sqrt(-discriminant) / (2 * a)

''' 

#  Answer 5
import math
print("Enter a,b,c in a single line")
a,b,c = map(int,input().split())

d = (b**2) - (4*a*c)

if d ==0:
    print("R1=R2" ,-b/2*a)
elif d>0:
    print("R1 = ",(-b + math.sqrt(d))/(2*a))
    print("R2 ",(-b - math.sqrt(d))/(2*a))

else:
    print("Real part = ", -b/(2*a))
    print("Imaginary part = ",math.sqrt(-d)/(2*a))        
