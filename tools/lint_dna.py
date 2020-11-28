import re
from pathlib import Path
from collections import Counter


def find_dna():
    dna_fpath = None
    dna_files_count = 0
    for fpath in Path('.').iterdir():
        if fpath.suffix == '.dna':
            dna_fpath = fpath
            dna_files_count += 1

    if dna_files_count != 1:
        raise Exception('There should be exactly one .dna file in repository')

    return dna_fpath


def lint_dna(fpath):
    if type(fpath) is str:
        text = fpath
        fpath = Path('.') / 'input.txt'
    else:
        text = fpath.read_text(encoding='utf-8')
    part = None
    atoms = set()
    signal_strands_cnt = 0
    signal_strands_dna_size = 0
    complexes_cnt = 0
    complexes_dna_size = 0
    fuel_complexes_cnt = 0
    fuel_complexes_dna_size = 0
    for line_no, line in enumerate(text.split('\n')):
        line = line.split('#')[0].strip()
        if line == '':
            continue
        msg_prefix = f'Line #{line_no} of {fpath.name}: '
        if line == 'Signal strands':
            if part is not None:
                raise Exception(msg_prefix + 'Does not expect "Signal strands" here')
            part = 'SIGNAL_STRANDS'
        elif line == 'Complexes':
            if part != 'SIGNAL_STRANDS':
                raise Exception(msg_prefix + 'Does not expect "Complexes" here')
            part = 'COMPLEXES'
        elif line == 'Fuel strands':
            if part != 'COMPLEXES':
                raise Exception(msg_prefix + 'Does not expect "Fuel strands" here')
            part = 'FUEL_STRANDS'
        elif part == 'SIGNAL_STRANDS':
            assert line.startswith('Strand '), msg_prefix + 'Does not start with "Strand "'
            line = line.replace('Strand ', '')
            parts = line.split(':')
            assert len(parts) == 2, msg_prefix + 'Should have exactly one ":" character'
            name, dna = parts[0].strip(), parts[1].strip()
            if not name.startswith('Fuel'):
                assert name[-1] in '0123456789', f'Unexpected species "{name}" last char'
                atoms.add(name[:-1])
            for char in dna:
                assert char in 'ACGT', msg_prefix + f'Unexpected DNA character {char}'
                signal_strands_dna_size += 1
            signal_strands_cnt += 1
        elif part == 'COMPLEXES':
            if line.startswith('Complex: '):
                complexes_cnt += 1
            elif line.startswith('Strand '):
                line = line.replace('Strand ', '')
                parts = line.split(':')
                assert len(parts) == 2, msg_prefix + 'Should have exactly one ":" character'
                name, dna = parts[0].strip(), parts[1].strip()
                for char in dna:
                    assert char in 'ACGT', msg_prefix + f'Unexpected DNA character {char}'
                    complexes_dna_size += 1
            else:
                raise Exception(msg_prefix + 'Unexpected complex line start')
        elif part == 'FUEL_STRANDS':
            if line.startswith('Complex: '):
                fuel_complexes_cnt += 1
            elif line.startswith('Strand '):
                line = line.replace('Strand ', '')
                parts = line.split(':')
                assert len(parts) == 2, msg_prefix + 'Should have exactly one ":" character'
                name, dna = parts[0].strip(), parts[1].strip()
                for char in dna:
                    assert char in 'ACGT', msg_prefix + f'Unexpected DNA character {char}'
                    fuel_complexes_dna_size += 1
            else:
                raise Exception(msg_prefix + 'Unexpected complex line start')
        else:
            raise Exception(msg_prefix + 'Unexpected state')
    return {
        'atoms': atoms,
        'signal_strands_cnt': signal_strands_cnt,
        'signal_strands_dna_size': signal_strands_dna_size,
        'complexes_cnt': complexes_cnt,
        'complexes_dna_size': complexes_dna_size,
        'fuel_complexes_cnt': fuel_complexes_cnt,
        'fuel_complexes_dna_size': fuel_complexes_dna_size,
    }
