import queue
n = int(input())
gymnasts = [list(map(int, input().split(';')[1:3])) for _ in range(n)]

def find_max_Height(gymnasts):
    result_weight = 0
    height_tower = 0
    gymnasts.sort(key=lambda h: h[0] + h[1])
    list_gym = []
    for i in range(len(gymnasts)):
        if result_weight <= gymnasts[i][0]:
            height_tower+=1
            result_weight+=gymnasts[i][1]
            list_gym.append((-gymnasts[i][1], i))
            list_gym.sort()  
        else:
            if -list_gym[0][0] > gymnasts[i][1]:
                result_weight -= -list_gym[0][0]
                list_gym.pop(0)  
                list_gym.append((-gymnasts[i][1], i))
                list_gym.sort()  
                result_weight += gymnasts[i][1]
    return height_tower

print(find_max_Height(gymnasts))