from selenium import webdriver
from selenium.webdriver.common.by import By
from math import fabs
import time
from dotenv import load_dotenv
import os

load_dotenv()

url = input('Вставьте ссылку на тест по математике: ')


options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36')

driver = webdriver.Chrome(options=options)
driver.minimize_window()

driver.get(url=url)
driver.minimize_window()

email_input = driver.find_element('id', 'Email')
email_input.clear()
email_input.send_keys(os.getenv('EMAIL'))

password_input = driver.find_element('id', 'Password')
password_input.clear()
password_input.send_keys(os.getenv('PASSWORD'))

driver.find_element('id', 'RememberMe').click() # клик по "Запомнить меня"

driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()

# ПЕРЕШЛИ НА СТРАНИЦУ С РЕЗУЛЬТАТАМИ


misstakes = driver.find_elements(By.CSS_SELECTOR, '.qmap-total-label.status-mistake')
skipped = driver.find_elements(By.CSS_SELECTOR, '.qmap-total-label.status-skipped')
missed = driver.find_elements(By.CSS_SELECTOR, '.qmap-total-label.status-missed')

error = misstakes[0].text
if len(skipped) == 0:
    skip = int(fabs(5 - int(missed[0].text)))
elif len(missed) == 0:
    skip = int(fabs(5 - int(skipped[0].text)))
else:
    skip = int(fabs(5 - (int(missed[0].text) + int(skipped[0].text))))


if int(skip) == 0 and int(error) == 0:
    print('<<< Ничего не писать >>>')

if int(error) == 0:
    if int(skip) == 1:
        print(f'{skip} задание пропущено в части с кратким ответом')
    elif int(skip) in (2, 3, 4):
        print(f'{skip} задания пропущено в части с кратким ответом')
    else:
        print(f'{skip} заданий пропущено в части с кратким ответом')

if int(skip) == 0:
    if int(error) == 1:
        print(f'{error} ошибка в части с кратким ответом')
    elif int(error) in (2, 3, 4):
        print(f'{error} ошибки в части с кратким ответом')
    else:
        print(f'{error} ошибок в части с кратким ответом')

if int(skip) != 0 and int(error) != 0:
    if int(error) == 1:
        if int(skip) == 1:
            print(f'{error} ошибка, {skip} пропущенное задание в части с кратким ответом')
        else:
            print(f'{error} ошибка, {skip} пропущенных заданий в части с кратким ответом')
    elif int(error) in (2, 3, 4):
        if int(skip) == 1:
            print(f'{error} ошибки, {skip} пропущенное задание в части с кратким ответом')
        else:
            print(f'{error} ошибки, {skip} пропущенных заданий в части с кратким ответом')
    else:
        if int(skip) == 1:
            print(f'{error} ошибок, {skip} пропущенное задание в части с кратким ответом')
        else:
            print(f'{error} ошибок, {skip} пропущенных заданий в части с кратким ответом')

driver.close()
driver.quit()
time.sleep(1000)
