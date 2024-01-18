import pandas as pd
import numpy as np
import plotly.express as px
import requests
import warnings
from APIfuctions import *
from RentalData import *
from Database import *
from sqlalchemy import create_engine
# settings
warnings.filterwarnings("ignore")
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)
pd.set_option("display.max_rows", None)
pd.set_option('display.width', 1000)
#######################################################################################################



########################################### Call Zillow API ##################################################################################
# #
# listing_url = "https://www.zillow.com/fresno-ca/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22" \
#               "%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A37.00480742129036%2C%22south%22%3A36.49093116751504%2C" \
#               "%22east%22%3A-119.42774904980469%2C%22west%22%3A-120.33274782910156%7D%2C%22filterState%22%3A%7B" \
#               "%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22price%22%3A%7B%22min%22%3A0%2C%22max%22" \
#               "%3A400000%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A2010%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D" \
#               "%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B" \
#               "%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse" \
#               "%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A18203%2C" \
#               "%22regionType%22%3A6%7D%5D%7D "
# listing_response = get_listings('c99d5365-e52d-4591-8805-5529e2cc28f9', listing_url)
#
# # Parce the JSON response
# df_listings1 = pd.json_normalize(listing_response.json()["data"]["cat1"]["searchResults"]["mapResults"])
# # print("Number of rows:", len(df_listings))
# # print("Number of columns:", len(df_listings.columns))
# print(df_listings1)
#
# # Save the listing to a CSV file
# df_listings.to_csv(r'C:\Users\BainB\Desktop\listing.csv')
# # print(df_listings)
# Read dataframe from a csv file
# df = pd.DataFrame()
df_listings1 = pd.read_csv(r'C:\Users\BainB\Desktop\listing.csv')
# df_listings3 = realtorListings()
# df_listings3 = df_listings3.json()
# for i in df_listings3['listings']:
#     print(i)
# df = pd.json_normalize(df_listings3['listings'])
# print(df)

###############################################################################################################################################################


# Rename columns






# Assign dataframe from csv to new dataframe
# saveToDatabase(df)
#ReadFromDatabase()
# # Calculate the monthly cash flow for each property in the dataframe
# df = monthly_cash_flow(df, .065, 360, 1000, .20)
#
# df1 = breakEvenCashFlow(df, .065)
# df1['Rent/Price'] = round(df1['RentEstimate'] / df1['Price'] * 100, 2)
# df1.sort_values(by=['Rent/Price'], inplace=True, ascending=False)
# print(df1)
#
# df2 = pd.DataFrame()
# df2 = df1.loc[[9, 8, 50, 2, 11, 3, 7, 20, 192, 57, 35, 82, 60, 84, 138, 93, 31, 171, 67, 71, 23, 40, 28, 110, 66, 42, 44, 48, 104], \
#               ['Address', 'Zipcode', 'Price', 'RentEstimate', 'MonthlyCashFlow', 'DownPaymentAmount']]
# df2['Tax/Insurance'] = round(df2['Price'] * .0125 / 12 + 100, 2)
# df2['Rent/Price'] = round(df2['RentEstimate'] / df2['Price'] * 100, 2)
# df2.reset_index(inplace=True)
# df2.drop(['index'], axis=1, inplace=True)


# print(df2)
# print('Total Down Payment: ' + str(round(df2['DownPaymentAmount'].sum(), 2)) + '\n')
# print('Total Monthly Cash Flow: ' + str(round(df2['MonthlyCashFlow'].sum(), 2)) + '\n')
# print('Total House Value: ' + str(round(df2['Price'].sum(), 2)) + '\n')
