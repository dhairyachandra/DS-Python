# Partitioning Function

def partition (arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range (low,high):
        if arr[j]<=pivot:
            i=i+1
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    temp=arr[i+1]
    arr[i+1]=arr[high]
    arr[high]=temp
    return i+1


def quicksort(arr,low,high):
    if low < high:
         s=partition(arr,low,high)
         quicksort(arr,low,s-1)
         quicksort(arr,s+1,high)


# Driver starts Here
arr=[10,80,-1,90,40,50,70]
n=len(arr)
quicksort(arr,0,n-1)
for i in arr:
    print (i)
