N, M = map(int, input().split())
colors = list(map(int, input().split()))

def count_tiles(arr, N):
    tiles = set()  
    tiles.add(N)
    
    if len(arr) > 1 and arr[0] == arr[1]:
        tiles.add(N - 1)
        
    for i in range(0, len(arr) - 1):
        if arr[i] == arr[i + 1]:  
            new_arr = arr[:i + 1]
            if new_arr[::-1] == arr[i + 1:len(new_arr)+i + 1] and len(new_arr) <= len(arr[i + 1:]):
                tiles.add(len(arr) - (i + 1))
    
    sorted_tiles = sorted(tiles, reverse=True)
    print(" ".join(map(str, sorted_tiles)))  

count_tiles(colors, N)