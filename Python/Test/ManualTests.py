import Main.StarSearch

search = Main.StarSearch.StarSearch()
racer = search.get_vehicle_by_id("19")
print("Racer max atmos speed: " + racer.max_atmosphering_speed)
print("Racer manufacturer: " + racer.manufacturer)

print(search.get_first_film().title)

film_list = search.get_all_resources(0)
for num in range(0, len(film_list)):
    print(film_list[num]["title"])
