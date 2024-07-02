import pandas as pd
import random

# Создаем исходные данные
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Преобразуем данные в one-hot encoding
one_hot_data = pd.DataFrame()

for category in data['whoAmI'].unique():
    one_hot_data[category] = (data['whoAmI'] == category).astype(int)

print(one_hot_data.head())