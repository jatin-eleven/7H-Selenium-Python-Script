
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



def inmail_list_fun():
    # Select All Button...
    driver.implicitly_wait(5)
    time.sleep(5)
    check_box = "profile-list__select-all"

    check_box_ele = driver.find_element(By.CLASS_NAME, check_box)
    check_box_ele.click()


    # # Message Button...
    msg_btn = "/html/body/div[3]/div[5]/div/div[2]/section/div[3]/div/div/div/div[1]/div[1]/div/div/div/section/span/div/form/div[1]/div/div[1]/div/div/div/div/div/div/div/div/div/div/ul/li[3]/button/span"
    # msg_btn = "/html/body/div[3]/div[5]/div/div[2]/section/div[3]/div/div/div/div[1]/div[1]/div/div/div/section/span/div/form/div[1]/div/div[1]/div/div/div/div/div/div/div/div/div/div/ul/li[4]/button/span/span[1]"
    msg_btn_element = driver.find_element(By.XPATH, msg_btn)
    msg_btn_element.click()


    # View All Button...
    view_btn = "inmail-component__button--tertiary"
    view_btn_element = driver.find_element(By.CLASS_NAME, view_btn)
    view_btn_element.click()


    # Extracting all the free InMail Person names...

    inmail_list = []
    try:
        inmail = "/html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/div/form/div[2]/div[1]/div[1]/section/dl[2]/dd"
        inmail_element = driver.find_element(By.XPATH, inmail)
        var = inmail_element.find_elements(
        By.CLASS_NAME, "compose-recipients__msg-to-list-item")
        time.sleep(1)    
        for k in var:
            inmail_list.append(k.text)


    except:
        print("no free in mail found")    

    print(inmail_list)
    paid_list = []
    try:
        inmail_paid = "/html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/div/form/div[2]/div[1]/div[1]/section/dl[1]/dd"
        inmail_element_paid = driver.find_element(By.XPATH, inmail_paid)
        var = inmail_element_paid.find_elements(
        By.CLASS_NAME, "compose-recipients__msg-to-list-item")
        time.sleep(1)    
        for k in var:
            paid_list.append(k.text)


    except:
        print("no Paid in mail found")    

    print(paid_list)


    # Cancel Button...
    cancel_btn = "inmail-component__button-tertiary-muted"
    cancel_btn_element = driver.find_element(By.CLASS_NAME, cancel_btn)
    cancel_btn_element.click()


    # Uncheck button..
    check_box = "profile-list__select-all"
    check_box_ele = driver.find_element(By.CLASS_NAME, check_box)
    check_box_ele.click()


    return inmail_list,paid_list

temp_list= []


# # looping into all Li presents...
def saving_to_next(inmail_list,paid_list,free_project,paid_project, limit):
    global  free_counter
    free_counter=0

    variablee = 0
    ol_path = "/html/body/div[3]/div[5]/div/div[2]/section/div[3]/div/div/div/div[1]/div[1]/div/div/div/section/span/div/form/ol"
    ol_ele = driver.find_element(By.XPATH, ol_path)


    try:
        li_ele = ol_ele.find_elements(By.CLASS_NAME, "profile-list__border-bottom")
    except:
        variablee=1
        print("Exception : No Li Foound : ", variablee)


    print(len(li_ele))
    li_Counter = 0
    for i in li_ele:
        print("in for")
        li_Counter += 1
        print(li_Counter)
        if(li_Counter < 26):
            if(li_Counter % 2 == 0):
                driver.execute_script("window.scrollBy(0,340);")
                print("scroling")
            try:
                span = "/html/body/div[3]/div[5]/div/div[2]/section/div[3]/div/div/div/div[1]/div[1]/div/div/div/section/span/div/form/ol/li["+ str(li_Counter)+"]/div/article/div/article/article/div/div[1]/div[1]/section/div/div[2]/span/span/div/a"
                span_ele = WebDriverWait(i, 10).until(EC.presence_of_element_located((By.XPATH, span)))
                span_ele = i.find_element(By.XPATH, span)
                textt = span_ele.text
            except Exception as E:
                error_name_list.append(textt)
                print("\n\nException : ",E)

            # temp_list.append(textt)
            # print(temp_list)
            if str(textt) in inmail_list:
                free_counter+=1
                
                print("Matched->dotbutton")
                try:
                    # dot_btn = "/html/body/div[3]/div[5]/div/div[2]/section/div[3]/div/div/div/div[1]/div[1]/div/div/div/section/span/div/form/ol/li["+ str(li_Counter)+"]/div/article/div/article/article/div/div[2]/aside/span/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/button"
                    dot_btn="/html/body/div[3]/div[5]/div/div[2]/section/div[3]/div/div/div/div[1]/div[1]/div/div/div/section/span/div/form/ol/li["+ str(li_Counter) +"]/div/article/div/article/article/div/div[2]/aside/span/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/button"         
                    dot_bt_ele = i.find_element(By.XPATH, dot_btn)
                    dot_bt_ele.click()
                except Exception as e:
                    error_name_list.append(textt)
                    print("exeption in dot button",e)

                print("->save project button")
                    
                time.sleep(3)
                try : 
                    save_to_project_path = "/html/body/div[3]/div[5]/div/div[2]/section/div[3]/div/div/div/div[1]/div[1]/div/div/div/section/span/div/form/ol/li["+ str(li_Counter)+"]/div/article/div/article/article/div/div[2]/aside/span/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/ul/li[4]/div"

                    save_to_project_ele = driver.find_element(By.XPATH, save_to_project_path).click()
                except:
                    error_name_list.append(textt)
                    print("Exception in Project btn :" )

                driver.implicitly_wait(5)
                time.sleep(3)
                print("sending keys")
                projectname_field = "/html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/form/div[1]/div[1]/div/div[1]/div/div/input"
                
                # projectname_element = driver.find_element(By.XPATH, projectname_field)

                # wait 10 seconds before looking for element
                projectname_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, projectname_field))
                )
                projectname_element.send_keys(free_project)
                print("clicking project ")
                time.sleep(2)

                path = "/html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/form/div[1]/div[1]/div/ul"
                # path="/html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/form/div[1]/div[1]/div/div[2]"
                project_dropdwn=driver.find_element(By.XPATH,path)
                projects=project_dropdwn.find_elements(By.CLASS_NAME,"project-lockup-title")

                print(projects, "\n\n\n")

                counter=0
                try : 
                    for i in projects: 
                        counter+=1
                        # project_list.append(i.text)
                        print(counter)

                        if(free_project==i.text):
                            print(counter)
                            time.sleep(2)
                                                                #    /html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/form/div[1]/div[1]/div/ul/li[1]/div/div[1]/span/
                            # project_dropdwn.find_element(By.XPATH,"/html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/form/div[1]/div[1]/div/div[2]/div["+ str(counter) +"]/div/div[1]").click()
                            project_dropdwn.find_element(By.XPATH, "/html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/form/div[1]/div[1]/div/ul/li[" + str(counter)+"]/div/div[1]/span").click()
                            break
                except Exception as e:
                    print("Exception in  project clicking  : ", e)
    
                print("save button clicked")
                savebtn = "/html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/form/div[2]/button[2]"
                savebtn_ele = driver.find_element(By.XPATH, savebtn)
                savebtn_ele.click()
                # time.sleep(2)
                print(textt, "\n\nsaved")
                time.sleep(3)

                print("haan mai hi hu ",limit)
                print("haan mai hi hu free counter :  ",free_counter)

                if(free_counter==limit):
                    variablee = 100
                    print("haan mai chal ra  hu")
                    break
                    

            # elif str(textt) in paid_list:
            #     print("Matched->dotbutton")
            #     try:
            #         # dot_btn = "/html/body/div[3]/div[5]/div/div[2]/section/div[3]/div/div/div/div[1]/div[1]/div/div/div/section/span/div/form/ol/li["+ str(li_Counter)+"]/div/article/div/article/article/div/div[2]/aside/span/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/button"
            #         dot_btn="/html/body/div[3]/div[5]/div/div[2]/section/div[3]/div/div/div/div[1]/div[1]/div/div/div/section/span/div/form/ol/li["+ str(li_Counter) +"]/div/article/div/article/article/div/div[2]/aside/span/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/button"         
            #         dot_bt_ele = i.find_element(By.XPATH, dot_btn)
            #         dot_bt_ele.click()
            #     except Exception as e:
            #         error_name_list.append(textt)
            #         print("exeption in dot button",e)

            #     print("->sending keys")
            #     time.sleep(3)
            #     try : 
            #         save_to_project_path = "/html/body/div[3]/div[5]/div/div[2]/section/div[3]/div/div/div/div[1]/div[1]/div/div/div/section/span/div/form/ol/li["+ str(li_Counter)+"]/div/article/div/article/article/div/div[2]/aside/span/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div/div/div/ul/li[4]/div"

            #         save_to_project_ele = driver.find_element(By.XPATH, save_to_project_path).click()
            #     except:
            #         error_name_list.append(textt)
            #         print("Exception in Project btn :" )
            #     driver.implicitly_wait(5)
            #     projectname_field = "/html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/form/div[1]/div[1]/div/div[1]/div/div/input"
            #     projectname_element = driver.find_element(By.XPATH, projectname_field)
            #     projectname_element.send_keys(paid_project)
            #     print("drop down ")
            #     time.sleep(2)

            #     try:
            #         # drop_down = '/html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/form/div[1]/div[1]/div/div[2]'
            #         drop_down = "/html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/form/div[1]/div[1]/div/div[2]/div[1]/div/div[1]/span"
            #         drop_down_ele = driver.find_element(By.XPATH, drop_down)
            #         # print(drop_down_ele.text)
            #         time.sleep(2)
            #         drop_down_ele.click()
            #     except Exception as e:
            #         error_name_list.append(textt)
            #         print("exception in drop down : ", e)

            #     savebtn = "/html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/form/div[2]/button[2]"
            #     savebtn_ele = driver.find_element(By.XPATH, savebtn)
            #     savebtn_ele.click()
            #     print(textt, "\n\nsaved")
            #     time.sleep(3)

            else:
                print("Omitted")
                time.sleep(3)

        else:
            print("li_couter>25")
            
            

    return variablee





def add_note_fun():
    # check button..
    check_box = "profile-list__select-all"
    check_box_ele = driver.find_element(By.CLASS_NAME, check_box)
    check_box_ele.click()
    add_note_btn = "/html/body/div[3]/div[5]/div/div[2]/section/div[3]/div/div/div/div[1]/div[1]/div/div/div/section/span/div/form/div[1]/div/div[1]/div/div/div/div/div/div/div/div/div/div/ul/li[5]/button/span"
    note_btn_element = driver.find_element(By.XPATH, add_note_btn)
    note_btn_element.click()
    # driver.implicitly_wait(3)
    time.sleep(2)

    
    anyone = "/html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/div[1]/form/fieldset/label[3]"
    anyone_btn = driver.find_element(By.XPATH, anyone)
    time.sleep(1)

    anyone_btn.click()


    note_msg = "/html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/div[1]/form/fieldset/label[2]"
    note_msg_element = driver.find_element(By.XPATH, note_msg)
    note_txt = note_msg_element.text

    print("primtedddd", note_txt)


    seach_area = "mentions-edit__text-box"
    search_btn = driver.find_element(By.CLASS_NAME, seach_area)
    search_btn.send_keys(note_txt)

    add_to = "/html/body/div[3]/div[6]/base-slidein-container/div/div/div[2]/div[1]/form/div[2]/div/button[2]"
    add_to_btn = driver.find_element(By.XPATH, add_to)
    add_to_btn.click()
    driver.refresh()
    driver.implicitly_wait(5)


    print("\n\n\nAdd Note Function : Done\n\n\n")
    driver.execute_script("window.scrollTo(100,-340);")




# main---------------------------
driver.implicitly_wait(10)
time.sleep(3)
rows = []
with open("C:/Users/pc/Desktop/JATIN-HARSHAL-TESTING/chat_testing/data2.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
        
    for i in rows:    
        print(i[0])
        driver.get(row[0])
        free_project=row[1]
        paid_project=row[2]
        print(row[1])
        print(row[2])
        print(row[3])
        print(int(row[3]))
        while True:    
            flag=0
            # driver.implicitly_wait(5)
            time.sleep(3)
            free_list, paid_list = inmail_list_fun()
            index = int(row[3])

            if(len(free_list)!=0 or len(paid_list)!=0):
                flag =saving_to_next(free_list, paid_list,free_project,paid_project, index)
            if(flag!=100):
                add_note_fun()
            print("\n\n\tlist : ", error_name_list)
            if flag == 1 or flag == 100:
                print("DONNNNNEEEEE")
                break

