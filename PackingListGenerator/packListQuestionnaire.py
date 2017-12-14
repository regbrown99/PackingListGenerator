# packListQuestionnaire.py - Questionnaire function for packingListGenerator

def questionnaire():
    """ This function gathers initial info with questions
    and prints the output to the screen.
    Inputs: None
    Outputs: a dictionary of values used to generate the packing list,
            printout of trip summary to the screen"""

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
    print('What is the temperature forecast for daytime? (hot, warm, cold, cool)')
    daytime_temp = input()
    daytime_temp = str2bool(daytime_temp)
    print('What is the temperature forecast for night/evenings? (hot, warm, cold, cool')
    night_temp = input()
    night_temp = str2bool(night_temp)
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
        print('You did not enter a drive/flight time\n')

    print('Is this an international trip?')
    intl_trip = input()
    intl_trip = str2bool(intl_trip)

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
    print('Bring DSLR? ' + dslr, end='\n')
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
