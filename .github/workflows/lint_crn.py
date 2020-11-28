import re
from pathlib import Path
from collections import Counter


def find_crn():
    crn_fpath = None
    crn_files_count = 0
    for fpath in Path('.').iterdir():
        if fpath.suffix == '.crn':
            crn_fpath = fpath
            crn_files_count += 1

    if crn_files_count != 1:
        raise Exception('There should be exactly one .crn file in repository')

    return crn_fpath


def lint_crn(fpath):
    if type(fpath) is str:
        text = fpath
        fpath = Path('.') / 'input.txt'
    else:
        text = fpath.read_text(encoding='utf-8')
    atoms = set()
    loc = 0
    reactions = []
    for line_no, line in enumerate(text.split('\n')):
        msg_prefix = f'Line #{line_no} of {fpath.name}: '
        line = line.strip()
        if line == '':
            continue
        eq_parts = line.split('->')
        if len(eq_parts) != 2:
            raise Exception(msg_prefix + 'non-empty line should contain exactly one "->"')
        loc += 1
        lhs, rhs = eq_parts
        lhs = [s.strip() for s in lhs.split('+') if s.strip()]
        rhs = [s.strip() for s in rhs.split('+') if s.strip()]
        if len(lhs) > 2:
            raise Exception(msg_prefix + 'left part of equation should contain at most 2 species')
        if len(rhs) > 2:
            raise Exception(msg_prefix + 'right part of equation should contain at most 2 species')
        for atom in lhs + rhs:
            if not re.match('^[a-zA-Z_0-9]+$', atom):
                raise Exception(msg_prefix + f'invalid atom "{atom}". Valid characters are a-z, A-Z and _')
            atoms.add(atom)
        reactions.append([lhs, rhs])
    return {
        'atoms': atoms,
        'loc': loc,
        'reactions': reactions,
    }
