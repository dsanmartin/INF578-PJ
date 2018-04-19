#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 14:06:35 2018

@author: dsanmartin
"""

import numpy as np
from scipy.stats import t
import scipy as sp
import scipy.stats
import matplotlib.pyplot as plt
np.random.seed(42)

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0*np.array(data)
    n = len(a)
    m, se = np.mean(a), np.std(a)#scipy.stats.sem(a)
    h = se * sp.stats.t._ppf((1+confidence)/2., n-1)
    print(se)
    return m, m-h, m+h

mean = []
intr = []

for i in range(10):
    data = np.random.rand(200)
    me = np.mean(data)
    st = np.std(data)
    
    i1 = t.interval(0.95, len(data), loc=me, scale=st)
    
    mean.append(me)
    intr.append(abs(me-i1[0]))


plt.figure()
plt.errorbar(np.arange(1, len(mean)+1), mean, yerr=intr)
plt.title("Simplest errorbars, 0.2 in x, 0.4 in y")