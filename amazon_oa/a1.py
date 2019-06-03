import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dfStore = pd.read_csv('StoreBalanceUpdate.csv', header=0)
# Print first five lines
print(dfStore.head(5))