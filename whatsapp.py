from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

browser = webdriver.Chrome()
browser.get('https://web.whatsapp.com')
time.sleep(14)

wait = WebDriverWait(browser, 600)

message = "Hello\nThis msg is sent using Python"

def send_msg():
    browser.find_element_by_class_name('_whatsapp_www__block_action')
    continue_to_chat_btn = browser.find_element_by_class_name('_whatsapp_www__block_action')
    continue_to_chat_btn.click()
    time.sleep(1)

    use_waweb_btn = browser.find_element_by_link_text('use WhatsApp Web')
    use_waweb_btn.click()
    time.sleep(5)

    inp_xpath = '//div[@class="_3FRCZ copyable-text selectable-text"][@dir="ltr"][@data-tab="1"]'
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath))) 

    input_box.send_keys(message + Keys.ENTER)

numbers = []
with open('numbers.txt', mode='r') as file:
    numbers = file.readlines()

for i in range(2):
    browser.get(f'https://wa.me/91{numbers[i]}')
    send_msg()
    time.sleep(2)

browser.quit()