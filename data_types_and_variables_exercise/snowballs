from math import ceil

number_of_snowballs = int(input())

the_best_snowball = 0

for _ in range(number_of_snowballs):

    snowball_value = 0

    weight_of_snowball = int(input())
    time_to_target = int(input())
    quality_of_snowball = int(input())

    snowball_value = (weight_of_snowball / time_to_target) ** quality_of_snowball

    if snowball_value > the_best_snowball:
        the_best_snowball = snowball_value
        the_best_snowball_weight = weight_of_snowball
        the_best_snowball_time = time_to_target
        the_best_snowball_quality = quality_of_snowball

print(f"{the_best_snowball_weight} : {the_best_snowball_time} = {ceil(the_best_snowball)} ({the_best_snowball_quality})")
