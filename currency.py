__author__ = 'matt'

import web_utility
import trip


def convert(amount, startingCurrencyCode, destinationCurrencyCode):
    errorValue = -1
    validAmount = True
    decimalCount = 0
    url_string = "https://www.google.com/finance/converter?a={}&from={}&" \
                 "to={}".format(amount, startingCurrencyCode, destinationCurrencyCode)

    result = web_utility.load_page(url_string)
    if type(amount) is str:
        for i in amount:
            if i not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
                validAmount = False
            if i in ".":
                decimalCount += 1
            amount = float(amount)
    if amount < 1 or validAmount is False or decimalCount > 1:
        return errorValue
    elif startingCurrencyCode == destinationCurrencyCode:
        return errorValue
    else:
        resStr = result[result.index('result'):]
        convtAmt = resStr[resStr.index("d>") + 2: resStr.index(destinationCurrencyCode) - 1]
        return round(float(convtAmt), 2)


def get_details(StartingCountry):
    infile = open("currency_details.txt", "r", encoding="utf-8")
    checkFile = infile.readlines()
    for line in checkFile:
        if line.startswith(StartingCountry):
            line = line.strip().split(",")
            gettingDetails = line[0], line[1], line[2]
            print("valid details {} {}".format(StartingCountry, gettingDetails))
            return tuple(gettingDetails)

    print("invalid Details {} {}".format(StartingCountry, tuple()))
    return tuple()


def convertTest(amount, startingCountryName, destinationCountryName):
    startingCountry = get_details(startingCountryName)
    destinationCountry = get_details(destinationCountryName)
    conversion = convert(amount, startingCountry[1], destinationCountry[1])
    reverseConversion = convert(conversion, destinationCountry[1], startingCountry[1])

    infile = open("currency_details.txt", "r", encoding="utf-8")
    list = []
    for line in infile:
        data = line.split(",")
        list.append(data)
    infile.close()
    cList = []
    for country in list:
        cList.append(country[0])

    if amount < 0 or startingCountry[0] not in cList or destinationCountry[0] not in cList or startingCountry[0] == \
            destinationCountry[0]:
        print("{:>25} {:>10} {} -> {} {:>10}".format("invalid conversion ",
                                                     round(amount, 2), startingCountry[1], destinationCountry[1],
                                                     conversion))
    else:
        print("{:>25} {:>10} {} -> {} {:>10}".format("valid conversion ",
                                                     round(amount, 2), startingCountry[1], destinationCountry[1],
                                                     conversion))
        print("{:>25} {:>10} {} -> {} {:>10}".format("valid reverse conversion ",
                                                     round(conversion, 2), destinationCountry[1], startingCountry[1],
                                                     reverseConversion))


amount = float(input("Enter Amount For Convertion: "))
startCountry = input("Enter Starting Country (Please enter country name): ")
destCountry = input("Enter your Destination Country (Please enter country name): ")
convertTest(amount, startCountry, destCountry)
