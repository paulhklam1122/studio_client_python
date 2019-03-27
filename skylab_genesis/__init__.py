"""
SkylabGenesis - Python Client
For more information, visit https://genesis.skylabtech.ai
"""

import logging

from .exceptions import APIError, AuthenticationError, ServerError
from .version import VERSION

API_HEADER_KEY = 'X-SLT-API-KEY'
API_HEADER_CLIENT = 'X-SLT-API-CLIENT'

LOGGER = logging.getLogger('skylab_genesis')
LOGGER.propagate = False

class API:
    """The client for accessing the Skylab Genesis platform.

    Args:
        api_key (str): Your account's API KEY.

    Attributes:
        api_proto (str): The API endpoint protocol.
        api_port (str): The API endpoint port.
        api_host (str): The API endpoint host name.
        api_version (str): The API endpoint version number.
        api_key (str): The API key to use.
        debug (boolean): Whether or not to allow debugging information to be printed.
    """

    api_proto = 'https'
    api_port = '443'
    api_host = 'genesis.skylabtech.ai'
    api_version = '1'
    api_key = 'THIS_IS_A_TEST_API_KEY'

    debug = False

    def __init__(self, api_key=None, **kwargs):
        if not api_key:
            raise Exception("You must specify an api key")

        self.api_key = api_key

        if 'api_host' in kwargs:
            self.api_host = kwargs['api_host']
        if 'api_proto' in kwargs:
            self.api_proto = kwargs['api_proto']
        if 'api_port' in kwargs:
            self.api_port = kwargs['api_port']
        if 'api_version' in kwargs:
            self.api_version = kwargs['api_version']
        if 'debug' in kwargs:
            self.debug = kwargs['debug']

        if self.debug:
            logging.basicConfig(format='%(asctime)-15s %(message)s', level=logging.DEBUG)

            LOGGER.debug('Debug enabled')
            LOGGER.propagate = True
