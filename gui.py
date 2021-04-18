import tkinter as tk
from tkinter import *
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import json
import os
import sys
from lxml import html




file2=open("kayit.txt","a",encoding="utf-8")
options=webdriver.FirefoxOptions()
options.set_headless()
driver_path ="geckodriver.exe"
browser = webdriver.Firefox(executable_path=driver_path,options=options)



window=tk.Tk()

window.title("Trendyol Bot (Licensed to GOD)")
window.geometry('850x700')



def sorgula():
    

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


            browser.find_element_by_xpath(
                "//*[@id='login-email']").click()
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
time.sleep(5)







file1=open("account.txt","a",encoding="utf-8")

def kaydet():
    mail_kayit=email_Entry.get()
    password_kayit=password_Entry.get()
    
    
    kayit1=mail_kayit
    kayit2=password_kayit
    output.insert(END,mail_kayit+","+password_kayit+"\n")

    file1.write(mail_kayit+","+password_kayit+"\n")
  





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

photo=tk.PhotoImage(file="logo.png",)
Label(window, image=photo).place(x=250,y=10)

email_Label = tk.Label(window)
email_Label.config(text="E-posta",font=("Vertana",15))
email_Label.place(x=50,y=200)

email_Entry=tk.Entry(window)
email_Entry.config(width=30)
email_Entry.place(x=50,y=235)


password_Label=tk.Label(window)
password_Label.config(text="Şifre",font=("Vertana","15"))
password_Label.place(x=280,y=200)

password_Entry=tk.Entry(window)
password_Entry.config(width=30)
password_Entry.place(x=280,y=235)

kaydet_Button=tk.Button(window)
kaydet_Button.config(text="Kaydet",bg="gray",fg="white",width=15,font=("Vertana","10"),command=kaydet)
kaydet_Button.place(x=180,y=270)

console_Label=tk.Label(window)
console_Label.config(text="Konsol--->",font=("Vertana","15"))
console_Label.place(x=50,y=350)

output = tk.Text(window, width=90, height=15,padx=10,pady=10)
output.insert(1.0,coupons)
output.place(x=50,y=380)

coupon_Label=tk.Label(window)
coupon_Label.config(text="Kupon Kontrol",font=("Vertana","15"))
coupon_Label.place(x=600,y=220)

coupon_Button=tk.Button(window)
coupon_Button.config(text="Başlat",bg="gray",fg="white",font=("Vertana","15"),command=sorgula)
coupon_Button.place(x=625,y=250)

window.mainloop()