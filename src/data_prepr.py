import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split

def fill_missing_with_median(df):
    for column in df.columns


def load_data(filepath:str)->pd.DataFrame:
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        raise Exception(f"Error loading data from {filepath}:{e}")
    
def split_data(data:pd.DataFrame,test_size:float):
    return train_test_split(data, test_size=test_size, random_state=42)

def save_data(df:pd.DataFrame,filepath:str)->None:
    df.to_csv(filepath,index=False)