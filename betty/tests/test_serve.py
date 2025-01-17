import os
from time import sleep

import requests
from pytest_mock import MockerFixture

from betty.app import App
from betty.serve import BuiltinAppServer


class TestBuiltinServer:
    async def test(self, mocker: MockerFixture) -> None:
        mocker.patch('webbrowser.open_new_tab')
        content = 'Hello, and welcome to my site!'
        app = App()
        os.makedirs(app.project.configuration.www_directory_path)
        with open(app.project.configuration.www_directory_path / 'index.html', 'w') as f:
            f.write(content)
        async with BuiltinAppServer(app) as server:
            # Wait for the server to start.
            sleep(1)
            response = requests.get(server.public_url)
            assert 200 == response.status_code
            assert content == response.content.decode('utf-8')
            assert 'no-cache' == response.headers['Cache-Control']
