import pandas as pd
import numpy as np
import re

import os

abs_dir = os.path.dirname(__file__) 
rel_path = "asu_raw.txt"
abs_path = os.path.join(abs_dir, rel_path)


names = np.array([])
types = np.array([])

type_options = ['Iron', 'Chondrite', 'Martian', 'Unknown', 'Pallasite', 'Achondrite', 'Mesosiderite']

with open(abs_path, 'r', encoding="utf-8") as f:
    for line in f:
        if 'Meteorite	Name ASU' not in line: 
            
            line = line.replace('\t', ' ')
            line = re.sub(' +',' ', line)
            #line = line.replace('(','')
            #line = line.replace(')', '')

            counter = 0
            for character in line:
                counter+=1
                if character.isnumeric(): 
                    counter-=2
                    break
            
            name = line[0:counter]

            if '(' in line: 
                paren_index = line.index('(')
                if counter>=paren_index: 
                    name = name[0:paren_index]

            names = np.append(names, name)

            type_found = False
            for type in type_options: 
                if type in line: 
                    types = np.append(types, type)
                    type_found = True
            
            if type_found == False: 
                types = np.append(types, 'Unknown')


names_set = np.array([])
types_set = np.array([])

for name, type in zip(names, types):
    if name not in list(names_set):
        names_set = np.append(names_set, name)
        types_set = np.append(types_set, type)

zipped = list(zip(names_set, types_set))
df = pd.DataFrame(zipped, columns=['Name', 'Type'])
df.to_csv('asu.csv', index=False)