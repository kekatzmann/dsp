[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

import numpy as np
import sys

import nsfg
import first
import thinkstats2
import thinkplot

import chap01soln # for chap01soln.ReadFemResp() function
import probability # for probabiliy.BiasPmf function

df = chap01soln.ReadFemResp()

pmf = thinkstats2.Pmf(df.numkdhh, label='numkdhh')

thinkplot.Pmf(pmf)
thinkplot.Show(xlabel='Number of children', ylabel='PMF')


biased = probability.BiasPmf(pmf, label='biased')

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased])
thinkplot.Show(xlabel='Number of children', ylabel='PMF')

def PmfMean(pmf): #computed mean of Pmf
    mean = 0.0
    for x, p in pmf.d.items():
        mean += p * x
    return mean

meanPmf = PmfMean(pmf)
meanBiased = PmfMean(biased)


print('The actual mean is: ', meanPmf)
print('The biased mean is: ', meanBiased)

