for i in range(int(input())):
    l,r=map(int,input().split())
    s=0
    for i in range(l,r+1):
        if i%10==2 or i%10==3 or i%10==9:
            s+=1
    print(s)