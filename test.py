import pytest
from main import somma

def test_somma_positivi():
    assert somma(2, 3) == 7

def test_somma_negativi():
    assert somma(-1, -1) == -2