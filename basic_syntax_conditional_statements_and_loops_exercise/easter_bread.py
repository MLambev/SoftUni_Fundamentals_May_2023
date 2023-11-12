from math import floor

eggs_pack = 1
flour_kilogram = 1
milk_in_milliliters = 250

budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25 / 4

loaf_bread_price = flour_price + eggs_price + milk_price
loaves_counter = 0
colored_eggs = 0

while budget > loaf_bread_price:
    budget -= loaf_bread_price
    loaves_counter += 1

    received_eggs = 3

    if loaves_counter % 3 == 0:
        received_eggs -= loaves_counter - 2

    colored_eggs += received_eggs

print(f"You made {loaves_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
