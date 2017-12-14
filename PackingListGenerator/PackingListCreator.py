""" THis program generates a packing list after asking
some initial questions.
Author: Reggie Brown
Date: November 2016
"""
import pandas as pd
import os


# TODO - Create initial questions list

def questionnaire():

    """ This function gathers initial info with questions
    and prints the output to the screen."""

    # Name the trip so you can save the packing lists by the trip name.
    print('What name would you like to call this trip?')
    tripname = input()

    # Trip Purpose

    print('Is this a business trip, personal trip, or mixed purpose?')
    purpose = input()

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
    dslr = input()
    if dslr == 'y':
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
    # This is optional
    print('========== TRIP SUMMARY ==========', end='\n')
    print('Trip Name: ' + tripname, end='\n')
    print('Trip Purpose: ' + purpose, end='\n')
    print('Number of Days: ' + nbr_days, end='\n')
    print('Number of Nights: ' + nbr_nights, end='\n')
    print('Daytime Temperature: ' + daytime_temp, end='\n')
    print('Night time Temperature: ' + night_temp, end='\n')
    print('Sunny? ' + sunny, end='\n')
    print('Rainy? ' + rain, end='\n')
    print('Snow? ' + snow, end='\n')
    print('Swim? ' + swim, end='\n')
    print('Suit? ' + suit, end='\n')
    print('Number of suits: ' + nbr_suits, end='\n')
    print('Go-out night(s)? ' + go_out_night, end='\n')
    print('How many go-out nights? ' + nbr_go_out_nights, end='\n')
    print('Shopping? ' + shopping, end='\n')
    print('Bring DSLR? ' + DSLR, end='\n')
    print('Travel mode: ' + transport_mode, end='\n')
    print('Flight time: ' + flight_time, end='\n')
    print('Drive time: ' + drive_time, end='\n')
    print('International trip? ' + intl_trip, end='\n')

    # Return these values as a dictionary instead of a tuple because
    # a dictionary allows me to look up the values with a suitable keyword.
    # This is useful since I'm going to lose the variable names
    # when the function is returned.
    return {"Trip Name": tripname, "Trip Purpose": purpose,
            "Nbr of Days": nbr_days, "Nbr of Nights": nbr_nights,
            "Daytime Temp": daytime_temp, "Night Temp": night_temp,
            "Sunny": sunny, "Rain": rain, "Snow": snow,
            "Swim": swim, "Suit": suit, "Nbr of Suits": nbr_suits,
            "Go Out Night": go_out_night, "Nbr of go-out nights": nbr_go_out_nights,
            "Shopping": shopping,
            "DSLR": dslr,
            "Transportation Mode": transport_mode,
            "Flight Time": flight_time, "Drive Time": drive_time,
            "International Trip": intl_trip}


def generatePackList(tripName, nbrDays, temp):
    """ This function "Calculates" and selects items based on the answers
    to the questionnaire function."""

    # Store standard packing list file location in a variable so it can be changed if desired.
    path = '/Users/RAB-Capital/Dropbox/111PackingLists/'
    standardPackingListFile = '''/Users/RAB-Capital/Dropbox/111PackingLists
                                /StandardOneBagPackingList.csv'''
    # Instantiate the standard packing list datafrome from csv file
    packingListdf = pd.read_csv(standardPackingListFile)
    # Set item names as index for the dataframe
    packingListdf.set_index('Item', inplace=True)
    # Ignore data types (dtypes) for the columns for now. May not be necessary at all.
    # To update the dataframe values, use df.loc[index, column]

    tops = {'shirts': 0, 'long sleeve shirts': 0}
    bottoms = {'shorts': 0, 'pants': 0}
    # Select number of shirts
    # One shirt for each day up to five max
    if nbrDays <= 5:
        tops['shirts'] = nbrDays
    else:
        tops['shirts'] = 5

    # Select number of bottoms
    # One pair of bottoms for every two days, up to 3 max
    if temp == 'Warm':
        if nbrDays <= 5:
            bottoms['shorts'] = ((nbrDays // 2) + (nbrDays % 2)) # rounds up for odd nbr of days
        else:
            bottoms['shorts'] = 3
    if temp == 'Cold':
        if nbrDays <= 5:
            bottoms['pants'] = ((nbrDays // 2) + (nbrDays % 2)) # rounds up for odd nbr of days
        else:
            bottoms['pants'] = 3

    # Save generated packing list as a new csv file.
    packingListdf.to_csv(path + tripName + '.csv')

# TODO - Export the packing list to csv, text file, Excel, or Evernote
def outputPackingList(tripName, generatedPackList):
    packList = open(tripName + '.txt', 'w')
    packing_list = pd.read_csv(generatedPackList)
    packList.write('     Qty     Item\n')
    packList.write('[ ]  ' + '     ' + packing_list.loc[1, 1] + '     ' + packing_list.loc[1, 2])

