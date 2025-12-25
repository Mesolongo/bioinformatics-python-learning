def process_text(text, *functions):
    # Your code here
    result = text

    for function in functions:
        result = function(result)
    return result

# Lambda functions
remove_spaces = lambda text: text.replace(' ', '')
to_uppercase = lambda text: text.upper()
reverse_text = lambda text: text[::-1]
remove_vowels = lambda text: ''.join([char for char in text if char.lower() not in 'aeiou'])

# Test cases
text = "Hello World"
print(process_text(text, to_uppercase))
print(process_text(text, remove_spaces, to_uppercase))
print(process_text(text, remove_spaces, to_uppercase, reverse_text))
print(process_text(text, to_uppercase, remove_vowels, reverse_text))