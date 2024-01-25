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
listing = 'https://www.zillow.com/fresno-ca-93722/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds' \
                  '%22%3A%7B%22north%22%3A36.864590586806386%2C%22south%22%3A36.740198069604425%2C%22east%22%3A-119' \
                  '.81193359997557%2C%22west%22%3A-119.9590474000244%7D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value' \
                  '%22%3A%22globalrelevanceex%22%7D%2C%22price%22%3A%7B%22min%22%3A0%7D%2C%22mp%22%3A%7B%22min%22%3A0%7D' \
                  '%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B' \
                  '%22value%22%3Afalse%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D' \
                  '%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%2C%22regionSelection%22%3A%5B%7B%22regionId%22' \
                  '%3A97431%2C%22regionType%22%3A7%7D%5D%2C%22pagination%22%3A%7B%7D%7D'
# df1 = pd.DataFrame()
# pages = 0
# zipCodes = ZillowZipcodeUrl()
# for zipcode in zipCodes:
#     pages = ZillowListings()
#     df1 = ZillowListings(zipcode, 1)
#     df1 = ZillowSetColumns(df1)

# SaveToDatabase(df1)
# for i in temp['results']:
#     print(i)


# for zipCode in zipCodes:
#     df = get_listings(zipCode)
#     df = ZillowSetColumns(df)
#     ZillowSetColumnTypes(df)
#     df1 = pd.concat([df1, df], axis=0)
#     df1.reset_index(drop=True, inplace=True)
# SaveToDatabase(df1)

# df1 = ZillowSetColumns(df1)
# ZillowSetColumnTypes(df1)
# df1 = monthly_cash_flow(df1, .07, 360, 100, .20)
# breakEven_df = breakEvenCashFlow(df1, .07)
# # breakEven_df.sort_values(by=['MonthlyCashFlow'])
# print(breakEven_df)

df = RealtorLocationListings('93720')
df = RealtorSetColumns(df)
RealtorSetColumnTypes(df)
print(df)
