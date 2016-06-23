import re
import os
import os.path
import subprocess
import sys

version = re.compile(r'\.\. versionadded::')
docs_role = re.compile(r':doc:')
data_directive = re.compile(r'\.\. data\w?:: (.+)\n', re.M)
data_role = re.compile(r':data:')

for root, dirs, files in os.walk(sys.argv[1]):
    for fname in files:
        name, ext = os.path.splitext(fname)
        if ext == ".rst":
            rst_lines = ""
            src_file = os.path.join(root, fname)
            with open(src_file) as src:
                rst_lines = src.read()

            rst_lines = version.sub('.. note:: new in version', rst_lines)
            rst_lines = docs_role.sub('', rst_lines)
            rst_lines = data_directive.sub(r'\1', rst_lines)
            rst_lines = data_role.sub('', rst_lines)

            dest = root + "/" +  name + ".md"
            print(dest)
            args = ["pandoc", "-f", "rst", "-t", "commonmark", "-o", dest]
            subprocess.run(args, input=rst_lines, universal_newlines=True)
