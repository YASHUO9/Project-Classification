
## <----------------------Scraping---------------------------------------->##
from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import os


def scrapping(urll):
    """This Function is used to Scrap the Movie Name , Movie Year, Movie Actor:
       It take the url as urll(which is the url of the site i.e wikipedia)"""
    url = urll

    website = requests.get(url)
    print(website.status_code)
    soup = BeautifulSoup(website.text, 'lxml')

    print(website)

    # Folders for files:
    cwd = os.getcwd()
    newpath = cwd + '\combine_folder'
    os.makedirs(newpath)

    years = []

    while True:

        # Here I have find the Table value in which data has been fitted.
        movies_years = soup.find('div', class_="hlist")

        years = []
        full_link = []

        # looping through each to get the required text
        for link in movies_years.find_all('a'):
            year = link.text
            years.append(year)
            links = link.get('href')
            year = link.text
            full_link.append(links)

        # Using the slicing technique to Obtain the required Year , Links
        total_link = full_link[1:5]
        list_year = years[1:5]
        count = 0
        actor = []
        movie = []

        while count <= 3:
            """Here IS THE SECOND MAIN PART IN THIS WE HAVE LOOP THROUGH THE EACH SITE OF WIKIPEDIA TO GET THE DATA:"""

            if count > 3:
                driver.Close()
            year = list_year[count]
            url = "https://en.wikipedia.org"+total_link[count]
            driver = webdriver.Chrome(
                "C:\\Users\\DELL\\Downloads\\chromedriver_win32\\chromedriver.exe")
            driver.get(url)

            for j in range(0, 250):
                try:
                    for i in driver.find_elements(By.XPATH, f'//*[@id="mw-content-text"]/div[1]/table[6]/tbody/tr[{j}]/td[2]/a'):
                        # HERE FINDING THE ACTOR NAME

                        actors = i.text
                        actor.append(actors)

                    for i in driver.find_elements(By.XPATH, f'//*[@id="mw-content-text"]/div[1]/table[6]/tbody/tr[{j}]/td[6]'):
                        # HERE FINDING THE MOVIE NAME

                        movies = i.text
                        movie.append(movies)

                except:
                    break
            count += 1

            """USING THE PANDAS TO MAKE THE DATAFRAME AND SAVING EACH DATA FRAME AS SEPARATE FILE THEN
            WE WILLL COMBINE THESE FILE IN ONE """
            a = {'Actor': actor, 'Movie': movie, 'Year': [
                year for i in range(0, len(actor))]}
            data = pd.DataFrame.from_dict(a, orient='index')
            data = data.transpose()
            data.to_csv(f'combine_folder//movie{count}.csv')

        if count > 3:
            # CLOSING THE DRIVER HERE
            driver.close()
            break
