word = input()

searched_indices = [index for index, char in enumerate(word) if char.isupper()]

print(searched_indices)
