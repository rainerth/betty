import json
from unittest import TestCase

from geopy import Point
from parameterized import parameterized

from betty.ancestry import Place, Ancestry, Person, PlaceName
from betty.json import JSONEncoder
from betty.locale import Locale


class JSONEncoderTest(TestCase):
    def assert_encodes(self, expected, data):
        self.assertAlmostEquals(expected, json.loads(
            json.dumps(data, cls=JSONEncoder)))

    @parameterized.expand([
        ('I am a string', 'I am a string'),
        (123, 123),
        ([], []),
        ((), []),
        ({}, {}),
    ])
    def test_builtin_type_should_encode(self, data, expected):
        self.assert_encodes(expected, data)

    def test_coordinates_should_encode(self):
        latitude = 12.345
        longitude = -54.321
        coordinates = Point(latitude, longitude)
        expected = {
            'latitude': latitude,
            'longitude': longitude,
        }
        self.assert_encodes(expected, coordinates)

    def test_place_should_encode_minimal(self):
        place_id = 'the_place'
        name = 'The Place'
        place = Place(place_id, [PlaceName(name)])
        expected = {
            'id': place_id,
            'names': [
                {
                    'name': name,
                },
            ],
        }
        self.assert_encodes(expected, place)

    def test_place_should_encode_full(self):
        place_id = 'the_place'
        name = 'The Place'
        locale = Locale('nl', 'NL')
        latitude = 12.345
        longitude = -54.321
        coordinates = Point(latitude, longitude)
        place = Place(place_id, [PlaceName(name, locale)])
        place.coordinates = coordinates
        expected = {
            'id': place_id,
            'names': [
                {
                    'name': name,
                    'locale': 'nl_NL',
                },
            ],
            'coordinates': {
                'latitude': latitude,
                'longitude': longitude,
            }
        }
        self.assert_encodes(expected, place)

    def test_person_should_encode_minimal(self):
        person_id = 'the_person'
        person = Person(person_id)
        expected = {
            'id': person_id,
            'family_name': None,
            'individual_name': None,
            'parent_ids': [],
            'child_ids': [],
            'private': None,
        }
        self.assert_encodes(expected, person)

    def test_person_should_encode_full(self):
        parent_id = 'the_parent'
        parent = Person(parent_id)

        child_id = 'the_child'
        child = Person(child_id)

        person_id = 'the_person'
        person_family_name = 'Person'
        person_individual_name = 'The'
        person = Person(person_id, person_individual_name, person_family_name)
        person.parents.add(parent)
        person.children.add(child)
        person.private = False

        expected = {
            'id': person_id,
            'family_name': person_family_name,
            'individual_name': person_individual_name,
            'parent_ids': [parent_id],
            'child_ids': [child_id],
            'private': False,
        }
        self.assert_encodes(expected, person)

    def test_ancestry_should_encode_minimal(self):
        ancestry = Ancestry()
        expected = {
            'places': {},
            'people': {},
        }
        self.assert_encodes(expected, ancestry)

    def test_ancestry_should_encode_full(self):
        ancestry = Ancestry()

        place_id = 'the_place'
        place_name = 'The Place'
        place_name_locale = Locale('nl', 'NL')
        place = Place(place_id, [PlaceName(place_name, place_name_locale)])
        ancestry.places[place_id] = place

        person_id = 'the_person'
        person_family_name = 'Person'
        person_individual_name = 'The'
        person = Person(person_id, person_individual_name, person_family_name)
        ancestry.people[person_id] = person

        expected = {
            'places': {
                place_id: {
                    'id': place_id,
                    'names': [
                        {
                            'name': place_name,
                            'locale': 'nl_NL',
                        },
                    ],
                },
            },
            'people': {
                person_id: {
                    'id': person_id,
                    'family_name': person_family_name,
                    'individual_name': person_individual_name,
                    'parent_ids': [],
                    'child_ids': [],
                    'private': None,
                },
            },
        }
        self.assert_encodes(expected, ancestry)
