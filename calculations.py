# takes in a name of a person the total bill before tax and the price of the items they got and determines the percentage of the bill that person owes 
def calcpercentageofbill(itemprices, totalbill):
    return sum(itemprices)/totalbill
# takes in a dictionary: keys: person, value: list of item prices. Calculates how much every person owes
def generatecost(billdict, tippercent, totalbill, tax):
    moneyowed = {}
    for person in billdict.keys():
        percent = calcpercentageofbill(billdict[person], totalbill)
        moneyowed[person] = totalbill * percent + tippercent * totalbill * percent + tax * percent
    return moneyowed
