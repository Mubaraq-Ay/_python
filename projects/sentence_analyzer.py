sentence = input('Enter a sentence: ')
total_characters = len(sentence)
char_without_spaces = len(sentence.replace(' ', ''))

sentence_parts = sentence.split()
first_word = sentence_parts[0]
last_word = sentence_parts[-1]


sentence_upper_case = sentence.upper()
sentence_lower_case = sentence.lower()
sentence_title_case = sentence.title()
sentence_reversed = sentence[::-1]

check_word = input('enter word to check: ')
starts_with = sentence.startswith(check_word)
ends_with = sentence.endswith(check_word)

print(f'Starts with {check_word}: {starts_with}')
print(f'Ends with {check_word}: {ends_with}')
print(f'Total characters: {total_characters}')
print(f'Total characters without spaces: {char_without_spaces}')
print(f'The first word: {first_word}')
print(f'The last word: {last_word}')
print(f'The sentence in upper case: {sentence_upper_case}')
print(f'The sentence in lower case: {sentence_lower_case}')
print(f'The sentence in title case: {sentence_title_case}')
print(f'The sentence when reversed: {sentence_reversed}')
