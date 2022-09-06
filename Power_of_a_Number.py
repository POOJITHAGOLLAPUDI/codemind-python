import math
x,y,b=map(int,input().split())
z=math.pow(x,y)
a=z%b
print(int(a))