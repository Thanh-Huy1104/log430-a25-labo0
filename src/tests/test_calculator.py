# src/tests/test_calculator.py
# SPDX-License-Identifier: LGPL-3.0-or-later
# Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025

import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import math
import pytest
from src.calculator import Calculator


def test_get_hello_message():
    calc = Calculator()
    assert calc.get_hello_message() == "== Calculatrice v1.0 =="


@pytest.mark.parametrize(
    "v1,v2,expected",
    [(0, 0, 0), (1, 2, 3), (-5, 10, 5), (1.5, 2.5, 4.0)],
)
def test_addition(v1, v2, expected):
    calc = Calculator()
    assert calc.addition(v1, v2) == expected
    assert calc.last_result == expected


@pytest.mark.parametrize(
    "v1,v2,expected",
    [(0, 0, 0), (5, 2, 3), (-5, -3, -2), (1.5, 2.5, -1.0)],
)
def test_subtraction(v1, v2, expected):
    calc = Calculator()
    assert calc.subtraction(v1, v2) == expected
    assert calc.last_result == expected


@pytest.mark.parametrize(
    "v1,v2,expected",
    [(0, 0, 0), (3, 2, 6), (-4, 2, -8), (1.5, 2.0, 3.0)],
)
def test_multiplication(v1, v2, expected):
    calc = Calculator()
    assert calc.multiplication(v1, v2) == expected
    assert calc.last_result == expected


@pytest.mark.parametrize(
    "v1,v2,expected",
    [(6, 2, 3.0), (-9, 3, -3.0), (1.5, 0.5, 3.0)],
)
def test_division(v1, v2, expected):
    calc = Calculator()
    res = calc.division(v1, v2)
    assert math.isclose(res, expected)
    assert math.isclose(calc.last_result, expected)


def test_division_by_zero_behavior():
    calc = Calculator()
    msg = calc.division(10, 0)
    assert msg == "Erreur : division par zéro"
    assert calc.last_result == "Error"