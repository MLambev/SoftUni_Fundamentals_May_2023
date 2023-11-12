number = int(input())

for a in range(0, number):
    for b in range(0, number):
        for c in range(0, number):
            print(f"{chr(97 + a)}{chr(97 + b)}{chr(97 + c)}")
