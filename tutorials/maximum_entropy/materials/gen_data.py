#!/usr/bin/python

cpt = {'R S': [.8, .2],
       'R C': [.6, .4],
       'Y S': [.3, .7],
       'Y C': [.1, .9]};

priors=[.4,.1,.1,.4];
features=['R S','R C','Y S','Y C'];
labels=['Cherry','Strawberry'];

import argparse
import random

parser=argparse.ArgumentParser(description='Generate data')
parser.add_argument('--num', type=int)

args = parser.parse_args()

numdata=100;
if (args.num):
    numdata=args.num

for i in range(numdata):
    r=random.random()
    totalprob=0
    for j in range(len(priors)):
        totalprob=totalprob+priors[j]
        if (r<totalprob):
            feature=features[j]
            break
    r2=random.random()
    if (r2<cpt[feature][0]):
        print 'Cherry '+feature
    else:
        print 'Strawberry '+feature
