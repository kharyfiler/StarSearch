import Main.StarSearch

s = Main.StarSearch.StarSearch()
print("\nFilm Tests ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("\nGet Film by Title - Pass")
film_by_title = s.get_film_by_title("Attack of the Clones")
print("\nFilm by title opening crawl============\n")
print(film_by_title.opening_crawl)
print("=======================================")
print("\nGet Film by Title - Fail")
s.get_film_by_title("Blimmy")
print("\nGet Film by ID - Pass")
film_by_id = s.get_film_by_id("4")
print("\nFilm by id opening crawl===============\n")
print(film_by_id.opening_crawl)
print("=======================================")
print("\nGet Film by ID - Fail")
s.get_film_by_id("0")
print("\nGet First Film")
s.get_first_film()
print("\nPerson Tests ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("\nGet Person by Name - Pass")
person_by_name = s.get_person_by_name("Gregar Typho")
print("Gender: " + person_by_name.gender)
print("Birth year: " + person_by_name.birth_year)
print("\nGet Person by Name - Fail")
s.get_person_by_name("Tupac Shakur")
print("\nGet Person by id - Pass")
person_by_id = s.get_person_by_id("15")
print("Gender: " + person_by_id.gender)
print("Birth year: " + person_by_id.birth_year)
print("\nGet Person by id - Fail")
s.get_person_by_id("9999")
print("\nGet First Person")
s.get_first_person()
print("\nStarship Tests ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("\nGet Starship by Name - Pass")
starship_by_name = s.get_starship_by_name("Executor")
print("Manufacturer: " + starship_by_name.manufacturer)
print("Cost in credits: " + starship_by_name.cost_in_credits)
print("\nGet Starship by Name - Fail")
s.get_starship_by_name("USS Enterprise")
print("\nGet Starship by id - Pass")
starship_by_id = s.get_starship_by_id("10")
print("Manufacturer: " + starship_by_id.manufacturer)
print("Cost in credits: " + starship_by_id.cost_in_credits)
print("\nGet Starship by id - Fail")
s.get_starship_by_id("9999")
print("\nGet First Starship")
s.get_first_starship()
print("\nPlanet Tests ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("\nGet Planet by Name - Pass")
planet_by_name = s.get_planet_by_name("Alderaan")
print("Population: " + planet_by_name.population)
print("Climate: " + planet_by_name.climate)
print("\nGet Planet by Name - Fail")
s.get_planet_by_name("Krikit")
print("\nGet Planet by id - Pass")
planet_by_id = s.get_planet_by_id("22")
print("Population: " + planet_by_id.population)
print("Climate: " + planet_by_id.climate)
print("\nGet Planet by id - Fail")
s.get_planet_by_id("9999")
print("\nGet First Planet")
s.get_first_planet()
print("\nSpecies Tests ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("\nGet Species by Name - Pass")
species_by_name = s.get_species_by_name("Hutt")
print("Language: " + species_by_name.language)
print("Average lifespan: " + species_by_name.average_lifespan + " years.")
print("\nGet Planet by Name - Fail")
s.get_species_by_name("Krikit")
print("\nGet Planet by id - Pass")
species_by_id = s.get_species_by_id("22")
print("Language: " + species_by_id.language)
print("Average lifespan: " + species_by_id.average_lifespan + " years.")
print("\nGet Species by id - Fail")
s.get_species_by_id("9999")
print("\nGet First Species")
s.get_first_species()
print("\nVehicle Tests ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("\nGet Vehicle by Name - Pass")
vehicle_by_name = s.get_vehicle_by_name("X-34 landspeeder")
print("Manufacturer: " + vehicle_by_name.manufacturer)
print("Cost in credits: " + vehicle_by_name.cost_in_credits)
print("\nGet Vehicle by Name - Fail")
s.get_vehicle_by_name("Tesla Model S")
print("\nGet Vehicle by id - Pass")
vehicle_by_id = s.get_vehicle_by_id("18")
print("Manufacturer: " + vehicle_by_id.manufacturer)
print("Cost in credits: " + vehicle_by_id.cost_in_credits)
print("\nGet Vehicle by id - Fail")
s.get_vehicle_by_id("9999")
print("\nGet First Vehicle")
s.get_first_vehicle()