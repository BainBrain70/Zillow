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
listing_url = "https://www.zillow.com/fresno-ca/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22" \
              "%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A37.00480742129036%2C%22south%22%3A36.49093116751504%2C" \
              "%22east%22%3A-119.42774904980469%2C%22west%22%3A-120.33274782910156%7D%2C%22filterState%22%3A%7B" \
              "%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22price%22%3A%7B%22min%22%3A0%2C%22max%22" \
              "%3A400000%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A2010%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D" \
              "%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B" \
              "%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse" \
              "%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A18203%2C" \
              "%22regionType%22%3A6%7D%5D%7D "
# listing_response = get_listings('c99d5365-e52d-4591-8805-5529e2cc28f9', listing_url)
#
# # Parce the JSON response
# df_listings1 = pd.json_normalize(listing_response.json()["data"]["cat1"]["searchResults"]["mapResults"])
# # print("Number of rows:", len(df_listings))
# # print("Number of columns:", len(df_listings.columns))
# print(df_listings1)


# df = get_listings(listing_url)
# df = ZillowSetColumns(df)
# ZillowSetColumnTypes(df)
list = ['93722', '93705', '93711', '93720', '93710', '93728']

# for i in list:
#     url = f'https://www.redfin.com/zipcode/{i}'
#     df = RedfinListing(url)
#     df = RedfinSetColumns(df)
#     RedfinSetColumnTypes(df)
#     SaveToDatabase(df)
#     df.drop(df.index, inplace=True)
#
# df = ReadFromDatabase()
# print(df)

temp = RedfinListing('https://www.redfin.com/zipcode/93722')
for i in temp['data']:
    print(i)
# df = pd.json_normalize(temp['data']['gis?al=1&include_nearby_homes=true&market=sacramento&num_homes=350&ord=redfin-recommended-asc' \
#                     '&page_number=1&region_id=38882&region_type=2&sf=1,2,3,5,6,7&start=0&status=9&uipt=1,2,3,4,5,6,7,' \
#                     '8&v=8']['homes'])
# print(df)
###############################################################################################################################################################



# saveToDatabase(df)
#ReadFromDatabase()
