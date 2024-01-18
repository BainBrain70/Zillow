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


def RedfinListing(listing_url):
    url = "https://redfin-com-data.p.rapidapi.com/property/detail"

    querystring = {f"url": {listing_url}}

    headers = {
        "X-RapidAPI-Key": "8c4d33ab1fmsh042342b8342f6f9p1a302djsnf9ae6918b4b9",
        "X-RapidAPI-Host": "redfin-com-data.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    # df = pd.json_normalize(response.json()['data'][
    #                            'gis?al=1&include_nearby_homes=true&market=sacramento&num_homes=350&ord=redfin'
    #                            '-recommended-asc&page_number=1&region_id=38891&region_type=2&sf=1,2,3,5,6,'
    #                            '7&start=0&status=9&uipt=1,2,3,4,5,6,7,8&v=8']['homes'])

    return response.json()


