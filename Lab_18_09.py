#  Wap to find palindrome word in a sentence

sentence = input("Write a sentence")

def palindrome(word):
    if (word == word[::-1]):
        return True
    else:
        return False


count =0 
for word in sentence.split():
    if palindrome(word):
        count +=1      

print("Palindrome count is ", count)

# Create list using list compreshension and find mean, median, mode
import statistics
lst =[int(i) for i in input().split()]

print("mean", statistics.mean(lst))
print("Median", statistics.median(lst))
print("Mode", statistics.mode(lst))

#  Make dictionary from list

course_code = input("Enter course code")
course_name = input("Enter name of course")
lst_1 = [course_code for course_code in course_code.split()]
lst_2 = [course_name for course_name in course_name.split()]

print(list(zip(lst_1,lst_2)))


