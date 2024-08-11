#Function to create a csv file with the index columns and values
import pandas as pd

def makecsv(textheader,labelheader,csv_obj):
    csvpath = 'CSV/labelling.csv'
    