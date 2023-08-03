from math import ceil

count_of_lost_fights = int(input())

total_cost = 0

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

for fight in range(1, count_of_lost_fights + 1):

    if fight % 2 == 0:
        total_cost += helmet_price
    if fight % 3 == 0:
        total_cost += sword_price
    if fight % 6 == 0:
        total_cost += shield_price
    if fight % 12 == 0:
        total_cost += armor_price

print(f"Gladiator expenses: {ceil(total_cost):.2f} aureus")
