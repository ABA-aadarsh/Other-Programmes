import time
x=[1,2,0] # input array
n=1
for i in x:
    if i>n:
        n=i
print("Lowest positive integer not in the array: ",n+1)
time.sleep(2)
