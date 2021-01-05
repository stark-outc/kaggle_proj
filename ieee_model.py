# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 14:22:24 2020

@author: 徐钦华
"""
import pandas as pd
from convert_big_dataset import Convert_Data
import sys
import vaex
import pprint

sys.path.append(r'/data/test/kaggle_proj')
# pd.set_option('display.float_format',lambda x:'%.2f'%x)
# train_identity = pd.read_csv('train_identity.csv')
# train_identity.index.size
# train_transaction = pd.read_csv('train_transaction.csv')
# test_identity = pd.read_csv('test_identity.csv')
# test_transaction = pd.read_csv('test_transaction.csv')
df = vaex.read_csv('train_transaction.csv',copy_index=False)
print(df.describe())
# m = Convert_Data(train_identity)
# converted_data = m.concat_data()
#
# import dask
# import dask.dataframe as dd
# from dask.diagnostics import ProgressBar
# print(dask.__version__)
# train_transaction = dd.read_csv('train_transaction.csv')
# with ProgressBar():
#     train_transaction = train_transaction.compute()
#
# m1 = Convert_Data(train_transaction)
# converted_train_transaction = m1.concat_data()
# with ProgressBar():
#     converted_train_transaction = converted_train_transaction.compute()
    
    
