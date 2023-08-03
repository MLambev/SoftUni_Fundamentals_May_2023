number = int(input())

water_tank_capacity = 255
water_counter = 0

for _ in range(number):
    water_flow = int(input())

    if water_flow > water_tank_capacity:
        print("Insufficient capacity!")
        continue

    water_tank_capacity -= water_flow
    water_counter += water_flow

print(water_counter)

