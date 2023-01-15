def way1(lst):
    #if division is allowed
    p=1
    output=[]
    for i in lst:
        p*=i
    for i in lst:
        output.append(int(p/i))
    return output
def way2(lst):
    #if division is not allowed
    output=[]
    for i in lst:
        p=1
        for j in lst:
            if j!=i:
                p*=j
        output.append(p)
    return output
lst=[1,2,3,4,5,6]
print(way1(lst))# if division is allowed
print(way2(lst))# if division is not allowed