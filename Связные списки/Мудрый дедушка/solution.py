word = input()
weight_letter = input().split()

alphabet = {
    'а': 0, 'б': 0, 'в': 0, 'г': 0, 'д': 0, 'е': 0, 'ж': 0, 'з': 0, 'и': 0, 'й': 0, 'к': 0, 'л': 0, 'м': 0,
    'н': 0, 'о': 0, 'п': 0, 'р': 0, 'с': 0, 'т': 0, 'у': 0, 'ф': 0, 'х': 0, 'ц': 0, 'ч': 0, 'ш': 0, 'щ': 0,
    'ъ': 0, 'ы': 0, 'ь': 0, 'э': 0, 'ю': 0, 'я': 0
}

def sort_alphabet_by_weight(alphabet):
    sorted_by_weight = dict(sorted(alphabet.items(), key=lambda item: int(item[1]), reverse=True))
    return sorted_by_weight

def create_hash_table(alphabet,weight_letter):
    hash_table = {}

    for letter, weight in zip(alphabet, weight_letter):
        hash_table[letter] = weight

    return hash_table

def process_sorted_alphabet(sorted_by_weight, num_amount, word, alphabet):
    result = ''
    length_str = len(word)
    result_weight = 0
    k = 0

    for char in sorted_by_weight:
        if sorted_by_weight[char] != '0' and char in num_amount and num_amount[char] > 1:
            result += char
            word = word.replace(char, '', 2)
            result_weight += int(alphabet[char]) * (length_str - 1 - k)
            k += 2

    return result, result_weight, word

count_letter = {char: word.count(char) for char in set(word)}
alphabet = create_hash_table(alphabet, weight_letter)
sorted_by_weight = sort_alphabet_by_weight(alphabet)

result, result_weight, new_word = process_sorted_alphabet(sorted_by_weight, count_letter, word, alphabet)

result = f'{result}{"".join(sorted(new_word))}{result[::-1]} {result_weight}'
print(result)