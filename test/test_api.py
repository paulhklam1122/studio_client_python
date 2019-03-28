import pytests

import skylab_genesis

class TestAPI(object):
    def test_list_jobs(api):
        """ Test list jobs endpoint. """
        result = api.list_jobs()
        assert result.status_code == 200