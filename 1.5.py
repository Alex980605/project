#1.5
import math
import folium
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

df_Location = pd.read_csv("processed_location_Sep20th2020.csv")

df2 = df_Location[df_Location['Country_Region'] == 'US'].groupby('Province_State').agg(
	Last_Update=('Last_Update',pd.Series.mode),
    Lat=('Lat', np.mean),
    Long_=('Long_', np.mean),
    Confirmed=('Confirmed', sum),
    Deaths=('Deaths', sum),
    Recovered=('Recovered', sum),
    Active=('Active', sum),
    Incidence_Rate=('Incidence_Rate', np.mean),
    CaseFatality_Ratio=('Case-Fatality_Ratio', np.mean)
).reset_index()

df2 = df2[df2.Province_State != 'Recovered']
df2 = df2[df2.Province_State != 'Grand Princess']
df2 = df2[df2.Province_State != 'Diamond Princess']
df2.rename(columns={'CaseFatality_Ratio':'Case-Fatality_Ratio'},inplace=True)

df2.insert(1,"Country_Region","US")
df2.insert(9,"Combined_Key","")
df2.to_csv('1.4.csv',index=False)

df_Location = df_Location[df_Location.Country_Region != 'US']
df_Location_new=df_Location.append(df2)
df_Location_new.to_csv('df_Location_new.csv',index=False)
df_Cases=pd.read_csv('processed_individual_cases_Sep20th2020.csv')

df_Location_new.rename(columns={'Province_State':'province', 'Country_Region':'country'},inplace = True)
df_Cases['country'] = df_Cases['country'].replace(['United States'],'US')
df_Combined = pd.merge(df_Cases,df_Location_new)  
df_Combined.drop(columns=['additional_information','Lat', 'Long_','source','Last_Update','Combined_Key'],inplace=True)

print(df_Combined)
print(df_Cases)
df_Combined.to_csv('Combined.csv',index=False)


