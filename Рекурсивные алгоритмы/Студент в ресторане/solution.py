def calculate_and_print_max_calories(menu, W):
    max_values = [0, "", -1]
    dish_number = [""] * len(menu)

    def calculate_calories(start, index, total_money, total_calories, dish_count):
        for i in range(start, len(menu)):  
            if index > len(dish_number) - 1:  
                dish_number.append(str(i + 1))
            else:
                dish_number[index] = str(i + 1)  
            if (total_money + menu[i][0] <= W
                    and (total_calories + menu[i][1] > max_values[0]
                         or (total_calories + menu[i][1] == max_values[0] and dish_count + 1 > max_values[2]))):
                max_values[0] = total_calories + menu[i][1]
                max_values[1] = " ".join(dish_number)
                max_values[2] = dish_count + 1

            if total_money + menu[i][0] >= W:
                continue
            
            calculate_calories(i + 1, index + 1, total_money + menu[i][0], total_calories + menu[i][1], dish_count + 1)

    calculate_calories(0, 0, 0, 0, 0)
    if max_values[2] == -1:  
        print("0 0\n")
    else:  
        print(max_values[2], max_values[0])
        print(" ".join(max_values[1].split()[:max_values[2]]).strip())

dish_count, W = map(int, input().split())
menu = []
for _ in range(dish_count):
    price, calories = map(int, input().split())
    menu.append((price, calories))
calculate_and_print_max_calories(menu, W)