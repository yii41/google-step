from collections import Counter

def calculate_score(word):
    scores = {'a': 1, 'b': 3, 'c': 2, 'd': 2, 'e': 1, 'f': 3, 'g': 3, 'h': 1, 'i': 1, 'j': 4, 'k': 4, 'l': 2, 'm': 2, 'n': 1, 'o': 1, 'p': 3, 'q': 4, 'r': 1, 's': 1, 't': 1, 'u': 2, 'v': 3, 'w': 3, 'x': 4, 'y': 3, 'z': 4}
    score = 0
    for letter in word:
        score += scores[letter]
    return score

def find_max_score_anagram(random_word, dictionary):
    count_letters_random_word = Counter(random_word)
    anagrams = [word for word in dictionary if all(count_letters_random_word[char] >= count for char, count in Counter(word).items())]

    max_score = 0
    max_score_anagram = ""

    for anagram in anagrams:
        score = calculate_score(anagram)
        if score > max_score:
            max_score = score
            max_score_anagram = anagram
    return max_score_anagram

with open('words.txt') as f:
    dictionary = f.read().splitlines()

# small
with open('small.txt') as f:
    small_random_words = f.read().splitlines()

with open('small_answer.txt', 'w') as o:
    for small_random_word in small_random_words:
        max_score_anagram = find_max_score_anagram(small_random_word, dictionary)
        o.write(f"{max_score_anagram}\n")

# medium
with open('medium.txt') as f:
    medium_random_words = f.read().splitlines()

with open('medium_answer.txt', 'w') as o:
    for medium_random_word in medium_random_words:
        max_score_anagram = find_max_score_anagram(medium_random_word, dictionary)
        o.write(f"{max_score_anagram}\n")

# large
with open('large.txt') as f:
    large_random_words = f.read().splitlines()

with open('large_answer.txt', 'w') as o:
    for large_random_word in large_random_words:
        max_score_anagram = find_max_score_anagram(large_random_word, dictionary)
        o.write(f"{max_score_anagram}\n")