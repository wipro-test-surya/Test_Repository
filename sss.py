from os import write
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json


browser = webdriver.Chrome() 
browser.get("https://github.com")
browser.maximize_window()
browser.implicitly_wait(10)

browser.find_element(By.LINK_TEXT, "Sign in" ).click()
browser.find_element(By.NAME, "login").send_keys("wipro-test-surya")
browser.find_element(By.NAME, "password").send_keys("KOTAsurya@1205")
browser.find_element(By.NAME, "commit").click()

browser.find_element(By.XPATH, "//span[contains(@class, 'css-truncate css-truncate-target')]").click()
browser.find_element(By.LINK_TEXT, "Settings").click()
browser.find_element(By.LINK_TEXT, "Webhooks").click()
browser.find_element(By.LINK_TEXT, "Edit").click()
browser.find_element(By.LINK_TEXT, "Recent Deliveries").click()
time.sleep(3)
browser.find_element(By.XPATH, "//*[@id='repo-content-pjax-container']/div/div[2]/ul/li[1]").click()

data1 = browser.find_elements(By.XPATH, "//*[@id='repo-content-pjax-container']/div/div[2]/ul/li[1]/details/tab-container/div[2]/div")
for j in data1:
    # print(j.text)
    required_file = j.text
    # print(required_file)
    print(type(required_file))
    
    out_file = open('payload_data.json','w')
    json.dump(required_file , out_file)
    out_file.close()
    
# C:\Users\su20237483\Desktop\AT&T\Python\payload_data.json
added =[]
removed = []
modified = []
with open('C:/Users/su20237483/Desktop/AT&T/Python\payload_data.json','r') as file:
    data = json.load(file)
    # print(data)
    print(type(data),'%%%%%%%%%%%%')
    
    stud_obj = json.loads(data)
    print(type(stud_obj),'$$$$$$$$$$$$$')

    for i,j in stud_obj.items():
        #print(i)
        if i=='commits':
           #print(i)
           for valuess in j:
            #    print(valuess)
               for ii,jj in valuess.items():
                    # print(ii)
                    if ii=='added':
                       for kk in jj:
                           added.append(kk)
                    elif ii=='removed':
                       for kk in jj:
                           removed.append(kk)
                    elif ii=='modified':
                       for kk in jj:
                           modified.append(kk)
            
    # print('addded::',added)
    # print('removed::',removed)
    # print('modified::',modified)

    if len(added) != 0:  
        # print('newly added', added)
        for i in added:
            aa = i
            print('newly added11111111', aa)
    elif len(removed) !=0 :
        for j in removed:
            bb = j
        print('newly removed222222222222', removed)
    elif len(modified) != 0:
        for k in modified:
            cc = k
        print('newly modified333333333333', modified)
    
    browser.back()
    time.sleep(2)
    browser.back()
    time.sleep(2)
    browser.back()
    time.sleep(2)
    browser.back()
    time.sleep(5)

    files = []
    lis = browser.find_elements(By.XPATH, "//*[@id='repo-content-pjax-container']/div/div[2]/div[1]/div[3]/div[3]")
    # //*[@id="repo-content-pjax-container"]/div/div[2]/div[1]/div[3]/div[3]
    for i in lis:
        # print(i)
        files.append(i.text)
    # print(files,'**********')

    c = [i.split() for i in files]
    for i in c:
        print('000000000000000000000')
        if aa in i:
            print('********')
            print(aa,'&&&&&&&&&&&&')
        elif bb in i:
            print(bb,'@@@@@@@@@@')
        elif cc in i:
            print(cc,'!!!!!!!!!!!')

# browser.find_element(By.LINK_TEXT, aa).click()
# browser.find_element(By.LINK_TEXT, "Raw").click()
# data = browser.find_elements(By.XPATH, "/html/body")
# for i in data:
#     print(i.text)
#     with open(str(aa), 'w') as newfile:
#         data = newfile.write(i.text)










# browser.find_element(By.LINK_TEXT, "Settings").click()
# browser.find_element(By.LINK_TEXT, "Webhooks").click()
# browser.find_element(By.LINK_TEXT, "Edit").click()
# browser.find_element(By.LINK_TEXT, "Recent Deliveries").click()
# time.sleep(5)
# browser.find_element(By.XPATH, "//*[@id='repo-content-pjax-container']/div/div[2]/ul/li[1]").click()

# print("enter into payload")
# payload_data = []
# # payload = '//*[@id="repo-content-pjax-container"]/div/div[2]/ul/li[1]/details'
# data = browser.find_element(By.XPATH,'//*[@id="repo-content-pjax-container"]/div/div[2]/ul/li[1]/details')

# data.is_displayed()
# print("displayed")
# data1 = str(data.text)
# # data1= (data.get_attribute('value'))
# print("DATA:",data1)
# payload_data.append(data1)
# print(payload_data)

# time.sleep(3)
# browser.close()









