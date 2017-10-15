""" THis program generates a packing list after asking
some initial questions.
"""
import pandas as pd
import sqlite3


# TODO - Create initial questions list
# Gather initial info with questions
# Trip Purpose

print('Is this a business trip, personal trip, or mixed purpose?')
trip_purpose = input()

# Trip Length
print('How many days will you be gone?')
nbr_days = input()
print('How many nights will you be gone?')
nbr_nights = input()

# Weather
print('What is the temperature forecast for daytime?')
daytime_temp = input()
print('What is the temperature forecast for night/evenings?')
night_temp = input()
print('Will it be sunny? (y or n)')
sunny = input()
print('Will it rain? (y or n)')
rain = input()
print('Will it snow? (y or n)')
snow = input()

# Activities Planned
print('Will you swim? (y or n)')
swim = input()
print('Will you have a formal outing that will require a suit? (y or n)')
suit = input()
nbr_suits = 0
if suit == 'y':
    print('How many suits do you want to bring?')
    nbr_suits = input()
print('Will you have a dressy "go out" night? (y or n)')
go_out_night = input()
nbr_go_out_nights = 0
if go_out_night == 'y':
    print('How many go-out nights will you have?')
    nbr_go_out_nights = input()
print('Will you be shopping?')
shopping = input()
print('Will you be taking high quality photos?')
DSLR = input()
if DSLR == 'y':
    # Add additional questions for camera kit here
    pass

# Travel Details
print('Are you flying or driving?')
transport_mode = input()
flight_time = 0
drive_time = 0
if transport_mode == 'flying':
    print('How long is your flight? (in hours)')
    flight_time = input()
elif transport_mode == 'driving':
    print('How long is your drive? (in hours)')
    drive_time = input()
else: print('You did not enter a drive/flight time\n')

print('Is this an international trip?')
intl_trip = input()

# Print a trip summary to the screen
print('========== TRIP SUMMARY ==========', end='\n')
print('Trip Purpose: ', trip_purpose, end='\n')
print('Number of Days: ', nbr_days, end='\n')
print('Number of Nights: ', nbr_nights, end='\n')
print('Daytime Temperature: ', daytime_temp, end='\n')
print('Night time Temperature: ', night_temp, end='\n')
print('Sunny? ', sunny, end='\n')
print('Rainy? ', rain, end='\n')
print('Snow? ', snow, end='\n')
print('Swim? ', swim, end='\n')
print('Suit? ', suit, end='\n')
print('Number of suits: ', nbr_suits, end='\n')
print('Go-out night(s)? ', go_out_night, end='\n')
print('How many go-out nights? ', nbr_go_out_nights, end='\n')
print('Shopping? ', shopping, end='\n')
print('Bring DSLR? ', DSLR, end='\n')
print('Travel mode: ', transport_mode, end='\n')
print('Flight time: ', flight_time, end='\n')
print('Drive time: ', drive_time, end='\n')
print('International trip? ', intl_trip, end='\n')


# TODO - Instantiate the standard packing list dataframe from csv file
data_types = ['text','int','bool','text','text','real','text','text']
packing_list = pd.read_csv('''/Users/RAB-Capital/Dropbox/111PackingLists
                            /StandardOneBagPackingList.csv''')

# TODO - Set item names as index for the dataframe (use .set_index, inplace=True?)
packing_list.set_index('Item', inplace=True)

# TODO - Set the data types for the columns
# Ignore dtypes for now. This may not even be necessary at all.

# TODO - Learn how to update data in a dataframe.
# use df.loc[index, column]

# TODO - "Calculate" and select items based on the answers to the questions.





# TODO - Export the packing list to text file, Excel, or Evernote
