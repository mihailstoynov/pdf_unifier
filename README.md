pdf_unifier
===

PDF single-side scans unifier
---

# Explanation
- there is a 10-page double-sided document
- there is a single-sided scanner
- when the 10-page document is scanned front and back, two document are produced:
  - the first contains pages [1,3,5,7,9]
  - the second - [10,8,6,4,2]
- This script unifies the two pdfs into one.

# Usage

```
git clone https://github.com/mihailstoynov/pdf_unifier/
cd pdf_unifier/
chmod u+x pdf.unifier.py
./pdf.unifier.py -o example/odd.pages.pdf -e example/even.pages.pdf -r example/result.pdf
```
