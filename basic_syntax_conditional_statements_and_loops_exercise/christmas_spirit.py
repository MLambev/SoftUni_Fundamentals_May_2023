quantity_of_decorations = int(input())
days_until_christmas = int(input())

christmas_spirit = 0
total_cost = 0

ornament_set_price = 2
ornament_set_points = 5
tree_skirt_price = 5
tree_skirt_points = 3
tree_garland_price = 3
tree_garland_points = 10
tree_lights_price = 15
tree_lights_points = 17

for day in range(1, days_until_christmas + 1):

    if day % 11 == 0:
        quantity_of_decorations += 2

    if day % 2 == 0:
        total_cost += quantity_of_decorations * ornament_set_price
        christmas_spirit += ornament_set_points

    if day % 3 == 0:
        total_cost += quantity_of_decorations * (tree_skirt_price + tree_garland_price)
        christmas_spirit += tree_skirt_points + tree_garland_points

    if day % 5 == 0:
        total_cost += quantity_of_decorations * tree_lights_price
        christmas_spirit += tree_lights_points
        if day % 3 == 0:
            christmas_spirit += 30

    if day % 10 == 0:
        christmas_spirit -= 20
        total_cost += tree_skirt_price + tree_lights_price + tree_garland_price

if days_until_christmas % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {christmas_spirit}")
