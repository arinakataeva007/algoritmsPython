N = int(input())
K = [int(input()) for _ in range(N)]

def count_stones(array, N):
    if N == 1:
        return 0
    
    middle = N // 2
    left = array[:middle]
    right = array[middle:]
    count = count_stones(left, middle) + count_stones(right, N - middle)

    i = 0
    j = 0
    
    for stone in range(N):
        if j >= N - middle or (i < middle and left[i] < right[j]):
            array[stone] = left[i]
            i += 1
        else:
            array[stone] = right[j]
            j += 1
            count += middle - i
    return count
print(count_stones(K, N))