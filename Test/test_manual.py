import pytest
import starwars_api.StarSearch


@pytest.fixture(scope='module')
def api():
    return starwars_api.StarSearch.StarSearch()


def test_person_name(api):
    person = api.get_person_by_name("Gregar Typho")
    assert person.name == "Gregar Typho"