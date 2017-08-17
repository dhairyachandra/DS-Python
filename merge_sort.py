def merge(arr,low,m,high):
    n1=m-low+1
    n2=high-m
    LArray=[0]*n1
    RArray=[0]*n2
    for i in range(0,n1):
        LArray[i]=arr[low+i]
    for j in range(0,n2):
        RArray[j]=arr[m+1+j]
    i=0
    j=0
    k=low
    while i<n1 and j<n2:
        if LArray[i]<=RArray[j]:
            arr[k]=LArray[i]
            i=i+1
        else:
            arr[k]=RArray[j]
            j=j+1
        k=k+1
    while i<n1:
        arr[k]=LArray[i]
        i=i+1
        k=k+1
    while j<n2:
        arr[k]=RArray[j]
        j=j+1
        k=k+1


def mergesort(arr,low,high):
    if low<high:
        mid=(low+high)/2
        mergesort(arr,low,mid)
        mergesort(arr,mid+1,high)
        merge(arr,low,mid,high)

# Driver starts Here
arr=[12,11,13,5,6,7]
n=len(arr)
mergesort(arr,0,n-1)
for i in arr:
    print i