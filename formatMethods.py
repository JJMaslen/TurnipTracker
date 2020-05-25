from datetime import datetime

import dbMethods

def databaseConcatenaterTurnipTable():
    data = dbMethods.readTable_turnipTable()

    nameColumn = ""
    valueColumn = ""
    updateColumn = ""

    for row in data:
        dateData = row[3].split(' ')
        todayDate = datetime.now().strftime('%d-%m')
        currentTime = datetime.now().strftime('%H')
        
        timeData = dateData[1].split(':')

        if dateData[0] == todayDate:

            if int(currentTime) < 12:
                nameColumn = nameColumn + str(row[1]) + "\n"
                valueColumn = valueColumn + str(row[2]) + "\n"
                updateColumn = updateColumn + str(row[3]) + "\n"
            elif int(timeData[0]) >= 12:
                nameColumn = nameColumn + str(row[1]) + "\n"
                valueColumn = valueColumn + str(row[2]) + "\n"
                updateColumn = updateColumn + str(row[3]) + "\n"                  

    nameColumn = dataFormatterGreen(nameColumn)
    valueColumn = dataFormatterYellow(valueColumn)
    updateColumn = dataFormatterYellow(updateColumn)
    
    return nameColumn,valueColumn,updateColumn

def databaseConcatenaterWeekPrices(id):
    data = dbMethods.readTable_weekPrices()

    for row in data:
        if id == row[0]:
            output = row

    return output

def dataFormatterGreen(text):
    startFormat = "```css\n"
    endFormat = "```"

    formattedText = startFormat + text + endFormat
    return formattedText

def dataFormatterYellow(text):
    startFormat = "```fix\n"
    endFormat = "```"

    formattedText = startFormat + text + endFormat
    return formattedText