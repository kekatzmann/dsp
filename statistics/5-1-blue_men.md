[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

import thinkstats2
import thinkplot

import scipy.stats

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)

#print(dist.mean(), dist.std())
#print(dist.cdf(mu))

low = dist.cdf(177.8)       #5'10" = 177.8 cm
high = dist.cdf(185.42)     #6'10" = 185.42 cm

#print(low)
#print(high)
print(100*(high-low), "percent of the US male population is between 5ft 10in and 6ft 1in.")



