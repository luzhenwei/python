from selenium import webdriver
browser = webdriver.Chrome(executable_path = r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
browser.get("https://account.xiaomi.com/pass/serviceLogin?callback=https%3A%2F%2Forder.mi.com%2Flogin%2Fcallback%3Ffollowup%3Dhttps%253A%252F%252Fwww.mi.com%252F%26sign%3DNzY3MDk1YzczNmUwMGM4ODAxOWE0NjRiNTU5ZGQyMzFhYjFmOGU0Nw%2C%2C&sid=mi_eshop&_bannerBiz=mistore&_qrsize=180")
"""
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
"""
name = browser.find_element_by_id("username")
pwd = browser.find_element_by_name("password")

name.send_keys("18238816132")
pwd.send_keys("LUZHENWEI123")
login_button = browser.find_element_by_id("login-button")
login_button.click()