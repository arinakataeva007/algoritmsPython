def selection_sort_with_half_print(array):
    length = len(array)
    middle = length // 2

    for i in range(length):
        if i == middle:
            print(*array)

        minimum = i

        for j in range(i + 1, length):
            if array[j] < array[minimum]:
                minimum = j
        array[i], array[minimum] = array[minimum], array[i]

    print(*array)

array = input().split()
array = [int(x) for x in array]
selection_sort_with_half_print(array)