import pytest

expected_path = "answers/single_star.py"


@pytest.mark.judge
def test_judge(compare_script):
    answer_path = "solves/single_star.py"
    assert compare_script(answer_path, expected_path)


def test_01(compare_output):
    test_input = "5"
    expected = "*"
    assert compare_output(expected_path, expected, test_input)
