animals = input().split(", ")
animals_descending = animals[::-1]

if animals_descending.pop(0) == "wolf":
    print("Please go away and stop eating my sheep")
    exit()

for animal in range(len(animals_descending)):
    if animals_descending[animal] == "wolf":
        print(f"Oi! Sheep number {animal + 1}! You are about to be eaten by a wolf!")
