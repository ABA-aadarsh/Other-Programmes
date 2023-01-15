def permutation(lst):
    if len(lst)==0:
        return []
    elif len(lst)==1:
        return [lst]
    else:
        l=[]
        for i in range(len(lst)):
            x=lst[i]
            xs=lst[:i]+lst[i+1:]
            for p in permutation(xs):
                l.append([x]+p)
        return l
alist=[1,1,2,1]
whole_list=permutation(alist)
result=[]
for i in whole_list:
    if not (i in result):
        result.append(i)
for i in result:
    print(i)
