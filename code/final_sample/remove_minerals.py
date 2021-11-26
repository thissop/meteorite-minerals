import numpy as np
import pandas as pd

df = pd.read_csv(r'C:\Users\Research\Documents\GitHub\meteorite-minerals\code\final_sample\found or synth list.csv')
print(df['Mineral'])
print(df['Synth'])