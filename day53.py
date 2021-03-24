import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep


URL = 'https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=REGION%5E87490&maxBedrooms=2&minBedrooms=1&maxPrice=300000&propertyTypes=&includeSSTC=false&mustHave=&dontShow=sharedOwnership%2Cretirement&furnishTypes=&keywords='
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
accept_lang = 'en-US,en;q=0.9'

google_form = 'https://docs.google.com/forms/d/e/1FAIpQLSeXnlrcf2eSUff9M5rrna39grisEXaM261YHCqd5i526jxPtw/viewform?usp=sf_link'

response = requests.get(URL, headers={"User-Agent":user_agent,
                           "Accept-Language":accept_lang})

web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

house_prices = []
house_links = []
house_location = []
url_start = 'www.rightmove.co.uk'
url_end = '#/'

#Get prices

house_prices_all = soup.find_all(class_='propertyCard-priceValue')

for item in house_prices_all:
    price = str(item.get_text()).strip()
    house_prices.append(price)

print(house_prices)

#Get link

for link in soup.find_all(class_='propertyCard-link'):
    house_links.append(url_start+ link.get('href')+url_end)
print(house_links)

#Get address

house_address_all = soup.find_all(class_='propertyCard-address')

for item in house_address_all:
    address = str(item.get_text()).strip('\n')
    house_location.append(address)

print(house_location)

def get_houses():
    chrome_driver_path = "/Users/annaoke/Documents/untitled folder/chromedriver"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)

    driver.get(google_form)

    for n in range(0,len(house_prices)-1):
        sleep(2)
        property_address = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        property_address.send_keys(house_location[n])
        sleep(1)

        property_price = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        property_price.send_keys(house_prices[n])
        sleep(1)

        property_link = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        property_link.send_keys(house_links[n])
        sleep(1)

        submit_button = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div').click()
        sleep(1)
        another_form = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()

get_houses()
