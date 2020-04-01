import dbMethods

def databaseConcatenater():
    data = dbMethods.readTable()

    nameColumn = ""
    valueColumn = ""
    updateColumn = ""

    for row in data:
        nameColumn = nameColumn + str(row[1]) + "\n"
        valueColumn = valueColumn + str(row[2]) + "\n"
        updateColumn = updateColumn + str(row[3]) + "\n"

    nameColumn = dataFormatterGreen(nameColumn)
    valueColumn = dataFormatterYelloe(valueColumn)
    updateColumn = dataFormatterYelloe(updateColumn)
    
    return nameColumn,valueColumn,updateColumn

def dataFormatterGreen(text):
    startFormat = "```css\n"
    endFormat = "```"

    formattedText = startFormat + text + endFormat
    return formattedText

def dataFormatterYelloe(text):
    startFormat = "```fix\n"
    endFormat = "```"

    formattedText = startFormat + text + endFormat
    return formattedText