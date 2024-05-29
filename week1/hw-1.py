def solution(random_word, dictionary):
    
    # sorted random word & dictionary
    sorted_random_word = ''.join(sorted(random_word))
    sorted_new_dictionary = sorted((''.join(sorted(word.strip())), word.strip()) for word in dictionary)

    # binary search
    left, right = 0, len(sorted_new_dictionary) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_word = sorted_new_dictionary[mid][0]

        if mid_word == sorted_random_word:
            return sorted_new_dictionary[mid][1]
        elif mid_word < sorted_random_word:
            left = mid + 1
        else:
            right = mid - 1

random_word = input('random word:')

with open('words.txt') as f:
    dictionary = f.read().splitlines()

print("anagram:", solution(random_word, dictionary))