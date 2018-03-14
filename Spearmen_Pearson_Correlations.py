"""
Developer : Naveen
Code to compute Pearson and Spearman correlations. This also plots the correlations
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#read the data
df = pd.read_csv(r'path to csv')

def drawPlot(methodName):
    """
	takes the parameter of correlation type and saves the correlations in a csv.
	"""
    sub = df.corr(method=methodName)
    sub.to_csv(methodName+'.csv')
	
	
	#read the columns
    sub = sub.loc['mediaUsage':'Scheduling_OfficeTools_Weather']
    x = np.arange(len(sub.index))
	
	#doing for all 5 traits
    o = sub['Openness']
    c = sub['Conscientiousness']
    e = sub['Extraversion']
    a = sub['Agreeableness']
    n = sub['Neuroticism']
    z = sub.columns.values.tolist()
    z.pop(0)
    z.pop(0)
	
	
	
	#plotting the values
    plt.plot(x, o, marker='o')
    plt.plot(x, c, marker='o')
    plt.plot(x, e, marker='o')
    plt.plot(x, a, marker='o')
    plt.plot(x, n, marker='o')
    plt.ylabel(methodName)
    plt.xticks(x, z, rotation='vertical')
    plt.legend(shadow=True, fancybox=True)
    plt.show()

drawPlot('spearman')
drawPlot('pearson')
