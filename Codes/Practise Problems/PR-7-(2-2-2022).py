''' Given a mapping a=1, b=2, c=3,.....,z=26 and encode message counts
    count the number of ways it can be decoded
    Example:
        "111" will decode as
        'aaa' , 'ak' and 'ka'
'''
#Pros of my code
#   well it works
# Cons of my code
#   it is unable to or takes too much time if the number is greater than 6 digits
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
def make21list(lst, N):
    whole_list=permutation(lst)
    sresult=[]
    for i in whole_list:
        if not (i in sresult):
            sresult.append(i)
    result=[]
    for i in sresult:
        temp=[]
        for j in i:
            ssum=sum(temp)
            if ssum<N:
                temp.append(j)
            elif ssum==N:
                if not (temp in result):
                    result.append(temp)
                break
            elif ssum>N:
                break
    return result
def makeList(lst):
    '''First of all we need to create list21, 
    for which we need to know the maximum number of 2 that can be used
    which is given by int(len(lst)/2)
    '''
    s=[]
    for i in range(len(lst)): # appending 1
        s.append(1)
    for i in range(int(len(lst)/2)): # appending 2
        s.append(2)
    # Now we need to create a permutation list of 2 and 1 whose sum must be equal to len(lst)
    list21=[]
    result=make21list(s,len(lst))
    return result
num_string=input(":::")
try:
    if num_string[0]!="0" and int(num_string)>0:
        l1=makeList(num_string)
        # now we have to intepret the list l1
        l2=[]
        for i in l1:
            index=0
            c=0
            temp=[]
            while index < len(num_string):
                if i[c]==1:
                    if int(num_string[index:index+1]) < 27 and int(num_string[index:index+1])>0:
                        temp.append(int(num_string[index:index+1]))
                        index+=1
                    else:
                        temp=[]
                        break
                elif i[c]==2:
                    if int(num_string[index:index+2]) < 27 and int(num_string[index:index+2])>0:
                        temp.append(int(num_string[index:index+2]))
                        index+=2
                    else: 
                        temp=[]
                        break
                c+=1
            if temp!=[]:
                l2.append(temp)
        # now we will do decoding, and store value in l3
        l3=[]
        for i in l2:
            temp=""
            for x in i:
                temp+=chr(x+97-1)
            l3.append(temp)
        # now displaying the code
        print("RESULTS: ")
        for i in l3:
            print(f"\t{i}")
    else:
        print("Invalid Input")
except:
    print("Invalid Input")