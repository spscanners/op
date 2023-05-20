#!/usr/local/bin/python3
import sys

data = sys.argv[1]
data=int(data)
if data <= 0:
    sys.stderr.write("Data input type error. ")
    sys.exit("Reset integer type!")
else:
     int(data)

def umNum(n):
    
    t=0
    add=0
    catena=len(str(n))
    banda=pow(10, catena-1)
    #print("banda=", banda)

    for i in range(catena):
        t=n//banda
#        print("(1)t=",t)
        r=t*banda
#        print("(2)r=",r)
        add += t
#        print("(3)add=",add)
        n = n - r
#        print("(4)n=",n)
        banda //= 10
#        print("(5)banda=",banda)
        i+=1
        
    return add

var=umNum(data)

if len(str(var))>=2:
    var=umNum(var)
    print("s:=",var)
else:
    print("s:=",var)

        
