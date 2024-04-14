keys_arr = list(map(int, input().split()))
elements_arr = list(map(int, input().split()))
def find_Count(keys_arr, elements_arr):
    hash_table = {}
    for i in elements_arr:
        if i in hash_table:
            hash_table[i] += 1
        else:
            hash_table[i] = 1
    result = []
    for j in keys_arr:
        if j in hash_table:
            result.append(str(hash_table[j]))
        else:
            result.append(str(0))
    print(" ".join(result))
find_Count(keys_arr, elements_arr)