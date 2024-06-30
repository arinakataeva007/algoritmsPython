def separation_by_pivot(arr, left, right):
    pivot = arr[right]
    i = left
    j = right - 1
    while True:  
        while i <= j and arr[i] <= pivot: 
            i = i + 1
        while i <= j and arr[j] >= pivot:  
            j = j - 1

        if i <= j:  
            arr[i], arr[j] = arr[j], arr[i]  
        else:
            arr[right], arr[i] = arr[i], arr[right]  
            return i  
        
def findOrder(array, k):
    left = 0
    right = len(array) - 1

    while True:
        pivot_index = separation_by_pivot(array, left, right)

        if pivot_index == k:
            return array[pivot_index]
        elif k < pivot_index:
            right = pivot_index - 1
        else:
            left = pivot_index + 1
array = list(map(int, input().split()))  
k = int(input())
print(findOrder(array, k))