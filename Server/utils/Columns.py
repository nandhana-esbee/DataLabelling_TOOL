import pandas as pd

def column(file):
    '''
    Get the column names of the uploaded file
    '''
    df = pd.read_csv(file)
    listss = list(df.columns)
    name = pd.DataFrame(listss)
    return listss

def Text(file , num ,textname):
    '''
    Get the text of the uploaded file from the column names
    '''
    df = pd.read_csv(file)
    try:
        text = df.loc[num ,textname]
    except:
        return "index out of range"
    return text


