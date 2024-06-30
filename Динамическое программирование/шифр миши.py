user_string = input()
s_len = len(user_string)
encoded_result = [[""] * s_len for _ in range(s_len)]

for current_length in range(1, s_len + 1):
    for start in range(s_len - current_length + 1):
        end = start + current_length - 1
        encoded_result[start][end] = user_string[start:end + 1]

        if current_length != 1:
            for mid_index in range(start, end):
                combined_string = encoded_result[start][mid_index] + encoded_result[mid_index + 1][end]
                if len(combined_string) < len(encoded_result[start][end]):
                    encoded_result[start][end] = combined_string

        for i in range(1, current_length):
            if current_length % i == 0 and user_string[start:start + i] * (current_length // i) == user_string[start:end + 1]:
                pattern = f'{current_length // i}({encoded_result[start][start + i - 1]})'
                if len(encoded_result[start][end]) > len(pattern):
                    encoded_result[start][end] = pattern

encoded_string = encoded_result[0][-1]
print(encoded_string)