#! python3
# getWeather.py - Prints the weather for a location from the command line.

def getWeather(zip_code, city, country):
    """This function retrieves weather from OpenWeatherMap.org's API for a given city or zip code.
    This can be set up to retrieve current weather and/or a weather forecast."""
    import json, requests
    
    # *****START CODE FROM ATBS*****
    # import sys

    # Compute location from command line arguments.
    #if len(sys.argv) < 2:
    #    print('Usage: quickWeather.py location')
    #    sys.exit()

    # location = ' '.join(sys.argv[1:])
    # *****END CODE FROM ATBS*****
    
    # Download the JSON data from OpenWeatherMap.org's API.
    # Code from ATBS: url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)

    # To call API, use this URL: http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={APIKEY}
    # My API key: 5482b2a3705d25d98c10f9364b53caee
    my_api_key = '5482b2a3705d25d98c10f9364b53caee'
    # url = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=5482b2a3705d25d98c10f9364b53caee'
    url = 'http://api.openweathermap.org/data/2.5/weather?zip=%s&APPID=%s' % (zip_code, my_api_key)

    # To api call by city name
    # api.openweathermap.org/data/2.5/weather?q={city name}
    # api.openweathermap.org/data/2.5/weather?q={city name},{country code}
    # Examples:
    # api.openweathermap.org/data/2.5/weather?q=London 
    # api.openweathermap.org/data/2.5/weather?q=London,uk

    # To api call by zip code
    # api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}
    # Example:
    # api.openweathermap.org/data/2.5/weather?zip=94040,us
    # Please note if country is not specified then the search works for USA as a default.

    response = requests.get(url)
    response.raise_for_status()

    # Load JSON data into a Python variable.
    weatherData = json.loads(response.text)
    # Print weather descriptions.
    # print(json.dumps(r.json(), indent=2))
    print('Using json.dumps... ')
    print(json.dumps(response.json(), indent=2))
    print()
    print('Using response.json... ')
    print(response.json())
    
    # *****START CODE FROM ATBS*****
    # Below code is from ATBS, but didn't work when I ran it on Cloud9, perhaps because I mistakenly ran it using python2
    # w = weatherData['list']
    # print('Current weather in %s: ' % (zip_code))
    # print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
    # print()
    # print('Tomorrow: ')
    # print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
    # print()
    # print('Day after tomorrow: ')
    # print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
    # *****END CODE FROM ATBS*****
    
if __name__ == '__main__':
    zip_code = 77494
    city = 'Katy'
    country = 'us'
    getWeather(zip_code, city, country)
    