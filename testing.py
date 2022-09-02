
import time
import csv
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

error_name_list = []

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "localhost:9014")

options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")


free_counter = 0

# counter = 1

driver = webdriver.Chrome(executable_path="C:\selenium\chromedriver_win32\chromedriver.exe", options=options)

print(driver.title)


# get the website
# driver.get("https://www.linkedin.com/talent/hire/733950330/discover/recruiterSearch?searchContextId=11134e2d-d75b-4276-bfbe-db79f2033af7&searchHistoryId=9973812154&searchRequestId=e454d07c-4bac-44ff-ac17-34d1be37e227&start=0")

# sleep for some time



# time.sleep(3)
# # get element through text
# try:

    
#     # a = driver.find_element(By.XPATH, "// span[contains(text(), 'Message ')]")
#     # a.click()
#     # time.sleep(3)
#     # b = driver.find_element(By.XPATH, "// button[contains(text(), 'View all')]")
#     # b.click()    
    
    
#     # msg_btn_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "// span[contains(text(), 'Message ')]")))
#     # msg_btn_element.click()
    
#     inmail_list = []
#     try:
#         inmail_element = driver.find_elements(By.XPATH, "//*[@aria-label='InMail recipients list']")



#     except Exception as e:
#         print("no free in mail found", e)    
    
# except Exception as e:
#     print("exc : ", e)

# # sleep for some time

# for j in inmail_element:
#     var = WebDriverWait(j, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME,  "compose-recipients__recipient-name")))
#     time.sleep(1)    
#     for k in var:
#         inmail_list.append(k.text)
#         print(k.text)

#     print(inmail_list)




a = "/html/body/div[3]/div[5]/div/div[2]/section/div[3]/div/div/div/div[1]/div[1]/section/div/div/section/span/div/form/ol/li[1]/div/article/span/input"
aa = driver.find_element(By.XPATH, a)

# image = wd.find_element_by_id("allImages")

# b = aa.find_element(By.XPATH, "//*[@type='checkbox']")
# data-artdeco-is-focused
driver.execute_script("arguments[0].data-artdeco-is-focused = 'false';", aa) 
# b.click()



