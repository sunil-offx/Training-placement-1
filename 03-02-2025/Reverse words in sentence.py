def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])

print(reverse_words("Hello World"))  # Output: "World Hello"
