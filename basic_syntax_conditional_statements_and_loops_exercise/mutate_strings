first_string = input()
second_string = input()
last_string = ""

for symbol in range(len(second_string)):
    left = second_string[:symbol + 1]
    right = first_string[symbol + 1:]

    new_string = left + right

    if new_string == last_string:
        continue

    print(new_string)

    last_string = new_string

