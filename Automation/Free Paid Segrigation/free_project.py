
import time
import csv
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "localhost:9014")

options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")


free_counter = 0


driver = webdriver.Chrome(executable_path="C:\selenium\chromedriver_win32\chromedriver.exe", options=options)
print(driver.title)



def inmail_list_fun():

    check_box = "profile-list__select-all"
    check_box_ele=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, check_box)))
    check_box_ele.click()

    # # Message Button...
    msg_btn =  "/html/body/div[3]/div[5]/div/div[2]/section/div[3]/div/div/div/div[1]/div[1]/section/div/div/section/span/div/form/div[1]/div/div[1]/div/div/div/div/div/div/div/div/div/div/ul/li[3]/button/span"
            
    msg_btn_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, msg_btn)))
    msg_btn_element.click()


    # View All Button...
    view_btn = "inmail-component__button--tertiary"
    view_btn_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, view_btn)))
    view_btn_element.click()


    # Extracting all the free InMail Person names...
    inmail_list = []
    try:
        inmail = "/html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/div/form/div[2]/div[1]/div[1]/section/dl[2]/dd"
        inmail_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, inmail)))

        var = WebDriverWait(inmail_element, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME,  "compose-recipients__msg-to-list-item")))
        time.sleep(1)    
        for k in var:
            inmail_list.append(k.text)


    except:
        print("no free in mail found")    

    print(inmail_list)
    


    # Cancel Button...
    cancel_btn = "inmail-component__button-tertiary-muted"
    cancel_btn_element  = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME,  cancel_btn)))
    cancel_btn_element.click()


    # Uncheck button..
    check_box = "profile-list__select-all"
    check_box_ele = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME,  check_box)))
    check_box_ele.click()


    return inmail_list

temp_list= []


# # looping into all Li presents...
def saving_to_next(inmail_list,free_project, limit):
    global  free_counter
    free_counter=0

    variablee = 0
    ol_path = "/html/body/div[3]/div[5]/div/div[2]/section/div[3]/div/div/div/div[1]/div[1]/section/div/div/section/span/div/form/ol"
              
    ol_ele = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,ol_path)))


    try:
        li_ele = WebDriverWait(ol_ele, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME,  "profile-list__border-bottom")))
    except:
        variablee=1
        print("Exception : No Li Foound : ", variablee)


    li_Counter = 0
    for i in li_ele:
        li_Counter += 1
        print(li_Counter)
        if(li_Counter < 26 ):
            driver.execute_script("arguments[0].scrollIntoView();", i)   
            print("scrolling")
            driver.execute_script("window.scrollBy(0, -200);")
            try:
                span="/html/body/div[3]/div[5]/div/div[2]/section/div[3]/div/div/div/div[1]/div[1]/section/div/div/section/span/div/form/ol/li["+ str(li_Counter)+"]/div/article/div/article/article/div/div[1]/div[1]/section/div/div[2]/span/span[1]/div/a"                
                span_ele = WebDriverWait(i, 10).until(EC.presence_of_element_located((By.XPATH, span)))
                textt = span_ele.text
                print("name= ",textt)
            except Exception as E:
                print("\n\nException for a: ",E)

            if str(textt) in inmail_list:
                free_counter+=1
                try:
                    dot_btn="/html/body/div[3]/div[5]/div/div[2]/section/div[3]/div/div/div/div[1]/div[1]/section/div/div/section/span/div/form/ol/li["+ str(li_Counter) +"]/div/article/div/article/article/div/div[2]/aside/span/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/button"         
                    dot_bt_ele = WebDriverWait(i, 10).until(EC.presence_of_element_located((By.XPATH, dot_btn)))
                    dot_bt_ele.click()
                except Exception as e:
                    print("exeption in dot button",e)
                    
                time.sleep(3)
                try : 
                    save_to_project_path = "/html/body/div[3]/div[5]/div/div[2]/section/div[3]/div/div/div/div[1]/div[1]/section/div/div/section/span/div/form/ol/li["+ str(li_Counter)+"]/div/article/div/article/article/div/div[2]/aside/span/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/ul/li[4]/div"

                    save_to_project_ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, save_to_project_path)))
                    save_to_project_ele.click()
                except:
                    print("Exception in Project btn :" )

                driver.implicitly_wait(5)
                time.sleep(3)
                projectname_field = "/html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/form/div[1]/div[1]/div/div[1]/div/div/input"

                # wait 10 seconds before looking for element
                projectname_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, projectname_field))
                )
                projectname_element.send_keys(free_project)
                time.sleep(2)

                path = "/html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/form/div[1]/div[1]/div/ul"
                project_dropdwn=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, path)))
                projects=WebDriverWait(project_dropdwn, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "project-lockup-title")))


                counter=0
                try : 
                    for i in projects: 
                        counter+=1
                        print(counter)

                        if(free_project==i.text):
                            print(counter)
                            match= WebDriverWait(project_dropdwn, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/form/div[1]/div[1]/div/ul/li[" + str(counter)+"]/div/div[1]/span")))
                            match.click()

                            break
                except Exception as e:
                    print("Exception in  project clicking  : ", e)

                savebtn = "/html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/form/div[2]/button[2]"
                savebtn_ele=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH
                , savebtn)))
                savebtn_ele.click()
     
                print(textt, "\n\nsaved")
                time.sleep(3)


                if(free_counter==limit):
                    variablee = 100
                    break
              
            else:
                print("Omitted")
                time.sleep(3)

        else:
            print("li_couter>25")
                      
    return variablee





def add_note_fun():
    # check button..
    check_box = "profile-list__select-all"
    check_box_ele =WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,check_box)))
    check_box_ele.click()
    add_note_btn = "/html/body/div[3]/div[5]/div/div[2]/section/div[3]/div/div/div/div[1]/div[1]/section/div/div/section/span/div/form/div[1]/div/div[1]/div/div/div/div/div/div/div/div/div/div/ul/li[5]/button/span"
    note_btn_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,add_note_btn)))
    note_btn_element.click()
    time.sleep(2)

    
    anyone = "/html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/div[1]/form/fieldset/label[3]"
    anyone_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,anyone)))
    time.sleep(1)

    anyone_btn.click()


    note_msg = "/html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/div[1]/form/fieldset/label[2]"
    note_msg_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,note_msg)))
    note_txt = note_msg_element.text


    seach_area = "mentions-edit__text-box"
    search_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,seach_area)))
    search_btn.send_keys(note_txt)

    add_to = "/html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/div[1]/form/div[2]/div/button[2]"
    add_to_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,add_to)))
    add_to_btn.click()
    driver.refresh()
    driver.implicitly_wait(2)


    print("\n\n\nAdd Note Function : Done\n\n\n")
    driver.execute_script("window.scrollTo(100,-340);")




# main---------------------------
driver.implicitly_wait(5)
time.sleep(2)
rows = []
with open("C:/Users/affin/OneDrive/Desktop/Automation/Free Paid Segrigation/free_project.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
        
    for i in rows:    
        driver.get(row[0])
        free_project=row[1]
        paid_project=row[2]
        print(row[1])
        print(row[2])
        print(row[3])
        print(int(row[3]))
        while True:    
            flag=0
 
            time.sleep(3)
            free_list = inmail_list_fun()
            index = int(row[3])

            if(len(free_list)!=0 ):
                flag =saving_to_next(free_list,free_project, index)
            if(flag!=100):
                add_note_fun()
            if flag == 1 or flag == 100:
                print("DONNNNNEEEEE")
                break
