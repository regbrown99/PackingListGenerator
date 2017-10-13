""" THis program generates a packing list after asking
some initial questions.
"""

# TODO - Create packing list item class
class Item():
    pass


# TODO - Create initial questions list
# Gather initial info with questions
# Trip Purpose

print('Is this a business trip, personal trip, or mixed purpose?\n')
trip_purpose = input()

# Trip Length
print('How many days will you be gone?\n')
nbr_days = input()
print('How many nights will you be gone?\n')
nbr_nights = input()

# Weather
print('What is the temperature forecast for daytime?\n')
daytime_temp = input()
print('What is the temperature forecast for night/evenings?\n')
night_temp = input()
print('Will it be sunny?\n')
sunny = input()
print('Will it rain?\n')
rain = input()
print('Will it snow?\n')
snow = input()

# Activities Planned
print('Will you swim? (y or n)\n')
swim = input()
print('Will you have a formal outing that will require a suit? (y or n)\n')
suit = input()
nbr_suits = 0
if suit == 'y':
    print('How many suits do you want to bring?\n')
    nbr_suits = input()
print('Will you have a dressy "go out" night? (y or n)\n')
go_out_night = input()
nbr_go_out_nights = 0
if go_out_night == 'y':
    print('How many go-out nights will you have?\n')
    nbr_go_out_nights = input()
print('Will you be shopping?\n')
shopping = input()
print('Will you be taking high quality photos?\n')
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
    print('How long is your flight?\n')
    flight_time = input()
elif transport_mode == 'driving':
    print('How long is your drive?\n')
    drive_time = input()
else: print('You did not enter a drive/flight time\n')

print('Is this an international trip?\n')
intl_trip = input()

# TODO - Print a trip summary to the screen
print(trip_purpose, end='\n')
print(nbr_days, end='\n')
print(nbr_nights, end='\n')
print(daytime_temp, end='\n')
print(night_temp, end='\n')
print(sunny, end='\n')
print(rain, end='\n')
print(snow, end='\n')
print(swim, end='\n')
print(suit, end='\n')
print(nbr_suits, end='\n')
print(go_out_night, end='\n')
print(nbr_go_out_nights, end='\n')
print(shopping, end='\n')
print(DSLR, end='\n')
print(transport_mode, end='\n')
print(flight_time, end='\n')
print(drive_time, end='\n')
print(intl_trip, end='\n')


# TODO - "Calculate" and select items based on the answers to the questions.


# TODO - Generate the packing list


# TODO - Instantiate the list items


# TODO - Export the packing list to text file, Excel, or Evernote