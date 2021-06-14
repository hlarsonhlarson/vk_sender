import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup


def scrolling_down():
    SCROLL_PAUSE_TIME = 0.5
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def friends_sender(friends):
    i = 0
    for friend in friends:
        print(friend.text)
        action = friend.find_element(By.CLASS_NAME, 'friends_field_act')
        action.click()
        time.sleep(2)
        box_container = driver.find_element(By.CLASS_NAME, 'popup_box_container')
        message_form = box_container.find_element(By.ID, 'mail_box_editable')
        message_form.send_keys(my_message)
        send_message = box_container.find_element(By.ID, 'mail_box_send')
        send_message.click()
        i += 1
        cross = driver.find_element(By.CLASS_NAME, 'notifier_close_wrap')
        cross.click()
        print('Hello ' + str(i))

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('https://vk.com/im')


    mail_box = driver.find_element(By.ID, 'email')
    mail_box.send_keys('your_mail')


    pass_box = driver.find_element(By.ID, 'pass')
    pass_box.send_keys('your_pass')

    login_button = driver.find_element(By.ID, 'login_button')
    login_button.click()

    time.sleep(2)

    driver.get('https://vk.com/friends')

    scrolling_down()

    friends = driver.find_elements(By.XPATH, '//*[contains(@id, \'friends_user_row\')]')

    print(len(friends))

    my_message = 'Простите за этот спам!!!'

    friends_sender(friends)

    driver.close()
