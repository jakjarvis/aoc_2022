# For this to work, you need to set your AoC session cookie as an env variable called AOC_SESSION in your Python environment.

# To retrieve your cookie, login in to advent of code, open developer tools, click on the 'Application' tab and find the cookies file under Storage->Cookies. Copy the value of the 'session' key.

# To create the environment variable, assuming you're using a conda environment, use the command {conda env config vars set AOC_SESSION=[value]} to set the variable then reactivate the environment with {conda activate [env-name]}

from aocd import get_data


def input_string(day, year):
    input_string = get_data(day=day, year=year)
    return input_string


def raw_input_string(day, year):
    input_string = get_data(day=day, year=year)
    return input_string.encode("unicode_escape")


def input_list(day, year):
    data = []
    i_string = input_string(day, year)
    input_list = i_string.split()
    return input_list
