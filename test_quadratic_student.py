import pytest
from quadratic_student import solve


def test_float_solution():
    assert solve(1, -4, 2) == (0.5857864376269049, 3.414213562373095)
    assert solve(1, -5, 3) == (0.6972243622680054, 4.302775637731995)


def test_int_solution():
    assert solve(1, -5, 6) == (2, 3)
    assert solve(1, -3, 2) == (1, 2)


def test_imaginary_solution():
    assert solve(1, -4, 8) == ((2 + 2j), 2 - 2j)
    assert solve(1, 4, 8) == (-2 + 2j, -2 - 2j)


def test_letter_input():
    with pytest.raises(TypeError):
        solve("A", "B", 2)


def test_symbol_input():
    with pytest.raises(TypeError):
        solve("!", ".", 2)


def test_float_cubic():
    assert solve(0, 4, -1) == (-0.5, 0.5)


def test_int_cubic():
    assert solve(0, 2, -8) == (-2, 2)


def test_one_float_input():
    assert solve(0.5, -12, 3) == (0.25265987552926994, 23.747340124470732)


def test_two_float_input():
    assert solve(0.5, -12.5, 3) == (0.24234932786873742, 24.757650672131263)


def test_all_float_input():
    assert solve(0.5, -12.5, 3.5) == (0.28320827712938446, 24.716791722870617)
