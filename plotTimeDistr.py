# plot the time distribution of the LIWC result

import numpy as np
import matplotlib.pyplot as plt
import os

#<<<<<<<<<<<<<<<<<<<<<< plot >>>>>>>>>>>>>>>>>>>>>>>>

path = "/Users/Xing/documents/IdentificationProject/Data_v3"
amputeeFile = "amputeeAvg.txt"
nonAmputeeFile = "nonAmputeeAvg.txt"

amputee = np.loadtxt(amputeeFile, dtype = np.float)
nonAmputee = np.loadtxt(nonAmputeeFile, dtype = np.float)



