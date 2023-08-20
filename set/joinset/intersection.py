"""
Keep only duplicate item for showing up
"""

x = {'apple', 'samsung', 'xiomi'}
y = {'canon', 'microsoft', 'google', 'apple'}

z = x.intersection(y) #only showing item in both, and must create set first
print(z)