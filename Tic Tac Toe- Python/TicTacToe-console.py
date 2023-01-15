def clue2(b1,b2,b3,n1,n2,n3,char):
    z=[b1,b2,b3,n1,n2,n3]
    if z.count(char)==2 and z.count(" ")==1:
        return z[z.index(" ")+3]+1
    else:
        return "NOPE"
def clue3(b1,b2,b3,n1,n2,n3):
    z=[b1,b2,b3,n1,n2,n3]
    if z.count(" ")==2 and z.count("O")==1:
        return z[z.index(" ")+3]+1
    else:
        return "NOPE"
def userchoose(positionleft,b):
    flag=0
    while(flag!=1):
        u=(input("YOUR TURN: "))
        validchar=["1","2","3","4","5","6","7","8","9"]
        if (u in validchar) and int(u) in positionleft:
            b.pop(int(u)-1)
            b.insert(int(u)-1,"X")
            positionleft.remove(int(u))
            flag=1 
        else:
            print("Give Proper Input. ")
def computerchoose(positionleft,b,p):
    b.pop(p-1)
    b.insert(p-1,"O")
    positionleft.remove(p)
    print(f"Computer choose position: {p}")
def checkAttack(positionleft,b):
    if clue2(b[0],b[1],b[2],0,1,2,"O")!="NOPE":
        computerchoose(positionleft,b,clue2(b[0],b[1],b[2],0,1,2,"O"))
        return 1
    elif clue2(b[3],b[4],b[5],3,4,5,"O")!="NOPE":
        computerchoose(positionleft,b,clue2(b[3],b[4],b[5],3,4,5,"O"))
        return 1
    elif clue2(b[6],b[7],b[8],6,7,8,"O")!="NOPE":
        computerchoose(positionleft,b,clue2(b[6],b[7],b[8],6,7,8,"O"))
        return 1
    elif clue2(b[0],b[3],b[6],0,3,6,"O")!="NOPE":
        computerchoose(positionleft,b,clue2(b[0],b[3],b[6],0,3,6,"O"))
        return 1
    elif clue2(b[1],b[4],b[7],1,4,7,"O")!="NOPE":
        computerchoose(positionleft,b,clue2(b[1],b[4],b[7],1,4,7,"O"))
        return 1
    elif clue2(b[2],b[5],b[8],2,5,8,"O")!="NOPE":
        computerchoose(positionleft,b,clue2(b[2],b[5],b[8],2,5,8,"O"))
        return 1
    elif clue2(b[0],b[4],b[8],0,4,8,"O")!="NOPE":
        computerchoose(positionleft,b,clue2(b[0],b[4],b[8],0,4,8,"O"))
        return 1
    elif clue2(b[2],b[4],b[6],2,4,6,"O")!="NOPE":
        computerchoose(positionleft,b,clue2(b[2],b[4],b[6],2,4,6,"O"))
        return 1
    elif (b[5]=="X" and b[7]=="X" and b[8]==" " and b[6]==0):
        computerchoose(positionleft,b,9)
        return 1
    elif b[4]=="O" and (b[1]=="X" or b[3]=="X" or b[5]=="X" or b[7]=="X") and (b[0]==b[2] and b[6]==b[8] and b[0]==" "):
        computerchoose(positionleft,b,1)
        return 1
    else:
        return 0
def checkDefense(positionleft,b):
    if clue2(b[0],b[1],b[2],0,1,2,"X")!="NOPE":
        computerchoose(positionleft,b,clue2(b[0],b[1],b[2],0,1,2,"X"))
        return 1
    elif clue2(b[3],b[4],b[5],3,4,5,"X")!="NOPE":
        computerchoose(positionleft,b,clue2(b[3],b[4],b[5],3,4,5,"X"))
        return 1
    elif clue2(b[6],b[7],b[8],6,7,8,"X")!="NOPE":
        computerchoose(positionleft,b,clue2(b[6],b[7],b[8],6,7,8,"X"))
        return 1
    elif clue2(b[0],b[3],b[6],0,3,6,"X")!="NOPE":
        computerchoose(positionleft,b,clue2(b[0],b[3],b[6],0,3,6,"X"))
        return 1
    elif clue2(b[1],b[4],b[7],1,4,7,"X")!="NOPE":
        computerchoose(positionleft,b,clue2(b[1],b[4],b[7],1,4,7,"X"))
        return 1
    elif clue2(b[2],b[5],b[8],2,5,8,"X")!="NOPE":
        computerchoose(positionleft,b,clue2(b[2],b[5],b[8],2,5,8,"X"))
        return 1
    elif clue2(b[0],b[4],b[8],0,4,8,"X")!="NOPE":
        computerchoose(positionleft,b,clue2(b[0],b[4],b[8],0,4,8,"X"))
        return 1
    elif clue2(b[2],b[4],b[6],2,4,6,"X")!="NOPE":
        computerchoose(positionleft,b,clue2(b[2],b[4],b[6],2,4,6,"X"))
        return 1
    else:
        return 0
def makeMove(positionleft,b):
    if clue3(b[0],b[1],b[2],0,1,2)!="NOPE":
        computerchoose(positionleft,b,clue3(b[0],b[1],b[2],0,1,2))
    elif clue3(b[3],b[4],b[5],3,4,5)!="NOPE":
        computerchoose(positionleft,b,clue3(b[3],b[4],b[5],3,4,5))
    elif clue3(b[6],b[7],b[8],6,7,8)!="NOPE":
        computerchoose(positionleft,b,clue3(b[6],b[7],b[8],6,7,8))
    elif clue3(b[0],b[3],b[6],0,3,6)!="NOPE":
        computerchoose(positionleft,b,clue3(b[0],b[3],b[6],0,3,6))
    elif clue3(b[1],b[4],b[7],1,4,7)!="NOPE": 
        computerchoose(positionleft,b,clue3(b[1],b[4],b[7],1,4,7))
    elif clue3(b[2],b[5],b[8],2,5,8)!="NOPE":
        computerchoose(positionleft,b,clue3(b[2],b[5],b[8],2,5,8))
    elif clue3(b[0],b[4],b[8],0,4,8)!="NOPE":
        computerchoose(positionleft,b,clue3(b[0],b[4],b[8],0,4,8))
    elif clue3(b[2],b[4],b[6],2,4,6)!="NOPE":
        computerchoose(positionleft,b,clue3(b[2],b[4],b[6],2,4,6))
    else:
        c=random.randint(0,len(positionleft)-1)
        print(f"Computer choose position:: {positionleft[c]}")
        b.pop(positionleft[c]-1)
        b.insert(positionleft[c]-1,"O")
        positionleft.pop(c)
def computerIntellec(positionleft,b,runtime,FT):
    if runtime==1:
        if FT=="u":
            temp=0
            for i in positionleft:
                temp+=i 
            user1position=(1+2+3+4+5+6+7+8+9)-temp
            if user1position==5:
                computerchoose(positionleft,b,1)
            else:
                computerchoose(positionleft,b,5)
        else:
            computerchoose(positionleft,b,5)
    else :
        cA=checkAttack(positionleft,b)
        if cA==0:   # if there is no clear win move then defend from the player
            cD=checkDefense(positionleft,b)
            if cD==0:  # if there is no threat from the player in next move then make next move based on "makeMove" function
                makeMove(positionleft,b)
        # checkDefense
        # Move
def whowin(b):
    if results(b,"O")=="WON":
        return "c"   # <---- Computer Won
    elif results(b,"X")=="WON":
        return "u"   # <---- User Won
    else:
        return 0
def results(b,c):
    if(b[0]==b[1] and b[1]==b[2] and b[0]==c):
        return "WON"
    elif(b[3]==b[4] and b[4]==b[5] and b[3]==c):
        return "WON"
    elif(b[6]==b[7] and b[7]==b[8] and b[6]==c):
        return "WON"
    elif(b[0]==b[4] and b[4]==b[8] and b[0]==c):
        return "WON"
    elif(b[2]==b[4] and b[4]==b[6] and b[2]==c):
        return "WON"
    elif(b[0]==b[3] and b[3]==b[6] and b[0]==c):
        return "WON"
    elif(b[1]==b[4] and b[4]==b[7] and b[1]==c):
        return "WON"
    elif(b[2]==b[5] and b[5]==b[8] and b[2]==c):
        return "WON"
    else:
        return "NOT WON"
import random
run1time=1
positionleft=[1,2,3,4,5,6,7,8,9]
b=[" "," "," "," "," "," "," "," "," "]
turns=["u","c"]
FT=turns[random.randint(0,1)]
if FT=="u":
    while (len(positionleft)!=0 ):
        print(".............")
        print(".",b[0],".",b[1],".",b[2],".")
        print(".",b[3],".",b[4],".",b[5],".")
        print(".",b[6],".",b[7],".",b[8],".")
        print(".............")
        userchoose(positionleft,b)
        if (whowin(b)!=0):
            break
        if (len(positionleft)!=0):
            computerIntellec(positionleft,b,run1time,FT)
            pass
        if (whowin(b)!=0):
            break
        run1time=0
else:
    while (len(positionleft)!=0 ):
        computerIntellec(positionleft,b,run1time,FT)
        print(".............")
        print(".",b[0],".",b[1],".",b[2],".")
        print(".",b[3],".",b[4],".",b[5],".")
        print(".",b[6],".",b[7],".",b[8],".")
        print(".............")
        if (whowin(b)!=0):
            break 
        if (len(positionleft)!=0):
            userchoose(positionleft,b)
            print(".............")
            print(".",b[0],".",b[1],".",b[2],".")
            print(".",b[3],".",b[4],".",b[5],".")
            print(".",b[6],".",b[7],".",b[8],".")
            print(".............")
        
        if (whowin(b)!=0):
            break 
        run1time=0


if FT=="u":
    print(".............")
    print(".",b[0],".",b[1],".",b[2],".")
    print(".",b[3],".",b[4],".",b[5],".")
    print(".",b[6],".",b[7],".",b[8],".")
    print(".............")
s=whowin(b)
if(s=="c"):
    print("\n**** COMPUTER WON ****")
elif(s=="u"):
    print("\n**** YOU WON ****")
else :
    print("\n**** DRAW ****")






