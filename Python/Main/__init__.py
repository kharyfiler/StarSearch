base_url = "https://swapi.co/api/"
# todo: improve base category reference block to a dictionary, static dictionary?
film_pages = 1
people_pages = 9
planet_pages = 7
species_pages = 4
starship_pages = 4
vehicle_pages = 4

categories = ["films", "people", "planets", "species", "starships", "vehicles"]

film_attributes = ["title", "episode_id", "opening_crawl", "director", "producer", "release_date", "species",
                   "starships", "vehicles", "characters", "planets", "url", "created", "edited"]

person_attributes = ["name", "birth_year", "eye_color", "gender", "hair_color", "height", "mass", "skin_color",
                     "homeworld", "films", "species", "starships", "vehicles", "url", "created", "edited"]

starship_attributes = ["name", "model", "starship_class", "manufacturer", "cost_in_credits", "length", "crew",
                       "passengers", "max_atmosphering_speed", "hyperdrive_rating", "MGLT", "cargo_capacity",
                       "consumables", "films", "pilots", "url", "created", "edited"]

vehicle_attributes = ["name", "model", "vehicle_class", "manufacturer", "length", "cost_in_credits", "crew",
                      "passengers", "max_atmosphering_speed", "cargo_capacity", "consumables", "films", "pilots", "url",
                      "created", "edited"]

species_attributes = ["name", "classification", "designation", "average_height", "average_lifespan", "eye_colors",
                      "hair_colors", "skin_colors", "language", "homeworld", "people", "films", "url", "created",
                      "edited"]

planet_attributes = ["name", "diameter", "rotation_period", "orbital_period", "gravity", "population", "climate",
                     "terrain", "surface_water", "residents", "films", "url", "created", "edited"]


class Film:

    def __init__(self, title, episode_id, opening_crawl, director, producer, release_date, species, starships, vehicles,
                 characters, planets, url, created, edited):
        self.title = title
        self.episode_id = episode_id
        self.opening_crawl = opening_crawl
        self.director = director
        self.producer = producer
        self.release_date = release_date
        self.species = species
        self.starships = starships
        self.vehicles = vehicles
        self.characters = characters
        self.planets = planets
        self.url = url
        self.created = created
        self.edited = edited


class Person:

    def __init__(self, name, birth_year, eye_color, gender, hair_color, height, mass, skin_color, homeworld, films,
                 species, starships, vehicles, url, created, edited):
        self.name = name
        self.birth_year = birth_year
        self.eye_color = eye_color
        self.gender = gender
        self.hair_color = hair_color
        self.height = height
        self.mass = mass
        self.skin_color = skin_color
        self.homeworld = homeworld
        self.films = films
        self.species = species
        self.starships = starships
        self.vehicles = vehicles
        self.url = url
        self.created = created
        self.edited = edited


class Starship:

    def __init__(self, name, model, starship_class, manufacturer, cost_in_credits, length, crew, passengers,
                 max_atmosphering_speed, hyperdrive_rating, MGLT, cargo_capacity, consumables, films, pilots, url,
                 created, edited):
        self.name = name
        self.model = model
        self.starship_class = starship_class
        self.manufacturer = manufacturer
        self.cost_in_credits = cost_in_credits
        self.length = length
        self.crew = crew
        self.passengers = passengers
        self.max_atmosphering_speed = max_atmosphering_speed
        self.hyperdrive_rating = hyperdrive_rating
        self.MGLT = MGLT
        self.cargo_capacity = cargo_capacity
        self.consumables = consumables
        self.films = films
        self.pilots = pilots
        self.url = url
        self.created = created
        self.edited = edited


class Vehicles:

    def __init__(self, name, model, vehicle_class, manufacturer, length, cost_in_credits, crew, passengers,
                 max_atmosphering_speed, cargo_capacity, consumables, films, pilots, url, created, edited):
        self.name = name
        self.model = model
        self.vehicle_class = vehicle_class
        self.manufacturer = manufacturer
        self.length = length
        self.cost_in_credits = cost_in_credits
        self.crew = crew
        self.passengers = passengers
        self.max_atmosphering_speed = max_atmosphering_speed
        self.cargo_capacity = cargo_capacity
        self.consumables = consumables
        self.films = films
        self.pilots = pilots
        self.url = url
        self.created = created
        self.edited = edited


class Species:

    def __init__(self, name, classification, designation, average_height, average_lifespan, eye_colors, hair_colors,
                 skin_colors, language, homeworld, people, films, url, created, edited):
        self.name = name
        self.classification = classification
        self.designation = designation
        self.average_height = average_height
        self.average_lifespan = average_lifespan
        self.eye_colors = eye_colors
        self.hair_colors = hair_colors
        self.skin_colors = skin_colors
        self.language = language
        self.homeworld = homeworld
        self.people = people
        self.films = films
        self.url = url
        self.created = created
        self.edited = edited


class Planet:

    def __init__(self, name, diameter, rotation_period, orbital_period, gravity, population, climate, terrain,
                 surface_water, residents, films, url, created, edited):
        self.name = name
        self.diameter = diameter
        self.rotation_period = rotation_period
        self.orbital_period = orbital_period
        self.gravity = gravity
        self.population = population
        self.climate = climate
        self.terrain = terrain
        self.surface_water = surface_water
        self.residents = residents
        self.films = films
        self.url = url
        self.created = created
        self.edited = edited
