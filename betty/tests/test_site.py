from unittest import TestCase

from betty.ancestry import Ancestry
from betty.config import Configuration
from betty.site import Site


class SiteTest(TestCase):
    def test_ancestry_should_return(self):
        ancestry = Ancestry()
        configuration = Configuration('foo', 'bar', 'baz')
        sut = Site(ancestry, configuration)
        self.assertEquals(ancestry, sut.ancestry)

    def test_configuration_should_return(self):
        ancestry = Ancestry()
        configuration = Configuration('foo', 'bar', 'baz')
        sut = Site(ancestry, configuration)
        self.assertEquals(configuration, sut.configuration)
