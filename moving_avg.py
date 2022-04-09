
def moving_avg(l,n):
    moving_avg=[]
    moving_avg+=(n-1)*['None']
    for index,i in enumerate(l):
        
        if index+n==len(l):
            break
        slice=l[index+n:index:-1]
        #print(slice)
        avg=sum(slice)/n
        moving_avg.append(avg)
    return (moving_avg)

l=[i for i in range(0,100)]

n=4
print(moving_avg(l,n))
