import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

brainFile = './Data/brainsize.txt'
brainFrame = pd.read_csv(brainFile)

print('\nHEAD:')
print(brainFrame.head())

print('\nDESCRIBE:')
print(brainFrame.describe())

menDf = brainFrame[(brainFrame.Gender == 'Male')]
womenDf = brainFrame[(brainFrame.Gender == 'Female')]

menMeanSmarts = menDf[["PIQ", "FSIQ", "VIQ"]].mean(axis=1)
plt.scatter(menMeanSmarts, menDf["MRI_Count"])
plt.show()

womenMeanSmarts = womenDf[["PIQ", "FSIQ", "VIQ"]].mean(axis=1)
plt.scatter(womenMeanSmarts, womenDf["MRI_Count"])
plt.show()

print('\nShared corr:')
print(brainFrame.corr(method='pearson'))

print('\nWomen corr:')
print(womenDf.corr(method='pearson'))

print('\nMen corr:')
print(menDf.corr(method='pearson'))

wcorr = womenDf.corr()
sns.heatmap(wcorr)
plt.savefig('women_attribute_correlations.png', tight_layout=True)

mcorr = menDf.corr()
sns.heatmap(mcorr)
plt.savefig('men_attribute_correlations.png', tight_layout=True)
