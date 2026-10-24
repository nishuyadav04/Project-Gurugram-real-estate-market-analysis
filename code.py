import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Data.csv")
# print(df.columns.tolist())  
# print(df.columns)
df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')   
# print(df.columns.tolist())
# df['status'] = df['status'].str.strip().str.lower()
