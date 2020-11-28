from lint_crn import lint_crn, find_crn
from tests_utils import emulate_crn, assert_approx, unit_test, assert_large


def make_initial(x, y):
    return {
        'q': 0.01,
        'cxtm': 0.606,
        'cytm': 0.898,
        'cztm': 1.243,
        'axp': 0.606,
        'ayp': 0.898,
        'azp': 1.243,
        'mxyzm': 0.3,
        'nx': 0.036 + 0.555 * x + 0.147 * y,
        'ny': 0.853 - 0.517 * y,
        'nz': 0.737 - 0.270 * x + 0.302 * y,
    }


reactions = lint_crn(find_crn())['reactions']


@unit_test
def test_center():
    # -*- text -*-
    initial = make_initial(0.5, 0.5)
    emulate_res = emulate_crn(initial, reactions, 0.1, 100000)
    assert_approx(emulate_res['R'], 2.16, 0.05)


@unit_test
def test_corner():
    initial = make_initial(0.0, 0.0)
    emulate_res = emulate_crn(initial, reactions, 0.1, 100000)
    assert_large(emulate_res['R'])


@unit_test
def test_edge_out():
    initial = make_initial(0.086, 0.5)
    emulate_res = emulate_crn(initial, reactions, 0.1, 100000)
    assert_large(emulate_res['R'])


@unit_test
def test_edge_in():
    initial = make_initial(0.095, 0.5)
    emulate_res = emulate_crn(initial, reactions, 0.1, 100000)
    assert_approx(emulate_res['R'], 2.62, 0.05)
