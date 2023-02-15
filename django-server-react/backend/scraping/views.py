from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BoatSerializer
from .models import Boat
from django.http import HttpResponse
from django.http import JsonResponse
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


class BoatView(viewsets.ModelViewSet):
    serializer_class = BoatSerializer
    queryset = Boat.objects.all()

def scraping_clickandboat(city):
    
    options = webdriver.ChromeOptions()
    options.add_argument('-headless')
    options.add_argument('-no-sandbox')
    options.add_argument('-disable-dev-shm-usage')
    options.add_argument("enable-automation")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--dns-prefetch-disable")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome('chromedriver', options = options)
    root = "https://www.clickandboat.com/en/"
    url = root + 'boat-rental/search?where=' + city + " &DateDebut=2023-02-15&DateFin=2023-02-17&ProduitTypeId=Sailboat"
    url = url.replace(' ', '%20') # it may contain spaces in city

    driver.get(url)

    num_pages = 3 # pages you want to scrape
    boats = [] # list of dicts

    for page in range(num_pages):
        
        container_results = driver.find_element(By.XPATH, "//div[@class='searchPage__products']")
        results = container_results.find_elements(By.XPATH, ".//app-search-product[@class='searchPage__productAd']")
        
        for i in results:
            try:
                link = i.find_element(By.XPATH, "//a").get_attribute("href") # for now it's temporary
                title = i.find_element(By.XPATH, ".//span[@class='dsCardDescription__title--ellipsed']").text
                price = i.find_element(By.XPATH, ".//h4[@class='dsCardDescription__subtitle']").text
                boats.append({"link":link,"title":title,"price":price}) # add to the list of dicts
            except:
                pass
            
        try:
            driver.implicitly_wait(3)
            next_button = driver.find_element(By.XPATH, "//li[@class='pagination__item--next']/a")
            next_button.click() # this clicks the button to pass on the other page
        except:
            break # if it doesn't exist, quit the scraping
    
    return boats 

def search_by_city(request, parameter):
    status = "success" # to use if errors, it needs updates
    error = None # for future development with the use of errors
    
    boats_list = scraping_clickandboat(parameter)

    data = {
        "status": status,
        "boats": boats_list,
        "error": error
    }

    return JsonResponse(data)
