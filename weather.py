#I am creating a weather that will allow the user to input the city and number of days they would like to see the forecast for.
#From the user input the app will print out selected weather information and sunset/sunrise times useful for Muslims
#who are fasting during Ramadan. I have also given the user the choice of inputting a number between 1 and 5 to see
#the weather forecast

#you can make requests to the url using this module
import requests

# you can interpret date/time using this module
import datetime

#prints data in a format readable to us humans
import pprint


# User input for city will be capitlised on first letter
city_name = input("Enter city name: ")
city_name = city_name.capitalize()

#string input but if its a digit, we will recognise it as an int
number_of_days_str = input('Number of days to forecast: ')
if not number_of_days_str.isdigit():
    print('Not a number. Please enter the number of days to forecast')
else:
    number_of_days = int(number_of_days_str)
#API key and endpoint
API_key = 'd9c69cf0157a7552cca56dabf8ec401b'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

#making a request to the API
response = requests.get(url)
if response.status_code == 200:
    #this will check if the API is giving access as it should
    #print('OK')
    data = response.json()

    #Use pretty print to see all the data for the city in a readable format
    #pprint.pprint(data)
    print(f'Today in {city_name} you can expect', data['weather'][0]['description'])
    print('A high of', (round(data['main']['temp_max'], )) ,'and a low of' , (round(data['main']['temp_min'], )))
#else:
    #print('Cannot retrieve data:', response.status_code)

#booleans and if...else to give output to user depending on weather temp
    feels_like=(round(data['main']['feels_like'], ))
    #print(feels_like)
    if feels_like < 10:
            print('Pack your scarf and gloves')
    elif 10 <=feels_like <= 20:
            print('Today is an okay day')
    else:
            print('It will be a warm day')
else:
    print(f'{city_name} not a valid city name')
    exit()
print('=======================================================================')
def sun_info(sunrise_converted, sunset_converted):
    print('Ramadan has started, let\'s find out what time the sun will rise and set today')
    print('The sun will rise at', sunrise_time)
    print('The sun will set at', sunset_time)

#grabs the data from the right place in the dictionary
sunrise_info = data['sys']['sunrise']
sunset_info = data['sys']['sunset']

#this does the conversion from the strange format in to a readable one
sunrise_converted = datetime.datetime.fromtimestamp(sunrise_info)
sunset_converted = datetime.datetime.fromtimestamp(sunset_info)

#string slicing as we only need a section of this data (the time)
sunrise_time = str(sunrise_converted)[11:16]
sunset_time = str(sunset_converted)[11:16]

#calls the function
sun_info(sunrise_converted, sunset_converted)

#breaks up the output a little bit for readability
print('===============================================================================')
print(f'===========Let\'s look at the weather forecast for {city_name} ============')


if number_of_days in range(1, 6):

    # forecast URL with the API key and input from the user
    url_fcast = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&cnt={number_of_days}&appid={API_key}&units=metric'

    # Send the request to the forecast endpoint
    response = requests.get(url_fcast)
    # Checking if the request was successful)
    if response.status_code == 200:
        # Parse the response as JSON
        data = response.json()
        # Print the forecast data in readable format to check the data
        #pp.pprint(data)
        daily_temp = []
        for temperature in data['list']:
            one_day = round(temperature['main']['temp'], )
            daily_temp.append(one_day)
        for i in range(number_of_days):
            print(f'Temperature for day {i + 1} in {city_name} will be {daily_temp[i]} degrees')
    else:
        print('Reason for failure:', response.status_code)
else:
    print('You must enter a number between 1 and 5.')
#project ends here