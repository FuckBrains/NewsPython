import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome(executable_path=os.path.join(os.getcwd(), 'chromedriver'))
driver.maximize_window()


wait = WebDriverWait(driver, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

driver.get("https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.find_element_by_id("identifierId").send_keys("zopplrmedia@gmail.com");

#wait.until(visible(By.XPATH("//div[@id='identifierNext']/div/button")))
driver.find_element_by_xpath("//div[@id='identifierNext']/div/button").click()
#wait.until(visible(By.XPATH("//input[@name='password']")))
driver.find_element_by_xpath("//input[@name='password']").send_keys("Password@123")
#wait.until(visible(By.XPATH("//div[@id='passwordNext']/div/button")))
driver.find_element_by_xpath("//div[@id='passwordNext']/div/button").click()

