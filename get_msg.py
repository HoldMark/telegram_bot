from db.get_data import get_expressions
from utils.convert_data import convert_data_to_msg


def get_msg():
    some_data = get_expressions()
    msg = convert_data_to_msg(some_data)

    return msg
