from os import listdir
from os.path import isfile, join, abspath
import os
from pathlib import Path
path = Path.cwd()
print(path)
onlyfiles = [f for f in listdir(path) if isfile(join(path,f))]

for i in onlyfiles:
    x = Path(i)
    x.rename(x.with_suffix('.pdf'))

print(onlyfiles)
