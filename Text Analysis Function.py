# This program performs different text analysis using functions

# function to count words
def count_words(text):
    words = text.split()
    return len(words)

# function to count vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# function to count consonants
def count_consonants(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

# function to reverse text
def reverse_text(text):
    return text[::-1]

# function to check palindrome
def is_palindrome(text):
    clean_text = text.lower().replace(" ", "")
    return clean_text == clean_text[::-1]

# function to remove vowels
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result

# function to get word frequency
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

# function to find longest word
def longest_word(text):
    words = text.split()
    longest = max(words, key=len)
    return longest, len(longest)

# main function to call everything
def analyze_text():
    user_text = input("Enter text: ")

    print("\n=== TEXT ANALYSIS ===")
    print("Words:", count_words(user_text))
    print("Vowels:", count_vowels(user_text))
    print("Consonants:", count_consonants(user_text))
    print("Reversed:", reverse_text(user_text))
    print("Palindrome:", "Yes" if is_palindrome(user_text) else "No")
    print("Without vowels:", remove_vowels(user_text))

    word, length = longest_word(user_text)
    print(f"Longest word: {word} ({length} letters)")

    freq = word_frequency(user_text)
    print("Word Frequency:", freq)

# run program
analyze_text()