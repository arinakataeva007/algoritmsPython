array = list(map(int, input().split()))
middle = (len(array) + 1) // 2

length = len(array)
for i in range(1, length):
    el = array[i]
    j = i

    if i == middle:
        print(' '.join(map(str,array)))

    while j > 0 and array[j -1] > el:
        array[j] = array[j - 1]
        j -= 1
    array[j] = el

print(' '.join(map(str,array)))