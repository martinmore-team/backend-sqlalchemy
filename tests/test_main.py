from backend_sqlalchemy.main import sum_two, concat_name, join_array


def test_sum_two():
    assert sum_two(4, 5) == 9


def test_concat_names():
    assert concat_name("Martin", "More") == "Martin More"


def test_join_array():
    assert join_array(["Martin", "More"]) == "Martin,More"
