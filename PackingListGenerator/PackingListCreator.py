#! /usr/bin/python3
""" This program generates a packing list after asking
some initial questions.
packingListCreator.py
Author: Reggie Brown
Date: October 14, 2017
"""
import pandas as pd
import os
import packListQuestionnaire
import generatePackList

# Store standard packing list file location in a variable so it can be changed if desired.
# path = '/Users/RAB-Capital/Dropbox/111PackingLists/'
path = '/home/ubuntu/workspace/PackingListGenerator'
standardPackingListFile = 'standardPackingList.xlsx'
standardPackingListSheet = 'StandardPackingList'

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

tripProfile = packListQuestionnaire.questionnaire()
generatePackList.generatePackList(path, standardPackingListFile, standardPackingListSheet, tripProfile)
