import pandas as pd
import numpy as np
import re

import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "asu_raw.txt"
abs_file_path = os.path.join(script_dir, rel_path)


names = np.array([])
types = np.array([])

with open(abs_file_path, 'r') as f:
    for line in f:
        if 'Meteorite	Name ASU' not in line: 
            counter = 0
            for character in line:
                counter+=1
                if character.isnumeric(): 
                    counter-=1
                    break
            
            stop_index = counter
            name = line[0:stop_index]

            if '(' in name:
                name = name[0:name.index('(')]
            
            name = re.sub(' +',' ', name)

            counter = 0
            for character in line: 
                counter+=1
                if counter > stop_index and (character.isnumeric()==False):
                    print(line)
                    print(line[counter])
                    break
                    #quit()
 
        #line_list = re.sub(' +',',',line).split(',')
        



