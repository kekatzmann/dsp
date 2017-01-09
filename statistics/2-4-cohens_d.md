[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

import numpy as np
import sys

import nsfg
import first
import thinkstats2
import thinkplot
import math

df = nsfg.ReadFemPreg()

first = df.loc[df['pregordr'] == 1]
notFirst = df.loc[df['pregordr'] != 1]

def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d

print (CohenEffectSize(first['totalwgt_lb'], notFirst['totalwgt_lb']))

