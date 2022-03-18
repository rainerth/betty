from betty.asyncio import sync
from betty.generate import generate
from betty.maps import Maps
from betty.app import App, AppExtensionConfiguration
from betty.tests import patch_cache, TestCase


class MapsTest(TestCase):
    @patch_cache
    @sync
    async def test_post_generate_event(self):
        async with App() as app:
            app.configuration.debug = True
            app.configuration.extensions.add(AppExtensionConfiguration(Maps))
            await generate(app)
            with open(app.configuration.www_directory_path / 'maps.js', encoding='utf-8') as f:
                betty_js = f.read()
            self.assertIn('maps.js', betty_js)
            with open(app.configuration.www_directory_path / 'maps.css', encoding='utf-8') as f:
                betty_css = f.read()
            self.assertIn('.map', betty_css)