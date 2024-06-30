n = int(input()) 
bacteria_temperatures = []
for _ in range(n):
    temperatures_from_user = input().split()
    bacteria_temperatures.append((int(temperatures_from_user[0]), int(temperatures_from_user[1])))

planet_temperatures = [int(x) for x in input().split()]


def calculate_live_bacteria(planet_temperatures, bacteria_temperatures):
    count = []
    for i in planet_temperatures:
        k = 0
        for j in bacteria_temperatures:
            if j[0] <= i <= j[1]:
                k += 1
        count.append(k)
    return count
   
result = calculate_live_bacteria(planet_temperatures, bacteria_temperatures)  
for live in result:  
    print(live)