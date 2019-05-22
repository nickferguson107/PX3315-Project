import RandomGraph
import numpy as np
'''
own = RandomGraph.multiplot(100, 1000, 0, 7.5)
nxc = nx_comparison.multiplot(100, 1000, 0, 7.5)

dif = own - nxc
'''

d = np.loadtxt("Results\difference.txt", delimiter='\t')
e = abs(d)
a = [i for i in e if i > 0.01]
print((1-(len(a)/1000))*100)