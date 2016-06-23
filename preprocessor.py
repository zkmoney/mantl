import re
import os
import os.path
import subprocess
import sys

REGEXP = [
        (re.compile(r':(?:data|doc):'), ''),
        (re.compile(r':envvar:`(.+)`'), r'``\1``'),
        (re.compile(r'\.\. (?:data|envvar|option)\w?:: (.+)\n', flags=re.M), r'\1'),
        (re.compile(r'\.\. (?:literal)?include:: (.+)'), r'[\1](\1)'),
        (re.compile(r'\.\. program:: (.+)\n'), r'\1\n~~~~~~~~~~~~~~~~~~~'),
        (re.compile(r'\.\. toctree::(.*\n)*^\w', re.M), r'[TOC]\n'),
        (re.compile(r'\.\. toctree::.*$', re.S), r'[TOC]\n'),
        (re.compile(r'\.\. versionadded::'), '.. note:: new in version'),
        ]

for root, dirs, files in os.walk(sys.argv[1]):
    for fname in files:
        name, ext = os.path.splitext(fname)
        if ext == ".rst":
            rst_lines = ""
            src_file = os.path.join(root, fname)
            with open(src_file) as src:
                rst_lines = src.read()

            for compiled_re, replace_str in REGEXP:
                rst_lines = compiled_re.sub(replace_str, rst_lines)

            dest = root + "/" +  name + ".md"
            print(dest)
            args = ["pandoc", "-f", "rst", "-t", "commonmark", "-o", dest]
            subprocess.run(args, input=rst_lines, universal_newlines=True)
