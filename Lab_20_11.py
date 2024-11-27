import matplotlib.pyplot as plt
import numpy as np
# # Madhya Pradesh
# # BJP - Win (163) INC - Win (66) BSP – Win ( 0) Others – Win (1)

# # Rajasthan
# # INC - Win (69) BJP- Win (115) BSP- Win (2) Others-Win (13)

# plt.figure(figsize=(10,7))
# plt.subplot(2,2,1)
# X_MP = ["BJP","INC","BSP","others"]
# y_MP = np.array([163,66,0,1])
# X_rj = ["INC","BJP","BSP","others"]
# y_rj = [69,115,2,13]
# plt.ylabel('Votes')
# plt.title("MP vote share")

# plt.bar(X_MP,y_MP,)


# plt.subplot(2,2,2)
# plt.bar(X_rj,y_rj)
# plt.ylabel('Votes')
# plt.title('Rajasthan Vote share')
# # plt.pie(y_MP,labels=X_MP,autopct='%1.1f%%',)

# plt.subplot(2,2,3)
# plt.pie(y_MP,labels=X_MP,explode=[0.1,0.0,0.15,0.15],autopct='%.2f')
# # plt.legend()
# plt.title("Rj vote share")

# plt.subplot(2,2,4)
# # plt.pie(y_rj,labels=X_rj,explode=[0,0.1,0,0],autopct='%.2f')
# # plt.title("MP vote share")
# # plt.legend()
# explode = [0.1 if size == 1 else 0 for size in y_MP]
# plt.pie(y_MP, labels=X_MP, autopct='%3.1f%%', explode=explode, colors=["orange", "blue", "green", "gray"], wedgeprops=dict(width=0.4))
# plt.title("Election Results (Donut Chart)")
# plt.show()


# Question 2 
# Form a list of K random numbers within a limit N where K and N are set by the    user. Minimum value of K should be 10.

# Define a function (or two functions) to return the composite numbers and prime numbers of this list as two separate lists.

#  Determine the square of all prime numbers and square root of all composite numbers
# Plot both prime numbers Vs their squares and composites Vs their square roots on the same figure object as scatterplots. ( two different subplots on the same figure object)

k,n = [int(x) for x in input().split() ]
lst = np.random.randint(0,n,k)
# print(k)
# print(n)
# print(lst)
def prime(x):
    cnt = 0
    for i in range(1,x+1):
        if x % i==0:
            cnt +=1
    if cnt >2:
        return False
    else:
        return True       

def splt(lst):
    prim = []
    cmpst =[]
    for num in lst:
        if prime(num):
            prim.append(num)
        else:
            cmpst.append(num)  

    return prim,cmpst
p,c=splt(lst)  
sqp=[i**2 for i in p]
rsqc=[i**0.5  for i in c]
print(sqp,rsqc)

plt.figure(figsize=(12,8))

plt.subplot(1,2,1)

plt.scatter(p,sqp)

plt.subplot(1,2,2)

plt.scatter(c,rsqc)

plt.show()