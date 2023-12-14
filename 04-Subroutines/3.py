def count_letter_occurrences(text, letter):
    count = text.lower().count(letter.lower())
    return count

# Sample text
sample_text = "You never get a second chance to make a first impression"

# Count occurrences of letter 'e' in the sample text
letter_to_count = 'e'
result = count_letter_occurrences(sample_text, letter_to_count)

print(f"The number of letter '{letter_to_count}': {result}")