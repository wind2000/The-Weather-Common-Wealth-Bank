# The Weather

The Weather-Station creates a toy model of the environment that evolves over time.

It considers data from Australian Government Bureau of Meteorologies monthly statistics of climate and weather data ( http://www.bom.gov.au/climate/data/index.shtml?bookmark=200 ).

The script considers following data from the monthly statistics

| Statistics                          | Jan | Feb | Mar | Apr | May | Jun | July | Aug | Sep | Oct | Nov | Dec |
|-------------------------------------|-----|-----|-----|-----|-----|-----|------|-----|-----|-----|-----|-----|
| Highest temperature (°C)            |     |     |     |     |     |     |      |     |     |     |     |     |
| Lowest temperature (°C)             |     |     |     |     |     |     |      |     |     |     |     |     |
| Highest minimum temperature (°C)    |     |     |     |     |     |     |      |     |     |     |     |     |
| Mean 9am relative humidity (%)      |     |     |     |     |     |     |      |     |     |     |     |     |
| Mean 9am dew-point temperature (°C) |     |     |     |     |     |     |      |     |     |     |     |     |
| Mean number of days of rain ≥ 1 mm  |     |     |     |     |     |     |      |     |     |     |     |     |

# Data Definition
| Features                            	| Definition                                                                                                                     	| Storage 	|
|-------------------------------------	|--------------------------------------------------------------------------------------------------------------------------------	|---------	|
| Highest temperature (°C)            	| The highest (by month and overall) maximum air temperature observed at the site.                                               	| float   	|
| Lowest temperature (°C)             	| The lowest (by month and overall) maximum air temperature observed at the site.                                                	| float   	|
| Highest minimum temperature (°C)    	| The highest recorded minimum temperature observed at the site, calculated over all years of record.                            	| float   	|
| Mean 9am relative humidity (%)      	| Approximate average relative humidity at 9am local time during a calendar month or year, calculated over the period of record. 	| integer 	|
| Mean 9am dew-point temperature (°C) 	| Dew-point temperatures at 9 am local time during a calendar month or year, averaged over the period of record.                 	| float   	|
| Mean number of days of rain ≥ 1 mm  	| Number of days in a calendar month or year with at least 1 mm of precipitation.                                                	| float   	|

The stations file contains the list of supported stations with their geo codes.

#Usage

Run generateWeather.py from console.
The script asks for the number of samples to be generated.
The output file with the toy model of the environment will be generated in the current directory with file name 'weather_data'
#Software Requirements

    - Python 2.7 with NumPy package

#TODOS

    - Write Test cases
