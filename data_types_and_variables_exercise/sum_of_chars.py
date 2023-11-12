number = int(input())

sum_of_letters = 0

for _ in range(number):
    letter = input()

    sum_of_letters += ord(letter)

print(f"The sum equals: {sum_of_letters}")
