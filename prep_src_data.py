# -*- coding: utf-8 -*-
"""
@author: Christian Winkler
"""

import pandas as pd

# BGH

## X. Senat

df = pd.read_feather("prep_data\dt_zs10.feather")

df_zs10_ls = df[df['bemerkung'].str.contains("Leitsatz")]

df_zs10_ls.to_excel('src_data\df_zs10_ls.xlsx')

## Xa. Senat

df = pd.read_feather("prep_data\dt_zs10a.feather")

df_zs10a_ls = df[df['bemerkung'].str.contains("Leitsatz")]

df_zs10a_ls.to_excel('src_data\df_zs10a_ls.xlsx')


# BPATG

df = pd.read_feather("prep_data\dt_bpatg.feather")

df_ls = df[df['bemerkung'].str.contains("Leitsatz")]

df_ls.to_excel('src_data\df_bpatg_ls.xlsx')

