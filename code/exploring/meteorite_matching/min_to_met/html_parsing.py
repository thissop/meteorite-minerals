import numpy as np
import pandas as pd
import requests 

our_ids = list(pd.read_csv('https://raw.githubusercontent.com/thissop/meteorite-minerals/main/code/exploring/meteorite_matching/our_list.csv?token=AQN5JT72YPUR5JKZQNOS7P3BOIB5K')['name'])
our_ids = np.array([i.upper() for i in our_ids])

athena_ids = np.array(pd.read_csv('https://raw.githubusercontent.com/thissop/meteorite-minerals/main/code/exploring/meteorite_matching/athena/athena.csv?token=AQN5JTY4HXWHF4EMTLYQYATBOICAM'))

shared_ids = np.intersect1d(athena_ids, our_ids)

with open('mineral_locations.txt', 'a') as f:
    f.write('Mineral,Meteorite(s)'+'\n')
    
for id in shared_ids: 
    url = 'http://athena.unige.ch/bin/minfich.cgi?s='+id
    r = requests.get(url)

    df_list = pd.read_html(r.text)
    
    athena_str = df_list[1].to_string()

    local_idx = athena_str.index('Type Locality')
    athena_str = athena_str[local_idx:]

    input_str = input(athena_str+'\n'+'Term(s): ')
    with open('mineral_locations.txt', 'a') as f:
        f.write(id+','+input_str+'\n')