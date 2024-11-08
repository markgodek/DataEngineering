import pandas as pd
from dask import dataframe as dd

#create pandas dataframe
odd_num = list(range(1,10,2))
even_num = [x+1 for x in list(range(1,10,2))]

pandas_df = pd.DataFrame({'odd_num': odd_num, 'even_num': even_num})
print(pandas_df)
#set npartition argument
df = dd.from_pandas(pandas_df, npartitions=2)

#Uncomment the line below if you are using Windows
df.to_csv(r'C:\Users\markg\DataEngineering\Module22\Activity22.1', index=False)