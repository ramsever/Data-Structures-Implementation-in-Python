#####################################################################
#
# Dictionary and List Sorting Examples
#
# Author: Ram Sever
# 
#####################################################################

import operator
import os

################################################
#
# Sorting: Dictionaries or Double Lists
#
################################################

# clear screen
os.system('cls')

# Sorting a dictionary by value (in contrast to key)
a = {'a' : 1,'c' :3 ,'b':2}
# without using the operator package, hence defining an inline function (using lambda)
c1 = sorted(a.iteritems(),key=lambda x:x[1], reverse=False)
# the sorter and quicker way, using the operator package
c2 = sorted(a.iteritems(),key=operator.itemgetter(1), reverse=False)

print 'Dictionary Sorting'
print '-------------------'
print 'Lambda method output:              ' , c1
print 'Operator.itemgetter method output: ' , c2

print '' # newline
print '' # newline

# Sorting a double list by value 
a = [['a',1],['c',3],['b',2]]
# without using the operator package, hence defining an inline function (using lambda)
c1 = sorted(a,key=lambda x:x[1], reverse=False)
# the sorter and quicker way, using the operator package
c2 = sorted(a,key=operator.itemgetter(1), reverse=False)

print 'Double List Sorting'
print '-------------------'
print 'Lambda method output:              ' , c1
print 'Operator.itemgetter method output: ' , c2