import requests
import starwars_api.ObjectClasses as ObjectClasses


class StarSearch:
    # todo: run initializer for all methods
    url_name_dict = {}

    # todo: refactor this method
    def complete_object_dict_maker(self):
        complete_dict = {}

        film_list = self.get_all_resources(0)
        people_list = self.get_all_resources(1)
        planet_list = self.get_all_resources(2)
        species_list = self.get_all_resources(3)
        starship_list = self.get_all_resources(4)
        vehicle_list = self.get_all_resources(5)

        print("Completing Films.")
        for film_entry in film_list:
            dict_entry = {film_entry["title"]: ObjectClasses.Film(film_entry)}
            complete_dict.update(dict_entry)
            self.url_name_dict.update({film_entry["url"]:film_entry["title"]})

        print("Completing People.")
        for person_entry in people_list:
            dict_entry = {person_entry["name"]: ObjectClasses.Person(person_entry)}
            complete_dict.update(dict_entry)
            self.url_name_dict.update({person_entry["url"]: person_entry["name"]})

        print("Completing Planets.")
        for planet_entry in planet_list:
            dict_entry = {planet_entry["name"]: ObjectClasses.Planet(planet_entry)}
            complete_dict.update(dict_entry)
            self.url_name_dict.update({planet_entry["url"]: planet_entry["name"]})

        print("Completing Species.")
        for species_entry in species_list:
            dict_entry = {species_entry["name"]: ObjectClasses.Species(species_entry)}
            complete_dict.update(dict_entry)
            self.url_name_dict.update({species_entry["url"]: species_entry["name"]})

        print("Completing Starships.")
        for starship_entry in starship_list:
            dict_entry = {starship_entry["name"]: ObjectClasses.Starship(starship_entry)}
            complete_dict.update(dict_entry)
            self.url_name_dict.update({starship_entry["url"]: starship_entry["name"]})

        print("Completing Vehicles.")
        for vehicle_entry in vehicle_list:
            dict_entry = {vehicle_entry["name"]: ObjectClasses.Vehicle(vehicle_entry)}
            complete_dict.update(dict_entry)
            self.url_name_dict.update({vehicle_entry["url"]: vehicle_entry["name"]})

        return complete_dict

    def get_all_resources(self, resource_index):
        resource_objects = []

        def page_finder(index_num):
            switcher = {
                0: 1,
                1: 9,
                2: 7,
                3: 4,
                4: 4,
                5: 4
            }
            return switcher.get(index_num, "Invalid resource index.")
        page_num = page_finder(resource_index)
        for page in range(1, page_num + 1):
            local_dict = requests.get("https://www.swapi.co/api/" + ObjectClasses.categories[resource_index] +
                                               "/?page=" + str(page)).json()
            local_objects = [local_dict["results"][num] for num in range(0, len(local_dict["results"]))]
            resource_objects.extend(local_objects)
        return resource_objects

    def object_by_name(self, starship_name):
        # todo: make resource categories avaialable via easy string call
        all_starships_dict = self.get_all_resources(4)
        names = [entry["name"] for entry in all_starships_dict]
        matched_name = [entry for entry in names if entry == starship_name]
        matched_index = [index for index, entry in enumerate(names) if entry == starship_name]
        if len(matched_name) == 0:
            matched_name = ["No such starship."]
            print(matched_name[0])
            return
        else:
            print("You requested: " + matched_name[0])
            single_starship_dict = all_starships_dict[matched_index[0]]
            return self.create_starship_object(single_starship_dict)

    # Films
    def create_film_object(self, film_dict):
        film_object = ObjectClasses.Film(film_dict)
        return film_object

    def get_film_by_title(self, film_title):
        # todo: make resource categories avaialable via easy string call
        all_films_list = self.get_all_resources(0)
        titles = [entry["title"] for entry in all_films_list]
        matched_title = [entry for entry in titles if entry == film_title]
        matched_index = [index for index, entry in enumerate(titles) if entry == film_title]
        if len(matched_title) == 0:
            matched_title = ["No such film title."]
            print(matched_title[0])
            return
        else:
            single_film_dict = all_films_list[matched_index[0]]
            return self.create_film_object(single_film_dict)

    def get_film_by_id(self, film_id):
        single_film_dict = requests.get(ObjectClasses.base_url + "films/" + film_id + "/").json()
        if len(single_film_dict) == 1:
            single_film_dict = {"title": "No such film id."}
            print(single_film_dict["title"])
        else:
            return self.create_film_object(single_film_dict)

    def get_first_film(self):
        return self.get_film_by_id("1")

    # People
    def create_person_object(self, person_dict):
        person_object = ObjectClasses.Person(person_dict)
        return person_object

    def get_person_by_name(self, person_name):
        # todo: make resource categories avaialable via easy string call
        all_persons_dict = self.get_all_resources(1)
        names = [entry["name"] for entry in all_persons_dict]
        matched_name = [entry for entry in names if entry == person_name]
        matched_index = [index for index, entry in enumerate(names) if entry == person_name]
        if len(matched_name) == 0:
            matched_name = ["No such person exists in this galaxy."]
            print(matched_name[0])
            return
        else:
            single_person_dict = all_persons_dict[matched_index[0]]
            return self.create_person_object(single_person_dict)

    def get_person_by_id(self, person_id):
        single_person_dict = requests.get(ObjectClasses.base_url + "people/" + person_id + "/").json()
        if len(single_person_dict) == 1:
            single_person_dict = {"name": "No such person id."}
            print(single_person_dict["name"])
        else:
            return self.create_person_object(single_person_dict)

    def get_first_person(self):
        return self.get_person_by_id("1")

    # Planets
    def create_planet_object(self, planet_dict):
        planet_object = ObjectClasses.Planet(planet_dict)
        return planet_object

    def get_planet_by_name(self, planet_name):
        # todo: make resource categories avaialable via easy string call
        all_planets_dict = self.get_all_resources(2)
        names = [entry["name"] for entry in all_planets_dict]
        matched_name = [entry for entry in names if entry == planet_name]
        matched_index = [index for index, entry in enumerate(names) if entry == planet_name]
        if len(matched_name) == 0:
            matched_name = ["No such planet exists in this galaxy."]
            print(matched_name[0])
            return
        else:
            single_planet_dict = all_planets_dict[matched_index[0]]
            return self.create_planet_object(single_planet_dict)

    def get_planet_by_id(self, planet_id):
        single_planet_dict = requests.get(ObjectClasses.base_url + "planets/" + planet_id + "/").json()
        if len(single_planet_dict) == 1:
            single_planet_dict = {"name": "No such planet id."}
            print(single_planet_dict["name"])
        else:
            return self.create_planet_object(single_planet_dict)

    def get_first_planet(self):
        return self.get_planet_by_id("1")

    # Species
    def create_species_object(self, species_dict):
        species_object = ObjectClasses.Species(species_dict)
        return species_object

    def get_species_by_name(self, species_name):
        # todo: make resource categories avaialable via easy string call
        all_species_dict = self.get_all_resources(3)
        names = [entry["name"] for entry in all_species_dict]
        matched_name = [entry for entry in names if entry == species_name]
        matched_index = [index for index, entry in enumerate(names) if entry == species_name]
        if len(matched_name) == 0:
            matched_name = ["No such species exists in this galaxy."]
            print(matched_name[0])
            return
        else:
            single_species_dict = all_species_dict[matched_index[0]]
            return self.create_species_object(single_species_dict)

    def get_species_by_id(self, species_id):
        single_species_dict = requests.get(ObjectClasses.base_url + "species/" + species_id + "/").json()
        if len(single_species_dict) == 1:
            single_species_dict = {"name": "No such species id."}
            print(single_species_dict["name"])
        else:
            return self.create_species_object(single_species_dict)

    def get_first_species(self):
        return self.get_species_by_id("1")

    # Starships
    def create_starship_object(self, starship_dict):
        starship_object = ObjectClasses.Starship(starship_dict)
        return starship_object

    def get_starship_by_name(self, starship_name):
        # todo: make resource categories avaialable via easy string call
        all_starships_dict = self.get_all_resources(4)
        names = [entry["name"] for entry in all_starships_dict]
        matched_name = [entry for entry in names if entry == starship_name]
        matched_index = [index for index, entry in enumerate(names) if entry == starship_name]
        if len(matched_name) == 0:
            matched_name = ["No such starship."]
            print(matched_name[0])
            return
        else:
            single_starship_dict = all_starships_dict[matched_index[0]]
            return self.create_starship_object(single_starship_dict)

    def get_starship_by_id(self, starship_id):
        single_starship_dict = requests.get(ObjectClasses.base_url + "starships/" + starship_id + "/").json()
        if len(single_starship_dict) == 1:
            single_starship_dict = {"name": "No such starship id."}
            print(single_starship_dict["name"])
        else:
            return self.create_starship_object(single_starship_dict)

    def get_first_starship(self):
        return self.get_starship_by_id("2")

    # Vehicles
    def create_vehicle_object(self, vehicle_dict):
        vehicle_object = ObjectClasses.Vehicle(vehicle_dict)
        return vehicle_object

    def get_vehicle_by_name(self, vehicle_name):
        # todo: make resource categories avaialable via easy string call
        all_vehicles_dict = self.get_all_resources(5)
        names = [entry["name"] for entry in all_vehicles_dict]
        matched_name = [entry for entry in names if entry == vehicle_name]
        matched_index = [index for index, entry in enumerate(names) if entry == vehicle_name]
        if len(matched_name) == 0:
            matched_name = ["No such vehicle."]
            print(matched_name[0])
            return
        else:
            single_vehicle_name = all_vehicles_dict[matched_index[0]]
            return self.create_vehicle_object(single_vehicle_name)

    def get_vehicle_by_id(self, vehicle_id):
        single_vehicle_dict = requests.get(ObjectClasses.base_url + "vehicles/" + vehicle_id + "/").json()
        if len(single_vehicle_dict) == 1:
            single_vehicle_dict = {"name": "No such vehicle id."}
            print(single_vehicle_dict["name"])
        else:
            return self.create_vehicle_object(single_vehicle_dict)

    def get_first_vehicle(self):
        return self.get_vehicle_by_id("4")