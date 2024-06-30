n, W = map(int, input().split())
cakes_arr = [[int(x) for x in input().split()] for _ in range(n)]

def price_per_gram(price, weight, remainder):
    return price / weight * remainder

def calculate_max_cost(cakes, bag_capacity):
    cakes.sort(key=lambda k: k[0] / k[1], reverse=True)
    result_cost = 0
    i = 0
    while i < len(cakes):
        if cakes[i][1] <= bag_capacity:
            bag_capacity -= cakes[i][1]
            result_cost += cakes[i][0]
        else:
            result_cost += price_per_gram(cakes[i][0], cakes[i][1], bag_capacity)
            break
        i += 1
    return result_cost

res = calculate_max_cost(cakes_arr, W)
print(f"{res:.2f}")