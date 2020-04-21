def searchRoles(roleList, search):

    for item in roleList:
        if item.name == search:
            searchResult = item
            return searchResult

def PriceCheck(price):

    lowPrice = 200
    midPrice = 300
    highPrice = 400
    
    if price >= highPrice:
        return 2
    elif price >= midPrice:
        return 1
    elif price >= lowPrice:
        return 0
    else:
        return 99