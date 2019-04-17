import math
n=int(input())
l=[]
for i in range(n):
    l.append(input())
mini,small=math.inf,""
for i in l:
    if ord(i[0])<min:
	    mini=ord(i[0])
	    small=i
print(small)
#abc