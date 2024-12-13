# Define a function my_zip() that can form a list of tuples by iterating the following customer details:- ‘customer Name, customer ID , shopping points’ and based on the keyword parameter ‘strct’: If strct = True, zipping shall be done only if all lists are of equal length. If strct = False, zipping can be done by taking the minimum length of the iterable.


def my_zip(customer_name:list,customer_ID:list,shopping_pts:list,strct):
    lst = []
    if strct:
        if len(customer_ID) == len(customer_name) == len(shopping_pts) :
            
            temp_lst =[]
            for i in range(len(customer_ID)):
                temp_lst.append(customer_name[i])
                temp_lst.append(customer_ID[i])
                temp_lst.append(shopping_pts[i])
                lst.append(tuple(temp_lst))
                temp_lst=[]


    if not strct:
        temp_lst =[]
        for i in range(min(len(customer_ID),len(customer_name),len(shopping_pts))):
            
            temp_lst.append(customer_name[i])
            temp_lst.append(customer_ID[i])
            temp_lst.append(shopping_pts[i])
            lst.append(tuple(temp_lst))
            temp_lst =[ ]
                       


    return lst    


name =["abhishek","Ranjan","kumar"]
id_ = ['45','12','99']
pts =[99,53,69]

show = my_zip(name,id_,pts,strct=True)
print(show)


#  OUTPUT =  [('abhishek', '45', 99), ('Ranjan', '12', 53), ('kumar', '99', 69)]

# # ##########  QUESTION 2 ########
# Define a function my_sort() to sort the list of tuples created using my_zip function in the last question. The function must have two types of arguments- the list that carry the data, the key that determines the argument of sorting:
# [Usage of built-in function sorted() is a punishable offense]
# Key = 0: sorting based on customer name in ascending order
# Key = 1: sorting based on Customer ID
# Key = 2: sorting based on shopping point


def my_sort(data, key=0):
    
    n = len(data)
    
    # Bubble sort implementation
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][key] > data[j+1][key]:
                # Swap the tuples
                data[j], data[j+1] = data[j+1], data[j]
    
    return data

# Example usage
data = [
    ("Abhishek", 102, 45),
    ("Ranjan", 101, 50),
    ("Kumar", 103, 40)
]

print("Original Data:")
print(data)

# Sort by customer name
sorted_by_name = my_sort(data.copy(), key=0)
print("\nSorted by Customer Name:")
print(sorted_by_name)

# Sort by Customer ID
sorted_by_id = my_sort(data.copy(), key=1)
print("\nSorted by Customer ID:")
print(sorted_by_id)

# Sort by Shopping Points
sorted_by_points = my_sort(data.copy(), key=2)
print("\nSorted by Shopping Points:")
print(sorted_by_points)

