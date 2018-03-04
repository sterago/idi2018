import pytest

from main import create_app


@pytest.fixture
def app():
    app = create_app()
    app.config.update(
        DEBUG=True,
        SERVER_NAME='192.168.1.108'
    )

    return app
