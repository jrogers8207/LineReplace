#!python3
# Copyright 2021 Jack Rogers

import sys
from pathlib import Path
import os

if len(sys.argv) < 3:
    raise Exception("Not enough arguments were supplied.")
if sys.argv[1] == ' ':
    text = ""
else:
    text = str(sys.argv[1])

lineNumber = int(sys.argv[2]) - 1

files = []
for i in range(3, len(sys.argv)):
    if not (Path.cwd() / Path(sys.argv[i])).is_file():
        raise Exception(f"\"{sys.argv[i]}\" is not a valid path.")
    else:
        files.append(Path.cwd() / Path(sys.argv[i]))

for file in files:

    openFile = open(file)

    lines = []
    for line in openFile.readlines():
        lines.append(line)
    openFile.close()
    if len(lines) < lineNumber + 1:
        raise Exception(f"{file} does not have at least {lineNumber + 1} lines.")
    os.unlink(file)

    lines[lineNumber] = text + "\n"
    newFile = open(file, 'w')
    for line in lines:
        newFile.write(line)
    print(f"Successfully modified {file}.")




