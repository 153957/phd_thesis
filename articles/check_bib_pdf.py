"""Check if a pdf file is available for each entry in a bib file

Also checks the reverse, if a bib entry is available for each pdf.

"""

from glob import glob
import os


def read_citekeys():
    """Read citekeys from the bib files"""

    citekeys = []
    bib_paths = glob('ch_*/*.bib')
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
    return citekeys


def check_pdfs_available(citekeys):
    """Check if pdf is available for each citekey"""

    for citekey in citekeys:
        check_pdf_available(citekey)


def check_pdf_available(citekey):
    """Check if a pdf file exists for the given citekey

    :param citekey: citekey including the relative path,
                    e.g. 'ch_detector/bartels2012mpv'.

    """
    pdf_name = citekey + os.extsep + 'pdf'
    if not os.path.exists(pdf_name):
        print 'Failed to find pdf for %s' % citekey


def read_pdfnames():
    """Read all available pdfs and remove the pdf extension

    :return: set of paths (citekeys with relative path).

    """
    citekeys = []
    pdfpaths = glob('ch_*/*.pdf')
    for pdfpath in pdfpaths:
        citekeys.append(os.path.splitext(pdfpath)[0])
    return set(citekeys)


if __name__ == "__main__":
    print 'Checking for missing pdfs'
    citekeys = read_citekeys()
    check_pdfs_available(citekeys)

    print 'Checking for missing citekeys'
    pdfs = read_pdfnames()
    missing_bib = pdfs.difference(citekeys)
    if len(missing_bib):
        print missing_bib
