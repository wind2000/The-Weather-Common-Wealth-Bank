import os
import numpy as np
import datetime

def convert_to_vapour_pressure( dewPointTemp ): # Formulae obtained from http://www.bom.gov.au/climate/austmaps/about-vprp-maps.shtml
    return np.exp(1.8096 + (17.269425 * dewPointTemp)/(237.3 + dewPointTemp)).astype(int)

def loadData(station) : # Data collected from http://www.bom.gov.au/climate/averages/tables/cw_066062_All.shtml
    return np.loadtxt(os.path.join('data',station))

def generateDates(numdays) :
    today = datetime.datetime.today()
    dates = [today - datetime.timedelta(days=x) for x in range(0, numdays)]
    return dates

def load_stations(station_data):
    return np.loadtxt(os.path.join('data',station_data),
               dtype={'names': ('station', 'latitude', 'longitude'),
                      'formats': ('|S3', np.float, np.float)},
               )

def generateWeather(samples,stations,weatherstats):
    currMonth = -1
    output = []  # Contains generated values
    for date in generateDates(samples):
        # select a random station
        station = np.random.choice(stations)
        # check Month
        if currMonth != date.month:
            currMonth = date.month
            noOfDaysOfRain = 0
        #Select a random number of range Loweset Temperature to Highest Temperature for the selected month
        temperature = np.random.uniform(weatherstats[station[0]][1,currMonth-1],weatherstats[station[0]][0,currMonth-1])
        minSunnyTemp = 32
        maxSunnyTemp = 40
        minSnowTemp = np.min(weatherstats[station[0]][1])
        maxSnowTemp = np.max(weatherstats[station[0]][2])
        if temperature >= minSunnyTemp and temperature <= maxSunnyTemp:
            condition = "Sunny"
        elif temperature >= minSnowTemp and temperature <= maxSnowTemp:
            condition = "Snow"
        #check for rainy
        if weatherstats[station[0]][3,currMonth-1] > 73 and noOfDaysOfRain < weatherstats[station[0]][5,currMonth-1]:
            condition = "Rain"
            noOfDaysOfRain += 1
        output.append( station[0] + "|" + str(station[1]) + "," + str(station[2]) + "|" +
                       str(date.strftime("%Y-%m-%dT%H:%M:%Sz")) + "|" + condition + "|" + str(temperature)
                       + "|" + str(weatherstats[station[0]][4,currMonth-1]) + "|"
                       + str(weatherstats[station[0]][3,currMonth-1]) + "\n")
    return output

def main():
    stations = load_stations('stations')
    # Load Data
    weatherData = {}
    for station in stations:
        weatherData[station[0]] = loadData(station[0])
        weatherData[station[0]][4] = np.apply_along_axis(convert_to_vapour_pressure, 0, arr=weatherData[station[0]][
            4])  # Prepare Data.. Convert dew point temperature to vapour pressure

    samples = input("Enter number of samples required:")
    outputFile = open("weather_data", 'w')
    outputFile.writelines(generateWeather(samples, stations, weatherData))
    outputFile.close()

if __name__ == '__main__':
    main()
