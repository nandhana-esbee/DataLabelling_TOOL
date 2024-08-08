#Function to get the list of index name from the file

import pandas as pd

def IndexnameList(filename):
    data = pd.read_csv(filename)
    index = list(data.columns)
    return index