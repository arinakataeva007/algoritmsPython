import math

V0, Vs = map(int, input().split())
pathAreaOutsideTheCity = int(input()) * 0.01

def searchForTotalTravelTime(dot, v0, vs, square):
    s1 = math.sqrt(dot**2 + square**2)
    t1 = s1 / v0
    s2 = math.sqrt((1 - dot)**2 + (1 - square)**2)
    t2 = s2 / vs
    return t1 + t2

dot_left = 0.0
dot_right = 1.0
next_dot = 0.5

while dot_right - dot_left > 1e-9: 
    left_time = searchForTotalTravelTime(dot_left, V0, Vs, pathAreaOutsideTheCity)
    right_time = searchForTotalTravelTime(dot_right, V0, Vs, pathAreaOutsideTheCity)
    next_time = searchForTotalTravelTime(next_dot, V0, Vs, pathAreaOutsideTheCity)
    
    if next_time - left_time < next_time - right_time:
        next_dot, dot_left = (dot_right + next_dot) / 2, next_dot
    elif next_time - left_time > next_time - right_time:
        next_dot, dot_right = (dot_left + next_dot) / 2, next_dot
    else:
        break

print(f"{next_dot:.6f}")