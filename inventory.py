import pandas as pd
import numpy as np

np.random.seed(42)
dates = pd.date_range(start="2022-01-01", periods=365, freq='D')
store_ids = [1, 2, 3]
item_ids = [101, 102, 103, 104]

data = []
for date in dates:
    for store in store_ids:
        for item in item_ids:
            units_sold = max(0, int(np.random.normal(loc=50, scale=10)))
            price = round(np.random.uniform(10, 100), 2)
            promo = np.random.choice([0, 1], p=[0.8, 0.2])
            holiday_flag = 1 if date.weekday() == 6 else 0  # Sunday as holiday
            data.append([date, store, item, units_sold, price, promo, holiday_flag])

df = pd.DataFrame(data, columns=["date", "store_id", "item_id", "units_sold", "price", "promo", "holiday_flag"])

file_path = "C:\\Users\\bhooo\\Downloads\\inventor management system\\Full_Demand_Forecasting_Dataset.xlsx"
df.to_excel(file_path, index=False)

file_path