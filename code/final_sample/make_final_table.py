from types import LambdaType
import pandas as pd
import numpy as np
import re

locs_df = pd.read_csv(r'C:\Users\Research\Documents\GitHub\meteorite-minerals\code\final_sample\final_locs.csv')
stacked_df = pd.read_csv(r'C:\Users\Research\Documents\GitHub\meteorite-minerals\code\visualization\stacked_df.csv')

out_df = locs_df

# give locations 

out_df['chondrite_count'] = np.array(stacked_df.loc[0])
out_df['achondrite_count'] = np.array(stacked_df.loc[1])
out_df['iron_count'] = np.array(stacked_df.loc[2])
out_df['pallasite_count'] = np.array(stacked_df.loc[3])

# give formulae

latex_ids = []
latex_formulae = []

with open(r'C:\Users\Research\Documents\GitHub\meteorite-minerals\code\final_sample\raw_latex.tex', 'r') as f:
    for line in f:
        new_line = line.replace(' ','')
        new_line = new_line.replace(r'\\','')

        print(new_line)
        line_list = line.split('&')
        latex_ids.append(line_list[0])
        latex_formulae.append(line_list[1])
        latex_ids.append(line_list[2])
        latex_formulae.append(line_list[3])

latex_ids = [i.upper() for i in latex_ids]

formulas = []

for id in out_df['Mineral']: 
    for idx, latex_id in enumerate(latex_ids):
        latex_id = latex_id.replace(' ','')
        if id==latex_id: 
            formulas.append(latex_formulae[idx].replace('\"',''))

out_df['chemical_formula'] = formulas

# give * to synth or analog synth minerals

synth_ids = np.array(pd.read_csv(r'C:\Users\Research\Documents\GitHub\meteorite-minerals\code\final_sample\synth_sample.csv')['mineral_name'])
synth_ids = np.array([i.upper() for i in synth_ids])

all_ids = np.array(out_df['Mineral'])

final_ids = np.array([])

# feeling lazy...for loop time
for id in all_ids: 
    synth = False
    for s_id in synth_ids: 
        if id==s_id: 
            final_ids = np.append(final_ids, id+'*')
            synth = True

    if synth == False: 
        final_ids = np.append(final_ids, id) 

out_df['Mineral']=final_ids

print(out_df)

out_df.to_csv('minerals_information.csv', index=False)