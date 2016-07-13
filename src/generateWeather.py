import os
import numpy as np
import datetime

def loadData(station_fname) :
    data_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'data'))
    return np.loadtxt(os.path.join(data_dir,station_fname))

def generateDates(numdays) :
    today = datetime.datetime.today()
    dates = [today - datetime.timedelta(days=x) for x in range(0, numdays)]
    return dates

def load_stations(stations_list_fname):
    data_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'data'))
    return np.loadtxt(os.path.join(data_dir,stations_list_fname),
               dtype={'names': ('station', 'latitude', 'longitude'),
                      'formats': ('|S3', np.float, np.float)},
               )

def generateWeather(samples,stations,weatherstats):
    currMonth = -1
    currYear  = -1
    output = []  # Contains generated values

    # Maintain a list of mean rainy days >= 1mm per month per station to limit the number of rainy days per month.
    meanRainyDays = {}

    for date in generateDates(samples):
        # select a random station
        station = np.random.choice(stations)
        # check Month
        if currMonth != date.month:
            currMonth = date.month
        if currYear  != date.year:
            currYear = date.year
            for station in stations:
                meanRainyDays[station[0]] = map(int, weatherstats[station[0]][4])
        #Select a random number from range Lowest Temperature to Highest Temperature for the selected month
        temperature = round(np.random.uniform(weatherstats[station[0]][1,currMonth-1],weatherstats[station[0]][0,currMonth-1]), 1)
        minSunnyTemp = 30 # Infered from Mean number of days = 30C row of the monthly statistics report as well as sunny days range from wikipedia.
        maxSunnyTemp = np.max(weatherstats[station[0]][0]) # Max of Highest temperature
        minSnowTemp = np.min(weatherstats[station[0]][1]) # Min of Lowest temperature
        maxSnowTemp = np.max(weatherstats[station[0]][2]) # Max of Highest minimum temperature
        humidity = int(np.random.uniform(weatherstats[station[0]][3, currMonth - 1] - 20,
                                         weatherstats[station[0]][3, currMonth - 1] + 20))
        if temperature >= minSunnyTemp and temperature <= maxSunnyTemp:
            condition = "Sunny"
        elif temperature >= minSnowTemp and temperature <= maxSnowTemp:
            condition = "Snow"
        else:
            condition = "Snow"

        # check for rainy day, If the relative humdity is greater than 85 it is considered as a rainy day.
        if humidity > 85 and meanRainyDays[station[0]][currMonth - 1] > 0:
            condition = "Rain"
            meanRainyDays[station[0]][currMonth - 1] -= 1

        temperature_in_str = "{a}".format(a="+" if temperature > 0 else "-") + str(temperature)

        atmospheric_pressure = int(np.random.uniform(800,1200)) #Atmospheric pressure can range from 800 to 1200.
        # Data obtained from http://www.bom.gov.au/australia/charts/synoptic_col.shtml

        output.append( station[0] + "|" + str(station[1]) + "," + str(station[2]) + "|" +
                       str(date.strftime("%Y-%m-%dT%H:%M:%Sz")) + "|" + condition + "|" +
                       temperature_in_str
                       + "|" + str(atmospheric_pressure) + "|"
                       + str(humidity) + "\n")
    return output

def main():
    stations = load_stations('stations')
    # Load Data
    weatherData = {}
    for station in stations:
        weatherData[station[0]] = loadData(station[0])

    samples = input("Enter number of samples required:")
    outputFile = open("weather_data", 'w')
    outputFile.writelines(generateWeather(samples, stations, weatherData))
    outputFile.close()

if __name__ == '__main__':
    main()
