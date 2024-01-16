farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

NE_Farm_Animals = farms[0]["agriculture"]

for animal in NE_Farm_Animals:
    print(animal)

print("Please select one of the following farms to see what is grown there")
print("NE FARM\nW Farm\nSE Farm")
selected_farm = input()
usr_selected_farm
