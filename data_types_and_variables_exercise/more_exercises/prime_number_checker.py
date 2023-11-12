number = int(input())

prime_number = False

if number == 2:
    prime_number = True

for i in range(2, number):
    if number % i == 0:
        print("False")
        prime_number = False
        break
    else:
        prime_number = True

if prime_number:
    print("True")
