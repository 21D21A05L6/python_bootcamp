n=5
k=3
arr=[9,2,5,3,7]
ans=0
for i in range(0,n-k+1):
    sub_arr=arr[i:i+k]
    
    sum=0
    for ind in range(1,k+1):
        sum+=sub_arr[ind-1]*ind
        
    
    if sum>ans:
        ans=sum
print(ans)
