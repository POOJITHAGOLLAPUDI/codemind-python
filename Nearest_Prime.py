t=int(input())
for _ in range(t):
    n=int(input())
    next=n
    while True:
        fc=0
        for i in range(1,next+1):
            if next%i==0:
                fc+=1
        if fc==2:
                break
        next+=1
    prev=n
    while True:
        fc=0
        for i in range(1,prev+1):
            if prev%i==0:
                fc+=1
        if fc==2:
                break
        prev-=1
    if n-prev<=next-n:
      print(prev)
    else:
      print(next)