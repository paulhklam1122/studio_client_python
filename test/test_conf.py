import pytest
import skylab_genesis


@pytest.fixture
def api_key():
    return 'PYTHON_API_CLIENT_TEST_KEY'

@pytest.fixture
def api_options():
    return {'DEBUG': False}

@pytest.fixture
def api(api_key, api_options):
    return skylab_genesis.api(api_key, **api_options)
