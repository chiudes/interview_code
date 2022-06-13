import pandas as pd
import pymysql
from functools import reduce
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:Passw0rd!@localhost:3306/lvrland')

df_a = pd.read_csv("data/a_lvr_land_a.csv")
df_b = pd.read_csv("data/b_lvr_land_a.csv")
df_e = pd.read_csv("data/e_lvr_land_a.csv")
df_f = pd.read_csv("data/f_lvr_land_a.csv")
df_h = pd.read_csv("data/h_lvr_land_a.csv")

dfs = [df_a, df_b, df_e, df_f, df_h]

df_sql = reduce(lambda  left,right: pd.merge(left, right, how='outer'), dfs)

df_sql = df_sql.rename(columns={
"date":"date_trade",
"use":"use_for"
})

df_sql = df_sql[['district','date_trade','style','use_for','floor','city']]

df_sql['id'] = pd.Categorical(df_sql['district']).codes

df_sql.to_sql('all_lvr_land', engine, if_exists='append', index= False)

print('Table all_lvr_land done')