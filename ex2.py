from itertools import permutations

__author__ = 'Pedro'

import itertools

def ParallelInter(a, b):
    #result list contains the parallel interleaving
    resultlist = []
    list2iter = b.__iter__()
    #For each item in a, append the item and then append the next item from b.  If b has any remaining elements then append them.
    for item in a:
        resultlist.append(item)
        try:
            resultlist.append(list2iter.next())
        except Exception as e:
            continue
    while True:
        try:
            resultlist.append(list2iter.next())
        except Exception as e:
            break
    #print resultlist
    return resultlist

print ParallelInter([1,2],[3,4])

def AllInter(a,b):
    if not a:
        #The only possible interleaving is just list b so return a list with this
        return [b]
    if not b:
        #The only possible interleaving is just list a so return a list with this
        return [a]
    else:
        list1 = AllInter(a[1:], b[0:])
        #Attach first element of list a to list1. This list should have all the interleavings that have as a start a[0]
        for i in range(0,len(list1)):
            list1[i].insert(0,a[0])

        list2 = AllInter(a[0:], b[1:])
        #Attach first element of list b to list2. This list should have all the interleavings that have as a start b[0]
        for i in range(0,len(list2)):
            list2[i].insert(0,b[0])

        return list1 + list2

print AllInter([1,2],[3,4])





