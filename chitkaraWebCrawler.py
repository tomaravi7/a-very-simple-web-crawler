from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get("https://www.google.com")
# PATH="C:\Program Files (x86)\chromedriver.exe"
# driver=webdriver.Chrome(PATH)
driver.get("https://www.chitkara.edu.in")

my_Url='https://www.chitkara.edu.in/'
uClient=uReq(my_Url)
page_html=uClient.read()
uClient.close()
soup=BeautifulSoup(page_html,'lxml')

file_name="Data.csv"
headers = "Field,Course \n"
f=open(file_name,"w")
f.write(headers)

fields=soup.find_all('div',class_='realb2')
for fields12 in fields:
    fieldout=fields12.h2.text
    f.write(fieldout+"\n")
html_tags=soup.find_all('div',class_='col-md-4 col-sm-12')
for field in html_tags:
    print(field.h3.text)
    f.write(field.h3.text+"\n")
html_tags3=soup.find_all('h3',class_='mtop5')
for field in html_tags3:
    print(field.a.text)
    f.write(field.a.text.replace(",","|")+"\n")

html_tags4=soup.find_all('ul',class_='hc-list')
for medical in html_tags4:
    medical_course=medical.li.a.text
    print(medical_course.replace("-",""))
    f.write(", "+medical_course.replace("-","")+"\n")


driver.get("https://www.chitkara.edu.in/cse/")
content = driver.find_element("name",'specialisationsList')
print(content.text.replace("Explore",""))
f.write(content.text.replace("Explore","")+"\n")

f.close()
driver.quit()