

from re import template
import time
import csv
from tkinter import*

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


driver = webdriver.Chrome(executable_path="C:\selenium\chromedriver_win32\chromedriver.exe", options=options)


def check_for_paid():
    view_btn = "inmail-component__button--tertiary"
    view_btn_element = driver.find_element(By.CLASS_NAME, view_btn)
    view_btn_element.click()
    paid_list = []
 
    try:
        inmail_paid = "/html/body/div[4]/div[6]/base-slidein-container/div/div/div[2]/div/form/div[2]/div[1]/div[1]/section/dl/dd[2]"
        inmail_element_paid = driver.find_element(By.XPATH, inmail_paid)
        var = inmail_element_paid.find_elements(
        By.CLASS_NAME, "compose-recipients__msg-to-list-item")
        time.sleep(1)    
        for k in var:
            paid_list.append(k.text)
    except:
        print("no Paid in mail found")    
        
    print(paid_list)
    return paid_list

# Select All Button...
def send_msg_fun(template_name):
    search_isempty=0
    driver.implicitly_wait(5)
    time.sleep(3)
    try:
        check_box = "profile-list__select-all"

        check_box_ele = driver.find_element(By.CLASS_NAME, check_box)
        check_box_ele.click()
    except:
        search_isempty = 1
        return search_isempty   


    # # Message Button...
    msg_btn = "/html/body/div[4]/div[5]/div/div[2]/section/div[3]/div/div/div[1]/div/section/div/div/div/div[1]/div/span/div/form/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/ul/li[2]/button/span"
                       

    msg_btn_element = driver.find_element(By.XPATH, msg_btn)
    msg_btn_element.click()
    
    flag = check_for_paid()

    if(len(flag) != 0):
        print("exiting.....")
        exit(0)
    else:
        input_path = "/html/body/div[4]/div[6]/base-slidein-container/div/div/div[2]/div/div/div/div[1]/div[1]/div/input"

        input_element = driver.find_element(By.XPATH, input_path)
        input_element.send_keys(template_name)


        time.sleep(2)



        form_path = "/html/body/div[4]/div[6]/base-slidein-container/div/div/div[2]/div/div/div/div[1]/ul/form"
        form_element = driver.find_element(By.XPATH,form_path)
        uls_path = "/html/body/div[4]/div[6]/base-slidein-container/div/div/div[2]/div/div/div/div[1]/ul/form/div/ul"
        uls_count = form_element.find_elements(By.XPATH, uls_path)

        print("length of ul : ", len(uls_count))

        for i in range(1, len(uls_count)+1):
            flag = 0
            try:
                li_path = "/html/body/div[4]/div[6]/base-slidein-container/div/div/div[2]/div/div/div/div[1]/ul/form/div/ul[" + str(i) + "]/li"
                li_count = driver.find_element(By.XPATH, li_path)
                div_path= "/html/body/div[4]/div[6]/base-slidein-container/div/div/div[2]/div/div/div/div[1]/ul/form/div/ul[" + str(i) + "]/li/li/div[1]"
                div_element= driver.find_elements(By.XPATH, div_path)
                for element in enumerate(div_element):
                    # print("elemts ka text : ",element[1].text)
                    if element[1].text.lower() == template_name.lower():
                        print("found\n")
                        element[1].click()
                        flag = 1

                        break
                if flag == 1:
                    break


            except Exception as e:
                print("Exception in loop : ", e)
            time.sleep(1)

        send_msg = "/html/body/div[4]/div[6]/base-slidein-container/div/div/div[2]/div/form/section/div[2]/div/button/span[2]"
                 
        send_msg_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, send_msg)))
        send_msg_element.click()
        time.sleep(2)
    return search_isempty
    
           
def change_state_fun():
    time.sleep(3)
   



    change_state="/html/body/div[4]/div[5]/div/div[2]/section/div[3]/div/div/div[1]/div/section/div/div/div/div[1]/div/span/div/form/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/ul/li[3]/div/div[1]/button/span[1]"
    change_state_ele= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, change_state)))
    change_state_ele.click()

    time.sleep(1)
    contacted_path="/html/body/div[4]/div[5]/div/div[2]/section/div[3]/div/div/div[1]/div/section/div/div/div/div[1]/div/span/div/form/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/ul/li[3]/div/div[1]/div/div/ol/li[2]/div/span[2]"
    contacted_ele=driver.find_element(By.XPATH,contacted_path).click()



def fun_main():
  
    linkk=a.get()
    templatee=b.get()


    driver.get(linkk)
    print(driver.title)

    driver.implicitly_wait(10)
    time.sleep(3)
    rows = []
 
    while True:    
        flag=0
        flag=send_msg_fun(templatee)
        try : 
            # cancel_btn = "/html/body/div[4]/div[6]/base-slidein-container/div/div/div[1]/button/li-icon"
                       
            # cancel_btn_element = driver.find_element(By.XPATH, cancel_btn)
            # print("cancel button clicked")
            # cancel_btn_element.click()
        except Exception as e:
            print("Exce in while : ", e)

        if(flag):
            print("condition broke")
            break
        # change_state_fun()   

        time.sleep(3)


root = Tk()
root.title("Send messages")

root.resizable(0,0)
root.configure(background='black')

#create text boxes
a = Entry(root, width = 30, borderwidth=0)
a.grid(row=0, column=1, padx=40, pady=(15, 0))

b = Entry(root, width = 30, borderwidth=0)
b.grid(row=1, column=1, pady=(5, 0))


# create text box label 
a_label = Label(root, text="Project Link", bg="black", fg="white")
a_label.grid(row=0, column=0, pady=(20, 5))

b_label = Label(root, text="Message Template Name" , bg="black", fg="white")
b_label.grid(row=1, column=0, pady=(10, 10), padx=(34, 0))

print("--------------------------------------")
print("--------------------------------------")
 


#create submit button
submit_btn = Button(root, text="Send Message", command=fun_main, pady=3, padx=15, bg="white")
submit_btn.grid(row=6, column=0, columnspan=2, padx=20, pady=20, ipadx=100)



root.mainloop()