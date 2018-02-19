import sys
import pytest

sys.path.insert(0, "..")

@pytest.fixture
def x_vars():
    sp.Symbol("x")
