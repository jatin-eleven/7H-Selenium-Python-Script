
import time

from selenium import webdriver
import codecs

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

error_name_list = []

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "localhost:9014")

options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")

driver = webdriver.Chrome(executable_path="C:\selenium\chromedriver_win32\chromedriver.exe", options=options)
# driver.get("https://www.linkedin.com/talent/inbox/0/main/id/2-ZGRhODc2NzctZDFhMi00MTA1LTg4OWYtN2I0ZjZlZDQwMzRjXzAxMg==")
print(driver.title)

f = codecs.open('C:/Users/2/Desktop/jatin-harshal_testing/data2.csv', 'a', 'utf-8')

time.sleep(2)



# extracting profile link....
# ----------------------------------------------------------
def profile_link():
#    element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "myDynamicElement")))
    
    driver.implicitly_wait(5)
    try:
        div_class="/html/body/div[3]/div[5]/div/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]"
        div_ele= WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, div_class)))
        print("in try:")
        a = "/html/body/div[3]/div[5]/div/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/article/div/div[1]/div[1]/section/div/div[2]/span/span[1]/div/a"
            #  /html/body/div[3]/div[5]/div/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/article/div/div[1]/div[1]/section/div/div[2]/span/span[1]/div/a
      

    except:    
        print("div not present")
        a = "/html/body/div[3]/div[5]/div/div[2]/div[1]/div[3]/div[1]/div[1]/div/article/div/div[1]/div[1]/section/div/div[2]/span/span[1]/div/a"
    try:
        a_element = driver.find_element(By.XPATH, a)
        print("got the a:")
        print(a_element.get_attribute("href"))
        profile_link = a_element.get_attribute("href")

    except Exception as e:
        print("exception in a element",e)

    return profile_link
# ----------------------------------------------------------



# Extracting messages.......
# ----------------------------------------------------------
def chat_work(chat_name):
    f.write('\n')
    p_link =  profile_link()

    driver.implicitly_wait(5)

    f.write('"')
    f.write(chat_name)
    f.write('"')
    f.write(',')
    f.write('"')
    f.write(p_link)
    f.write('"')
    f.write(',')

    chat_panel = "/html/body/div[3]/div[5]/div/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/ul"
    panel_element = driver.find_element(By.XPATH, chat_panel)


    # message, name.. extracting....
    # ----------------------------------------------------------
    panel = "/html/body/div[3]/div[5]/div/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/ul/li"
    l_elements = driver.find_elements(By.XPATH, panel)
    # print(len(l_elements))
    tag = ""
    try:
        li_2 = "_message-reply-status_1gj1uc"
        li2_ele =  panel_element.find_element(By.CLASS_NAME, li_2)
        tag = li2_ele.text
        f.write(tag)
        f.write(",")
    except :
        print("\n exception in acc/rej tag\n ")


    iterator=0
    for i in l_elements:
        iterator += 1
        if(iterator != 1):
            f.write(" ")
            f.write(',')
            f.write(' ')
            f.write(',')
            f.write(' ')
            f.write(',')

        time.sleep(1)
        name_date="_message-metadata_1gj1uc"
        name_date_ele=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, name_date)))

        div_data = name_date_ele.text
        # print("div_data:-",div_data)
        div_data = div_data.replace("•", "_")
        div_data = div_data.replace(" at ", "_")
        div_data = div_data.replace("\n", "_")
        

        div_data = div_data.split("_")
        # print("div_data:-",div_data)

        print(div_data)
        time.sleep(2)
        
        md = ""
        try : 
            message = "_message-body_content_1gj1uc"
            message_ele = i.find_element(By.CLASS_NAME, message)
            # print(message_ele.text)
            md = message_ele.text
            md = md.replace("\n", " ")
        except Exception as e:
            print("\n\tException in message\n",e)
        strr = ""
        for ele in enumerate(div_data):
            if ele[1] != "Accepted" and ele[1] != "Declined":
                # print("ele :- ",ele)
                strr += '"' + ele[1] + '"'
                strr += ","   
                # print("str== ",strr)

        # print(md) 

        f.write(strr)
        f.write('"')
        f.write(md)
        f.write('"')
        f.write('\n')

# ----------------------------------------------------------



# looping through all li's
# ----------------------------------------------------------
ul_path = "/html/body/div[3]/div[5]/div/div[2]/div[1]/div[2]/div[2]/ul/li"
ul_list = driver.find_elements(By.XPATH, ul_path)

flagger = 90
counter = 90

while True:

    counter += 1
    flagger += 1

    try:
        pp = "/html/body/div[3]/div[5]/div/div[2]/div[1]/div[2]/div[2]/ul/li[" + str(counter) + "]/div/div/div/div[2]/div[1]/a/p"
        pp_ele =WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, pp)))
        chat_name = pp_ele.text
        print("\n\n")
        print("Name : ", pp_ele.text)
        print("counter : ", counter)

        try :
            element_path = "/html/body/div[3]/div[5]/div/div[2]/div[1]/div[2]/div[2]/ul/li[" + str(flagger) + "]"
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, element_path)))
            element.click()
            time.sleep(7)
        except Exception as e:    
            print("\n\nException in li clicking : ", e )
        
        chat_work(chat_name)
        time.sleep(3)
        driver.execute_script("arguments[0].scrollIntoView();", element)   



    except Exception as e:    
        print("\n\tException in listtttt\n", e)
        time.sleep(2)
        try:
            show_more="/html/body/div[3]/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/button"
            show_more_ele=driver.find_element(By.XPATH,show_more)
            show_more_ele.click()
            time.sleep(2)
        except Exception as e:
            print("Exception in Show more : ", e)
        flagger -= 1
        counter -= 1  
        driver.execute_script("arguments[0].scrollIntoView();", element)  