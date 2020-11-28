from lint_crn import lint_crn
from tests_utils import emulate_crn, assert_approx, unit_test


initial = {
    'X': 0.61,
    'Y': 0.60,
}


reactions = lint_crn('''
X + Y -> X + T
Y + X -> Y + T
T + X -> X + X
T + Y -> Y + Y
''')['reactions']


@unit_test
def test_1():
    global initial, reactions
    initial = dict(initial)
    reactions = list(reactions)
    emulate_res = emulate_crn(initial, reactions, 0.01, 10000)
    assert_approx(emulate_res['X'], 1.21, 0.01)
