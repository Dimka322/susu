import pytest
from array import array

from array1 import found_element


def correct_program_result(mocker):
    mocker.patch('array1.found_element', return_value=(array('i', [1, 2, 3, 4])))

    assert found_element() == 1
