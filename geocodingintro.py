# To-do: Adding a column for latitude and longitude

# pip install geopy
# geopy has a geocoder module which requires an internet connection
from geopy.geocoders import ArcGIS
import pandas

nom = ArcGIS()

addressWCoordinates = nom.geocode('90 Cypress St, Brookline, MA 02445')
# For some reason, the latitude and longtide values are not displayed in the following print command
print(addressWCoordinates)
# However, they are stored in the variable and can be accessed
print(addressWCoordinates.latitude)
print(addressWCoordinates.longitude)

# Loading a CSV file
# When commas are used as separators, they do not need to be given in the argument. All other separator are rerquired as input
stores_df = pandas.read_csv("D://OneDrive//Documents//Eigene Dateien//Studium//Python//StackSkillsPythonData//supermarkets.csv")
print(stores_df)

# Creating an address column which can be used as input in ArcGIS
stores_df['Geocode_Address'] = stores_df['Address'] + ', ' + stores_df['City'] + ', ' + stores_df['State'] + ', ' + stores_df['Country']
print(stores_df)

# Now send Geocode_Address to geocode method
# The apply method iterates through all rows
stores_df['Coordinates'] = stores_df['Geocode_Address'].apply(nom.geocode)
print(stores_df)

stores_df['Longitude'] = stores_df['Coordinates'].apply(lambda x: x.longitude if x != None else None)
stores_df['Latitude'] = stores_df['Coordinates'].apply(lambda x: x.latitude if x != None else None)

print(stores_df)