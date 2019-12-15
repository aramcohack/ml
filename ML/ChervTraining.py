# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
import pandas as pd
import numpy as np
import catboost as cat

# %%
train = pd.read_csv('./Geochemistry Data/CNS_gas_train.csv')

train.head()

#%%
test = pd.read_csv('Geochemistry Data/CNS_')

#%%
train['Country'].unique()

# %%
test = pd.read_csv('./Geochemistry Data/CNS_gas_test.csv')


# %%
test_colls = 'GAS_C1, GAS_C2, GAS_C3, GAS_IC4, GAS_NC4, GAS_IC5, GAS_NC5'.replace(',', '').split()


# %%
coll_mask = (train.describe().loc[['unique']].values > 2)[0]


# %%
coll_mask


# %%
good_colls = np.array(train.columns)[coll_mask]


# %%
print("GOOD COLS: ", len(good_colls))


# %%
train_colls = list(set(good_colls) - set(test_colls))


# %%
full_data = train[train_colls]


# %%
full_data.fillna(0)


# %%
full_data


# %%



# %%



# %%



