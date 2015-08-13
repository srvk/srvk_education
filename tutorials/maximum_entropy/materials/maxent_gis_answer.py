#!/usr/bin/python

import argparse
import string
import math

parser=argparse.ArgumentParser(description='Generate data')
# add argument for epsilon, data
parser.add_argument('--epsilon', type=float, default=0.001)
parser.add_argument('--data')

args = parser.parse_args()

# read all of the data into memory
with open(args.data) as file:
    data=[string.split(line.rstrip('\n')) for line in file]

# Create a dictionary with "Label Feature" pairs
observed={}
labels={}

for datum in data:
    # column 0 holds the label, rest are features
    # assume one binary feature for each column, and all labels are distinct
    for feature in range(1,len(datum)):
        key=datum[0]+' '+datum[feature]
        if key not in observed:
            observed[key]=1
        else:
            observed[key]=observed[key]+1
        # collect labels
        if datum[0] not in labels:
            labels[datum[0]]=0

# initialize lambda weights for all keys
lambdawt={key: 0 for key in observed.keys()};

# find maxiumum feature count
cmax=observed[max(observed)]

converged=False;

while not converged:
    converged=True;

    # initialize expected counts
    expected={key: 0 for key in observed.keys()}

    #make a pass through the data
    for datum in data:

        # step 1: collect the z normalizer and individual label-ftr contributions
        znormalizer=0
        s={}
        for label in labels.keys():
            s[label]=0;
            for feature in range(1,len(datum)):
                key=label+' '+datum[feature]
                # this assumes presence of label/ftr = 1, 0 otherwise
                s[label]=s[label]+lambdawt[key]
            znormalizer=znormalizer+math.exp(s[label])
        

        # step 2: compute expected counts 
        for label in labels.keys():
            for feature in range(1,len(datum)):
                key=label+' '+datum[feature]
                expected[key]=expected[key]+math.exp(s[label])/znormalizer

    # once the pass is completed, update the lamdas
    for key in lambdawt.keys():
        deltalambda=(1/float(cmax)) * math.log(float(observed[key])/float(expected[key]))
        if abs(deltalambda) > args.epsilon:
            converged=False 
        lambdawt[key]=lambdawt[key]+deltalambda

    print 'Observed counts: ',[[key,observed[key]] for key in sorted(observed)]
    print 'Expected counts: ',[[key,expected[key]] for key in sorted(expected)]
    print 'Lambda: ',[[key,lambdawt[key]] for key in sorted(lambdawt)]
    print 




