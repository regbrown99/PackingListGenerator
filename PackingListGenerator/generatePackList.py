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
tripProfileDict = exampleDict


def generatePackList(path, standardPackingListFile, tripProfileDict):
    """ This function generates a packing list by selecting items from the Standard Packing List based on the answers
    to the questionnaire function (stored in a dictionary).
    Inputs: path to the standard packing list file,
            filename of the standard packing list (in csv format),
            a dictionary of values used to generate the packing list
    Output: a text file with the generated packing list in a readable format with filename=tripname"""

    # Instantiate the standard packing list datafrome from csv file
    dfpackingList = pd.read_csv(
        standardPackingListFile)  # usecols=['Item', 'Qty', 'Completed'])

    # Set item names as index for the dataframe
    dfpackingList.set_index('Item', inplace=True)

    # Ignore data types (dtypes) for the columns for now. May not be necessary at all.
    # To update the dataframe values, use df.loc[index, column]

    tops = {'shirts': 0, 'long sleeve shirts': 0}
    bottoms = {'shorts': 0, 'pants': 0}
    # Select number of shirts
    # One shirt for each day up to five max
    if tripProfileDict['Nbr of Days'] <= 5:
        tops['shirts'] = tripProfileDict['Nbr of Days']
        # dfpackingList.loc['shirts', 'Qty'] = nbrDays
    else:
        tops['shirts'] = 5
        # dfpackingList.loc['shirts', 'Qty'] = 5

    # Select number of bottoms
    # One pair of bottoms for every two days, up to 3 max
    nbrDays = tripProfileDict['Nbr of Days']
    if tripProfileDict['Daytime Temp'].lower() == 'warm':
        if tripProfileDict['Nbr of Days'] <= 5:

            bottoms['shorts'] = (
            (nbrDays // 2) + (nbrDays % 2))  # rounds up for odd nbr of days
        else:
            bottoms['shorts'] = 3
    if tripProfileDict['Daytime Temp'].lower() == 'cold':
        if tripProfileDict['Nbr of Days'] <= 5:
            bottoms['pants'] = (
            (nbrDays // 2) + (nbrDays % 2))  # rounds up for odd nbr of days
        else:
            bottoms['pants'] = 3

    # Save generated packing list as a new csv file.
    dfpackingList.to_csv(path + tripProfileDict['Trip Name'] + '.csv')


# TODO - Export the packing list to csv, text file, Excel, or Evernote
def outputPackingList(tripName, generatedPackList):
    packList = open(tripName + '.txt', 'w')
    packing_list = pd.read_csv(generatedPackList)
    packList.write('     Qty     Item\n')
    packList.write(
        '[ ]  ' + '     ' + packing_list.loc[1, 1] + '     ' + packing_list.loc[1, 2])
