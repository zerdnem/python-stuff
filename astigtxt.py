from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


url = "http://astigtxt.biz/free-sms/"
driver = webdriver.Firefox()

class sendText():

    def __init__(self):
        driver.get(url)

    def sender(self):
        name = raw_input("Enter sender name: ")
        sender = driver.find_element_by_xpath("//input[@name='sender-name']")
        sender.send_keys(name)

    def network(self):
        networks = {'1':'Globe / TM','2':'Smart / TNT / Red Mobile','3':'Sun Cellular'}
        print("1. Globe/TM\n2. Smart/TNT/Red Mobile\n3. Sun Cellular")
        choice = raw_input("Enter Network [1-3]: ")
        try:
            print(networks[choice])
            network = driver.find_element_by_xpath("//select[@name='network-type']")
            for option in network.find_elements_by_tag_name('option'):
                if option.text == networks[choice]:
                    option.click()
                    break
        except KeyError:
            print('Network %s not found ' % choice)

    def cel_number(self):
        number = raw_input("Enter cellphone number [ex.09201212121]: ")
        prefix = number[:4]
        postfix = number[-7:]
        try:
            network_prefix = driver.find_element_by_xpath("//select[@name='network-prefix']")
            postfix_number = driver.find_element_by_xpath("//input[@name='7digit']")
            postfix_number.send_keys(postfix)
            for option in network_prefix.find_elements_by_tag_name("option"):
                if option.text == prefix:
                    option.click()
                    break
        except KeyError:
            print('Number % not found ' % number)

    def text_message(self):
        message = raw_input("Type your message: ")
        text_message = driver.find_element_by_name('message')
        text_message.send_keys(message)

    def captcha(self):
        img = driver.find_element_by_id("captcha")
        src = img.get_attribute('src')
        driver.get(src)
        driver.save_screenshot("captcha.png")
        driver.back()
        im = Image.open('captcha.png')
        img_str = image_to_string(im)
        print img_str
        c = raw_input("Input captcha: ")
        captcha_code = driver.find_element_by_name('code')
        captcha_code.send_keys(c)

    def submit(self):
        driver.find_element_by_id("sms_submit").click()

a = sendText()
a.sender()
a.network()
a.cel_number()
a.text_message()
a.submit()