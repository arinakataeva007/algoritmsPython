cakes_count, bag_capacity = map(int, input().split())
cakes = [[int(price), int(weight), can_cut, int(price)/int(weight)] for _ in range(cakes_count) for price, weight, can_cut in [input().split()]]

cakes = sorted(cakes, key=lambda j: j[3], reverse=True)
result = 0

for price, weight, can_cut, price_per_gram in cakes:
    if bag_capacity == 0:
        break
    if can_cut == 'Д':
        amount = min(weight, bag_capacity)
        result += amount * price_per_gram
        bag_capacity -= amount
    elif can_cut == 'Н' and weight <= bag_capacity:
        result += price
        bag_capacity -= weight

print("{:.2f}".format(result))
