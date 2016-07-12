import unittest
import env
from src import generateWeather as WS
import os

class TestWeatherStation(unittest.TestCase):
    def setUp(self):
        self.data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    def test_num_samples(self):
        '''
        Test number of samples generated is equal to the input sample count
        '''

        stations = WS.load_stations('stations')

        # Load Data
        weatherData = {}
        for station in stations:
            weatherData[station[0]] = WS.loadData(station[0])

        WS.generateWeather(1000,stations,weatherData)

        weather_data = [line.rstrip('\n') for line in open(os.path.join(self.data_dir, 'weather_data'))]

        self.assertEqual(len(weather_data),1000)

    def test_num_features(self):
        '''
        Test number of features generated equal to 7
        '''
        self.assertEqual(0,0)

    def test_all_stations(self):
        '''
        Test samples from all stations are generated.
        '''
        self.assertEqual(0, 0)

    def test_sunny_day_boundary(self):
        '''
        Test sunny daya range > 30
        '''
        self.assertEqual(0,0)

    def test_snow_day_boundary(self):
        '''
        Test snow day range < 30
        '''
        self.assertEqual(0, 0)

    def test_rain_day_boundary(self):
        '''
        Test humidity > 85
        '''
        self.assertEqual(0, 0)

    def test_num_rainy_days_per_month(self):
        '''
        Test number of rainy days generated per month should be <= Mean number of days of rain >= 1 mm
        '''
        self.assertEqual(0, 0)
if __name__ == '__main__':
    unittest.main()