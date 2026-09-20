

from bs4 import BeautifulSoup               
import requests
import cloudscraper
import pandas as pd
from flask import Flask,render_template
import os
import time
radef=Flask(__name__)
@radef.route("/")
def home():
    url1="https://www.matalan.co.uk/c/baby/new-in/"
    
            # url2
            # url3
            # url4
    children=requests.get(url1).text
    soup1=BeautifulSoup(children,"html.parser")
    children1=soup1.find_all("div",class_="flex h-full w-full flex-col justify-start")
    data=[]
    
      
            
    for item_children in children1:
        item1=item_children.find("a",class_="text-body title-order product-item-title line-clamp-2 overflow-hidden font-normal text-ellipsis hover:underline focus:underline").text.strip()
        
        item23=item_children.find_all("div",class_="product-item-price-wrapper price-order")
        for ite23 in item23:
            item2=ite23.find("span",class_="text-md product-variant-price font-bold text-pap").text.strip()
            item3=ite23.find("div",class_="product-item-price-discounts-alignment flex flex-row gap-2").text.strip()
            
        imag1=item_children.find("img")
        
        


        if imag1:
            img_url1=imag1.get("src")
            if "url=" in img_url1:
                img_url1=img_url1.split("url=")[1]
                img_url1=img_url1.split("&")[0]
                print("hi radef ho are kardi in srl")
    
    
    
                    
                
         
        data.append({"image_url":img_url1,"ittem":item1,"itttem":item2,"ittttem":item3})
    url2="https://www.caganbutik.com/urunler"
    man=requests.get(url2).text
    soup2=BeautifulSoup(man,"html.parser")
    mans=soup2.find_all("div",class_="product-card fade-in group relative")
    
    data1=[]
    for mans1 in mans:
        man1=mans1.find("h3",class_="text-sm font-medium font-sans hover:text-warm-gray transition-colors line-clamp-1").text.strip()
        mans23=mans1.find_all("div",class_="flex items-center space-x-2")
        for man23 in mans23:
            man2=man23.find("span",class_="text-xs text-warm-gray line-through").text.strip()
            man3=man23.find("span",class_="text-sm font-semibold").text.strip()
        imag2=mans1.find("img")
            
                        
        if imag2:
            img_url2=imag2.get("src")
            if "url=" in img_url2:
                img_url2=img_url2.split("url=")[1]
                img_url2=img_url2.split("&")[0]
   
        
        imag2=mans1.find("img")
            
                        
        if imag2:
            img_url2=imag2.get("src")
            if "url=" in img_url2:
                img_url2=img_url2.split("url=")[1]
                img_url2=img_url2.split("&")[0]
        data1.append({"man":man1,"manw":man2,"manr":man3,"img":img_url2})



    url3="https://www.nevermore.com.tr/newnow"
    weman=requests.get(url3)
    # print(radef.text[111500:112500])
    soup=BeautifulSoup(weman.text,"html.parser")
    wemans=soup.find_all("div",class_="card-product")
    data3=[]
    for weman123 in wemans:
        weman1=weman123.find("div",class_="title").text.strip()
        weman2=weman123.find("div",class_="sale-price line").text.strip()
        weman3=weman123.find("span",class_="sale-price prom-fiyat").text.strip()
        weman4=weman123.find("div",class_="prom-oran").text.strip()
        img3=weman123.find("img")
        if img3:
            img_url3=img3.get("src")
            if "url=" in img_url3:
                img_url3=img_url3.split("url=")[1]
                img_url3=img_url3.split("&")[0]
        data3.append({"weman1":weman1,"weman2":weman2,"weman3":weman3,"weman4":weman4,"img3":img_url3})

    return render_template('web.html',item=data,item43=data1,weman33=data3)
    

    
    
if __name__=="__main__":
    radef.run(debug=True)

