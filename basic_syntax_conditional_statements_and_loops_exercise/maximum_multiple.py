divisor = int(input())
boundary = int(input())

searched_number = 0

for number in range(1, boundary + 1):
    if number % divisor == 0:
        searched_number = number

print(searched_number)
