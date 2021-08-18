t=int(input())
for _ in range(t):
    count=0
    sum1=0
    a=int(input())
    l=[int(x) for x in input().split()]
    for i in range(0,len(l)-1):
        count=0
        for j in range(i+1,len(l)):
            if(l[i]>l[j]):
                count=count+1
        sum1=sum1+count
    if(sum1%2==0):
        print("YES")
    else:
        print("NO")

