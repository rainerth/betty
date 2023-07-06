from typing import Any

import pytest

from betty.app import App
from betty.extension.cotton_candy import _ColorConfiguration, CottonCandyConfiguration
from betty.model import Entity, get_entity_type_name, UserFacingEntity
from betty.project import EntityReference
from betty.serde.dump import Dump
from betty.serde.load import AssertionFailed
from betty.tests.serde import raises_error


class TestColorConfiguration:
    def test_hex_with_valid_value(self) -> None:
        hex_value = '#000000'
        sut = _ColorConfiguration('#ffffff')
        sut.hex = hex_value
        assert hex_value == sut.hex

    @pytest.mark.parametrize('hex_value', [
        'rgb(0,0,0)',
        'pink',
    ])
    def test_hex_with_invalid_value(self, hex_value: str) -> None:
        sut = _ColorConfiguration('#ffffff')
        with App():
            with pytest.raises(AssertionFailed):
                sut.hex = hex_value

    def test_load_with_valid_hex_value(self) -> None:
        hex_value = '#000000'
        dump = hex_value
        sut = _ColorConfiguration('#ffffff').load(dump)
        assert hex_value == sut.hex

    @pytest.mark.parametrize('dump', [
        False,
        123,
        'rgb(0,0,0)',
        'pink',
    ])
    def test_load_with_invalid_value(self, dump: Dump) -> None:
        sut = _ColorConfiguration('#ffffff')
        with raises_error(error_type=AssertionFailed):
            sut.load(dump)

    def test_dump_with_value(self) -> None:
        hex_value = '#000000'
        assert hex_value == _ColorConfiguration(hex_value=hex_value).dump()


class CottonCandyConfigurationTestEntity(UserFacingEntity, Entity):
    pass


class CottonCandyConfigurationTestEntitytest_load_with_featured_entities:
    pass


class TestCottonCandyConfiguration:
    def test_load_with_minimal_configuration(self) -> None:
        dump: dict[str, Any] = {}
        CottonCandyConfiguration().load(dump)

    def test_load_without_dict_should_error(self) -> None:
        dump = None
        with raises_error(error_type=AssertionFailed):
            CottonCandyConfiguration().load(dump)

    def test_load_with_featured_entities(self) -> None:
        entity_type = CottonCandyConfigurationTestEntity
        entity_id = '123'
        dump: Dump = {
            'featured_entities': [
                {
                    'entity_type': get_entity_type_name(entity_type),
                    'entity_id': entity_id,
                },
            ],
        }
        sut = CottonCandyConfiguration.load(dump)
        assert entity_type == sut.featured_entities[0].entity_type
        assert entity_id == sut.featured_entities[0].entity_id

    def test_load_with_primary_inactive_color(self) -> None:
        hex_value = '#000000'
        dump: Dump = {
            'primary_inactive_color': hex_value,
        }
        sut = CottonCandyConfiguration.load(dump)
        assert hex_value == sut.primary_inactive_color.hex

    def test_load_with_primary_active_color(self) -> None:
        hex_value = '#000000'
        dump: Dump = {
            'primary_active_color': hex_value,
        }
        sut = CottonCandyConfiguration.load(dump)
        assert hex_value == sut.primary_active_color.hex

    def test_load_with_link_inactive_color(self) -> None:
        hex_value = '#000000'
        dump: Dump = {
            'link_inactive_color': hex_value,
        }
        sut = CottonCandyConfiguration.load(dump)
        assert hex_value == sut.link_inactive_color.hex

    def test_load_with_link_active_color(self) -> None:
        hex_value = '#000000'
        dump: Dump = {
            'link_active_color': hex_value,
        }
        sut = CottonCandyConfiguration.load(dump)
        assert hex_value == sut.link_active_color.hex

    def test_dump_with_minimal_configuration(self) -> None:
        sut = CottonCandyConfiguration()
        expected = {
            'primary_inactive_color': CottonCandyConfiguration.DEFAULT_PRIMARY_INACTIVE_COLOR,
            'primary_active_color': CottonCandyConfiguration.DEFAULT_PRIMARY_ACTIVE_COLOR,
            'link_inactive_color': CottonCandyConfiguration.DEFAULT_LINK_INACTIVE_COLOR,
            'link_active_color': CottonCandyConfiguration.DEFAULT_LINK_ACTIVE_COLOR,
        }
        assert expected == sut.dump()

    def test_dump_with_featured_entities(self) -> None:
        sut = CottonCandyConfiguration()
        entity_type = CottonCandyConfigurationTestEntity
        entity_id = '123'
        sut.featured_entities.append(EntityReference(entity_type, entity_id))
        expected = [
            {
                'entity_type': get_entity_type_name(entity_type),
                'entity_id': entity_id,
            },
        ]
        dump = sut.dump()
        assert isinstance(dump, dict)
        assert expected == dump['featured_entities']

    def test_dump_with_primary_inactive_color(self) -> None:
        hex_value = '#000000'
        sut = CottonCandyConfiguration()
        sut.primary_inactive_color.hex = hex_value
        dump = sut.dump()
        assert isinstance(dump, dict)
        assert hex_value == dump['primary_inactive_color']

    def test_dump_with_primary_active_color(self) -> None:
        hex_value = '#000000'
        sut = CottonCandyConfiguration()
        sut.primary_active_color.hex = hex_value
        dump = sut.dump()
        assert isinstance(dump, dict)
        assert hex_value == dump['primary_active_color']

    def test_dump_with_link_inactive_color(self) -> None:
        hex_value = '#000000'
        sut = CottonCandyConfiguration()
        sut.link_inactive_color.hex = hex_value
        dump = sut.dump()
        assert isinstance(dump, dict)
        assert hex_value == dump['link_inactive_color']

    def test_dump_with_link_active_color(self) -> None:
        hex_value = '#000000'
        sut = CottonCandyConfiguration()
        sut.link_active_color.hex = hex_value
        dump = sut.dump()
        assert isinstance(dump, dict)
        assert hex_value == dump['link_active_color']