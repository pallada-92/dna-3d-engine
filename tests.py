from lint_crn import lint_crn, find_crn
from tests_utils import emulate_crn, assert_approx, unit_test


def make_initial(x, y):
    return {
        'cxm': 0.606,
        'cym': 0.898,
        'czm': 1.243,
        'mxyzm': 0.3,
        'nx': 0.036 + 0.555 * x + 0.147 * y,
        'ny': 0.853 - 0.517 * y,
        'nz': 0.737 - 0.270 * x + 0.302 * y,
    }


reactions = lint_crn(find_crn())['reactions']


@unit_test
def test_1():
    # -*- text -*-
    initial = make_initial(0.5, 0.5)
    emulate_res = emulate_crn(initial, reactions, 0.01, 10000)
    assert_approx(emulate_res['R'], 0.0244, 0.01)


@unit_test
def test_2():
    # -*- text -*-
    initial = make_initial(0.0, 0.0)
    emulate_res = emulate_crn(initial, reactions, 0.01, 10000)
    assert_approx(emulate_res['R'], 0.244, 0.01)
