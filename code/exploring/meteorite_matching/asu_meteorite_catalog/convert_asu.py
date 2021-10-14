import pandas as pd
import numpy as np
import re

import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "asu_raw.txt"
abs_file_path = os.path.join(script_dir, rel_path)


names = np.array([])
types = np.array([])

m_types = []

with open(abs_file_path, 'r') as f:
    for line in f:
        print(line)
        if 'Meteorite	Name ASU' not in line: 
            
            line = re.sub(' +',' ', line)
            line = line.replace('(','')
            line = line.replace(')', '')



            counter = 0
            for character in line:
                counter+=1
                if character.isnumeric(): 
                    counter-=2
                    break
            

            stop_index = counter
            name = line[0:stop_index]
 
            csv_line = re.sub(' +', ',', line)


            type_index_start = 0
            type_index_end = 0
            
            counter = 0
            for character in line: 
                counter+=1
                if not(character.isnumeric()): 
                    if line[counter-2].isnumeric():
                        type_index_start = counter
                        break 
            

            sub_line_list = line[type_index_start:].split(' ')
            
            meteorite_type = sub_line_list[0]

            m_types.append(meteorite_type)

        #line_list = re.sub(' +',',',line).split(',')
        

print(list(set(m_types)))

