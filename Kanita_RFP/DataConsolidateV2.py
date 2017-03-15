# The purpose is to consolidate price data from all bidders into one workbook so it can then be analyzed.



# import all required modules
import pandas as pd
import os, openpyxl

# Create the consolidated workbook
wb1 = openpyxl.Workbook()
wb1.save('000ConsolidatedBS')

# Create an empty dataframe
df = pd.DataFrame()

# Create a list of all the files
fileList = os.listdir(ENTER_PATH_HERE)


# Open each file in the fileList and loop through the following steps:
for fileName in fileList:
    tempFileName = str(fileName)
    wb2 = read_excel(tempFileName, sheetname=None) #open workbook in pandas
    #wb2 = openpyxl.load_workbook(tempFileName) #load workbook
    #sheetnames = wb2.get_sheet_names() #list sheetnames
    print("These are the worksheets in ' + fileName + ':')
    print(wb2.sheet_names)
    #for sheet in sheetnames:
        #tempSheet = str(sheet)
        #print(tempSheet)
    ws = input('which sheet would you like to open? ')
    #loadSheet = wb.get_sheet_by_name(ws) #open ws
    df = read_excel(tempFileName, sheetname=ws)
    # pd.DataFrame(loadSheet) #write ws to dataframe
    #openpyxl.load_workbook('000ConsolidatedBS')#open consolidated workbook
    temp = str(fileName) #turns the filename into a string
    temp = temp[7] #shortens it to first 7 chars
    #wb1.create_sheet(title=temp) #create a worksheet named temp
    df.to_excel('000ConsolidatedBS.xlsx', sheet_name=temp, engine='openpyxl')#put dataframe into the new worksheet
    wb1.save('000ConsolidatedBS.xlsx') #save the workbook
    wb1.close() #close workbook
    wb2.close()  # close workbook