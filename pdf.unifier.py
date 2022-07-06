#!/usr/bin/env python3
import sys
import argparse
from argparse import RawTextHelpFormatter
from pdfrw import PdfReader, PdfWriter


class MyParser(argparse.ArgumentParser):
    """
    Print full help without -h
    https://stackoverflow.com/questions/4042452/display-help-message-with-python-argparse-when-script-is-called-without-any-argu
    """

    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)


def main():
    # RawTextHelpFormatter is so we can have multiline help:
    # https://stackoverflow.com/questions/29613487/multiple-lines-in-python-argparse-help-display
    parser = MyParser(description='\n'.join([
        'PDF single-side scans unifier. If you have a 10page double-sided document, when you scan it single-sidedly, '
        'you produce two 5-page documents, the first contains pages [1,3,5,7,9], the second - [10,8,6,4,2]. This script'
        ' unifies the two pdfs into one.',
        'Example usage:',
        './pdf.unifier.py -o odd.pages.pdf -e even.pages.pdf -r result.pdf']),
        formatter_class=RawTextHelpFormatter)
    parser.add_argument('-o', '--odd-pages-pdf', required=True, help='The pdf containing the odd pages.')
    parser.add_argument('-e', '--even-pages-pdf', required=True, help='The pdf containing the even pages.')
    parser.add_argument('-r', '--result-pdf', required=True, help='The result pdf after unification.')
    args = parser.parse_args()

    odd_pages = PdfReader(args.odd_pages_pdf)
    even_pages = PdfReader(args.even_pages_pdf)
    writer_output = PdfWriter()

    if len(odd_pages.pages) != len(even_pages.pages):
        print(f'Two input pdf files with unequal page count:\n'
              f'{args.odd_pages_pdf}: {len(odd_pages.pages)} pages\n'
              f'{args.even_pages_pdf}: {len(even_pages.pages)} pages')

    page_count = len(odd_pages.pages)
    for i in range(page_count):
        writer_output.addPage(odd_pages.pages[i])
        writer_output.addPage(even_pages.pages[page_count - 1 - i])

    writer_output.write(args.result_pdf)


if __name__ == '__main__':
    main()
