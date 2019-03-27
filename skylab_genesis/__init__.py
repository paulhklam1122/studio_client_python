import logging

from .encoder import SkylabGenesisJSONEncoder
from .exceptions import APIError, AuthenticationError, ServerError
from .version import version

class api:
  API_PROTO = 'https'
  API_PORT = '443'
  API_HOST = 'genesis.skylabtech.ai'
  API_VERSION = '1'
  API_HEADER_KEY = 'X-SLT-API-KEY'
  API_HEADER_CLIENT = 'X-SLT-API-CLIENT'
  API_KEY = 'THIS_IS_A_TEST_API_KEY'

  DEBUG = False

  def __init__(self, api_key=None, json_encoder=SkylabGenesisJSONEncoder, raise_errors=False, default_timeout=None, **kwargs):
    if not api_key:
      raise Exception("You must specify an api key")

    self.API_KEY = api_key
    self._json_encoder = json_encoder
    self._raise_errors = raise_errors

    if 'API_HOST' in kwargs:
      self.API_HOST = kwargs['API_HOST']
    if 'API_PROTO' in kwargs:
      self.API_PROTO = kwargs['API_PROTO']
    if 'API_PORT' in kwargs:
      self.API_PORT = kwargs['API_PORT']
    if 'API_VERSION' in kwargs:
      self.API_VERSION = kwargs['API_VERSION']
    if 'DEBUG' in kwargs:
      self.DEBUG = kwargs['DEBUG']

    if self.DEBUG:
      logging.basicConfig(format=LOGGER_FORMAT, level=logging.DEBUG)
      logger.debug('Debug enabled')
      logger.propagate = True
