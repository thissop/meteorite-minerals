import numpy as np
import pandas as pd

df = pd.read_csv(r'C:\Users\Research\Documents\GitHub\meteorite-minerals\code\final_sample\found or synth list.csv')

names = np.array(df['Mineral'])
synth = np.array(df['Synth'])
on_earth = np.array(df['Earth'])

synth_mask = np.logical_or(synth=='Maybe', synth=='Yes')
earth_mask = np.logical_or(on_earth=='Maybe', on_earth=='Yes')

synth_to_remove = names[synth_mask]
on_earth_to_remove = names[earth_mask]

xor = np.setxor1d(synth_to_remove, on_earth_to_remove)
both = np.intersect1d(synth_to_remove, on_earth_to_remove)

to_remove = np.append(xor, both)
print(names, to_remove)
to_keep = np.setdiff1d(names, to_remove)

final_df = pd.DataFrame(to_keep, columns=['mineral_name'])
final_df.to_csv('final_sample.csv', index=False)