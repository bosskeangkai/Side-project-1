import pandas as pd

data=pd.read_csv('./datasets/superstore.csv')

# print(data.head(2))

# print(data.isnull().count())

data.drop(['total_inv','min','cost_discount','start_inventory','cost','frequency','lead_time','order_year','order_month','order_day'],axis=1,inplace=True)

# print(data.columns)

data.to_csv('datasets.csv',index=False)