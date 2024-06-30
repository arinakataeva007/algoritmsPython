growths = list(map(int, input().split()))
pivot_list = []

def quickSort(lower, higher, arr):
    if higher <= lower + 1:
        return
    
    pivot = split_into_subarrays(lower, higher, arr)
    pivot_list.append(arr[pivot])
    
    quickSort(lower, pivot, arr)
    quickSort(pivot + 1, higher, arr)

def split_into_subarrays(lower, higher, arr):
    if higher - 1 - lower == 0:
        return lower
    
    i = lower
    j = higher - 1
    pivot = arr[higher - 1]

    while j > i:
        while pivot > arr[i]:
            i += 1
        while j > i and arr[j] >= pivot:  
            j -= 1
        if j > i:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i], arr[higher - 1] = arr[higher - 1], arr[i]
    return i

quickSort(0, len(growths), growths)

for pivot in pivot_list:
    print(pivot)

print(*growths)