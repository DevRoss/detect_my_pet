import pandas as pd
import numpy as np
import os

DATA_PATH = 'data'
FULL_CSV = 'herbal_tea_labels.csv'

csv_to_split = pd.read_csv(os.path.join(DATA_PATH, FULL_CSV))
csv_size = len(csv_to_split)
grouped = csv_to_split.groupby(level=0)
grouped_list = [grouped.get_group(x) for x in grouped.groups]
300
# 318
print (csv_size)
train_list = np.random.choice(csv_size, size=200, replace=False)
test_list = np.setdiff1d(list(range(csv_size)), train_list)
print(len(train_list))
print(len(test_list))


train = pd.concat([grouped_list[i] for i in train_list])
test = pd.concat([grouped_list[i] for i in test_list])

train.to_csv(os.path.join(DATA_PATH, 'train_labels.csv'), index=None)
test.to_csv(os.path.join(DATA_PATH, 'test_labels.csv'), index=None)

# print(grouped_list[10])
