def remove_chars(word, n):
    print("This is the original word", word)
    x = word[n:]
    return x

print(remove_chars("mongodb",4))
print(remove_chars("purple", 2))
