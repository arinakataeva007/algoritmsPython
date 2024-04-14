s = str(input())
result_k = 1
result_t = ''
for k in range(1, len(s) + 1):
    if len(s) % k == 0:
        if s[:len(s)//k] * k == s:
            result_k = k
            result_t = s[:len(s)//result_k]

print(result_k, result_t)