word = input()
reversed_word = ""

for chr in range (len(word) - 1, -1, -1):
    reversed_word += word[chr]

print(reversed_word)
