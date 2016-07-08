import numpy as np
import datetime

def convert_to_vapour_pressure( dewPointTemp ): # Formulae obtained from http://www.bom.gov.au/climate/austmaps/about-vprp-maps.shtml
    return np.exp(1.8096 + (17.269425 * dewPointTemp)/(237.3 + dewPointTemp)).astype(int)

def loadData(station) : # Data collected from http://www.bom.gov.au/climate/averages/tables/cw_066062_All.shtml
    return np.loadtxt(".\\stations\\" + station)

stations = ["SYD"] #TODO: Add more stations
geocode = {}
geocode["SYD"] = [-33.8556,151.2082]
#Load Data
weatherData = {}
for station in stations :
    weatherData[station] = loadData(station)
    weatherData[station][4] = np.apply_along_axis( convert_to_vapour_pressure, 0, arr=weatherData[station][4] ) #Prepare Data.. Convert dew point temperature to vapour pressure

samples = input("Enter number of samples required:")
numdays = samples
currMonth = -1
output = [] # Contains generated values
today = datetime.datetime.today()
dates = [today - datetime.timedelta(days=x) for x in range(0, numdays)]
for date in dates:
    # select a random station
    station = stations[0]
    # check Month
    if currMonth != date.month: 
        currMonth = date.month
        noOfDaysOfRain = 0
    #Select a random number of range Loweset Temperature to Highest Temperature for the selected month
    temperature = np.random.uniform(weatherData[station][2,currMonth-1],weatherData[station][0,currMonth-1])
    minSunnyTemp = 32
    maxSunnyTemp = 40
    minSnowyTemp = np.min(weatherData[station][2])
    maxSnowyTemp = np.max(weatherData[station][0])
    if temperature >= minSunnyTemp and temperature <= maxSunnyTemp:
        condition = "Sunny"
    elif temperature >= minSnowyTemp and temperature <= maxSnowyTemp:
        condition = "Snow"
    #check for rainy
    if weatherData[station][3,currMonth-1] > 73 and noOfDaysOfRain < weatherData[station][5,currMonth-1]:
        condition = "Rain"
        noOfDaysOfRain += 1
    output.append( station + "|" + str(geocode[station][0]) + "," + str(geocode[station][1]) + "|" + str(date) + "|" + condition + "|" + str(temperature) + "|" + str(weatherData[station][4,currMonth-1]) + "|" + str(weatherData[station][3,currMonth-1]) + "\n")

outputFile = open("weather_data",'w')
outputFile.writelines(output)
outputFile.close()