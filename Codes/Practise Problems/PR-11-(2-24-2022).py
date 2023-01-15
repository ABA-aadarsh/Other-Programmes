#Given an array and k such that 1<=k<=(length of array), compute maximum value of each subarray of length k
array=[10,5,2,7,8,7]
k=3
r=[]
for i in range(len(array)-k+1):
    temp=0
    # print(array[i:i+k])
    for j in array[i:i+k]:
        if j>=temp:
            temp=j
    r.append(temp)
print(r)