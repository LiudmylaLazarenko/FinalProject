from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver')
driver.get("https://botanikabeauty.com/")

driver.maximize_window()

logo = driver.find_element_by_xpath("//img[@alt='BotanikaBeauty']")

#Twitter
Twitter = driver.find_element_by_xpath("//a[@title='BotanikaBeauty on Twitter']")
Twitter.click()
driver.find_element_by_xpath("//*[@id]//h1/a").is_displayed

#Facebook
Facebook = driver.find_element_by_xpath("//a[@title='BotanikaBeauty on Facebook']")
Facebook.click()
driver.find_element_by_xpath("//*[@id]/div/div[1]/div/div[2]/div[1]/a").is_displayed

#Instagram
Instagram = driver.find_element_by_xpath("//a[@title='BotanikaBeauty on Instagram']")
Instagram.click()
driver.find_element_by_xpath("//img[@alt='Instagram']").is_displayed

#Home
Home = driver.find_element_by_xpath("//a[@title='Home']")
Home.click()

#Contact Us
Contact_Us = driver.find_element_by_xpath("//li[6]/a/span")
Contact_Us.click()

#Terma Of Service
Terms_Of_Service = driver.find_element_by_xpath("//a[contains(text(),'Terms Of Service')]")
Terms_Of_Service.click()
