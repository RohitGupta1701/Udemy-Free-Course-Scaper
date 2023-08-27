import requests,re
from bs4 import BeautifulSoup

course = input('What course you want to search? ')
page_nums=int(input('How many pages you want to scaper? '))
print("")
key=str(course).replace(' ','+')

a=1
list=[]
while a < page_nums+1:
    link="https://www.tutorialbar.com/page/"+str(a)+"/?s="+key+"&post_type=post"
    a+=1
    r=requests.get(link)
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("figure",{"class":"mb20 position-relative text-center"})
    for page in all:
        new_link=page.a['href']
        udemy_link=requests.get(new_link)
        udemy_content=udemy_link.content
        udemy_soup=BeautifulSoup(udemy_content,"html.parser")
        udemy=udemy_soup.find_all("span",{"class":"rh_button_wrapper"})[0].a['href']
        if "https://www.udemy.com/course/" in udemy:
            list.append(udemy)
            print(udemy)

a=1
while a < page_nums+1:
    link="https://www.discudemy.com/search/"+str(a)+"/"+key+".jsf"
    a+=1
    r=requests.get(link)
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div",{"class":"content"})
    for page in all:
        pag=page.find_all("div",{"class":"header"})
        for pa in pag:
            new_link=pa.a['href']
            new_link_front=re.search(re.compile('www.discudemy.com/[^]/]*[/]'),str(new_link)).group(0)
            new_link=new_link.replace(new_link_front,"www.discudemy.com/English/")
            new_link=new_link.replace("English","go")
            udemy_link=requests.get(new_link)
            udemy_content=udemy_link.content
            udemy_soup=BeautifulSoup(udemy_content,"html.parser")
            udemy=udemy_soup.find_all("div",{"class":"ui segment"})[0].a['href']
            if "https://www.udemy.com/course/" in udemy:
                list.append(udemy)
                print(udemy)


with open("udemy.txt",'w+') as f:
    f.write("Free Coupon for "+course+": \n")
    for page in list:
        if page not in f:
            f.write("%s\n" % page)
