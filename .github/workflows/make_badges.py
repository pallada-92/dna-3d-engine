from pathlib import Path
import sys

from lint_crn import find_crn, lint_crn
from lint_dna import find_dna, lint_dna
from code_coverage import code_coverage
from tests_utils import run_tests

sys.path.append(str(Path(__file__).parent / '../..'))
import tests


def make_badges():
    crn_fpath = find_crn()
    crn_info = lint_crn(crn_fpath)

    dna_fpath = find_dna()
    dna_info = lint_dna(dna_fpath)

    loc_badge = f'{crn_info["loc"]} reactions'

    dna_total_size = dna_info['signal_strands_dna_size'] + dna_info['fuel_complexes_dna_size']
    bundle_size_badge = f'{dna_total_size / 1000:4.2f}K nucleotides'

    coverage = code_coverage(crn_info, dna_info)
    coverage_badge = f'{round(coverage * 100)}%'

    passed_tests, total_tests = run_tests()
    failed_tests = total_tests - passed_tests
    if failed_tests:
        tests_badge = f'{passed_tests} passed, {failed_tests} failed'
    else:
        tests_badge = f'{passed_tests} passed'

    return dict(
        loc_badge=loc_badge,
        bundle_size_badge=bundle_size_badge,
        coverage_badge=coverage_badge,
        tests_badge=tests_badge,
    )


# print(make_badges())
