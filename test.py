from datetime import date
# import readline
import time

from selenium import webdriver
import codecs

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

s = codecs.open("C:/Users/affin/OneDrive/Desktop/Automation/Free Paid Segrigation/extract.csv", 'r+', "utf-8")
lines = s.readlines()


strrr = "\nHELLLOOOOO WORLDDDD\n"




lines.insert(0, strrr)
print(lines)
s.seek(0)

# to erase all data 
s.truncate() 

for i in lines:
    s.write(i)
# s.write(lines)


# # # return s
# line_offset = []
# offset = 0
# for line in s:
#     line_offset.append(offset)
#     offset += len(line)
    
# s.seek(0)

# # Now, to skip to line n (with the first line being line 0), just do

# print(line_offset)
# s.seek(line_offset[2])

# # s.write("\n")
# # s.seek(line_offset[2])








# f = codecs.open("C:/Users/affin/OneDrive/Desktop/Automation/Free Paid Segrigation/temp.csv", 'w+', "utf-8")
# f.write("world\n")





# for i in lines:
#     f.write(i)
# s.seek(0)
# s.truncate(0)
# f.seek(0)
# n=f.readlines()
# print (n)
# for i in n:
#     s.write(i)
# f.delete()
# # f.close()    
    
    