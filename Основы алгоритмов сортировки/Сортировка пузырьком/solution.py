array = list(map(int, input().split()))
n = int(input())

for i in range(len(array) - 1):
    if i == n:
         print(' '.join(map(str, array)))
    for j in range(len(array) - 1 - i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
print(' '.join(map(str, array)))