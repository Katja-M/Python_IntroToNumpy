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