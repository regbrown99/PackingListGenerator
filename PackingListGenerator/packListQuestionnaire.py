#! /usr/bin/python3
# packListQuestionnaire.py - Questionnaire function for packingListGenerator

def questionnaire():
    """ This function gathers initial info with questions
    and prints the output to the screen.
    Inputs: None
    Outputs: all variables captured by the answers to the questions"""

    def str2bool(string):
        "This function translates an answer to a boolean value."
        yesAnswer = ['y', 'yes', 'true']
        noAnswer = ['n', 'no', 'false']
        if string.lower() in yesAnswer:
            return True
        elif string.lower() in noAnswer:
            return False
        else:
            raise Exception('Invalid answer.')

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
    print('What is the temperature forecast for daytime? (hot, warm, cool, or cold)')
    daytime_temp = input()
    print('What is the temperature forecast for night/evenings? (hot, warm, cool, or cold)')
    night_temp = input()
    print('Will it be sunny? (y or n)')
    sunny = input()
    sunny = str2bool(sunny)
    print('Will it rain? (y or n)')
    rain = input()
    rain = str2bool(rain)
    print('Will it snow? (y or n)')
    snow = input()
    snow = str2bool(snow)

    # Activities Planned
    print('Will you swim? (y or n)')
    swim = input()
    swim = str2bool(swim)

    print('Will you have a formal outing that will require a suit? (y or n)')
    suit = input()
    suit = str2bool(suit)
    if suit == False:
        nbr_suits = 0
    elif suit == True:
        print('How many suits do you want to bring?')
        nbr_suits = input()

    print('Will you have a dressy "go out" night? (y or n)')
    go_out_night = input()
    go_out_night = str2bool(go_out_night)
    if go_out_night == False:
        nbr_go_out_nights = 0
    if go_out_night == True:
        print('How many go-out nights will you have?')
        nbr_go_out_nights = input()

    print('Will you be shopping?')
    shopping = input()
    shopping = str2bool(shopping)

    print('Will you be taking high quality photos?')
    dslr = input()
    dslr = str2bool(dslr)
    if dslr == True:
        # Add additional questions for camera kit here
        pass

    # Travel Details
    print('Are you flying or driving?')
    transport_mode = input()
    flight_time = 0
    drive_time = 0
    if transport_mode.lower() == 'flying':
        print('How long is your flight? (in hours)')
        flight_time = input()
    elif transport_mode == 'driving':
        print('How long is your drive? (in hours)')
        drive_time = input()
    else:
        print('You did not enter a drive/flight time.\n')

    print('Is this an international trip?')
    intl_trip = input()
    intl_trip = str2bool(intl_trip)

    
    # Return these values as a dictionary instead of a tuple because
    # a dictionary allows me to look up the values with a suitable keyword.
    # This is useful since I'm going to lose the variable names
    # when the function is returned.
    
    tripProfileDict = {"Trip Name": tripname, "Trip Purpose": purpose,
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
    
    return tripProfileDict


def tripSummaryToScreen(tripProfileDict):
    """
    This function prints a Trip Profile Summary to the screen.
    Input: Trip Profile (as a dictionary)
    Output: Prints a Trip Profile Summary to the screen
    """
    print('TRIP SUMMARY')
    print('Trip Name: ' + tripProfileDict["Trip Name"])
    print('Trip Purpose: ' + tripProfileDict["Trip Purpose"])
    print('Number of Days: ' + tripProfileDict["Nbr of Days"])
    print('Number of Nights: ' + tripProfileDict["Nbr of Nights"])
    print('Daytime Temperature: ' + tripProfileDict["Daytime Temp"])
    print('Night time Temperature: ' + tripProfileDict["Night Temp"])
    print('Sunny? ' + str(tripProfileDict["Sunny"]))
    print('Rainy? ' + str(tripProfileDict["Rain"]))
    print('Snow? ' + str(tripProfileDict["Snow"]))
    print('Swim? ' + str(tripProfileDict["Swim"]))
    print('Suit? ' + str(tripProfileDict["Suit"]))
    print('Number of suits: ' + str(tripProfileDict["Nbr of Suits"]))
    print('Go-out night(s)? ' + str(tripProfileDict["Go Out Night"]))
    print('How many go-out nights? ' + str(tripProfileDict["Nbr of go-out nights"]))
    print('Shopping? ' + str(tripProfileDict["Shopping"]))
    print('Bring DSLR? ' + str(tripProfileDict["DSLR"]))
    print('Travel mode: ' + tripProfileDict["Transportation Mode"])
    print('Flight time: ' + str(tripProfileDict["Flight Time"]))
    print('Drive time: ' + str(tripProfileDict["Drive Time"]))
    print('International trip? ' + str(tripProfileDict["International Trip"]))
    
    pass


def tripSummaryToFile(tripProfileDict):
    """
    This function prints a Trip Profile Summary to a text file.
    Input: Trip Profile Dictionary
    Output: text file containing Trip Profile Summary
    """
    TripSummary = open('./outputs/' + tripProfileDict["Trip Name"] + '-TripSummary.txt', 'w')
    
    TripSummary.write('TRIP SUMMARY')
    TripSummary.write('\n')
    TripSummary.write('Trip Name: ' + tripProfileDict["Trip Name"])
    TripSummary.write('\n')
    TripSummary.write('Trip Purpose: ' + tripProfileDict["Trip Purpose"])
    TripSummary.write('\n')
    TripSummary.write('Number of Days: ' + tripProfileDict["Nbr of Days"])
    TripSummary.write('\n')
    TripSummary.write('Number of Nights: ' + tripProfileDict["Nbr of Nights"])
    TripSummary.write('\n')
    TripSummary.write('Daytime Temperature: ' + tripProfileDict["Daytime Temp"])
    TripSummary.write('\n')
    TripSummary.write('Night time Temperature: ' + tripProfileDict["Night Temp"])
    TripSummary.write('\n')
    TripSummary.write('Sunny? ' + str(tripProfileDict["Sunny"]))
    TripSummary.write('\n')
    TripSummary.write('Rainy? ' + str(tripProfileDict["Rain"]))
    TripSummary.write('\n')
    TripSummary.write('Snow? ' + str(tripProfileDict["Snow"]))
    TripSummary.write('\n')
    TripSummary.write('Swim? ' + str(tripProfileDict["Swim"]))
    TripSummary.write('\n')
    TripSummary.write('Suit? ' + str(tripProfileDict["Suit"]))
    TripSummary.write('\n')
    TripSummary.write('Number of suits: ' + str(tripProfileDict["Nbr of Suits"]))
    TripSummary.write('\n')
    TripSummary.write('Go-out night(s)? ' + str(tripProfileDict["Go Out Night"]))
    TripSummary.write('\n')
    TripSummary.write('How many go-out nights? ' + str(tripProfileDict["Nbr of go-out nights"]))
    TripSummary.write('\n')
    TripSummary.write('Shopping? ' + str(tripProfileDict["Shopping"]))
    TripSummary.write('\n')
    TripSummary.write('Bring DSLR? ' + str(tripProfileDict["DSLR"]))
    TripSummary.write('\n')
    TripSummary.write('Travel mode: ' + tripProfileDict["Transportation Mode"])
    TripSummary.write('\n')
    TripSummary.write('Flight time: ' + str(tripProfileDict["Flight Time"]))
    TripSummary.write('\n')
    TripSummary.write('Drive time: ' + str(tripProfileDict["Drive Time"]))
    TripSummary.write('\n')
    TripSummary.write('International trip? ' + str(tripProfileDict["International Trip"]))
    TripSummary.write('\n')
    
    TripSummary.close()

    pass

if __name__ == '__main__':
    print('Executing as ' + __name__)
    tripProfileDict = questionnaire()
    
    # Print the summary to screen
    tripSummaryToScreen(tripProfileDict)
    
    # Save the summary to a file
    tripSummaryToFile(tripProfileDict)
    