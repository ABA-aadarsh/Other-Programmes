'''Using Morte Carlo method estimate the value of PI
    Approach:   I will create a coordinate space as sample space 
                then create a square with length "r" and sector of circle with radius "r"
                then choosing coordinates randomly within a closed space and 
                by morte carlos approach pi can be estimated as
                x=(number of points in circle/number of points in square)
                pi~4*x/(x+1)
'''
import random
r=1
N=10000
ns, nc=0,0
for i in range(N):
    x=random.randint(0,r*100)/100
    y=random.randint(0, r*100)/100
    if pow(pow(x,2)+pow(y,2), 0.5)<=r:
        nc+=1
    else:
        ns+=1
estimated_pi=4*(nc/ns)/((nc/ns)+1)
print("The estimated value of pi is",estimated_pi)
temp=input("")
