import pandas

# Building a data frame
# A data frame is made of series
df1 = pandas.DataFrame([2,4,6],[10,20,30])
print(df1)
df2 = pandas.DataFrame([[2,4,6],[10,20,30]])
# When printing, one can also see the name of the rows and columns
print(df2)
#Column and row names can be personalized
df3 = pandas.DataFrame([[2,4,6],[10,20,30]], columns = ["Price","Age","Value"], index = ['Peter', 'Tom'])
print(df3)

#Putting dictionaries into dataframes
df4 = pandas.DataFrame([{"Name":'John','Surname': "Stuart", "Age":20},{"Name": "Jack", "Age": 19}])
print(df4)

# Getting the mean of a columns
print(df3.mean())

# Getting a certain column
print(df3.Price)
# Dataframe methods can also be used for subelements of the data frame
print(df3.Price.mean())

# Loading a CSV file
# When commas are used as separators, they do not need to be given in the argument. All other separator are rerquired as input
load_csv = pandas.read_csv("D://OneDrive//Documents//Eigene Dateien//Studium//Python//StackSkillsPythonData//supermarkets.csv")
print(load_csv)
# Loading a JSON file
load_JSON = pandas.read_json("D://OneDrive//Documents//Eigene Dateien//Studium//Python//StackSkillsPythonData//supermarkets.json")
print(load_JSON)

import xlrd

# Loading an excel file
# The sheet has to specified by using an index starting at 0
load_xlsx = pandas.read_excel("D://OneDrive//Documents//Eigene Dateien//Studium//Python//StackSkillsPythonData//supermarkets.xlsx", sheet_name = 0)
print(load_xlsx)

# Loading txt-file that is separated by commas
load_txtcommas = pandas.read_csv("D://OneDrive//Documents//Eigene Dateien//Studium//Python//StackSkillsPythonData//supermarkets-commas.txt")
print(load_txtcommas)
# Loading a txt-file that is not separated by commas
load_txtsemicolons = pandas.read_csv("D://OneDrive//Documents//Eigene Dateien//Studium//Python//StackSkillsPythonData//supermarkets-semi-colons.txt", sep = ";")
print(load_txtsemicolons)

# Loading a file where we know it does not contain headers
load_noheaders = pandas.read_excel("D://OneDrive//Documents//Eigene Dateien//Studium//Python//StackSkillsPythonData//supermarkets_noheader.xlsx", header= None)
# You will get a default header made of numbers. Otherwise Python uses the first row as a header
print(load_noheaders)
# Adding column headers to the no header datafram
load_noheaders.columns = ["ID", "Address", "City", "State", "Country", "Name", "Employees"]
print(load_noheaders)
# Assigning a specific column to be the index
# However, this method does not modify the dataframe. So the object remains the same
load_noheaders.set_index("ID")
print(load_noheaders)
print(load_noheaders.set_index("ID"))
# If the dataframe needs to be modified, use the following argument
load_noheaders.set_index('ID', inplace = True)
print(load_noheaders)
# If you use another column as index, the old index column will disappear
# In order to avoid that a column declared as index is dropped after a new column is used as index
load_noheaders.set_index("Name", inplace = True, drop = False)
print(load_noheaders)

# Accessing data frames based on labels
# nameOfDataframe.loc['entry of first row I am interested in of index column: last row I am interested in of index column, first column I am interested in: last column I am interested in]
# When accesing single cell
    # nameofDataframe.loc['entry of row I am interested in which is in index column', 'name of column I am interested in']
# Accesing all entries of a column
    # nameofDataframe.loc[:, 'name of Column I am interested in']

# Accesing data frames basend on index
# nameofDataFrame.iloc[1:3, 1:3]
    # Output: mini data frame with first and second entry (zero-based indexing) of index column and first and second columns (zero-based indexing)
print(load_noheaders.iloc[1,0:3])

# Deleting columns or rows in data frame based on labels
# Using the drop method
    # 1: Delete a column
    # 0: Delete a row
print(load_noheaders.drop('City', 1))
print(load_noheaders.drop('Bready Shop', 0))
# The drop method does not update the data frame
print(load_noheaders)

# Deleting columns or rows in data frame based on indices
# Deleting rows
print(load_noheaders.drop(load_noheaders.index[0:3], 0))
# Deleting columns
print(load_noheaders.drop(load_noheaders.columns[0:3], 1))