# Write a program that calculates the number of packages of hot dogs and the number of 
# packages of hot dog buns needed for a cookout, with the minimum amount of leftovers.

# The program should ask the user for the number of people attending the cookout and 
# the number of hot dogs each person will be given.

# Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8.

# The program should display the following details:

# • The minimum number of packages of hot dogs required
# • The minimum number of packages of hot dog buns required
# • The number of hot dogs that will be left over
# • The number of hot dog buns that will be left over

HOTDOG_PACK = 10
HOT_DOG_BUNS = 8

num_people = int(input("How many people will be attending the cookout?: "))
hotdogs_per_person = float(input("How many hotdogs will each person be eating?: "))

num_food_needed = num_people * hotdogs_per_person

def num_packs(num_food_needed, pack):
    if num_food_needed % pack == 0:
        num_packs = num_food_needed / pack
    else:
        num_packs = (num_food_needed // pack) + 1

    return num_packs

def leftovers(total_packs, pack, num_food_needed):
    leftover = ((total_packs * pack) - num_food_needed)
    return leftover

hotdog_packs = num_packs(num_food_needed, HOTDOG_PACK)
pack_of_buns = num_packs(num_food_needed, HOT_DOG_BUNS)

leftover_hotdogs = leftovers(hotdog_packs, HOTDOG_PACK, num_food_needed)
leftover_hotdog_buns = leftovers(pack_of_buns,HOT_DOG_BUNS, num_food_needed)

print("The minimum number of packs of hotdogs needed are", hotdog_packs)
print("The minimum number of packs of hotdog buns needed are", pack_of_buns)
print("The number of hot dogs that will be left over is", leftover_hotdogs)
print("The number of hot dog buns that will be left over is", leftover_hotdog_buns)