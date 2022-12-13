from selenium import webdriver
from selenium.webdriver.support.select import Select,By
import time
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
import os
from pathlib import Path
import pandas as pd
import openpyxl


options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--disable-extensions")
options.add_experimental_option('useAutomationExtension', False)

file_path =str(Path(__file__).resolve().parent.parent)
print("abhishek ",file_path)
driver = webdriver.Chrome(file_path+'\cromedriver.exe',options=options)

product_link = 'https://www.ajio.com/puma-flair-2-lace-up-running-shoes/p/469112409_grey?user=new'
driver.get(product_link)
time.sleep(5)
x_path= '//*[@id="appContainer"]/div[2]/div/div/div[2]/div/div[3]/div/div[4]/div[1]/div[2]/div[2]/div[1]/span[2]'

cell_text = driver.find_element('xpath',x_path).text
print("offer price",cell_text)
if(cell_text < '₹1700') :
    print("its offer time")

print(file_path)
df = pd.read_excel(file_path+'\Ajio_price_alter\products_track.xlsx')
# print(df.df.itertuples())
# writing logic for iterate over rows and check for condition true
for i in df.itertuples():
    product_link = i.Product_link
    driver.get(product_link)
    time.sleep(5)
    x_path= '//*[@id="appContainer"]/div[2]/div/div/div[2]/div/div[3]/div/div[4]/div[1]/div[2]/div[2]/div[1]/span[2]'

    cell_text = driver.find_element('xpath',x_path).text
    print("offer price",cell_text)
    if(i.Expected_Price >= int(cell_text[1:]) ) :
        print("its offer time")
time.sleep(10)
