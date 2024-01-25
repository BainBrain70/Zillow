import requests
import pandas as pd


def get_listings(listing_url):
    url = "https://app.scrapeak.com/v1/scrapers/zillow/listing"

    querystring = {
        "api_key": 'ab8ddf03-94b5-4d52-a90e-3295c0c3dab3',
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


def RealtorUrlListings():
    import requests

    url = "https://us-real-estate-listings.p.rapidapi.com/v2/property"

    querystring = {
        "property_url": "https://www.realtor.com/realestateandhomes-detail/4666-E-Orleans-Ave_Fresno_CA_93702_M15563-75055?from=srp-list-card"}

    headers = {
        "X-RapidAPI-Key": "8c4d33ab1fmsh042342b8342f6f9p1a302djsnf9ae6918b4b9",
        "X-RapidAPI-Host": "us-real-estate-listings.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())


def RealtorLocationListings(location):
    df = pd.DataFrame()
    url = "https://us-real-estate-listings.p.rapidapi.com/for-sale"

    querystring = {"location": location, "offset": "0", "limit": "200"}

    headers = {
        "X-RapidAPI-Key": "8c4d33ab1fmsh042342b8342f6f9p1a302djsnf9ae6918b4b9",
        "X-RapidAPI-Host": "us-real-estate-listings.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    df = pd.json_normalize(response.json()['listings'])
    return df



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


def ZillowListings(listing_url, pageNumber):
    url = "https://zillow-working-api.p.rapidapi.com/search/byurl"

    querystring = {
        "url": listing_url,
        "page": pageNumber}

    headers = {
        "X-RapidAPI-Key": "8c4d33ab1fmsh042342b8342f6f9p1a302djsnf9ae6918b4b9",
        "X-RapidAPI-Host": "zillow-working-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    df = pd.json_normalize(response.json()['Results'])
    return df


def ZillowZipcodeUrl():
    Zillow93722 = 'https://zillow.com/fresno-ca-93722/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds' \
                  '%22%3A%7B%22north%22%3A36.871937850818554%2C%22south%22%3A36.73283815503686%2C%22east%22%3A-119' \
                  '.78077706005858%2C%22west%22%3A-119.9902039399414%7D%2C%22usersSearchTerm%22%3A%228153%20N%20Cedar' \
                  '%20Ave%20%23129%20Fresno%2C%20CA%2093720%22%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22' \
                  '%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22tow%22%3A%7B%22value%22' \
                  '%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C' \
                  '%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%7D%2C' \
                  '%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%2C%22regionSelection%22%3A%5B%7B%22regionId%22' \
                  '%3A97431%2C%22regionType%22%3A7%7D%5D%2C%22pagination%22%3A%7B%7D%7D'

    Zillow93720 = 'https://www.zillow.com/fresno-ca-93720/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C' \
                  '%22mapBounds%22%3A%7B%22north%22%3A36.89889711124698%2C%22south%22%3A36.829403367399564%2C%22east' \
                  '%22%3A-119.71074728002928%2C%22west%22%3A-119.81546071997069%7D%2C%22usersSearchTerm%22%3A%228153' \
                  '%20N%20Cedar%20Ave%20%23129%20Fresno%2C%20CA%2093720%22%2C%22filterState%22%3A%7B%22sort%22%3A%7B' \
                  '%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22tow%22%3A%7B' \
                  '%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22' \
                  '%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%7D' \
                  '%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%2C%22regionSelection%22%3A%5B%7B%22regionId%22' \
                  '%3A97429%2C%22regionType%22%3A7%7D%5D%2C%22pagination%22%3A%7B%7D%7D'

    Zillow93705 = 'https://www.zillow.com/fresno-ca-93705/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C' \
                  '%22mapBounds%22%3A%7B%22north%22%3A36.82125687406157%2C%22south%22%3A36.75169254968076%2C%22east' \
                  '%22%3A-119.7745407800293%2C%22west%22%3A-119.8792542199707%7D%2C%22usersSearchTerm%22%3A%228153' \
                  '%20N%20Cedar%20Ave%20%23129%20Fresno%2C%20CA%2093720%22%2C%22filterState%22%3A%7B%22sort%22%3A%7B' \
                  '%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22tow%22%3A%7B' \
                  '%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22' \
                  '%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%7D' \
                  '%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%2C%22regionSelection%22%3A%5B%7B%22regionId%22' \
                  '%3A97416%2C%22regionType%22%3A7%7D%5D%2C%22pagination%22%3A%7B%7D%7D'

    Zillow93711 = 'https://www.zillow.com/fresno-ca-93711/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C' \
                  '%22mapBounds%22%3A%7B%22north%22%3A36.907976289605614%2C%22south%22%3A36.76894213918674%2C%22east' \
                  '%22%3A-119.7256510600586%2C%22west%22%3A-119.93507793994141%7D%2C%22usersSearchTerm%22%3A%228153' \
                  '%20N%20Cedar%20Ave%20%23129%20Fresno%2C%20CA%2093720%22%2C%22filterState%22%3A%7B%22sort%22%3A%7B' \
                  '%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22tow%22%3A%7B' \
                  '%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22' \
                  '%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%7D' \
                  '%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%2C%22regionSelection%22%3A%5B%7B%22regionId%22' \
                  '%3A97422%2C%22regionType%22%3A7%7D%5D%2C%22pagination%22%3A%7B%7D%7D'

    Zillow93710 = 'https://www.zillow.com/fresno-ca-93710/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C' \
                  '%22mapBounds%22%3A%7B%22north%22%3A36.85422044243024%2C%22south%22%3A36.784686068675306%2C%22east' \
                  '%22%3A-119.7099347800293%2C%22west%22%3A-119.8146482199707%7D%2C%22usersSearchTerm%22%3A%228153' \
                  '%20N%20Cedar%20Ave%20%23129%20Fresno%2C%20CA%2093720%22%2C%22filterState%22%3A%7B%22sort%22%3A%7B' \
                  '%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22tow%22%3A%7B' \
                  '%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22' \
                  '%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%7D' \
                  '%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%2C%22regionSelection%22%3A%5B%7B%22regionId%22' \
                  '%3A97421%2C%22regionType%22%3A7%7D%5D%2C%22pagination%22%3A%7B%7D%7D'

    Zillow93728 = 'https://www.zillow.com/fresno-ca-93728/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C' \
                  '%22mapBounds%22%3A%7B%22north%22%3A36.7908501819575%2C%22south%22%3A36.72125825056633%2C%22east%22' \
                  '%3A-119.76504978002929%2C%22west%22%3A-119.8697632199707%7D%2C%22usersSearchTerm%22%3A%228153%20N' \
                  '%20Cedar%20Ave%20%23129%20Fresno%2C%20CA%2093720%22%2C%22filterState%22%3A%7B%22sort%22%3A%7B' \
                  '%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22tow%22%3A%7B' \
                  '%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22' \
                  '%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%7D' \
                  '%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%2C%22regionSelection%22%3A%5B%7B%22regionId%22' \
                  '%3A97436%2C%22regionType%22%3A7%7D%5D%2C%22pagination%22%3A%7B%7D%7D'

    Zillow93726 = 'https://www.zillow.com/fresno-ca-93726/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C' \
                  '%22mapBounds%22%3A%7B%22north%22%3A36.82770809522596%2C%22south%22%3A36.7581496305962%2C%22east%22' \
                  '%3A-119.70796928002929%2C%22west%22%3A-119.8126827199707%7D%2C%22usersSearchTerm%22%3A%228153%20N' \
                  '%20Cedar%20Ave%20%23129%20Fresno%2C%20CA%2093720%22%2C%22filterState%22%3A%7B%22sort%22%3A%7B' \
                  '%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22tow%22%3A%7B' \
                  '%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22' \
                  '%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%7D' \
                  '%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%2C%22regionSelection%22%3A%5B%7B%22regionId%22' \
                  '%3A97434%2C%22regionType%22%3A7%7D%5D%2C%22pagination%22%3A%7B%7D%7D'

    zipCodeUrls = [Zillow93722, Zillow93726, Zillow93728, Zillow93711, Zillow93710, Zillow93705, Zillow93720]

    return zipCodeUrls
