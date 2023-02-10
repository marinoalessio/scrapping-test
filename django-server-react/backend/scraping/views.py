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
import re
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
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    # print(soup.prettify())

    # things to do: get the container, get info for each boat, test click for next page until 3 pages

    return None # boats_list

def search_by_city(request, parameter):
    status = "success"
    error = None
    
    boats_list = scraping_clickandboat(parameter)

    data = {
        "status": status,
        "boats": [
            {
                "link": "https://blabla",
                "title": parameter,
                "price": "123€",
            },
        ],
        "error": error
    }

    return JsonResponse(data)
