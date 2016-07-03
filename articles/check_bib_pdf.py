"""Check if a pdf file is available for each entry in a bib file

Also checks the reverse, if a bib entry is available for each pdf.

"""

from glob import glob
from re import compile
import os


def get_paths(extension='bib'):
    paths = glob('*/*.%s' % extension)
    paths = [p for p in paths
             if p[0] in '123456789' or p[0] == 'a' and p[1] in '123456789']
    return paths


def read_citekeys():
    """Read citekeys from the bib files"""

    citekeys = []
    bib_paths = get_paths('bib')
    for bib_path in bib_paths:
        base_path = os.path.dirname(bib_path)
        with open(bib_path, 'r') as bib_file:
            bibtex = bib_file.readlines()
        for line in bibtex:
            if line.startswith('@'):
                citekey = line.split('{', 1)[1].split(',')[0]
                citekeys.append(os.path.join(base_path, citekey))
    if len(citekeys) is not len(set(citekeys)):
        print 'Duplicate keys!'
    return set(citekeys)


def read_pdfnames():
    """Read all available pdfs and remove the pdf extension

    :return: set of paths (citekeys with relative path).

    """
    citekeys = []
    pdf_paths = get_paths('pdf')
    for pdfpath in pdf_paths:
        citekeys.append(os.path.splitext(pdfpath)[0])
    if len(citekeys) is not len(set(citekeys)):
        print 'Duplicate pdfs!?!'
    return set(citekeys)


def check_pdfs_available(citekeys):
    """Check if pdf is available for each citekey"""

    for citekey in citekeys:
        check_pdf_available(citekey)


def check_pdf_available(citekey):
    """Check if a pdf file exists for the given citekey

    :param citekey: citekey including the relative path,
                    e.g. '2_station/bartels2012mpv'.

    """
    pdf_name = citekey + os.extsep + 'pdf'
    if not os.path.exists(pdf_name):
        print 'Failed to find pdf for %s' % citekey


if __name__ == "__main__":
    citekeys = set(read_citekeys())
    pdfs = read_pdfnames()

    print 'Checking for missing pdfs:'
    missing_pdf = citekeys.difference(pdfs)
    if len(missing_pdf):
        print '\n'.join(missing_pdf)

    print 'Checking for missing citekeys:'
    missing_bib = pdfs.difference(citekeys)
    if len(missing_bib):
        print '\n '.join(missing_bib)
