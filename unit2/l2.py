import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('loansData.csv')
# loansData.info()
loansData.dropna(inplace=True)

loansData.boxplot(column='Amount.Funded.By.Investors')
plt.show()

# plt.figure()
loansData.hist(column='Amount.Funded.By.Investors')
plt.show()

'''
http://stackoverflow.com/questions/12082568/what-exactly-do-the-whiskers-in-pandas-boxplots-specify
'''

# box plt standard shows MEDIAN, first and third quartile (25,75) are the box
# full range indicated by the "whiskers".
# Dots beyond whisker are outliers called fliers

# hist shows amount in different bucket ranges, shows weight of loan values
# can't show where most things lie (e.g. 25,75 range)
# does show their weight

plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'],dist="norm"
                       ,plot=plt)
plt.show()
