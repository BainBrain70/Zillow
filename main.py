import pandas as pd
import numpy as np
# import plotly.express as px
import requests
import warnings
from APIfuctions import *
from RentalData import *
from Database import *

# settings
warnings.filterwarnings("ignore")
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)
pd.set_option("display.max_rows", None)
pd.set_option('display.width', 1000)
#######################################################################################################

list1 = ['93710', '93728']  # ['93722', '93705', '93711', '93720']

# for i in list:
#     url = f'https://www.redfin.com/zipcode/{i}'
#     df = RedfinListing(url)
#     df = RedfinSetColumns(df)
#     RedfinSetColumnTypes(df)
#     SaveToDatabase(df)
#     df.drop(df.index, inplace=True)


# temp = pd.DataFrame()
# for i in list1:
#     url = f'https://www.redfin.com/zipcode/{i}'
#     df = RedfinListing(url)
#     df = RedfinSetColumns(df)
#     RedfinSetColumnTypes(df)
#     temp = pd.concat([temp, df], axis=0)
# print(temp)

# temp = RedfinListingCity("https://www.redfin.com/city/6904/CA/Fresno")
# temp = RedfinSetColumns(temp)
# RedfinSetColumnTypes(temp)
# print(temp)

df1 = pd.DataFrame()
# zipCodes = ZillowZipcodeUrl()
# for zipCode in zipCodes:
#     df = get_listings(zipCode)
#     df = ZillowSetColumns(df)
#     ZillowSetColumnTypes(df)
#     df1 = pd.concat([df1, df], axis=0)
#     df1.reset_index(drop=True, inplace=True)
df1 = pd.read_csv("C:\\Users\\cbain\\Desktop\\listing.csv")
df1 = ZillowSetColumns(df1)
ZillowSetColumnTypes(df1)
df1 = monthly_cash_flow(df1, .07, 360, 100, .20)
breakEven_df = breakEvenCashFlow(df1, .07)
# breakEven_df.sort_values(by=['MonthlyCashFlow'])
print(breakEven_df)
