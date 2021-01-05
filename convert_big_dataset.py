# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 18:47:28 2020

@author: 徐钦华
"""
import pandas as pd
class Convert_Data(object):
    '''
    数据类型转化
    '''
    def __init__(self,dataset):
        self.dataset=dataset
        for dtype in ['float','int','object']:
            selected_dtype = self.dataset.select_dtypes(include=[dtype])
            mean_usage_b = selected_dtype.memory_usage(deep=True).mean()
            mean_usage_mb = mean_usage_b / 1024 ** 2
            print('Average memory usage for {} columns: {:03.2f} MB'.format(dtype,mean_usage_mb))

    def compare_convert(self,dataset_type):
        if isinstance(dataset_type,pd.DataFrame):
            usage_b = dataset_type.memory_usage(deep = True).sum()
        else:
            usage_b = dataset_type.memory_usage(deep = True)
        usage_mb =  usage_b/1024**2
        return ( '{:03.2f} MB'.format(usage_mb))
        
    def convert_int(self):
        data_int = self.dataset.select_dtypes(include=['int']).copy()
        converted_int = data_int.apply(pd.to_numeric,downcast='int',axis=1)
        print(f'convert_int before usage: {self.compare_convert(data_int)}',f'\n convert_int after usage: {self.compare_convert(converted_int)}')
        return converted_int
    def convert_float(self):
        data_float = self.dataset.select_dtypes(include=['float']).copy()
        converted_float = data_float.apply(pd.to_numeric,downcast='float',axis=1)
        print(f'convert_float before usage: {self.compare_convert(data_float)}',f'\n convert_float after usage: {self.compare_convert(converted_float)}')
        return converted_float
    def convert_obj(self):
        data_obj = self.dataset.select_dtypes(include=['object']).copy()
        converted_obj = pd.DataFrame()
        for col in data_obj.columns:
            num_unique_values = len(data_obj[col].unique())
            num_total_values = len(data_obj[col])
            if num_unique_values / num_total_values <0.5:
                converted_obj.loc[:,col] = data_obj[col].astype('category')
            else:
                converted_obj.loc[:,col] = data_obj[col]
        print(f'convert_obj before usage: {self.compare_convert(data_obj)}',f'\n convert_obj after usage: {self.compare_convert(converted_obj)}')
        return converted_obj
    def concat_data(self):
        data_lst = [self.convert_int(),self.convert_float(),self.convert_obj()]
        data = pd.concat(data_lst,axis=1)
        return data
    
# def load_data(reference_data):
    
    