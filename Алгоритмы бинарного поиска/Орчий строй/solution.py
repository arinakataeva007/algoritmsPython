heights = list(map(int, input().split()))
posibilityHeight = list(map(int, input().split()))

positions = {}
for posHeight in posibilityHeight:
    if posHeight not in positions:
        positions[posHeight] = []

        for i in range(len(heights) - 1):
            if posHeight == heights[i] and posHeight != heights[i + 1]:
                positions[posHeight].append(i)

result = []
maxFList = {}
for height in posibilityHeight:
    if height in maxFList:
        result.append(str(maxFList[height]))
        continue

    maxf = 0
    for position in positions[height]:
        leftSum = heights[:position + 1].count(height)
        rightSum = sum(1 for h in heights[position:] if h != height)
        maxf = max(maxf, leftSum * rightSum)
    
    maxFList[height] = maxf
    result.append(str(maxf))

print(" ".join(result))