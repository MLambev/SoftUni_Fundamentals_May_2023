number_of_messages = int(input())

for _ in range(number_of_messages):
    digit = input()

    if digit == "88":
        print("Hello")
    elif digit == "86":
        print("How are you?")

    digit = int(digit)

    if digit < 88 and digit != 88 and digit != 86:
        print("GREAT!")
    elif digit > 88:
        print("Bye.")
