import pytest
from solution import sum_two


def test_valid_arguments():
    assert sum_two(1, 2) == 3


def test_invalid_type_second_argument():
    with pytest.raises(TypeError) as exc_info:
        sum_two(1, 2.5)
    assert "Аргумент 'b'" in str(exc_info.value)


def test_invalid_type_first_argument():
    with pytest.raises(TypeError) as exc_info:
        sum_two("1", 2)
    assert "Аргумент 'a'" in str(exc_info.value)
    
def test_invalid_type_both_argument():
    with pytest.raises(TypeError) as exc_info:
        sum_two("1", 2.3)
    assert "Аргумент 'a'" in str(exc_info.value)


def test_too_few_arguments():
    with pytest.raises(TypeError) as exc_info:
        sum_two(1)
    assert "ожидает 2 аргумента" in str(exc_info.value)


def test_too_many_arguments():
    with pytest.raises(TypeError) as exc_info:
        sum_two(1, 2, 3)
    assert "ожидает 2 аргумента" in str(exc_info.value)


def test_none_arguments():
    with pytest.raises(TypeError) as exc_info:
        sum_two()
    assert "ожидает 2 аргумента" in str(exc_info.value)