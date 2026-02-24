# This program takes a sentence from the user
# Then it shows different information about that sentence

# asking the user to type a sentence
user_sentence = input("Enter a sentence: ")

# 1️⃣ printing the original sentence
print("\nOriginal:", user_sentence)

# 2️⃣ counting total characters including spaces
total_characters_with_spaces = len(user_sentence)
print("Characters (with spaces):", total_characters_with_spaces)

# 3️⃣ counting characters without spaces
sentence_without_spaces = user_sentence.replace(" ", "")  # removing spaces
total_characters_without_spaces = len(sentence_without_spaces)
print("Characters (without spaces):", total_characters_without_spaces)

# 4️⃣ counting total words
words_list = user_sentence.split()  # splits sentence into words
total_words = len(words_list)
print("Words:", total_words)

# 5️⃣ converting sentence to uppercase
uppercase_sentence = user_sentence.upper()
print("UPPERCASE:", uppercase_sentence)

# 6️⃣ converting sentence to lowercase
lowercase_sentence = user_sentence.lower()
print("lowercase:", lowercase_sentence)

# 7️⃣ converting sentence to title case (first letter capital)
title_case_sentence = user_sentence.title()
print("Title Case:", title_case_sentence)

# 8️⃣ getting the first word from the list
first_word = words_list[0]
print("First word:", first_word)

# 9️⃣ getting the last word
last_word = words_list[-1]
print("Last word:", last_word)

# 🔟 reversing the whole sentence
reversed_sentence = user_sentence[::-1]  # slicing trick to reverse
print("Reversed:", reversed_sentence)