n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

def findMaxCountCoin(city,n, m):
    for column in range(1, n):
        city[column][0] += city[column-1][0]
    for row in range(1, m):
        city[0][row] += city[0][row-1]
    for column in range(1, n):
        for row in range(1, m):
            city[column][row] += max(city[column-1][row], city[column][row-1])
    return city[n-1][m-1]

print(findMaxCountCoin(city, n, m))