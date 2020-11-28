def emulate_crn(initial, reactions, dt, steps):
    conc = {
        species: value
        for species, value in initial.items()
    }

    for i in range(steps):
        next_conc = dict(conc)
        for lhs, rhs in reactions:
            rate = dt
            for species in lhs:
                rate *= conc.get(species, 0)
            for species in lhs:
                next_conc[species] = max(0, next_conc.get(species, 0) - rate)
            for species in rhs:
                next_conc[species] = max(0, next_conc.get(species, 0) + rate)
        conc = next_conc

    return conc


def assert_approx(test_val, ref_val, max_rel_error=0.01):
    if abs(test_val - ref_val) > ref_val * max_rel_error:
        raise Exception(f"Value {test_val} is too far from {ref_val}")


def assert_large(test_val, threshold=1000):
    if test_val < threshold:
        raise Exception(f"Value {test_val} is less, than {threshold}")


all_tests = []


def unit_test(fun):
    all_tests.append(fun)
    return fun


def run_tests():
    total_tests = 0
    passed_tests = 0
    for no, test in enumerate(all_tests):
        total_tests += 1
        try:
            test()
        except Exception as e:
            print(f'TEST {no}: FAIL: {e}')
        else:
            print(f'TEST {no}: OK')
            passed_tests += 1
    return (passed_tests, total_tests)
