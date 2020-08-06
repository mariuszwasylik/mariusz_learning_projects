from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path='C:\\Users\Mariusz\Desktop\Testowanie_automatyczne\chromedriver_win32\chromedriver.exe')
browser.get('https://app-pea-author6-prod.avallain.net/login')
browser.maximize_window()

username_input = browser.find_element_by_name('username')
password_input = browser.find_element_by_name('password')

# login process
username_input.send_keys('mwasylik')
password_input.send_keys('mariuszw')
browser.maximize_window()

login = browser.find_element_by_class_name('css-1eaa88k')
login.submit()
time.sleep(5.0)

# home page navigation and creating Learning Object template
home = browser.find_element_by_id('app-navigation-home')
home.click()

content_menu = browser.find_element_by_id('project-navigation-content')
content_menu.click()
time.sleep(8.0)

create_LO = browser.find_element_by_id('cmdBttWPCreateLO')
create_LO.click()
time.sleep(2.0)
name_LO = browser.find_element_by_id('createLOForm:loName')
name_LO.send_keys('test_object')

continue_button = browser.find_element_by_id('createLOForm:continueButton')
continue_button.click()
time.sleep(8.0)

# editing options (sorry za brak definicji :) )
browser.find_element_by_id('cmdBttEditLOOptions').click()
time.sleep(4.0)
browser.find_element_by_xpath('//*[@id="LOOptionsDialogForm:catoptions:optionslist:7:options:0:optionSelect"]/div[3]').click()
time.sleep(4.0)
browser.find_element_by_id('LOOptionsDialogForm:catoptions:optionslist:7:options:0:optionSelect_1').click()
time.sleep(4.0)
browser.find_element_by_id('LOOptionsDialogForm:cmdBttLOOptions_LOOptionsDialog_ok').click()
time.sleep(4.0)
browser.find_element_by_id('tabs:activityType').click()
time.sleep(4.0)
browser.find_element_by_id('tabs:activityType_4').click()
time.sleep(4.0)
browser.find_element_by_id('tabs:activityName').clear()
time.sleep(4.0)
browser.find_element_by_id('tabs:activityName').send_keys('test_object')
time.sleep(4.0)
browser.find_element_by_xpath('//*[@id="tabs"]/ul/li[2]/a').click()
time.sleep(4.0)

# save and exit to content menu
browser.find_element_by_id('save').click()
time.sleep(5.0)
browser.find_element_by_id('project-navigation-content').click()
time.sleep(3.0)

# search for test_object on the list
search = browser.find_element_by_id('searchinput_learningobject_input')
search.send_keys('test_object')
time.sleep(4.0)

browser.quit()

