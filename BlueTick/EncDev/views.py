import time
import random
from selenium import webdriver
from django.shortcuts import render
from django.contrib import messages
from .algo import Decryptmsg , Encryptmsg
from html.parser import HTMLParser
# Create your views here.

def decryption(request):
    if request.method == 'POST':
        sender = request.POST['sender']
        try:
            driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
            driver.get('https://web.whatsapp.com/');
            time.sleep(10) # Let the user actually see something!
            search_box = driver.find_element_by_css_selector("input[title*='Search or start new chat']").click();
           # time.sleep(5)
            search_box = driver.find_element_by_css_selector("input[title*='Search or start new chat']").send_keys(sender);
            #time.sleep(5)
            search_box = driver.find_element_by_css_selector("span[title='%s']"%sender).click();

            s = ""
            element =   driver.find_elements_by_css_selector("span[class*='_F7Vk selectable-text invisible-space copyable-text']")

            s = element[-1].get_attribute('innerHTML')
            data = s.split(">")
            s = data[1]
            da = s.split("<")
            mess = da[0]
            h = HTMLParser()
            mes = h.unescape(mess)
            print()
            print(mes+"SSS")
            print()
            mes =  Decryptmsg(mes)
            print("HH"+mes+"HH")
            return render(request , 'decrypted.html' ,{'mes' : mes, 'sender' : sender})

        except:
            print('NOT SEND')
            messages.success(request, 'Try Again.. \n Check internet connection or write the username as saved in contacts list')
            return render(request , 'decrypt.html' , {})
        return render(request, 'home.html' , {})
    else:
        return render(request , 'decrypt.html' , {})


def home(request):
    return render(request , 'home.html' ,{})

def encryption(request):
    if request.method == 'POST':
        try :
            name = request.POST['name']
            tempmsg = request.POST['msg']
            msg = Encryptmsg(tempmsg)
            driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
            driver.get('https://web.whatsapp.com/');
            time.sleep(12) # Let the user actually see something!
            search_box = driver.find_element_by_css_selector("input[title*='Search or start new chat']").click();
            #search_box = driver.find_element_by_name('q')
            #time.sleep(5)
            search_box = driver.find_element_by_css_selector("input[title*='Search or start new chat']").send_keys(name);
            #search_box.sendkeys('Mudit')
            #driver.findElement(By.id("invoice_supplier_id")).sendKeys("value", "your value");
            #search_box.submit()
            time.sleep(5)
            search_box = driver.find_element_by_css_selector("span[title=%s]" %name).click();
            # Let the user actually see something!
            s = ""
            element =   driver.find_element_by_css_selector("div[class*='_3u328 copyable-text selectable-text']").click();
            element = driver.find_element_by_css_selector("div[class*='_3u328 copyable-text selectable-text']").send_keys(msg);
            element = driver.find_element_by_css_selector("span[data-icon='send']").click();
            #time.sleep(1000)
            #driver.quit()
            messages.success(request , 'Hooray !!! Your Message is Sent to %s .'%name)
            return render(request,"home.html",{})
        except :
            messages.success(request, 'Try Again.. \n Check internet connection or write the username as saved in contacts list')
            return render(request,"encrypt.html",{})
    else:
        return render(request,"encrypt.html",{})

def dec(request):
    return render(request , 'decrypted.html' ,{})