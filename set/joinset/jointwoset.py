"""
there are several way to joining set you can use syntax .update() && .union()
two sytax will showing randomly item, bacause set is unindexed
"""

set1 = {1, 2, 3}
set2 = {'a', 'b', 'c'}
set3 = {'x', 'y', 'z'}

set1.update(set2)
set4 = set2.union(set3)

print(set1)
print(set4)