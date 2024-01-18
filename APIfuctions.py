import requests
import pandas as pd


def get_listings(listing_url):
    url = "https://app.scrapeak.com/v1/scrapers/zillow/listing"

    querystring = {
        "api_key": 'c99d5365-e52d-4591-8805-5529e2cc28f9',
        "url": listing_url
    }

    response = requests.request("GET", url, params=querystring)
    df = pd.json_normalize(response.json()["data"]["cat1"]["searchResults"]["mapResults"])
    return df

def get_property_detail(api_key, zpid):
    url = "https://app.scrapeak.com/v1/scrapers/zillow/property"

    querystring = {
        "api_key": api_key,
        "zpid": zpid
    }
    return requests.request("GET", url, params=querystring)


def get_zpid(api_key, street, city, state, zip_code=None):
    url = "https://app.scrapeak.com/v1/scrapers/zillow/zpidByAddress"

    querystring = {
        "api_key": api_key,
        "street": street,
        "city": city,
        "state": state,
        "zip_code": zip_code
    }

    return requests.request("GET", url, params=querystring)


def rapidAPI_Zipcode():
    url = "https://us-real-estate.p.rapidapi.com/v2/for-sale-by-zipcode"

    querystring = {"zipcode": "93722", "offset": "0", "limit": "50"}

    headers = {
        "X-RapidAPI-Key": "8c4d33ab1fmsh042342b8342f6f9p1a302djsnf9ae6918b4b9",
        "X-RapidAPI-Host": "us-real-estate.p.rapidapi.com"
    }

    return requests.get(url, headers=headers, params=querystring)


def rapidAPI_City():
    url = "https://us-real-estate.p.rapidapi.com/v3/for-sale"

    querystring = {"state_code": "CA", "city": "Fresno", "sort": "newest", "offset": "0", "limit": "50"}

    headers = {
        "X-RapidAPI-Key": "8c4d33ab1fmsh042342b8342f6f9p1a302djsnf9ae6918b4b9",
        "X-RapidAPI-Host": "us-real-estate.p.rapidapi.com"
    }

    return requests.get(url, headers=headers, params=querystring)


def realtorListings():

    url = "https://us-real-estate-listings.p.rapidapi.com/for-sale"

    querystring = {"location": "Fresno, CA", "offset": "0", "limit": "1"}

    headers = {
        "X-RapidAPI-Key": "8c4d33ab1fmsh042342b8342f6f9p1a302djsnf9ae6918b4b9",
        "X-RapidAPI-Host": "us-real-estate-listings.p.rapidapi.com"
    }

    return requests.get(url, headers=headers, params=querystring)


def RedfinListingCity(listing_url):
    url = "https://redfin-com-data.p.rapidapi.com/property/search-url"

    querystring = {"url": listing_url}

    headers = {
        "X-RapidAPI-Key": "8c4d33ab1fmsh042342b8342f6f9p1a302djsnf9ae6918b4b9",
        "X-RapidAPI-Host": "redfin-com-data.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)

    df = pd.json_normalize(response.json()['data']['homes'])
    return df


def RedfinListingZipcode(listing_url):
    url = "https://redfin-com-data.p.rapidapi.com/property/search-url"

    querystring = {"url": listing_url}

    headers = {
        "X-RapidAPI-Key": "8c4d33ab1fmsh042342b8342f6f9p1a302djsnf9ae6918b4b9",
        "X-RapidAPI-Host": "redfin-com-data.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    for key in response.json()['data']:
        if key[:5] == 'gis?a':
            start_index = key.find("&region_id=") + len("&region_id=")
            end_index = key.find("&", start_index)
            region_id = key[start_index:end_index]
            df = pd.json_normalize(response.json()['data'][key]['homes'])
            return df


def ZillowZipcodeUrl():
    Zillow93722 = 'https://www.zillow.com/fresno-ca-93722/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds' \
                  '%22%3A%7B%22north%22%3A36.864590586806386%2C%22south%22%3A36.740198069604425%2C%22east%22%3A-119' \
                  '.81193359997557%2C%22west%22%3A-119.9590474000244%7D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value' \
                  '%22%3A%22globalrelevanceex%22%7D%2C%22price%22%3A%7B%22min%22%3A0%7D%2C%22mp%22%3A%7B%22min%22%3A0%7D' \
                  '%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B' \
                  '%22value%22%3Afalse%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D' \
                  '%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%2C%22regionSelection%22%3A%5B%7B%22regionId%22' \
                  '%3A97431%2C%22regionType%22%3A7%7D%5D%2C%22pagination%22%3A%7B%7D%7D'

    Zillow93720 = 'https://www.zillow.com/fresno-ca-93720/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds' \
                  '%22%3A%7B%22north%22%3A36.89522486438987%2C%22south%22%3A36.83307877889589%2C%22east%22%3A-119' \
                  '.72632554998778%2C%22west%22%3A-119.79988245001219%7D%2C%22filterState%22%3A%7B%22sort%22%3A%7B' \
                  '%22value%22%3A%22globalrelevanceex%22%7D%2C%22price%22%3A%7B%22min%22%3A0%7D%2C%22mp%22%3A%7B%22min%22' \
                  '%3A0%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22' \
                  '%3A%7B%22value%22%3Afalse%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22manu%22%3A%7B%22value%22' \
                  '%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A14%2C%22regionSelection%22%3A%5B%7B' \
                  '%22regionId%22%3A97429%2C%22regionType%22%3A7%7D%5D%2C%22pagination%22%3A%7B%7D%7D'

    Zillow93705 = 'https://www.zillow.com/fresno-ca-93705/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds' \
                  '%22%3A%7B%22north%22%3A36.81758089466494%2C%22south%22%3A36.75537169120043%2C%22east%22%3A-119' \
                  '.7901190499878%2C%22west%22%3A-119.86367595001221%7D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value' \
                  '%22%3A%22globalrelevanceex%22%7D%2C%22price%22%3A%7B%22min%22%3A0%7D%2C%22mp%22%3A%7B%22min%22%3A0%7D' \
                  '%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B' \
                  '%22value%22%3Afalse%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D' \
                  '%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A14%2C%22regionSelection%22%3A%5B%7B%22regionId%22' \
                  '%3A97416%2C%22regionType%22%3A7%7D%5D%2C%22pagination%22%3A%7B%7D%7D'

    Zillow93711 = 'https://www.zillow.com/fresno-ca-93711/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds' \
                  '%22%3A%7B%22north%22%3A36.900632493021114%2C%22south%22%3A36.77629859100323%2C%22east%22%3A-119' \
                  '.75680759997559%2C%22west%22%3A-119.90392140002442%7D%2C%22filterState%22%3A%7B%22sort%22%3A%7B' \
                  '%22value%22%3A%22globalrelevanceex%22%7D%2C%22price%22%3A%7B%22min%22%3A0%7D%2C%22mp%22%3A%7B%22min%22' \
                  '%3A0%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22' \
                  '%3A%7B%22value%22%3Afalse%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22manu%22%3A%7B%22value%22' \
                  '%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%2C%22regionSelection%22%3A%5B%7B' \
                  '%22regionId%22%3A97422%2C%22regionType%22%3A7%7D%5D%2C%22pagination%22%3A%7B%7D%7D'

    Zillow93710 = 'https://www.zillow.com/fresno-ca-93710/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds' \
                  '%22%3A%7B%22north%22%3A36.85054604692661%2C%22south%22%3A36.78836362737308%2C%22east%22%3A-119' \
                  '.7255130499878%2C%22west%22%3A-119.79906995001221%7D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value' \
                  '%22%3A%22globalrelevanceex%22%7D%2C%22price%22%3A%7B%22min%22%3A0%7D%2C%22mp%22%3A%7B%22min%22%3A0%7D' \
                  '%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B' \
                  '%22value%22%3Afalse%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D' \
                  '%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A14%2C%22regionSelection%22%3A%5B%7B%22regionId%22' \
                  '%3A97421%2C%22regionType%22%3A7%7D%5D%2C%22pagination%22%3A%7B%7D%7D'

    Zillow93728 = 'https://www.zillow.com/fresno-ca-93728/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds' \
                  '%22%3A%7B%22north%22%3A36.78717274260414%2C%22south%22%3A36.72493885105098%2C%22east%22%3A-119' \
                  '.78062804998778%2C%22west%22%3A-119.8541849500122%7D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value' \
                  '%22%3A%22globalrelevanceex%22%7D%2C%22price%22%3A%7B%22min%22%3A0%7D%2C%22mp%22%3A%7B%22min%22%3A0%7D' \
                  '%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B' \
                  '%22value%22%3Afalse%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D' \
                  '%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A14%2C%22regionSelection%22%3A%5B%7B%22regionId%22' \
                  '%3A97436%2C%22regionType%22%3A7%7D%5D%2C%22pagination%22%3A%7B%7D%7D'

    Zillow93726 = 'https://www.zillow.com/fresno-ca-93726/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds' \
                  '%22%3A%7B%22north%22%3A36.82403242571349%2C%22south%22%3A36.76182846244164%2C%22east%22%3A-119' \
                  '.72354754998779%2C%22west%22%3A-119.7971044500122%7D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value' \
                  '%22%3A%22globalrelevanceex%22%7D%2C%22price%22%3A%7B%22min%22%3A0%7D%2C%22mp%22%3A%7B%22min%22%3A0%7D' \
                  '%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B' \
                  '%22value%22%3Afalse%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D' \
                  '%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A14%2C%22regionSelection%22%3A%5B%7B%22regionId%22' \
                  '%3A97434%2C%22regionType%22%3A7%7D%5D%2C%22pagination%22%3A%7B%7D%7D'

    zipCodeUrls = [Zillow93722, Zillow93726, Zillow93728, Zillow93711, Zillow93710, Zillow93705, Zillow93720]

    return zipCodeUrls
