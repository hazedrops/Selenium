from selenium import webdriver
# Need to be imported to use the time sleep for the loading period
from selenium.webdriver.common.by import By
# Need to be imported to use the time sleep for the loading period
from selenium.webdriver.support.ui import WebDriverWait
# Need to be imported to use the time sleep for the loading period
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://flight.naver.com/flights/"
browser.get(url)

browser.find_element_by_link_text("가는날 선택").click()

# Select 27th, 28th of this month
# # Pick the 27 of this month by taking [0]th of "27"s
# browser.find_elements_by_link_text("27")[0].click()

# # Pick the 28 of this month by taking [0]th of "28"s
# browser.find_elements_by_link_text("28")[0].click()

# Select 27th, 28th of the next month - [1]
# browser.find_elements_by_link_text("27")[1].click()
# browser.find_elements_by_link_text("28")[1].click()

# Pick 27th of this month & 28th of the next month
browser.find_elements_by_link_text("27")[0].click()
browser.find_elements_by_link_text("28")[1].click()

# Pick "Jeju"
browser.find_element_by_xpath(
    "//*[@id='recommendationList']/ul/li[1]").click()

# Click "Search Flight Ticket" button
browser.find_element_by_link_text("항공권 검색").click()

# Wait 10 second max, until the element of the xpath is located
# If the element is not located until the 10 second has passed, then error will be occured
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    # Output the first search result
    print(elem.text)

finally:
    browser.quit()

# # Output the first search result
# elem=browser.find_element_by_xpath(
#     "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# print(elem.text)
