import csv
import os
from scipy import io
import numpy as np

filename = "/Users/omushota/Downloads/faceData/FacesInTheWild.mat"
matdata = io.loadmat(filename, squeeze_me=True)
filepaths = matdata["metaData"]
filepaths = filepaths.tolist()
filepaths = [tup.tolist()[0] for tup in filepaths]
print(type(filepaths[0]))
print(filepaths[0])

with open('facedata.csv', 'w') as w:
    writer = csv.writer(w)
    for filepath in sorted(filepaths):
        print(filepath)
        writer.writerow([filepath, '1'])

