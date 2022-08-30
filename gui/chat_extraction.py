
# cd C:\Program Files\Google\Chrome\Application && chrome.exe -remote-debugging-port=9014 --user-data-dir="C:\test\Chorme_Test_profile"
import time

from selenium import webdriver
from tkinter import *
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





# extracting profile link....
# ----------------------------------------------------------
def profile_link():
#    element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "myDynamicElement")))
    
    driver.implicitly_wait(5)
    try:
        div_class="_project-context_10umn7"
                # #   /html/body/div[4]/div[5]/div/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]
                #     /html/body/div[4]/div[5]/div/div[2]/div[1]/div[3]/div[1]/div[1]/div
                #     /html/body/div[4]/div[5]/div/div[2]/div[1]/div[3]/div[1]/div[1]/div/article
        div_ele= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, div_class)))
        print("in try:")
        a = "/html/body/div[4]/div[5]/div/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/article/div/div[1]/div[1]/section/div/div[2]/span/span[1]/div/a"
               
      
    except:    
        print("div not present")
        a = "/html/body/div[4]/div[5]/div/div[2]/div[1]/div[3]/div[1]/div[1]/div/article/div/div[1]/div[1]/section/div/div[2]/span/span[1]/div/a"
        # /html/body/div[4]/div[5]/div/div[2]/div[1]/div[3]/div[1]/div[1]/div/article/div/div[1]/div[1]/section/div/div[2]/span/span[1]/div/a
            # /html/body/div[4]/div[5]/div/div[2]/div[1]/div[3]/div[1]/div[1]
            # div/article/div/div[1]/div[1]/section/div/div[2]/span/span[1]/div/a
    try:
        print("in try 2")
        time.sleep(1)
        a_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, a)))
        # a_element = driver.find_element(By.XPATH, a)
        print("got the a:")
        print(a_element.get_attribute("href"))
        profile_link = a_element.get_attribute("href")

    except Exception as e:
        print("exception in a element",e)
    print("link== ",profile_link)
    return profile_link
monthDict={'January':1, 'Febraury':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10,'November':11,'December':12}
# ----------------------------------------------------------
def ext_recent(xx):
    print("in check")
    # f = codecs.open('C:/Users/affin/OneDrive/Desktop/JatinHarshal/data.csv', 'r+', "utf-8")
    # # x = len(f.readlines())
    # xx = f.readlines()
    # # flag=0


    print(len(xx))
    y  = 3
    if len(xx):
        for i in range(3, len(xx)):
            print(i)    
            if xx[i] == "\n":
                print("Entereed line")
                # print(xx[i-1])
                y = i-1
                print(xx[y])
                print("y  :", y)
                break
     
        print("y  :", y)
        y=xx[y]    
        print(y)
        y = y.split('"')
        print(y[3],y[5])
        var=y[3].split(" ")
        
        print(var)
        print(y[3],y[5])
        print(y)
        print("var[1]==",var[1])
        if var[1] in monthDict:
            print("in ifff")
            var[1]=monthDict[var[1]]
            print(monthDict.values())
            print("month= ",var[1])        
            var[2]=var[2].replace(",","")
            print("day",var[2]) 
            print("year",var[3]) 
            print("time", y[5])

        # f.seek()
        return int(var[1]),int(var[2]),int(var[3]),y[5]
    else:
        print("file is empty")








        return (None,None,None,None)
# ----------------------------------------------------------

    
def check(mon,dayy,yearr,timee):

    # div_data== div of message consisting name date etc
    #temp== lis formed by splitting date

    chat_panel = "/html/body/div[4]/div[5]/div/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/ul"
    panel_element = driver.find_element(By.XPATH, chat_panel)


    # message, name.. extracting....
    # ----------------------------------------------------------
    panel = "/html/body/div[4]/div[5]/div/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/ul/li"
    
    l_elements = driver.find_elements(By.XPATH, panel)
    # print(len(l_elements))
    try:
        name_date="/html/body/div[4]/div[5]/div/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/ul/li["+str(len(l_elements))+"]/div/section/div[2]/div/div[1]"

        # name_date="/html/body/div[4]/div[5]/div/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/ul/li[" + str(iterator) + "]/div/section/div[2]/div/div[1]"
        name_date_ele=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, name_date)))
        div_data = name_date_ele.text

    except Exception as e:
        print("Exception in name data  : ", e)
        # iterator += 1 
        # continue
    



    # print("div_data:-",div_data)
    div_data = div_data.replace("•", "_")
    div_data = div_data.replace(" at ", "_")
    div_data = div_data.replace("\n", "_")
    print("\n", div_data)
    div_data = div_data.split("_")
    

    print("div_data:-",div_data)
    temp=div_data[1].split(" ")
    print("temp==",temp)
    if temp[1] in monthDict:
        print("in ifff")
        temp[1]=monthDict[temp[1]]
        # print(monthDict.values())
        print("month=",temp[1])        
        temp[2]=temp[2].replace(",","")
        print("day",temp[2]) 
        print("year",temp[3]) 
    


    if(int(temp[3])>=yearr and int(temp[1])>=mon and int(temp[2])>=dayy):
        print("in date condition")
        print(div_data[2],"timee-",timee)
        # print("temp[2]=",temp[2],"dayy-",dayy)
        if(int(temp[2])==int(dayy)):
            print("IN SAME DAY")
            if(timee<div_data[2]):
                print("in time condition returning true")
                return True
            else:
                print("in time condition returning false")
                return False

        print("returning true")
        return True

    else:
        print("in date condition returning false ")
        return False    




def save_into_csv(newdata):
    s = codecs.open('C:/Users/affin/OneDrive/Desktop/JatinHarshal/data.csv', 'a', 'utf-8')

    data = s.readlines()

    # strrr = "Hello World"

    # data.insert(0, newdata)
    # print(data)
    # s.seek(0)

    # to erase all data 
    s.truncate() 
    
    # fun()

    for i in data:
        s.write(i)


# Extracting messages.......
# ----------------------------------------------------------
def chat_work(chat_name, indexx):

    current_data = []

    newstring = ""


    # f.write('\n')
    p_link =  profile_link()

    driver.implicitly_wait(5)

    chat_panel = "/html/body/div[4]/div[5]/div/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/ul"
    panel_element = driver.find_element(By.XPATH, chat_panel)


    # message, name.. extracting....
    # ----------------------------------------------------------
    panel = "/html/body/div[4]/div[5]/div/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/ul/li"
    
    l_elements = driver.find_elements(By.XPATH, panel)
    # print(len(l_elements))
    
    tag = ""
    try:
        li_2 = "_message-reply-status_1gj1uc"
        li2_ele =  panel_element.find_element(By.CLASS_NAME, li_2)
        tag = li2_ele.text
 
    except :
        print("\n exception in acc/rej tag\n ")


    iterator=0

    for i in l_elements:
        newstring = ""

        iterator += 1
   
        if(iterator == 1):    
            newstring +=   '"' +chat_name + '"' + "," + '"' + p_link  + '"' + "," + '"' + tag  + '"' + ","
        else:
            newstring +=  ",,,"


        time.sleep(1)
        try:
            name_date="_message-metadata_1gj1uc"

            # name_date="/html/body/div[4]/div[5]/div/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/ul/li[" + str(iterator) + "]/div/section/div[2]/div/div[1]"
            name_date_ele=WebDriverWait(i, 10).until(EC.presence_of_element_located((By.CLASS_NAME, name_date)))
            div_data = name_date_ele.text

        except Exception as e:
            print("Exception in name data  : ", e)
            iterator += 1
            continue



        # print("div_data:-",div_data)
        div_data = div_data.replace("•", "_")
        div_data = div_data.replace(" at ", "_")
        div_data = div_data.replace("\n", "_")
        print("\n", div_data)
        div_data = div_data.split("_")
        

        # print("div_data:-",div_data)

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
        # print("Strrr : ", strr)

        newstring += strr  + '"' + md +'"' + "\n"

        print("\n\n\n" , newstring , "\n\n")

        f.write(newstring)
    f.write("\n")
        # f.write("\n\n")
    

# ----------------------------------------------------------
def fun_main():
    
    linkk = a.get()
    print("link",linkk)

    driver.get(linkk)

    mon, dayy,yearr,timee  = ext_recent(data)
    print("m,d,t,e",mon,dayy,yearr,timee)
    # print(ext_recent(data))
    # print(var)
    # looping through all li's
    # ----------------------------------------------------------
    ul_path = "/html/body/div[4]/div[5]/div/div[2]/div[1]/div[2]/div[2]/ul/li"
    ul_list = driver.find_elements(By.XPATH, ul_path)

    flagger = 0
    counter = 0

    try : 
        filter_tag = "_filter-wrapper_19domm"
        filter_tag_ele = driver.find_element(By.CLASS_NAME, filter_tag)

        value = 3

    except Exception as e:
        value = 2
        print("Exception in filter tag : ", e)



    while True:
        # newstring = ""
        counter += 1
        flagger += 1

        print(value)
        time.sleep(3)
        # try : 
        pp = "/html/body/div[4]/div[5]/div/div[2]/div[1]/div[2]/div[" + str(value) + "]/ul/li[" + str(counter) + "]/div/div/div/div[2]/div[1]/a/p"
            #  /html/body/div[4]/div[5]/div/div[2]/div[1]/div[2]/div[                  3]/ul/li[1]                   /div/div/div/div[2]/div[1]/a/p
            #   /html/body/div[4]/div[5]/div/div[2]/div[1]/div[2]/div[3                 ]/ul/li[                   1]/div/div/div/div[2]/div[1]/a/p

        pp_ele =WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, pp)))
        chat_name = pp_ele.text
        print("\n\n")
        print("Name : ", pp_ele.text)
        print("counter : ", counter)

        try :
            element_path = "/html/body/div[4]/div[5]/div/div[2]/div[1]/div[2]/div[" + str(value) +"]/ul/li[" + str(flagger) + "]"
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, element_path)))
            element.click()
            time.sleep(3)
        except Exception as e:    
            print("\n\nException in li clicking : ", e )
        if(mon!=None and dayy!=None):
            
            print("not none ")
            var=check(mon,dayy,yearr,timee)
            if(var==True):
                print("returned true")
                

                chat_work(chat_name, counter)
                

                print("hha hhaa mai chal raha hu")

                time.sleep(3)
                driver.execute_script("arguments[0].scrollIntoView();", element)   
            else:
                print("done")
                if(len(data)>3):
                    for i in data:
                        f.write(i)
            
                break
        else:
            print("file is empty running full")
            chat_work(chat_name, counter)
            time.sleep(3)
            driver.execute_script("arguments[0].scrollIntoView();", element)
                        
        # except Exception as e:    
            # print("\n\tException in listtttt\n", e)
            # time.sleep(2)
            # try:
            #     show_more="/html/body/div[4]/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/button"
            #     show_more_ele=driver.find_element(By.XPATH,show_more)
            #     show_more_ele.click()
            #     time.sleep(2)
            # except Exception as e:
            #     print("Exception in Show more : ", e)
            # flagger -= 1
            # counter -= 1  
            # driver.execute_script("arguments[0].scrollIntoView();", element)  



driver = webdriver.Chrome(executable_path="C:\selenium\chromedriver_win32\chromedriver.exe", options=options)
print(driver.title)
f = codecs.open('C:/Users/affin/OneDrive/Desktop/JatinHarshal/data.csv', 'r+', 'utf-8')

data=f.readlines()
if(len(data)>2):
    f.truncate()

    f.seek(0)
    data.pop(0)
    data.pop(0)
    data.pop(0)

f.write("Name,Link,Tag,Sender's_name,Date,Time,Msg\n\n\n")

time.sleep(2)


root = Tk()
root.title("Message Extration")

root.resizable(0,0)
root.configure(background='black')

#create text boxes
a = Entry(root, width = 30, borderwidth=0)
a.grid(row=0, column=1, padx=40, pady=(15, 0))

# b = Entry(root, width = 30, borderwidth=0)
# b.grid(row=1, column=1, pady=(5, 0))


# create text box label 
a_label = Label(root, text="Project Link", bg="black", fg="white")
a_label.grid(row=0, column=0, pady=(20, 5))

# b_label = Label(root, text="Free Project Name" , bg="black", fg="white")
# b_label.grid(row=1, column=0, pady=(10, 10), padx=(34, 0))

print("--------------------------------------")
print("--------------------------------------")
 


#create submit button
submit_btn = Button(root, text="Start Extraction", command=fun_main, pady=3, padx=15, bg="white")
submit_btn.grid(row=6, column=0, columnspan=2, padx=20, pady=20, ipadx=100)



root.mainloop()