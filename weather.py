import csv
from datetime import datetime
import numpy as np
from collections import Counter
import glob
import os

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    temp = compile('u"\N{DEGREE SIGN}"', '', 'eval')
    return f"{temp}{DEGREE_SYBMOL}"

    pass



def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date = str(datetime.now())
    expected_result = str(input())
    if date == expected_result:
        return date.strftime('%A %d %B %Y')#'%Y-%m-%dT%H:%M:%S.%f%z'

pass

# def convert_f_to_c(temp_in_farenheit):

def convert_f_to_c(temp_in_f):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_in_c = (int(temp_in_f) - 32) * (5.0/9.0)
    return round(float(temp_in_c),1) #cannot figure out how to get def test_convert_f_to_c_float(self): to work
#     return temp_in_f
# print(convert_f_to_c(350))



floats = []


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    # if item in weather_data

    # temperatures = (str(weather_data))

    # for temperatures in weather_data:
    #     temperatures == int
    # else temperatures == str

    temperatures = float(weather_data)
    expected_results = float(weather_data)

    if temperatures in weather_data: # gives an OK for test_calculate_mean
        floats.append(float(temperatures))
    elif temperatures in weather_data:
        floats.append(int(temperatures))
    elif temperatures in weather_data:
        floats.append(str(temperatures))

    count = len(floats)
    sum_list = sum(floats)
    weather_data = expected_results(sum_list/count)
    return float(weather_data)

    # return str(sum_list/count)



def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    
# This is doesn't work --------------------------------------------------------------
    # files = ['example_two.csv', 'example_three.csv']

    # with open("outfile","wt") as fw:
    #     writer = csv.writer(fw)
    #     for file in files:
    #         with open(file) as csvfile:
    #             info = csv.reader(csvfile, delimiter=",")
    #             info_types = []
    #             records = 0
    #             processed_row = []
    #             for row in info:
    #                 writer.writerow(processed_row)

    # return processed_row()

    #-----------------------------------------------------------------------------------

    path = r'\tests\data'
    all_files = os.listdir(path)

    for your_file_name in all_files:
        print(your_file_name)


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    pass


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
