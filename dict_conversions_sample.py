#####################################################################
#
# Dictionary to List Conversion Examples
#
# Author: Ram Sever
# 
#####################################################################

import operator 

# This is the dictionary we want to convert
a = {'h':1,'d':4,'f':6,'b':2,'e':5,'g':7}

#####################################################################
#
# Convert a dictionary to a list of tuples
# 
#####################################################################
b = [ (key,a[key]) for key in a.keys()]

#####################################################################
#
# A First methods for converting a list of tuples to a dictionary
# 
#####################################################################
c = dict(b) 

#####################################################################
#
# A Second method to convert a list of tuples into a dictionary
# 
#####################################################################
d = dict()
for t in b:
    d[t[0]] = t[1]

#####################################################################
#
# A Third method to convert two lists into a dictionary
# 
#####################################################################

# First we use "map" to take from the dictionary either keys
# or the values
k = map(lambda x:x[0],b)
v = map(lambda x:x[1],b)
# We than convert the two lists into a list of tuples
# and run the dict constructor
e = dict(zip(k,v))
print e