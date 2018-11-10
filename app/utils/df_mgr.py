import ipdb
import pandas as pd
import numpy as np

def get_dataframe(files):

    '''
        Function to concatenate multiple python files and return a dataframe
        :param files: list of excel files to be concatenated
        :return: pandas dataframe that is concat of all the files supplied in the param
    '''

    all_dfs = [pd.read_excel(file, skiprows=1, index_col = 0) for file in files]
    df = pd.concat(all_dfs)
    df.drop_duplicates()
    return  df
