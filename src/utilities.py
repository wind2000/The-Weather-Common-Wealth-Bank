
''' Utility methods for data manipulation and weather calculation'''


import os
import numpy as np
import datetime

''' Method to load dataset and return it as Numpy.Array'''
def loadData(data_folder_path, station_file_name) :
    return np.loadtxt(os.path.join(data_folder_path,station_file_name))

''' Method to generate List of dates starting from today to today - number of days'''
def generateDates(numdays) :
    today = datetime.datetime.today()
    dates = [today - datetime.timedelta(days=x) for x in range(0, numdays)]
    return dates

''' Method to load weather station configuration file. '''
def load_stations(data_folder_path,station_conf_file_name):
    data_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'data'))
    return np.loadtxt(os.path.join(data_folder_path,station_conf_file_name),
               dtype={'names': ('station', 'latitude', 'longitude'),
                      'formats': ('|S3', np.float, np.float)},
               )

''' Method to calculate the Probability of Precipitation. '''
def calculate_probability_of_precipitation(temperature, maxSnowTemp, relativeHumidity, pressure):
    # PoP = C x A where "C" = the confidence that precipitation will occur somewhere in the forecast area,
    # and where "A" = the percent of the area that will receive measureable precipitation, if it occurs at all.

    # Rainfall depends on multiple variables such as amount of waterr available, temperature, air pressure, wind speed,
    # Relative Humidity etc.
    # Currently considering only 3 variables: Temperature, Relative Humidity and Air Pressure
    if temperature > maxSnowTemp and relativeHumidity > 90 and pressure < 900:
        confidence = np.random.uniform(0.8, 1.0)  # Set confidence to 80% or above
        area = np.random.uniform(0.7, 1.0)  # Set area to 70% or above
    else:
        confidence = np.random.uniform(0.1, 0.4)
        area = np.random.uniform(0.1, 1.0)

    return confidence * area