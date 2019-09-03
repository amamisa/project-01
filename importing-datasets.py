import pandas as pd
year19 = pd.concat(map(pd.read_csv, ['turnstile_190504.txt']))

print(year19)