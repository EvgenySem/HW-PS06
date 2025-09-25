import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
url = "https://www.divan.ru/category/svet"

browser.get(url)
time.sleep(3)

light_cards = browser.find_elements(By.CLASS_NAME, 'LlPhw')
parsed_data = []

for light_card in light_cards:
    try:
        name = light_card.find_element(By.CLASS_NAME, 'lsooF').find_element(By.TAG_NAME, 'span').text
        price = light_card.find_element(By.CLASS_NAME, 'q5Uds').find_element(By.TAG_NAME, 'span').text
        url = light_card.find_element(By.TAG_NAME, 'a').get_attribute('href')
    except:
        print("Не удалось найти информацию")
        continue

    parsed_data.append([name, price, url])

browser.quit()


with open('lights.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Название товара", "Цена", "Ссылка на товар"])
    writer.writerows(parsed_data)
