import numpy as np
import pandas as pd
import re

'''
with open(r'', 'r') as f: 
    for line in f: 
        line = re.sub(' +', '@@', line)
        line = line.replace('//','')
        line_list = line.split('@@')
'''

initial_df = pd.read_csv(r'C:\Users\Research\Documents\GitHub\meteorite-minerals\code\exploring\meteorite_matching\min_to_met\mineral_locations.csv')
initial_ids = np.array(initial_df['Mineral'])
initial_locs = np.array(initial_df['Meteorite(s)'])

final_ids = np.array(pd.read_csv(r'C:\Users\Research\Documents\GitHub\meteorite-minerals\code\final_sample\final_sample.csv')['mineral_name'])
final_ids = np.array([i.upper() for i in final_ids])
synth_ids = np.array(pd.read_csv(r'C:\Users\Research\Documents\GitHub\meteorite-minerals\code\final_sample\synth_sample.csv')['mineral_name'])
synth_ids = np.array([i.upper() for i in synth_ids])

final_ids = np.append(final_ids, synth_ids)

shared_names, shared_idx , _ = np.intersect1d(initial_ids, final_ids, return_indices=True)

print(shared_idx)

print(shared_idx.shape)

final_df = pd.DataFrame(list(zip(shared_names,initial_locs[shared_idx])), 
                        columns=['Mineral','Meteorite(s)'])

final_df.to_csv('final_locs.csv', index=False)