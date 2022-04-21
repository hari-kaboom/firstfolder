arr=[2,4,1,6,3]
n=len(arr)
for i in range(n):
    swaped=True
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            swaped=False
            arr[j+1],arr[j]=arr[j],arr[j+1]
    if swaped:
        break
print(arr)