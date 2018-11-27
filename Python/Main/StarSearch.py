import Main
import requests
import json


# todo: refactor this class. Helper methods?
class StarSearch:

    def get_all_resources(self, resource_index):
        self.__init__()
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
            # todo: "eval" is very slow but it works! Replace when possible.
            # # use json library to parse the str(json) into a dictionary
            # local_dict = json.loads(str(requests.get(Main.base_url + Main.categories[resource_index] +
            #                                    "/?page=" + str(page)).json()))
            # Working code below
            local_dict = eval(str(requests.get(Main.base_url + Main.categories[resource_index] +
                                               "/?page=" + str(page)).json()))
            local_objects = [local_dict["results"][num] for num in range(0, len(local_dict["results"]))]
            resource_objects.extend(local_objects)
        return resource_objects


    def object_by_name(self, starship_name):
        self.__init__()
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
        self.__init__()
        film_object = Main.Film(film_dict[Main.film_attributes[0]],
                                film_dict[Main.film_attributes[1]],
                                film_dict[Main.film_attributes[2]],
                                film_dict[Main.film_attributes[3]],
                                film_dict[Main.film_attributes[4]],
                                film_dict[Main.film_attributes[5]],
                                film_dict[Main.film_attributes[6]],
                                film_dict[Main.film_attributes[7]],
                                film_dict[Main.film_attributes[8]],
                                film_dict[Main.film_attributes[9]],
                                film_dict[Main.film_attributes[10]],
                                film_dict[Main.film_attributes[11]],
                                film_dict[Main.film_attributes[12]],
                                film_dict[Main.film_attributes[13]])
        return film_object

    def get_film_by_title(self, film_title):
        self.__init__()
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
            print("You requested: " + matched_title[0])
            single_film_dict = all_films_list[matched_index[0]]
            return self.create_film_object(single_film_dict)

    def get_film_by_id(self, film_id):
        self.__init__()
        # todo: replace "eval" method with something better.
        single_film_dict = eval(str(requests.get(Main.base_url + "films/" + film_id + "/").json()))
        if len(single_film_dict) == 1:
            single_film_dict = {"title": "No such film id."}
            print(single_film_dict["title"])
        else:
            print("You requested: " + single_film_dict["title"])
            return self.create_film_object(single_film_dict)

    def get_first_film(self):
        self.__init__()
        return self.get_film_by_id("1")

    # People
    def create_person_object(self, person_dict):
        self.__init__()
        person_object = Main.Person(person_dict[Main.person_attributes[0]],
                                    person_dict[Main.person_attributes[1]],
                                    person_dict[Main.person_attributes[2]],
                                    person_dict[Main.person_attributes[3]],
                                    person_dict[Main.person_attributes[4]],
                                    person_dict[Main.person_attributes[5]],
                                    person_dict[Main.person_attributes[6]],
                                    person_dict[Main.person_attributes[7]],
                                    person_dict[Main.person_attributes[8]],
                                    person_dict[Main.person_attributes[9]],
                                    person_dict[Main.person_attributes[10]],
                                    person_dict[Main.person_attributes[11]],
                                    person_dict[Main.person_attributes[12]],
                                    person_dict[Main.person_attributes[13]],
                                    person_dict[Main.person_attributes[14]],
                                    person_dict[Main.person_attributes[15]])
        return person_object

    def get_person_by_name(self, person_name):
        self.__init__()
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
            print("You requested: " + matched_name[0])
            single_person_dict = all_persons_dict[matched_index[0]]
            return self.create_person_object(single_person_dict)

    def get_person_by_id(self, person_id):
        self.__init__()
        # todo: replace "eval" method with something better.
        single_person_dict = eval(str(requests.get(Main.base_url + "people/" + person_id + "/").json()))
        if len(single_person_dict) == 1:
            single_person_dict = {"name": "No such person id."}
            print(single_person_dict["name"])
        else:
            print("You requested: " + single_person_dict["name"])
            return self.create_person_object(single_person_dict)

    def get_first_person(self):
        self.__init__()
        return self.get_person_by_id("1")

    # Planets
    def create_planet_object(self, planet_dict):
        self.__init__()
        planet_object = Main.Planet(planet_dict[Main.planet_attributes[0]],
                                    planet_dict[Main.planet_attributes[1]],
                                    planet_dict[Main.planet_attributes[2]],
                                    planet_dict[Main.planet_attributes[3]],
                                    planet_dict[Main.planet_attributes[4]],
                                    planet_dict[Main.planet_attributes[5]],
                                    planet_dict[Main.planet_attributes[6]],
                                    planet_dict[Main.planet_attributes[7]],
                                    planet_dict[Main.planet_attributes[8]],
                                    planet_dict[Main.planet_attributes[9]],
                                    planet_dict[Main.planet_attributes[10]],
                                    planet_dict[Main.planet_attributes[11]],
                                    planet_dict[Main.planet_attributes[12]],
                                    planet_dict[Main.planet_attributes[13]])
        return planet_object

    def get_planet_by_name(self, planet_name):
        self.__init__()
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
            print("You requested: " + matched_name[0])
            single_planet_dict = all_planets_dict[matched_index[0]]
            return self.create_planet_object(single_planet_dict)

    def get_planet_by_id(self, planet_id):
        self.__init__()
        # todo: replace "eval" method with something better.
        single_planet_dict = eval(str(requests.get(Main.base_url + "planets/" + planet_id + "/").json()))
        if len(single_planet_dict) == 1:
            single_planet_dict = {"name": "No such planet id."}
            print(single_planet_dict["name"])
        else:
            print("You requested: " + single_planet_dict["name"])
            return self.create_planet_object(single_planet_dict)

    def get_first_planet(self):
        self.__init__()
        return self.get_planet_by_id("1")

    # Species
    def create_species_object(self, species_dict):
        self.__init__()
        species_object = Main.Species(species_dict[Main.species_attributes[0]],
                                      species_dict[Main.species_attributes[1]],
                                      species_dict[Main.species_attributes[2]],
                                      species_dict[Main.species_attributes[3]],
                                      species_dict[Main.species_attributes[4]],
                                      species_dict[Main.species_attributes[5]],
                                      species_dict[Main.species_attributes[6]],
                                      species_dict[Main.species_attributes[7]],
                                      species_dict[Main.species_attributes[8]],
                                      species_dict[Main.species_attributes[9]],
                                      species_dict[Main.species_attributes[10]],
                                      species_dict[Main.species_attributes[11]],
                                      species_dict[Main.species_attributes[12]],
                                      species_dict[Main.species_attributes[13]],
                                      species_dict[Main.species_attributes[14]])
        return species_object

    def get_species_by_name(self, species_name):
        self.__init__()
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
            print("You requested: " + matched_name[0])
            single_species_dict = all_species_dict[matched_index[0]]
            return self.create_species_object(single_species_dict)

    def get_species_by_id(self, species_id):
        self.__init__()
        # todo: replace "eval" method with something better.
        single_species_dict = eval(str(requests.get(Main.base_url + "species/" + species_id + "/").json()))
        if len(single_species_dict) == 1:
            single_species_dict = {"name": "No such species id."}
            print(single_species_dict["name"])
        else:
            print("You requested: " + single_species_dict["name"])
            return self.create_species_object(single_species_dict)

    def get_first_species(self):
        self.__init__()
        return self.get_species_by_id("1")

    # Starships
    def create_starship_object(self, starship_dict):
        self.__init__()
        starship_object = Main.Starship(starship_dict[Main.starship_attributes[0]],
                                        starship_dict[Main.starship_attributes[1]],
                                        starship_dict[Main.starship_attributes[2]],
                                        starship_dict[Main.starship_attributes[3]],
                                        starship_dict[Main.starship_attributes[4]],
                                        starship_dict[Main.starship_attributes[5]],
                                        starship_dict[Main.starship_attributes[6]],
                                        starship_dict[Main.starship_attributes[7]],
                                        starship_dict[Main.starship_attributes[8]],
                                        starship_dict[Main.starship_attributes[9]],
                                        starship_dict[Main.starship_attributes[10]],
                                        starship_dict[Main.starship_attributes[11]],
                                        starship_dict[Main.starship_attributes[12]],
                                        starship_dict[Main.starship_attributes[13]],
                                        starship_dict[Main.starship_attributes[14]],
                                        starship_dict[Main.starship_attributes[15]],
                                        starship_dict[Main.starship_attributes[16]],
                                        starship_dict[Main.starship_attributes[17]],)
        return starship_object

    def get_starship_by_name(self, starship_name):
        self.__init__()
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

    def get_starship_by_id(self, starship_id):
        self.__init__()
        # todo: replace "eval" method with something better.
        single_starship_dict = eval(str(requests.get(Main.base_url + "starships/" + starship_id + "/").json()))
        if len(single_starship_dict) == 1:
            single_starship_dict = {"name": "No such starship id."}
            print(single_starship_dict["name"])
        else:
            print("You requested: " + single_starship_dict["name"])
            return self.create_starship_object(single_starship_dict)

    def get_first_starship(self):
        self.__init__()
        return self.get_starship_by_id("2")

    # Vehicles
    def create_vehicle_object(self, vehicle_dict):
        self.__init__()
        vehicle_object = Main.Vehicles(vehicle_dict[Main.vehicle_attributes[0]],
                                       vehicle_dict[Main.vehicle_attributes[1]],
                                       vehicle_dict[Main.vehicle_attributes[2]],
                                       vehicle_dict[Main.vehicle_attributes[3]],
                                       vehicle_dict[Main.vehicle_attributes[4]],
                                       vehicle_dict[Main.vehicle_attributes[5]],
                                       vehicle_dict[Main.vehicle_attributes[6]],
                                       vehicle_dict[Main.vehicle_attributes[7]],
                                       vehicle_dict[Main.vehicle_attributes[8]],
                                       vehicle_dict[Main.vehicle_attributes[9]],
                                       vehicle_dict[Main.vehicle_attributes[10]],
                                       vehicle_dict[Main.vehicle_attributes[11]],
                                       vehicle_dict[Main.vehicle_attributes[12]],
                                       vehicle_dict[Main.vehicle_attributes[13]],
                                       vehicle_dict[Main.vehicle_attributes[14]],
                                       vehicle_dict[Main.vehicle_attributes[15]])
        return vehicle_object

    def get_vehicle_by_name(self, vehicle_name):
        self.__init__()
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
            print("You requested: " + matched_name[0])
            single_vehicle_name = all_vehicles_dict[matched_index[0]]
            return self.create_vehicle_object(single_vehicle_name)

    def get_vehicle_by_id(self, vehicle_id):
        self.__init__()
        # todo: replace "eval" method with something better.
        single_vehicle_dict = eval(str(requests.get(Main.base_url + "vehicles/" + vehicle_id + "/").json()))
        if len(single_vehicle_dict) == 1:
            single_vehicle_dict = {"name": "No such vehicle id."}
            print(single_vehicle_dict["name"])
        else:
            print("You requested: " + single_vehicle_dict["name"])
            return self.create_vehicle_object(single_vehicle_dict)

    def get_first_vehicle(self):
        self.__init__()
        return self.get_vehicle_by_id("4")