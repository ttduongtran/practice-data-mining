import pandas as pd

# loc method

df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
                  index=['cobra', 'viper', 'sidewinder'],
                  columns=['max_speed', 'shield'])
df

df.loc['viper']

# Set value for an entire column
df.loc[:, 'max_speed'] = 30
df
