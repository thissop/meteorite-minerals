import os
import re
import numpy as np
import pandas as pd

abs_dir = os.path.dirname(__file__) 
rel_path = "athena_raw.txt"
abs_path = os.path.join(abs_dir, rel_path)

names = np.array([])

with open(abs_path, 'r', encoding="utf-8") as f:
    for line in f:
        line = line.replace('\t', ' ')
        linelist = re.sub(' +',r'$$$', line).split(r'$$$')
        mineral = linelist[-2]
        names = np.append(names, mineral)

zipped = list(zip(names))
df = pd.DataFrame(zipped, columns=['Mineral Name'])

df.to_csv('athena.csv', index=False)