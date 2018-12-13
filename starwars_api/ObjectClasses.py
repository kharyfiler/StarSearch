import datetime

base_url = "https://swapi.co/api/"
# todo: improve base category reference block to a dictionary, static dictionary?
film_pages = 1
people_pages = 9
planet_pages = 7
species_pages = 4
starship_pages = 4
vehicle_pages = 4

categories = ["films", "people", "planets", "species", "starships", "vehicles"]


# todo: pass the response into the class object as a parameter
class Film:

    def __init__(self, film_response):

        self.title = film_response["title"]
        self.episode_id = film_response["episode_id"]
        self.opening_crawl = film_response["opening_crawl"]
        self.director = film_response["director"]
        self.producer = film_response["producer"]
        self.release_date = film_response["release_date"]
        self.species = film_response["species"]
        self.starships = film_response["starships"]
        self.vehicles = film_response["vehicles"]
        self.characters = film_response["characters"]
        self.planets = film_response["planets"]
        self.url = film_response["url"]
        self.created = film_response["created"]
        self.edited = film_response["edited"]


class Person:

    def __init__(self, person_response):

        self.name = person_response["name"]
        self.birth_year = person_response["birth_year"]
        self.eye_color = person_response["eye_color"]
        self.gender = person_response["gender"]
        self.hair_color = person_response["hair_color"]
        self.height = person_response["height"]
        self.mass = person_response["mass"]
        self.skin_color = person_response["skin_color"]
        self.homeworld = person_response["homeworld"]
        self.films = person_response["films"]
        self.species = person_response["species"]
        self.starships = person_response["starships"]
        self.vehicles = person_response["vehicles"]
        self.url = person_response["url"]
        self.created = person_response["created"]
        self.edited = person_response["edited"]


class Starship:

    def __init__(self, starship_response):

        self.name = starship_response["name"]
        self.model = starship_response["model"]
        self.starship_class = starship_response["starship_class"]
        self.manufacturer = starship_response["manufacturer"]
        self.cost_in_credits = starship_response["cost_in_credits"]
        self.length = starship_response["length"]
        self.crew = starship_response["crew"]
        self.passengers = starship_response["passengers"]
        self.max_atmosphering_speed = starship_response["max_atmosphering_speed"]
        self.hyperdrive_rating = starship_response["hyperdrive_rating"]
        self.MGLT = starship_response["MGLT"]
        self.cargo_capacity = starship_response["cargo_capacity"]
        self.consumables = starship_response["consumables"]
        self.films = starship_response["films"]
        self.pilots = starship_response["pilots"]
        self.url = starship_response["url"]
        self.created = starship_response["created"]
        self.edited = starship_response["edited"]


class Vehicle:

    def __init__(self, vehicle_response):

        self.name = vehicle_response["name"]
        self.model = vehicle_response["model"]
        self.vehicle_class = vehicle_response["vehicle_class"]
        self.manufacturer = vehicle_response["manufacturer"]
        self.length = vehicle_response["length"]
        self.cost_in_credits = vehicle_response["cost_in_credits"]
        self.crew = vehicle_response["crew"]
        self.passengers = vehicle_response["passengers"]
        self.max_atmosphering_speed = vehicle_response["max_atmosphering_speed"]
        self.cargo_capacity = vehicle_response["cargo_capacity"]
        self.consumables = vehicle_response["consumables"]
        self.films = vehicle_response["films"]
        self.pilots = vehicle_response["pilots"]
        self.url = vehicle_response["url"]
        self.created = vehicle_response["created"]
        self.edited = vehicle_response["edited"]


class Species:

    def __init__(self, species_response):

        self.name = species_response["name"]
        self.classification = species_response["classification"]
        self.designation = species_response["designation"]
        self.average_height = species_response["average_height"]
        self.average_lifespan = species_response["average_lifespan"]
        self.eye_colors = species_response["eye_colors"]
        self.hair_colors = species_response["hair_colors"]
        self.skin_colors = species_response["skin_colors"]
        self.language = species_response["language"]
        self.homeworld = species_response["homeworld"]
        self.people = species_response["people"]
        self.films = species_response["films"]
        self.url = species_response["url"]
        self.created = species_response["created"]
        self.edited = species_response["edited"]


class Planet:

    def __init__(self, planet_response):

        self.name = planet_response["name"]
        self.diameter = planet_response["diameter"]
        self.rotation_period = planet_response["rotation_period"]
        self.orbital_period = planet_response["orbital_period"]
        self.gravity = planet_response["gravity"]
        self.population = planet_response["population"]
        self.climate = planet_response["climate"]
        self.terrain = planet_response["terrain"]
        self.surface_water = planet_response["surface_water"]
        self.residents = planet_response["residents"]
        self.films = planet_response["films"]
        self.url = planet_response["url"]
        self.created = planet_response["created"]
        self.edited = planet_response["edited"]
