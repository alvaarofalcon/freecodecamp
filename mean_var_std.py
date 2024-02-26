# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 21:25:05 2024

@author: Alvaro R. Gutierrez Falcón Valle
"""
import numpy as np
def calculate(lista):
    if type(lista) == list:
        if len(lista) == 9:
            matriz = np.array(lista).reshape(3,3)
            prm_col = np.mean(matriz, axis=0)
            prm_fil = np.mean(matriz, axis=1)
            prm_mtr = np.mean(matriz)
            vrz_col = np.var(matriz, axis=0)
            vrz_fil = np.var(matriz, axis=1)
            vrz_mtr = np.var(matriz)
            std_col = np.std(matriz, axis=0)
            std_fil = np.std(matriz, axis=1)
            std_mtr = np.std(matriz)
            max_col = np.max(matriz, axis=0)
            max_fil = np.max(matriz, axis=1)
            max_mtr = np.max(matriz)
            min_col = np.min(matriz, axis=0)
            min_fil = np.min(matriz, axis=1)
            min_mtr = np.min(matriz)
            sum_col = np.sum(matriz, axis=0)
            sum_fil = np.sum(matriz, axis=1)
            sum_mtr = np.sum(matriz)
        else:
            raise ValueError("List must contain nine numbers")
    else:
        raise ValueError('A list was expected')    
    result = {
        'mean' : [prm_col, prm_fil, prm_mtr],
        'variance' : [vrz_col, vrz_fil, vrz_mtr],
        'standard deviation' : [std_col,std_fil, std_mtr],
        'max' : [max_col, max_fil, max_mtr],
        'min' : [min_col, min_fil, min_mtr],
        'sum' : [sum_col, sum_fil, sum_mtr]
                }
    return result