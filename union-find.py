'''
This script is to implement the union-find algorithm
on a basic example of a sequence of numbers 1..n

find_parent: O(logn)
union: O(logn)
'''
from collections import defaultdict


def init_parents(key_count):
    return {i:i for i in range(key_count)}


def find_parent(key):
    currentKey = key
    while parents[currentKey] != currentKey:
        currentKey = parents[currentKey]
    return currentKey


def union(keyA, keyB):
    parents[find_parent(keyA)] = parents[keyB]


def get_groups():
    groups = defaultdict(lambda: [])
    for key in parents:
        groups[find_parent(key)].append(key)
    return groups.items() 


parents = init_parents(10)    

union(0, 1)
union(1, 2)
union(2, 3)
union(3, 4)
union(8, 9)

for parent_key, group in get_groups():
    print(f'parent: {parent_key}, group: {group}')

'''
output
    parent: 4, group: [0, 1, 2, 3, 4]
    parent: 5, group: [5]
    parent: 6, group: [6]
    parent: 7, group: [7]
    parent: 9, group: [8, 9]
'''