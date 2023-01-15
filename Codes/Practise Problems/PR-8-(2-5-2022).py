def adj(lst):
    if len(lst)==0:
        return []
    else:
        r=[]
        # b=[0,0,0]
        s=[]
        for i in range(int(len(lst)/2)+1):
            x=lst[i]
            xs=lst[:i]+lst[i+2:]
            print(x, xs)
            s.append([x]+adj(xs))
            r+=s
        return r

l=[1,2,3,4,5]
print(adj(l))

