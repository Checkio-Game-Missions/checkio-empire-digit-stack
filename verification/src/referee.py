from checkio_referee import RefereeCodeGolf, representations

import settings
import settings_env
from tests import TESTS

cover = """def cover(func, data):
    return f(tuple(str(x) for x in data))
"""


class Referee(RefereeCodeGolf):
    TESTS = TESTS
    EXECUTABLE_PATH = settings.EXECUTABLE_PATH
    CURRENT_ENV = settings_env.CURRENT_ENV
    FUNCTION_NAME = "golf"
    DEFAULT_MAX_CODE_LENGTH = 200
    BASE_POINTS = 15
    ENV_COVERCODE = {
        "python_2": cover,
        "python_3": cover,
        "javascript": None
    }
    CALLED_REPRESENTATIONS = {
        "python_2": representations.py_tuple_representation,
        "python_3": representations.py_tuple_representation,
        "javascript": None
    }
