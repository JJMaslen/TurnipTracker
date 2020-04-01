from datetime import datetime

import dbMethods

def databaseConcatenater():
    data = dbMethods.readTable()

    nameColumn = ""
    valueColumn = ""
    updateColumn = ""

    for row in data:
        dateData = row[3].split(' ')
        now = datetime.now().strftime('%d-%m')

        if dateData[0] == now:
            nameColumn = nameColumn + str(row[1]) + "\n"
            valueColumn = valueColumn + str(row[2]) + "\n"
            updateColumn = updateColumn + str(row[3]) + "\n"     

    nameColumn = dataFormatterGreen(nameColumn)
    valueColumn = dataFormatterYellow(valueColumn)
    updateColumn = dataFormatterYellow(updateColumn)
    
    return nameColumn,valueColumn,updateColumn

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