from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """


def test_bound_basic1():
    assert bound_to_180(0) == 0


def test_bound_to_180_already_in_range():
    assert bound_to_180(135) == 135.0


def test_bound_to_180_needs_wrapping():
    assert bound_to_180(200) == -160.0


def test_bound_to_180_extreme_positive():
    assert bound_to_180(900) == -180.0


def test_bound_to_180_negative():
    assert bound_to_180(-200) == 160.0


""" Tests for is_angle_between() """


def test_between_basic1():
    assert is_angle_between(0, 1, 2)


def test_is_angle_between_true_case():
    assert is_angle_between(0, 45, 90)


def test_is_angle_between_false_case():
    assert not is_angle_between(45, 90, 270)


def test_is_angle_between_wraparound_true():
    assert is_angle_between(270, 315, 45)


def test_is_angle_between_wraparound_false():
    assert not is_angle_between(270, 100, 45)
