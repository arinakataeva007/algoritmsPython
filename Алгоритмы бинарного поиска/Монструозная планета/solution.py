import math

n, m, l = map(int, input().split())
legs_of_many_legs = [list(map(int, input().split())) for _ in range(n)]
legs_of_many_arms = [list(map(int, input().split())) for _ in range(m)]
queries = int(input())
#queries = [list(map(int, input().split())) for _ in range(q)]

def findMinCon(first_arr, second_arr):
    minLimbs = 1000000000
    left = 0
    right = len(first_arr) - 1
    k = -1 

    while left <= right:
        mid = (left + right) // 2
        max_el = max(first_arr[mid], second_arr[mid])
        if minLimbs >= max_el:
            minLimbs = max_el
            k = mid 
        if first_arr[mid] < second_arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return k

results = []
for q in range(queries):
    i, j = map(int, input().split())
    first_list = legs_of_many_legs[i]
    second_list = legs_of_many_arms[j]
    index = findMinCon(first_list, second_list)
    while index < len(second_list) - 1:
        curr_max = max(first_list[index], second_list[index])
        next_max = max(first_list[index+1], second_list[index+1])
        if curr_max != next_max:
            break
        index += 1
    results.append(index)
print(*results, sep='\n')