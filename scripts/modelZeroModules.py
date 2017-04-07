"""NCT Heidelberg
Elvira Mingazova 2017
Here are useful functions for completing week2 tasks"""

#a function which will process the given text file and return {"chr name": chr length} pairs inside of a dictionary
def getDimensionDict(filename):
    d={}
    with open(filename) as dimension_file:
        for line in dimension_file:
            key, value = line.split()
            d[key.strip()]=int(value.strip())
        dimension_file.close()
    return d
import random
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
#a new parameter "filename" was added to this function in order 
#to be able to call getDimensionDict(filename) from within
def plotDistribution(n,chrom,filename):
    dimension_dict = getDimensionDict(filename)
    chrLen = dimension_dict[chrom]
    position = []
    for i in range(n):
        position.append(random.randint(1,chrLen))
    position.sort()
    pmean = np.mean(position)
    pstd = np.std(position)
    pdf = stats.norm.pdf(position, pmean, pstd)
    plt.hist(position,normed=True, label = 'experimental PDF')
    plt.plot(position, pdf, label = 'norm PDF')
    plt.xlabel("$Position\ on\ a\ chromosome$")
    plt.ylabel("$Probability$")
    plt.legend(loc='lower right')
    plt.show()