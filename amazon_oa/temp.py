# import modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dfBank = pd.read_csv('bank_performance.csv', index_col=0, header=0)
dfBank.head(5)

groupConsumer = dfBank.groupby('Consumer ID')
dfConsumer = groupConsumer.sum()
numberofunique = dfConsumer.shape[0]


dfSorted = dfConsumer.sort_values(by='Amount', ascending = False).head(5)

Topfive = dfSorted.index.values

TopfiveService = dfBank[dfBank['Consumer ID'].isin(Topfive)]



print (TopfiveService)