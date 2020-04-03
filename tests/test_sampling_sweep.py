from easyvvuq.sampling.sweep import BasicSweep, wrap_iterable
import pytest


@pytest.fixture
def basic_sweep_sampler():
    return BasicSweep({'a': [1, 2, 3], 'b': [4, 5, 6]})


def test_wrap_iterable():
    res = []
    for var_name, val in wrap_iterable('a', [1, 2, 3]):
        res.append((var_name, val))
    assert(res == [('a', 1), ('a', 2), ('a', 3)])


def test_init():
    pass


def test_init_exceptions():
    pass


def test_element_version():
    pass


def test_is_finite():
    pass


def test_iter():
    pass


def test_is_restartable():
    pass


def test_get_restart_dict():
    pass
