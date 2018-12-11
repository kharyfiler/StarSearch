import pytest
import starwars_api.StarSearch


@pytest.fixture(scope='module')
def api():
    return starwars_api.StarSearch.StarSearch()


def test_person_name(api):
    person = api.get_person_by_name("Gregar Typho")
    assert person.name == "Gregar Typho"


def test_person_id(api):
    person = api.get_person_by_id("1")
    assert person.name == "Luke Skywalker"


def test_film_title(api):
    film = api.get_film_by_title("A New Hope")
    assert film.title == "A New Hope"


def test_film_id(api):
    film = api.get_film_by_id("2")
    assert film.title == "The Empire Strikes Back"


def test_planet_id(api):
    planet = api.get_planet_by_id("10")
    assert planet.name == "Kamino"


def test_planet_name(api):
    planet = api.get_planet_by_name("Kashyyyk")
    assert planet.name == "Kashyyyk"


def test_species_id(api):
    species = api.get_species_by_id("26")
    assert species.name == "Kel Dor"


def test_species_name(api):
    species = api.get_species_by_name("Ewok")
    assert species.name == "Ewok"


def test_starship_by_id(api):
    starship = api.get_starship_by_id("9")
    assert starship.name == "Death Star"


def test_starship_by_name(api):
    starship = api.get_starship_by_name("Rebel transport")
    assert starship.name == "Rebel transport"


def test_vehicle_by_id(api):
    vehicle = api.get_vehicle_by_id("14")
    assert vehicle.name == "Snowspeeder"


def test_vehicle_by_name(api):
    vehicle = api.get_vehicle_by_name("Bantha-II cargo skiff")
    assert vehicle.name == "Bantha-II cargo skiff"