[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

import numpy as np
import random
import thinkstats2
import thinkplot

count = 0
nums = []
while count < 1000:
    nums.append(random.random())
    count += 1

pmf = thinkstats2.Pmf(nums, label='numbers')
thinkplot.Pmf(pmf)
thinkplot.Show(xlabel='Random Numbers', ylabel='PMF', axis=[0, 1, 0, 0.0015])

cdf = thinkstats2.Cdf(nums, label='numbers')
thinkplot.Cdf(cdf)
thinkplot.Show(xlabel='Random Numbers', ylabel='CDF')

"""
The distribution does appear uniform, which we would expect given such
a large sample and equal probabilities for each number to be generated.
"""
