from typing import Set, Type

from geopy import Point

from betty import load, generate, serve
from betty.app import App, AppExtensionConfiguration, LocaleConfiguration
from betty.app.extension import Extension
from betty.http_api_doc import HttpApiDoc
from betty.load import Loader
from betty.locale import Date, DateRange
from betty.maps import Maps
from betty.model.ancestry import Place, PlaceName, Person, Presence, Subject, PersonName, Link, Source, Citation, Event
from betty.model.event_type import Marriage, Birth, Death
from betty.serve import Server
from betty.trees import Trees
from betty.wikipedia import Wikipedia


class Demo(Extension, Loader):
    @classmethod
    def depends_on(cls) -> Set[Type[Extension]]:
        return {HttpApiDoc, Maps, Trees, Wikipedia}

    async def load(self) -> None:
        amsterdam = Place('betty-demo-amsterdam', [PlaceName('Amsterdam')])
        amsterdam.coordinates = Point(52.366667, 4.9)
        amsterdam.links.add(Link('https://nl.wikipedia.org/wiki/Amsterdam'))
        self._app.ancestry.entities.append(amsterdam)

        ilpendam = Place('betty-demo-ilpendam', [PlaceName('Ilpendam')])
        ilpendam.coordinates = Point(52.465556, 4.951111)
        ilpendam.links.add(Link('https://nl.wikipedia.org/wiki/Ilpendam'))
        self._app.ancestry.entities.append(ilpendam)

        personal_accounts = Source('betty-demo-personal-accounts', 'Personal accounts')
        self._app.ancestry.entities.append(personal_accounts)

        cite_first_person_account = Citation('betty-demo-first-person-account', personal_accounts)
        self._app.ancestry.entities.append(cite_first_person_account)

        bevolkingsregister_amsterdam = Source('betty-demo-bevolkingsregister-amsterdam', 'Bevolkingsregister Amsterdam')
        bevolkingsregister_amsterdam.author = 'Gemeente Amsterdam'
        bevolkingsregister_amsterdam.publisher = 'Gemeente Amsterdam'
        self._app.ancestry.entities.append(bevolkingsregister_amsterdam)

        david_marinus_lankester = Person('betty-demo-david-marinus-lankester')
        PersonName(david_marinus_lankester, 'David Marinus', 'Lankester')
        self._app.ancestry.entities.append(david_marinus_lankester)

        geertruida_van_ling = Person('betty-demo-geertruida-van-ling')
        PersonName(geertruida_van_ling, 'Geertruida', 'Van Ling')
        self._app.ancestry.entities.append(geertruida_van_ling)

        marriage_of_dirk_jacobus_lankester_and_jannigje_palsen = Event('betty-demo-marriage-of-dirk-jacobus-lankester-and-jannigje-palsen', Marriage(), Date(1922, 7, 4))
        marriage_of_dirk_jacobus_lankester_and_jannigje_palsen.place = ilpendam
        self._app.ancestry.entities.append(marriage_of_dirk_jacobus_lankester_and_jannigje_palsen)

        birth_of_dirk_jacobus_lankester = Event('betty-demo-birth-of-dirk-jacobus-lankester', Birth(), Date(1897, 8, 25))
        birth_of_dirk_jacobus_lankester.place = amsterdam
        self._app.ancestry.entities.append(birth_of_dirk_jacobus_lankester)

        death_of_dirk_jacobus_lankester = Event('betty-demo-death-of-dirk-jacobus-lankester', Death(), Date(1986, 8, 18))
        death_of_dirk_jacobus_lankester.place = amsterdam
        self._app.ancestry.entities.append(death_of_dirk_jacobus_lankester)

        dirk_jacobus_lankester = Person('betty-demo-dirk-jacobus-lankester')
        PersonName(dirk_jacobus_lankester, 'Dirk Jacobus', 'Lankester')
        Presence(dirk_jacobus_lankester, Subject(), birth_of_dirk_jacobus_lankester)
        Presence(dirk_jacobus_lankester, Subject(), death_of_dirk_jacobus_lankester)
        Presence(dirk_jacobus_lankester, Subject(), marriage_of_dirk_jacobus_lankester_and_jannigje_palsen)
        dirk_jacobus_lankester.parents.append(david_marinus_lankester, geertruida_van_ling)
        self._app.ancestry.entities.append(dirk_jacobus_lankester)

        birth_of_marinus_david_lankester = Event('betty-demo-birth-of-marinus-david', Birth(), DateRange(Date(1874, 1, 15), Date(1874, 3, 21), start_is_boundary=True, end_is_boundary=True))
        birth_of_marinus_david_lankester.place = amsterdam
        self._app.ancestry.entities.append(birth_of_marinus_david_lankester)

        death_of_marinus_david_lankester = Event('betty-demo-death-of-marinus-david', Death(), Date(1971))
        death_of_marinus_david_lankester.place = amsterdam
        self._app.ancestry.entities.append(death_of_marinus_david_lankester)

        marinus_david_lankester = Person('betty-demo-marinus-david-lankester')
        PersonName(marinus_david_lankester, 'Marinus David', 'Lankester')
        Presence(marinus_david_lankester, Subject(), birth_of_marinus_david_lankester)
        Presence(marinus_david_lankester, Subject(), death_of_marinus_david_lankester)
        marinus_david_lankester.parents.append(david_marinus_lankester, geertruida_van_ling)
        self._app.ancestry.entities.append(marinus_david_lankester)

        birth_of_jacoba_gesina_lankester = Event('betty-demo-birth-of-jacoba-gesina', Birth(), Date(1900, 3, 14))
        birth_of_jacoba_gesina_lankester.place = amsterdam
        self._app.ancestry.entities.append(birth_of_jacoba_gesina_lankester)

        jacoba_gesina_lankester = Person('betty-demo-jacoba-gesina-lankester')
        PersonName(jacoba_gesina_lankester, 'Jacoba Gesina', 'Lankester')
        Presence(jacoba_gesina_lankester, Subject(), birth_of_jacoba_gesina_lankester)
        jacoba_gesina_lankester.parents.append(david_marinus_lankester, geertruida_van_ling)
        self._app.ancestry.entities.append(jacoba_gesina_lankester)

        jannigje_palsen = Person('betty-demo-jannigje-palsen')
        PersonName(jannigje_palsen, 'Jannigje', 'Palsen')
        Presence(jannigje_palsen, Subject(), marriage_of_dirk_jacobus_lankester_and_jannigje_palsen)
        self._app.ancestry.entities.append(jannigje_palsen)

        marriage_of_johan_de_boer_and_liberta_lankester = Event('betty-demo-marriage-of-johan-de-boer-and-liberta-lankester', Marriage(), Date(1953, 6, 19))
        marriage_of_johan_de_boer_and_liberta_lankester.place = amsterdam
        self._app.ancestry.entities.append(marriage_of_johan_de_boer_and_liberta_lankester)

        cite_birth_of_liberta_lankester_from_bevolkingsregister_amsterdam = Citation('betty-demo-birth-of-liberta-lankester-from-bevolkingsregister-amsterdam', bevolkingsregister_amsterdam)
        cite_birth_of_liberta_lankester_from_bevolkingsregister_amsterdam.location = 'Amsterdam'
        self._app.ancestry.entities.append(cite_birth_of_liberta_lankester_from_bevolkingsregister_amsterdam)

        birth_of_liberta_lankester = Event('betty-demo-birth-of-liberta-lankester', Birth(), Date(1929, 12, 22))
        birth_of_liberta_lankester.place = amsterdam
        birth_of_liberta_lankester.citations.append(cite_birth_of_liberta_lankester_from_bevolkingsregister_amsterdam)
        self._app.ancestry.entities.append(birth_of_liberta_lankester)

        death_of_liberta_lankester = Event('betty-demo-death-of-liberta-lankester', Death(), Date(2015, 1, 17))
        death_of_liberta_lankester.place = amsterdam
        death_of_liberta_lankester.citations.append(cite_first_person_account)
        self._app.ancestry.entities.append(death_of_liberta_lankester)

        liberta_lankester = Person('betty-demo-liberta-lankester')
        PersonName(liberta_lankester, 'Liberta', 'Lankester')
        PersonName(liberta_lankester, 'Betty')
        Presence(liberta_lankester, Subject(), birth_of_liberta_lankester)
        Presence(liberta_lankester, Subject(), death_of_liberta_lankester)
        Presence(liberta_lankester, Subject(), marriage_of_johan_de_boer_and_liberta_lankester)
        liberta_lankester.parents.append(dirk_jacobus_lankester, jannigje_palsen)
        self._app.ancestry.entities.append(liberta_lankester)

        birth_of_johan_de_boer = Event('betty-demo-birth-of-johan-de-boer', Birth(), Date(1930, 6, 20))
        birth_of_johan_de_boer.place = amsterdam
        self._app.ancestry.entities.append(birth_of_johan_de_boer)

        death_of_johan_de_boer = Event('betty-demo-death-of-johan-de-boer', Death(), Date(1999, 3, 10))
        death_of_johan_de_boer.place = amsterdam
        death_of_johan_de_boer.citations.append(cite_first_person_account)
        self._app.ancestry.entities.append(death_of_johan_de_boer)

        johan_de_boer = Person('betty-demo-johan-de-boer')
        PersonName(johan_de_boer, 'Johan', 'De Boer')
        PersonName(johan_de_boer, 'Hans')
        Presence(johan_de_boer, Subject(), birth_of_johan_de_boer)
        Presence(johan_de_boer, Subject(), death_of_johan_de_boer)
        Presence(johan_de_boer, Subject(), marriage_of_johan_de_boer_and_liberta_lankester)
        self._app.ancestry.entities.append(johan_de_boer)

        parent_of_bart_feenstra_child_of_liberta_lankester = Person('betty-demo-parent-of-bart-feenstra-child-of-liberta-lankester')
        PersonName(parent_of_bart_feenstra_child_of_liberta_lankester, 'Bart\'s parent')
        parent_of_bart_feenstra_child_of_liberta_lankester.parents.append(johan_de_boer, liberta_lankester)
        self._app.ancestry.entities.append(parent_of_bart_feenstra_child_of_liberta_lankester)

        bart_feenstra = Person('betty-demo-bart-feenstra')
        PersonName(bart_feenstra, 'Bart', 'Feenstra')
        bart_feenstra.parents.append(parent_of_bart_feenstra_child_of_liberta_lankester)
        self._app.ancestry.entities.append(bart_feenstra)


class DemoServer(Server):
    def __init__(self):
        self._server = None
        self._app = None

    @property
    def public_url(self) -> str:
        return self._server.public_url

    async def start(self) -> None:
        self._app = App()
        await self._app.activate()
        self._app.configuration.extensions.add(AppExtensionConfiguration(Demo))
        # Include all of the translations Betty ships with.
        self._app.configuration.locales.replace([
            LocaleConfiguration('en-US', 'en'),
            LocaleConfiguration('nl-NL', 'nl'),
            LocaleConfiguration('fr-FR', 'fr'),
            LocaleConfiguration('uk', 'uk'),
        ])
        self._server = None
        try:
            await load.load(self._app)
            await generate.generate(self._app)
            self._server = serve.AppServer(self._app)
            await self._server.start()
        except BaseException:
            await self._app.deactivate()
            raise

    async def stop(self) -> None:
        await self._server.stop()
        await self._app.deactivate()