'''Question:    If there are N number of steps in a staircase and
                you can climb 1 or 2 steps at a time, 
                write a function to show all possible ways to climb the staircase. 
                (order does matters).
'''
from itertools import permutations
def loop(i,P,l,b):
    if i>len(P)-1:
        n=[]
        temp=0
        for i in b:
           temp+=i
           n.append(i)
        if temp==N:
            l.append(n) 
    else:
        for x in P[i]:
            b[i]=x
            loop(i+1, P,l,b)
def ways(X,N):
    P_steps=[]
    for i in X:
        temp=[]
        for j in range(int(N/i)+1):
            temp.append(j*i)
        P_steps.append(temp)
    b=[]
    for i in range(len(X)):
        b.append(0)
    Order_list=[]
    loop(0,P_steps,Order_list,b)
    result=[]
    for i in Order_list:
        temp=[]
        for index,j in enumerate(i):
            if j!=0:
                s=int(j/X[index])
                for t in range(s):
                    temp.append(X[index])
        suedo_result=list(permutations(temp))
        for z in suedo_result:
            if not (z in result):
                result.append(z)
    return result
        #answers are holded in result
N=int(input("Enter the value of N: "))
X=[]
len_of_X=int(input("How many different steps you gonnna take? "))
for i in range(len_of_X):
    X.append(int(input(f"X[{i}] : ")))
result=ways(X, N)
print("Answer:")
if result==[]:
    print("No possible way")
else:
    for i in result:
        print(i)
a=input("")
# at this point i seriously can't explain what i have done and why
'''
Approach1:
suppose if X={1,2} and N=4
int(4/1)=4 gives the maximum number of 1 that can be used
int(4/2)=2 gives the maximum number of 2 that can be used and like this...
possible use of 1 is (0,1,2,3,4) and of 2 is (0,1,2) this might help to make the problem easy
'''
