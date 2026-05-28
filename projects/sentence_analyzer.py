sentence = input('Enter a sentence: ')
total_characters = len(sentence)

char_without_spaces = len(sentence.replace(' ', ''))


print(total_characters)
print(char_without_spaces)

sentence_parts = sentence.split()
first_word = sentence_parts[0]
last_word = sentence_parts[-1]

print(first_word)
print(last_word)

sentence_upper_case = sentence.upper()
print(sentence_upper_case)

sentence_lower_case = sentence.lower()
print(sentence_lower_case)

sentence_title_case = sentence.title()
print(sentence_title_case)

sentence_reversed = sentence[::-1]
print(sentence_reversed)
