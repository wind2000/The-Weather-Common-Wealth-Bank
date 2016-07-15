
''' Utility classes for data manipulation '''


import os
import numpy as np
import datetime

''' Load dataset and return it as Numpy.Array'''
def loadData(data_folder_path, station_file_name) :
    return np.loadtxt(os.path.join(data_folder_path,station_file_name))

''' Generate List of dates starting from today to today - number of days'''
def generateDates(numdays) :
    today = datetime.datetime.today()
    dates = [today - datetime.timedelta(days=x) for x in range(0, numdays)]
    return dates

''' Load weather station configuration file. '''
def load_stations(data_folder_path,station_conf_file_name):
    data_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'data'))
    return np.loadtxt(os.path.join(data_folder_path,station_conf_file_name),
               dtype={'names': ('station', 'latitude', 'longitude'),
                      'formats': ('|S3', np.float, np.float)},
               )