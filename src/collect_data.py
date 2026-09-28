import pandas as pd
import requests
from io import StringIO

#NASA GISTEMP
TEMP_URL="https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv"
resp= requests.get(TEMP_URL, timeout=30)
resp.raise_for_status()

#this CVS has an extra row before the actual table header, so skiprows=1 skips it
temp_df=pd.read_csv(StringIO(resp.text), skiprows=1)

#we are only interested in the Year and J-D columns (the annual average January to December)
temp_df=temp_df[['Year', 'J-D']].rename(columns={'Year': 'year', 'J-D': 'temp_anomaly'})

#in this file, missing values are represented as "***" text rather than NaN.
#we force the column to numeric values, and anything that cannot be converted to a number becomes NaN.                                     
temp_df['temp_anomaly']=pd.to_numeric(temp_df['temp_anomaly'], errors='coerce')

#CO2 Mauna Loa Observatory
CO2_URL="https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_mlo.csv"
resp= requests.get(CO2_URL, timeout=30)
resp.raise_for_status()

#This file contains several comment lines at the beginning that start with "#".
#comment="#" tells pandas to automatically ignore all such lines.
co2_df=pd.read_csv(StringIO(resp.text), comment='#')
co2_df=co2_df[['year','mean']].rename(columns={'year': 'year', 'mean': 'co2_ppm'})

#merge by year
merged=pd.merge(temp_df, co2_df, on='year', how='inner')
merged=merged.dropna()

print(f"\nFinal dataset: {len(merged)} rows")
print(f"Year range: {merged['year'].min()} - {merged['year'].max()}")
print(merged.head())
merged.to_csv("data/raw/temp_co2_merged.csv", index=False)
print("\nSaved to data/raw/temp_co2_merged.csv")