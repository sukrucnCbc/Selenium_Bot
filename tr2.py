from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import json

file2=open("kayit.txt","a",encoding="utf-8")
options=webdriver.FirefoxOptions()
options.set_headless()
driver_path ="geckodriver.exe"
browser = webdriver.Firefox(executable_path=driver_path,options=options)

with open("account.txt","r",encoding="utf-8") as file:
    content=file.readlines()# her satırdaki veriyi listenin bir elemanı olarak belirler
    """döngü için blok"""
    for satır in content:
        mail_password=satır.split(",") # bir liste döndürür
        mail=mail_password[0]
        passwords=mail_password[1].strip()
        
    
    # """deneme için tekli blok"""
    # i=content[0]
    # mail_password=i.split(",") # bir liste döndürür
    # mail=mail_password[0]
    # passwords=mail_password[1].strip()
    # print(mail)
    
    # print(passwords)
        


        browser.get("https://www.trendyol.com/Hesabim/IndirimKuponlari")

        email=browser.find_element_by_xpath("//*[@id='login-email']")
        password=browser.find_element_by_name("login-password")
        



        email.send_keys(mail)
        password.send_keys(passwords)

        login_btn=browser.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[1]/form/button")
        login_btn.click()
        time.sleep(3)
        
        print("\n\n")
        print(f" {mail} ".center(50,"*"))
        file2.write(f" {mail} ".center(50,"*"))
        file2.write("\n\n")
        try:
            cn=browser.find_element_by_xpath("//*[@id='account-layout-container']/div/a[5]/span")
            cn.click()
        except:
            print("E-mail veya şifre hatalı")
            file2.write("hatalı giriş\n\n")
            continue
        time.sleep(3)

        coupons=browser.find_elements_by_class_name("coupon-name")
        couponlist=[]
        for cp in coupons:
            couponlist.append(cp.text)

        min=browser.find_elements_by_class_name("coupon-min-price")
        minlist=[]
        for tutar in min:
            minlist.append(tutar.text)
            
            
        tarih=browser.find_elements_by_class_name("coupon-valid-dates")
        tarihlist=[]
        for son in tarih:
            tarihlist.append(son.text)
            

        price=browser.find_elements_by_xpath("//*[@id='coupon-discount']")
        pricelist=[]

        for tut in price:
            pricelist.append(tut.text)
        
            
        result=0    
        
        for cpname in couponlist:
            print(cpname)
            print(minlist[result])
            print(tarihlist[result])
            print(pricelist[result])
            print("\n\n")
            
                            
            file2.write(cpname)
            file2.write("\n")
            file2.write(minlist[result])
            file2.write("\n")
            file2.write(tarihlist[result])
            file2.write("\n")
            file2.write(pricelist[result])
            file2.write("\n\n")
            result+=1
        time.sleep(3)

        

        browser.get("https://www.trendyol.com/authentication/logout")
        time.sleep(2)

        browser.get("https://www.trendyol.com/Hesabim/IndirimKuponlari")

# print(couponlist)
# print(minlist)
# print(tarihlist)
# print(pricelist)
time.sleep(3)
