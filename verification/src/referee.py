from checkio_referee import RefereeCodeGolf, representations, covercodes, ENV_NAME


import settings_env
from tests import TESTS

cover = """def cover(f, data):
    return f(tuple(str(x) for x in data))
"""


class Referee(RefereeCodeGolf):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "golf"
    DEFAULT_MAX_CODE_LENGTH = 250

    BASE_POINTS = 15
    ENV_COVERCODE = {
        ENV_NAME.PYTHON: covercodes.py_tuple
    }
    CALLED_REPRESENTATIONS = {
        ENV_NAME.PYTHON: representations.py_tuple_representation
    }
