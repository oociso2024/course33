from  src.utils import get_data, get_filtered_data, get_sorted_data, print_result

import pytest


file_name = "cw3/src/operations.json"
def test_get_data():
    assert isinstance(get_data(file_name), list)

def test_get_filtered_data():
    assert len(get_filtered_data([{"state": "EXECUTED"}, {"state": "CANCELED"}])) == 1

def test_get_sorted_data():
    assert get_sorted_data([{'date': "2020-07-16T10:50:58.294041"}, {'date': "2019-02-20T10:50:58.294041"},
                            {'date': "2021-08-26T10:50:58.294041"}])

def test_print_result():
    assert print_result(data=[{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
    }]) == None