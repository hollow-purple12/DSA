swaps=0
n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
           swaps+=1
           arr[j],arr[j+1]=arr[j+1],arr[j]
print(' '.join(map(str,arr)))
print(swaps)
