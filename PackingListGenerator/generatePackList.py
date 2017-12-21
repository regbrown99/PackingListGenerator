#! /usr/bin/python3
import pandas as pd
import os

exampleDict = {"Trip Name": 'Aruba', "Trip Purpose": 'Personal',
               "Nbr of Days": 5, "Nbr of Nights": 5,
               "Daytime Temp": 'Warm', "Night Temp": 'Warm',
               "Sunny": True, "Rain": False, "Snow": False,
               "Swim": True, "Suit": False, "Nbr of Suits": 0,
               "Go Out Night": False, "Nbr of go-out nights": 0,
               "Shopping": True,
               "DSLR": True,
               "Transportation Mode": 'Flight',
               "Flight Time": 3, "Drive Time": 0,
               "International Trip": False}


def generatePackList(path, standardPackingListFile, standardPackListSheet, tripProfileDict):
    """ This function generates a packing list by selecting items from the Standard Packing List based on the answers
    to the questionnaire function (stored in a dictionary).
    Inputs: path to the standard packing list file,
            filename of the standard packing list (in csv format),
            a dictionary of values used to generate the packing list
    Output: a text file with the generated packing list in a readable format with filename=tripname"""

        
    nbrDays = tripProfileDict['Nbr of Days']
    
    def selectTops(nbrDays, dayTemp, nightTemp, tripPurpose):
        """ This function selects the quantity of shirts based on the number of days of the trip and the temperature.
        Criteria:
            Qty: 1 shirt for each day, up to 5 shirts max
            Temp: Warm/hot weather = short-sleeve shirt
                  Cool/cold weather = long-sleeve, sweater, and/or jacket
            Purpose: business trip = dress shirts
                     personal trip = casual shirts
        Inputs: number of days, daytime temperature, nighttime temperature, tripPurpose
        Outputs: type of top (casual, business)
                 temp of top (short-sleeve shirt, long-sleeve shirt, sweater)
                 quantity of shirts
        Returns: a dictionary of the above items"""
        
        pass
    
    def selectBottoms(tripPurpose, nbrDays, dayTemp, nightTemp):
        """ This function selects the quantity of bottoms based on the number of days of the trip and the temperature.
        Criteria:
            Qty: 1 bottom for every 2 days, up to 3 bottoms max
            Temp: Warm/hot weather = shorts
                  Cool/cold weather = pants
            Purpose: business trip = dress pants
                     personal trip = casual pants or shorts
        Inputs: number of days, daytime temperature, nighttime temperature, tripPurpose
        Outputs: type of bottom (casual, business)
                 temp of bottom (shorts, pants)
                 quantity of bottoms
        Returns: a dictionary of the above items"""
        pass
    
    def selectUnderwear(nbrNights, tripPurpose, dayTemp, nightTemp):
        """ This function selects the quantity and type of underwear based on the purpose of trip and the temperature.
        Criteria:
            Qty: 1 pair underwear for each night up to 5 max, 1 undershirt for every 2 nights, 1 pair socks per 2 days
            Temp: hot weather       = undershirt
                  warm weather      = undershirt
                  cool weather      = light long john top
                  cold weather      = light long john top or heavy long john top
                  very cold weather = heavy long john top, long john bottom
            Purpose: business trip = dress socks
                     personal trip = casual socks
        Inputs: number of nights, daytime temp, nighttime temp
        Outputs: type of underwear (socks, underwear, undershirts, light long john tops, light long john bottoms,
                                    heavy long john tops, heavy long john bottoms)
                 quantity of underwear
        Returns: a dictionary of the above items"""
        
        pass
    
    def selectShoes(tripPurpose):
        pass
    
    def selectOuterwear(tripPurpose, dayTemp, nightTemp):
        """ This function selects the quantity and type of outerwear based on the purpose of trip and the temperature.
        Criteria:
            Qty: 1 coat if cold, 0 coats if war 1 jacket if cool or hot (due to AC), 0
            Temp: hot weather = indoor jacket (for air conditioning)
                  warm weather = none
                  cool weather = light outdoor jacket
                  cold weather = outdoor coat and indoor jacket
            Purpose: business trip = dressy coat or jacket
                     personal trip = casual coat or jacket
        Inputs: tripPurpose, daytime temp, nighttime temp
        Outputs: type of outerwear (casual, business)
                 temp of outerwear (jacket, coat)
                 quantity of outerwear
        Returns: a dictionary of the above items"""
        pass
    
    def selectLuggage(tripPurpose, nbrDays):
        """ This function selects the primary, secondary, and packed bags based on the trip purpose and number of days of the trip.
        Criteria:
            Qty: 0-2 days = Antler bag
                 2-5 days = Tumi carry-on or Tumi garment bag
                 5+ days  = Tumi checked bag
                 secondary bag?
            Purpose: business trip: secondary bag = Tumi briefcase or Tumi backpack
                     personal trip: secondary bag = Samsonite briefcase, Tumi briefcase and optional Eddie Bauer daypack
        Inputs: trip purpose, number of days
        Outputs: primary bag (Antler bag, Tumi carry-on, Tumi garment bag, Tumi checked bag)
                 secondary bag (Samsonite briefcase, Tumi briefcase)
                 packable bag (Tumi briefcase, Eddie Bauer daypack)
                 quantity of bags
        Returns: a dictionary of the above items"""
        pass
    
    def selectActivityGear(suit, beach, go_out_night, swim, shopping):
        """ This function selects the quantity and type of clothing for other trip activities based on whether or not those activities will occur.
        Criteria:
            Qty: 
            Activity: suit required = suit or blazer, suit shirt, tie, dress shoes, trench coat?
                      go out night  = dressy shirt, nice jeans or nice slacks, and nice shoes (optional: belt, accessories)
                      swim          = swim trunks, goggles?
                      beach         = sunblock, sunglasses, flip-flops
                      shopping      = extra space in bag (why is this included?)
            Purpose: business trip = 
                     personal trip = 
        Inputs: suit, go_out_night, swim, shopping
        Outputs: suit required items, go out night items, swim items, shopping items
                 quantity of above items
        Returns: a dictionary of the above items"""
        
        pass
    
        def selectWeatherGear(sunny, rain, snow):
        """ This function selects the quantity and type of items needed based on weather.
        Criteria:
            Qty: 
            Weather: sunny = sunglasses, sunblock
                     rain  = raincoat or umbrella
                     snow  = boots, gloves
        Inputs: sunny, rain, snow
        Outputs: sunglasses, sunblock, raincoat, umbrella, boots, gloves
                 quantity of above items
        Returns: a dictionary of the above items"""
        
        pass
    
    def selectCameraGear(dslr):
        """Select items related to my DSLR camera."""
        pass
    
    def selectTravelItems(transportationMode, transportationTime, internationalDomestic):
        """Select travel docs and items related to time in transit."""
        pass
    
    def selectToiletries():
        pass
    
    def selectMeds():
        pass
    
    def selectUtilityItems():
        pass
    
    def selectPapersandBooks():
        pass
    
    
    
    # Select number of shirts
    # One shirt for each day up to five max
    if nbrDays <= 5:
        dfpackingList.loc['shirts', 'Qty'] = nbrDays
    else:
        dfpackingList.loc['shirts', 'Qty'] = 5
    
    
    
    # Select number of bottoms
    # One pair of bottoms for every two days, up to 3 max
    
    if tripProfileDict['Daytime Temp'].lower() == 'warm':
        if nbrDays <= 5:
            dfpackingList.loc['shorts', 'Qty'] = (
            (nbrDays // 2) + (nbrDays % 2))  # rounds up for odd nbr of days
        else:
            dfpackingList.loc['shorts', 'Qty'] = 3
    if tripProfileDict['Daytime Temp'].lower() == 'cold':
        if nbrDays <= 5:
            dfpackingList.loc['pants', 'Qty'] = (
            (nbrDays // 2) + (nbrDays % 2))  # rounds up for odd nbr of days
        else:
            dfpackingList.loc['pants', 'Qty'] = 3

    def updateDataFrame():
        """ This function retrieves the standard packing list and updates it based on the return values of the
        select items set of functions. It then saves the new DataFrame to file with the trip name from
        the questionnaire function."""
        # Instantiate the standard packing list datafrome from csv file
        dfpackingList = pd.read_excel(standardPackingListFile, sheet_name=standardPackListSheet)
        # usecols=['Item', 'Qty', 'Completed'])

        # Set item names as index for the dataframe
        dfpackingList = dfpackingList.set_index('Item')

        # Ignore data types (dtypes) for the columns for now. May not be necessary at all.
        # To update the dataframe values, use df.loc[index, column]
        
        # TODO - Export the packing list to csv, text file, Excel, or Evernote
        def outputPackingList(tripName, generatedPackList):
            packList = open(tripName + '.txt', 'w')
            packing_list = pd.read_csv(generatedPackList)
            packList.write('     Qty     Item\n')
            packList.write('[ ]  ' + '     ' + packing_list.loc[1, 1] + '     ' + packing_list.loc[1, 2])
    
            pass

        # Save generated packing list as a new Excel file.
        dfpackingList.to_excel(path + tripProfileDict['Trip Name'] + 'xlsx')
        # dfpackingList.to_csv(path + tripProfileDict['Trip Name'] + '.csv')

    pass

if __name__ == '__main__':
    print('Executing as ' + __name__)
    path = '/home/ubuntu/workspace/packing-list-generator/PackingListGenerator/'
    standardPackingListFile = 'StandardPackingList.xlsx'
    tripProfileDict = exampleDict
    generatePackList(path, standardPackingListFile, tripProfileDict)
    