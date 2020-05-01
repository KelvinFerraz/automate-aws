#!/usr/bin/env python

from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.options import Log
import time
import os
import pickle
import pdfkit
import shutil
import datetime
import requests


from PIL import Image
from os import path


# Take year and month (Global)
x = datetime.datetime.now()

# Variables user 
useraws = 'user'
passwdaws = 'password'

def connected_to_internet(url='http://www.google.com/', timeout=5):
    try:
        _ = requests.get(url, timeout=timeout)
        arcaclients()
        time.sleep(5)
        arcasolutions()
        time.sleep(5)
        legacy()
        savetopdf()
    except requests.ConnectionError:
        print("No internet connection available.")
    return False

def arcaclients():

    # Display Off
    display = Display(visible=0, size=[1980, 1080])
    display.start()

    # Acess site AWS
    log = Log()
    log.level = "TRACE"
    options = Options()
    options.add_argument(log.level)
    browser = webdriver.Firefox(options=options, executable_path=r'webdriver/geckodriver', service_log_path='logs/automate.log')
    #print("Acesss the page AWS")
    browser.get("https://console.aws.amazon.com/")

    time.sleep(2)

    # Entry on Page AWS
    #print("Log-in")
    iam = browser.find_element_by_id("resolving_input")
    iam.send_keys("arcaclients")
    entry = browser.find_element_by_id("next_button")
    entry.click()


    # Use user and password
    #print("Acess whit user")
    username = browser.find_element_by_id("username")
    username.send_keys("{useraws}")
    password = browser.find_element_by_id("password")
    password.send_keys("{passwdaws}")

    # Acess AWS Console
    entrar_console = browser.find_element_by_id("signin_button")
    entrar_console.click()

    time.sleep(5)

    # Access Billings Page
    browser.get("https://console.aws.amazon.com/billing/home#/")
    time.sleep(7)

    #print("Saving Billings")
    browser.save_screenshot('img/arcaclients_billings.png') # ----- SAVE BILLINGS MONTH PAGE ON PNG ------

    # Acess Billings Details
    browser.get("https://console.aws.amazon.com/billing/home?#/bills?year={x.year}&month={x.month}")
    time.sleep(7)

    #print("Saving Billings Month")
    browser.save_screenshot('img/arcaclients_month.png') # ----- SAVE BILLINGS MONTH PAGE ON PNG ------


    # Access Cost-Management
    browser.get("https://console.aws.amazon.com/cost-management/home?#/dashboard")
    time.sleep(8)

    # save prin cost-management
    browser.save_screenshot('img/arcaclients_costmanager.png')

    time.sleep(10)
    browser.close()

def arcasolutions():
    
    # Display Off
    display = Display(visible=0, size=[1980, 1080])
    display.start()
    
    # Acess site AWS
    log = Log()
    log.level = "TRACE"
    options = Options()
    options.add_argument(log.level)
    browser = webdriver.Firefox(options=options, executable_path=r'webdriver/geckodriver', service_log_path='logs/automate.log')
    #print("Acesss the page AWS")
    browser.get("https://console.aws.amazon.com/")

    time.sleep(2)

    # Entry on Page AWS
    #print("Log-in")
    iam = browser.find_element_by_id("resolving_input")
    iam.send_keys("arcasolutions")
    entry = browser.find_element_by_id("next_button")
    entry.click()


    # Use user and password
    #print("Acess whit user")
    username = browser.find_element_by_id("username")
    username.send_keys("{useraws}")
    password = browser.find_element_by_id("password")
    password.send_keys("{passwdaws}")

    # Acess AWS Console
    entrar_console = browser.find_element_by_id("signin_button")
    entrar_console.click()

    time.sleep(5)

    # Access Billings Page
    browser.get("https://console.aws.amazon.com/billing/home#/")
    time.sleep(7)

    #print("Saving Billings")
    browser.save_screenshot('img/arcasolutions_billings.png') # ----- SAVE BILLINGS MONTH PAGE ON PNG ------

    # Acess Billings Details
    browser.get("https://console.aws.amazon.com/billing/home?#/bills?year={x.year}&month={x.month}")
    time.sleep(7)

    #print("Saving Billings Month")
    browser.save_screenshot('img/arcasolutions_month.png') # ----- SAVE BILLINGS MONTH PAGE ON PNG ------


    # Access Cost-Management
    browser.get("https://console.aws.amazon.com/cost-management/home?#/dashboard")
    time.sleep(8)

    # save prin cost-management
    browser.save_screenshot('img/arcasolutions_costmanager.png')


    time.sleep(10)
    browser.close()

def legacy():

     
    # Display Off
    display = Display(visible=0, size=[1980, 1080])
    display.start()
    
    # Acess site AWS
    log = Log()
    log.level = "TRACE"
    options = Options()
    options.add_argument(log.level)
    browser = webdriver.Firefox(options=options, executable_path=r'webdriver/geckodriver', service_log_path='logs/automate.log')
    #print("Acesss the page AWS")
    browser.get("https://console.aws.amazon.com/")

    time.sleep(2)

    # Entry on Page AWS
    #print("Log-in")
    iam = browser.find_element_by_id("resolving_input")
    iam.send_keys("arcasolutions")
    entry = browser.find_element_by_id("next_button")
    entry.click()


    # Use user and password
    #print("Acess whit user")
    username = browser.find_element_by_id("username")
    username.send_keys("{useraws}")
    password = browser.find_element_by_id("password")
    password.send_keys("{passwdaws}")

    # Acess AWS Console
    entrar_console = browser.find_element_by_id("signin_button")
    entrar_console.click()

    time.sleep(5)

    
    # Acess Billings Details
    browser.get("https://console.aws.amazon.com/cost-reports/home?#/custom?groupBy=None&hasBlended=false&hasAmortized=false&excludeDiscounts=true&excludeTaggedResources=false&excludeCategorizedResources=false&excludeForecast=false&timeRangeOption=CurrentMonth&granularity=Monthly&reportName=&reportType=CostUsage&isTemplate=true&filter=%5B%7B%22dimension%22:%22TagKeyValue%22,%22values%22:null,%22include%22:true,%22children%22:%5B%7B%22dimension%22:%22Client%22,%22values%22:%5B%22Legacy%22%5D,%22include%22:true,%22children%22:null%7D%5D%7D%5D&chartStyle=Group&forecastTimeRangeOption=Custom&usageAs=usageQuantity&startDate=2020-04-01&endDate=2020-04-30&forecastStartDate=2020-04-14&forecastEndDate=2020-04-30")
    time.sleep(7)

     # Close tutorial
    close_tutorial = browser.find_element_by_xpath("//a[@class='introjs-button introjs-skipbutton']")
    close_tutorial.click()

    #print("Saving Billings Month")
    browser.save_screenshot('img/legacy.png') # ----- SAVE BILLINGS MONTH PAGE ON PNG ------


    time.sleep(10)
    browser.close()

def savetopdf():

    #print("Exporting to PDF")
    image1 = Image.open(r'img/arcaclients_month.png')
    image2 = Image.open(r'img/arcaclients_billings.png')
    image3 = Image.open(r'img/arcaclients_costmanager.png')
    image4 = Image.open(r'img/arcasolutions_month.png')
    image5 = Image.open(r'img/arcasolutions_billings.png')
    image6 = Image.open(r'img/arcasolutions_costmanager.png')
    image7 = Image.open(r'img/legacy.png')
    im1 = image1.convert('RGB')
    im2 = image2.convert('RGB')
    im3 = image3.convert('RGB')
    im4 = image4.convert('RGB')
    im5 = image5.convert('RGB')
    im6 = image6.convert('RGB')
    im7 = image7.convert('RGB')
    imagelist = [im2,im3,im4,im5,im6,im7]
    im1.save(r'pdfs/aws_billings.pdf',save_all=True, append_images=imagelist)



# Validade connection
connected_to_internet()