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

    # Instantiate the standard packing list datafrome from csv file
    dfpackingList = pd.read_excel(standardPackingListFile, sheet_name=standardPackListSheet)
        # usecols=['Item', 'Qty', 'Completed'])

    # Set item names as index for the dataframe
    dfpackingList = dfpackingList.set_index('Item')

    # Ignore data types (dtypes) for the columns for now. May not be necessary at all.
    # To update the dataframe values, use df.loc[index, column]
    
    defTemperatureMapping(temperature):
        """This function takes a temperature and maps it to my own temperature description.
        Input: temperature
        Output: a verbal description of temperature based on the number that was input."""
        if temperature >= 95:
            tempDescription = 'Really Hot'
        elif temperature >= 85:
            tempDescription = 'Hot'
        elif temperature >= 75:
            tempDescription = 'Warm'
        elif temperature >= 65:
            tempDescription = 'Cool'
        elif tempDescription >= 55:
            tempDescription = 'Chilly'
        elif tempDescription >= 45:
            tempDescription = 'Cold'
        else:
            tempDescription = 'Really Cold'
        return tempDescription
        
    nbrDays = tripProfileDict['Nbr of Days']
    
    def selectTops(nbrDays, dayTemp, nightTemp, tripPurpose):
        """ This function selects the quantity of shirts based on the number of days of the trip and the temperature.
        Inputs: number of days, daytime temperature, nighttime temperature, tripPurpose
        Outputs: type of shirt (casual, business)
                 temp of shirt (short-sleeve, long-sleeve, sweater, jacket)
                 quantity of shirts.
        Returns: a dictionary of the above items"""
        # Qty: One shirt for each day, up to 5 shirts max.
        # Temp: Short-sleeve for warm/hot weather, long-sleeve and/or sweater for cold
        pass
    
    def selectBottoms(tripPurpose, nbrDays, dayTemp, nightTemp):
        """Select pants, shorts."""
        pass
    
    def selectLuggage(tripPurpose, nbrDays):
        """Select primary and secondary bags."""
        pass
    
    def selectActivityGear(suit, go_out_night, swim, shopping):
        """Select items needed for various activities."""
        pass
    
    def selectUnderwear(nbrDays, nbrNights, dayTemp, nightTemp):
        """ Select underwear, long johns, undershirts, socks"""
        pass
    
    def selectWeatherGear(sunny, rain, snow):
        """Select items for various weather types."""
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

    # Save generated packing list as a new Excel file.
    dfpackingList.to_excel(path + tripProfileDict['Trip Name'] + 'xlsx')
    # dfpackingList.to_csv(path + tripProfileDict['Trip Name'] + '.csv')


# TODO - Export the packing list to csv, text file, Excel, or Evernote
def outputPackingList(tripName, generatedPackList):
    packList = open(tripName + '.txt', 'w')
    packing_list = pd.read_csv(generatedPackList)
    packList.write('     Qty     Item\n')
    packList.write('[ ]  ' + '     ' + packing_list.loc[1, 1] + '     ' + packing_list.loc[1, 2])

if __name__ == '__main__':
    print('Executing as ' + __name__)
    path = '/home/ubuntu/workspace/packing-list-generator/PackingListGenerator/'
    standardPackingListFile = 'StandardPackingList.xlsx'
    tripProfileDict = exampleDict
    generatePackList(path, standardPackingListFile, tripProfileDict)
    