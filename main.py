# <---------------------Required Import--------------------------------->#
import os
from clean import clean_file
from combine_csv_file import combining_csv
from Scrapping_wikipedia import scrapping

urll = "https://en.wikipedia.org/wiki/Lists_of_films"


"""##<-----Here I am Scapping the wikipedia page using selenium and Beautiful Soap---->##"""
scrapping(urll)


# <--------------Folders for files:--------------->#
cwd = os.getcwd()
newpath = cwd + '\combine_folder'
os.makedirs(newpath)


## -------------combining the csv files:----------->#
file_location = newpath
combining_csv(file_location, cwd=cwd)


# <--------------Checking any null value------------->#
new_file_name = clean_file("Output.csv")

# Starting the Classification:
