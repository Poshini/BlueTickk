from django.shortcuts import render
# Create your views here.
import time
from selenium import webdriver
from .algo import Encryptmsg
import random
# Create your models here.

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
            return render(request,"inc.html",{})
        except :
            return render(request,"inc.html",{})
    else:
        return render(request,"inc.html",{})
