import time
from selenium import webdriver
from django.shortcuts import render
from django.contrib import messages
from .algo import Decryptmsg
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
            return render(request , 'decrypted.html' ,{'mes' : mes})

        except:
            print('NOT SEND')
            messages.success(request, 'Could not Decrypt it .Try Again')
            return render(request , 'decrypt.html' , {})
        return render(request, 'home.html' , {})
    else:
        return render(request , 'decrypt.html' , {})


def home(request):
    return render(request , 'home.html' ,{})

def encryption(request):
    return render(request, 'encrypt.html' ,{})


def dec(request):
    return render(request , 'decrypted.html' ,{})