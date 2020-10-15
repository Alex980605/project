import math
import folium
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

def missing_value(df):
	return df.isnull().sum()

#show the confirmed, deaths and recovered rated grouped by country
#showed the top and last 5 info
def group_by(df,groupby,attribute):
	by_country=df.groupby([groupby])[[attribute]].sum()
	print(by_country.sort_values(by=attribute,ascending=False))
  
#read the location_dataset
#read the dataset
df_Location=pd.read_csv('processed_location_Sep20th2020.csv')

# for every attribute print the number of missing values
Location_missing_data=missing_value(df_Location)
print("The number of missing value for every attributes")
print(Location_missing_data)
print()

#check the last updated time
Location_Last_Update = df_Location['Last_Update'].value_counts()
print(Location_Last_Update.head(5))
print()
#the time last updated is almost all the same->useless attribute

#ignore the NaN data in lat and long column
#for attribute Lat and long_
Location_incidents = folium.map.FeatureGroup()
Location_mapInfo = df_Location.dropna(subset=['Lat'])
Location_mapInfo = df_Location.dropna(subset=['Long_'])
for lat,long, in zip(Location_mapInfo.Lat,Location_mapInfo.Long_):
    Location_incidents.add_child(folium.CircleMarker([lat,long],radius=3,color='red',fill=True,fill_color='red',fill_opacity=0.1))
Location_cases_Distribute=folium.Map()
Location_cases_Distribute.add_child(Location_incidents)
Location_cases_Distribute.save('Location_cases_Distribute.html')

#for attributes ['Confirmed','Deaths','Recovered','Active']
list=['Confirmed','Deaths','Recovered','Active']
for attribute in list:
    group_by(df_Location,'Country_Region',attribute)
    print()

#Incidence_Rate attribute
#shows the top 10 result only as the last 10 is NaN
incidentrate=df_Location[['Combined_Key','Incidence_Rate']]
print(incidentrate.sort_values(by=['Incidence_Rate'],ascending=False).head(10))
print()

#Case-Fatality_Ratio
#shows the top 10 result only as the last 10 is NaN
caseFatalityRatio=df_Location[['Combined_Key','Case-Fatality_Ratio']]
print(caseFatalityRatio.sort_values(by=['Case-Fatality_Ratio'],ascending=False).head(10))
print()


df_Cases=pd.read_csv('processed_individual_cases_Sep20th2020.csv')

# for every attribute print the number of missing values
Cases_missing_data=missing_value(df_Cases)
print("The number of missing value for every attributes")
print(Cases_missing_data)
print()


# age attribute
#just shows the trend of the range of age
ageInfo = df_Cases['age'].value_counts()
print(ageInfo.head(10))
ageInfo.head(4).plot.bar()
plt.show()
print()

# sex attribute
sexInfo = df_Cases['sex'].value_counts()
print(sexInfo)
sexInfo.plot.bar()
plt.show()
print()

#ignore the additional_information and source attribute

#for date_confirmation attribute
dfdata = pd.to_datetime(df_Cases.date_confirmation,format='%d.%m.%Y',errors='coerce')
date_confirmation_Info = dfdata.value_counts().sort_index()
print(date_confirmation_Info)
date_confirmation_Info.plot(kind='line')
plt.show()
print()

#for outcome attribute
outcomeInfo = df_Cases['outcome'].value_counts()
print(outcomeInfo)
outcomeInfo.plot.bar()
plt.show()

#*****Long Computation*****
#ignore attribute province and country 
#used lat and long to show province and country details
#ignore the NaN data in lat and long column
#for attribute lat and long_
incidents = folium.map.FeatureGroup()
mapInfo = df_Cases.dropna(subset=['latitude'])
mapInfo = df_Cases.dropna(subset=['longitude'])
for lat,long, in zip(mapInfo.latitude,mapInfo.longitude):
    incidents.add_child(folium.CircleMarker([lat,long],radius=3,color='red',fill=True,fill_color='red',fill_opacity=0.1))
Individual_cases_Distribute=folium.Map()
Individual_cases_Distribute.add_child(incidents)
Individual_cases_Distribute.save('individual_cases_Distribute.html')
print()
