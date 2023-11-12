while True:
    name = input()

    if name == "Voldemort" or name == "Welcome!":
        break

    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")

if name == "Voldemort":
    print("You must not speak of that name!")
else:
    print("Welcome to Hogwarts.")
