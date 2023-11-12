key = int(input())
n = int(input())
message = []

for _ in range(n):
    letter = input()
    letter_number = ord(letter) + key
    new_letter = chr(letter_number)

    message.append(new_letter)

print("".join(message))
