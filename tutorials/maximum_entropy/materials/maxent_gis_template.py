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
        #
        # ***THIS IS CRITICAL***
        #
        # We store each feature/observed/expected/lambdawt in a dictionary
        # that maps a string containing the label and feature to the 
        # desired quantity.  For example, if you wanted the number of times
        # you see Cherry, R in the data, look at observed["Cherry R"].
        # 
        # The following code constructs the observed counts for
        # each label-feature pair.
        key=datum[0]+' '+datum[feature]
        if key not in observed:
            observed[key]=1
        else:
            observed[key]=observed[key]+1

        # collect labels into a dictionary
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

    # TO DO: implement GIS update.  Store expected counts for each key.
    #    Update lambdas based on difference with observed counts.


    # At end of pass through data, print out the expected and observed
    # counts, as well as the new lambda weights
    print 'Observed counts: ',[[key,observed[key]] for key in sorted(observed)]
    print 'Expected counts: ',[[key,expected[key]] for key in sorted(expected)]
    print 'Lambda: ',[[key,lambdawt[key]] for key in sorted(lambdawt)]
    print 




