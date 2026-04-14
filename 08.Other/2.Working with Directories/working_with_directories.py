# This code lists all the files in the current directory using the pathlib module.

from pathlib import Path

path = Path()
for file in (path.glob("*")):
    print(file)