'''
	pandas official documentation : https://pandas.pydata.org/docs/user_guide/index.html
	Install pandas : pip install pandas
	Import pandas : import pandas 
'''

import pandas as pd

# Creating DataFrames
my_dict = {
    'colors': ['red', 'green', 'black'], 
    'numbers': [45,89,25]
}

data = pd.DataFrame(my_dict)
print(type(data))
print(data)

# DataFrame with userdefined Index
data = pd.DataFrame(my_dict, index=['Index_1', 'Index_2', 'Index_3'])
print(data)

data = pd.read_csv('pokemon.csv')

# Load data from .csv file
data = pd.read_csv('pokemon.csv')
print(data.head(5))

# Set 4th column as index
data = pd.read_csv('pokemon.csv', index_col=4)
print(data.head(5))

# Load data from .txt file
data = pd.read_csv('pokemon.txt', delimiter='\t')
print(data.head(5))

# Load data from excel file
data = pd.read_excel(r'pokemon.xls')
print(data.head(5))

# print first n rows & last n rows
print(data.head(5))
print(data.tail(5))

# To print info about loaded data
print(data.info())

# To get rows and columns
print(data.shape)

# To get no. of rows
print(len(data))

# Append another dataframe
new_data = data.append(data)
print(new_data.shape)

my_dict = {
    'colors': ['red', 'green', 'black'], 
    'numbers': [45,89,25]
}

to_data = pd.DataFrame(my_dict)
new_data = data.append(to_data)
print(new_data.columns)

# Drop duplicate rows
data = new_data.drop_duplicates()
print(data.shape)

new_data.drop_duplicates(inplace=True)		# removes duplicates in the existing dataframe

# Get all the column names
print(data.columns)

# To get index of specific column
print(list(data.columns).index('name'))

# Rename a column
data.rename(columns = { 'against_bug' : 'a_bug' }, inplace=True)
print(data.columns)

# Access column data
print(data['name'])			# all names
print(data['name'][1])			# all 2nd name
print(data[['name', 'speed', 'attack']])		# multiple column data

# Access row data
print(data.iloc[5])				# 4th row
print(data.iloc[0:10])				# multiple rows using index
print(data.iloc[0:20:2])				# multiple rows using index and step

# Access data -- specific location [row, col]
print(data.iloc[2,1])
print(data.iloc[100,30])

# dropping a column
data = data.drop(['abilities'], axis = 1)
print(data.columns)

# Looping over rows -- iterrows()
for index, row in data.iterrows():
    print(index, ' -- ',  row['name'])

# Accessing rows based on conditions
print(data.loc[(data.attack >= 100), ['name', 'type1', 'type2']])

# Sorting the data - sort_values()
print(data.sort_values('weight_kg'))
print(data.sort_values('weight_kg', ascending=False))

# Removing unnecessary columns
# print(data.columns)
data = data[['name', 'classfication','attack', 'speed', 'defense',  'hp', 'sp_attack', 'sp_defense', 'pokedex_number',
       'type1', 'type2', 'height_m', 'weight_kg', 'experience_growth']]

# Modifying the data (Insertion of new column)
type_1 = list(data['type1'])
type_2 = list(data['type2'])
comb_type = [str(type_1[i]) + '-' + str(type_2[i]) for i in range(len(type_1)) ]

# defining new column
data['type'] = comb_type

# using .insert()
data.insert(2, "type", comb_type, True)

print(data[['type1', 'type2','type']])

# Drop the specific column
data = data.drop(['type'], axis = 1) 
print(data)

# Export data to a file (pip install openpyxl -- needed for excel files)
data.to_csv('modified.csv', index=False)
data.to_excel(r'00modified.xlsx', sheet_name='My sheet', index = False)
data.to_csv('00modified.txt', index=False, sep='\t')

# Get mean and median of all the columns
print(data.mean())
print(data.median())

# Filtering Data
new_data = data.loc[(data['type1'] == 'steel') & (data['type2'] == 'rock')]
new_data = data.loc[(data['type1'] == 'fire') & (data['attack'] > 100)]
new_data.reset_index(drop=True, inplace=True)		# removes old indices
print(new_data[['name', 'type1', 'type2', 'attack']])

# Grouping data 
type1_grp = data.groupby('type1')
type1_type2_grp = data.groupby(['type1', 'type2'])
# get all groups
all_type1_groups = type1_grp.groups
print(all_type1_groups)
# get a specific group
name_group = type1_grp.get_group('bug')['name']
print(name_group)

# Agreegating groups
type1_grp = data.groupby('type1')
print(type1_grp['speed'].agg(np.mean))
print(type1_grp['speed'].agg(np.size))
print(type1_grp['speed'].agg([np.sum, np.min, np.max, np.std, np.var]))

# Modifying column data based on conditions
print(data.head(5)[['type1', 'classfication']])
data.loc[data['type1'] == 'fire', ['classfication']] = ['NEW_C']
print(data.head(5)[['type1', 'classfication']])

# Get the Nan values
print(data['type1'].isna())
print(data['type1'].isnull())
# Fill the NaN values 
data['type1'].fillna("No Type", inplace = True) 

# get a summary of the distribution of continuous variables:
# gives count, mean, std, min, max .... 
print(data.describe())

# frequency of all values 
print(data['attack'].value_counts())