name = "Rupika"
species = "cat"
age = 6

print(name + " is a " + species + ". " "He is " + str(age) + " years old.")

total_plants = 3
plants_killed_by_flatmate = 1
flatmate_name = "Soma"

def plants_alive():
    current_plants = total_plants - plants_killed_by_flatmate
    print(flatmate_name + " killed " + str(plants_killed_by_flatmate) + " plant, but I still have " + str(current_plants) + " beautiful plants.")

plants_alive()
