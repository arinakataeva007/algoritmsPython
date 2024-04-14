number_of_students, minimum_score, maximum_score = map(int, input().split())

def make_a_subsequence(minimum_score, maximum_score, index, number_of_students, array, result):
    if index == number_of_students:
        result.append(" ".join(array))
        return result
    for i in range(minimum_score + number_of_students - index - 1, maximum_score + 1):
        array[index] = str(i)
        result = make_a_subsequence(minimum_score, i - 1, index + 1, number_of_students, array, result)
    return result

result = make_a_subsequence(minimum_score, maximum_score, 0, number_of_students, ["0"] * number_of_students, [])
result.append(str(len(result)))
print("\n".join(result))