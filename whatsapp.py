from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

browser = webdriver.Chrome()
browser.get('https://web.whatsapp.com')
time.sleep(15)


wait = WebDriverWait(browser, 600)
# if we use nextline character -> (\n), two messages will be sent. Because whatsapp web uses enter to send
message = "Hello\nThis msg is sent using Python"


def send_msg():
    #continue to chat button
    continue_to_chat_btn = browser.find_element(By.LINK_TEXT, 'Continue to Chat')
    #continue_to_chat_btn = browser.find_element(By.CLASS_NAME, '_9rne _9vcv _9u4i _9scb')
    continue_to_chat_btn.click()
    time.sleep(1)

    #use whatsapp web button
    use_waweb_btn = browser.find_element(By.LINK_TEXT, 'use WhatsApp Web')
    use_waweb_btn.click()
    time.sleep(10)

    #for finding the path of input message box on whatsapp web
    inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@dir="ltr"][@data-tab="10"]'
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath))) 
    input_box.send_keys(message + Keys.ENTER)


try:
    with open('numbers.txt', mode='r') as file:
        numbers = file.readlines()
        for i in range(len(numbers)):
            browser.get(f'https://wa.me/91{numbers[i]}')
            send_msg()
            time.sleep(3)
except Exception as e:
    print(f'{e}\n"numbers.txt" file was not found')

browser.close()