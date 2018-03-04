from os import getenv

import pytest

from main import create_app


@pytest.fixture
def app():
    app = create_app()
    app.config.update(
        DEBUG=True,
        SERVER_NAME=getenv('RUNNER_IP')
    )

    return app
