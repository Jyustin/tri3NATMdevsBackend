import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json('quotedata/quotes.json')

# DIFFERENT WAYS OF SORTING

# OPTION 1: SORTING BY QUOTE
print(df.sort_values('Quote'))

# OPTION 2: SORTING BY NAME
print(df.sort_values('Name'))

# OPTION 3: SORTING BY DATE
print(df.sort_values(by=['Year']))



