from betty.app import App
from betty.extension import Maps
from betty.generate import generate
from betty.project import ExtensionConfiguration
from betty.tests import patch_cache


class TestMaps:
    @patch_cache
    async def test_generate(self) -> None:
        async with App() as app:
            app.project.configuration.debug = True
            app.project.configuration.extensions.append(ExtensionConfiguration(Maps))
            await generate(app)
            with open(app.project.configuration.www_directory_path / 'maps.js', encoding='utf-8') as f:
                betty_js = f.read()
            assert 'maps.js' in betty_js
            with open(app.project.configuration.www_directory_path / 'maps.css', encoding='utf-8') as f:
                betty_css = f.read()
            assert '.map' in betty_css
