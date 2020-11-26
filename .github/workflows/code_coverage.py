import re
from pathlib import Path
from collections import Counter


def code_coverage(crn_info, dna_info):
    crn_dna = crn_info['atoms'] - dna_info['atoms']
    dna_crn = dna_info['atoms'] - crn_info['atoms']
    if crn_dna or dna_crn:
        print('Uncovered species:')
        print('CRN - DNA =', crn_dna)
        print('DNA - CRN =', dna_crn)
        print()

    intersection = len(crn_info['atoms'] & dna_info['atoms'])
    union = len(crn_info['atoms'] | dna_info['atoms'])
    coverage = intersection / union

    not_used = set()
    for atom in crn_info['atoms']:
        used = False
        for lhs, rhs in crn_info['reactions']:
            left_count = lhs.count(atom)
            right_count = rhs.count(atom)
            if left_count != right_count and left_count > 0:
                used = True
        if not used:
            not_used.add(atom)
    
    print(f'Not-essential species (usually input or output): {not_used}')

    return coverage
