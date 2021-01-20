# This is a sample Python script.
from selenium import webdriver
import winsound
import time

from selenium.webdriver.common.keys import Keys
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

inStock = False
driver = webdriver.Chrome()

# def login():
#     #LOGIN NOW 90 SECS
#     driver.find_element_by_id("fld-e").send_keys("xxxxx@gmail.com")
#     driver.find_element_by_id("fld-p1").send_keys("xxxxx")
#     test = driver.find_elements_by_class_name("cia-form__controls ")
#     test[0].click()
#     time.sleep(5)

# def addToCart(id):
#     global elem
#     global driver
#     elem = id
#     elem.click()
#     driver.implicitly_wait(1)
#     driver.get("https://www.bestbuy.com/cart")
#     driver.implicitly_wait(2)
#     elem = driver.find_elements_by_class_name("checkout-buttons__checkout")
#     elem[0].click()
#     driver.implicitly_wait(2)
#     driver.find_element_by_id("credit-card-cvv").send_keys("xxx")
#     driver.find_element_by_class_name("button--place-order-fast-track").click()

def checkInStock():
    global inStock
    global elem
    global driver
    #driver.get("https://www.bestbuy.com/site/evga-geforce-rtx-3080-ftw3-gaming-10gb-gddr6x-pci-express-4-0-graphics-card/6436191.p?skuId=6436191")
    driver.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402")
    elem = driver.find_elements_by_class_name("fulfillment-add-to-cart-button")
    if(elem[0].text == "Add to Cart"):
        winsound.Beep(6500,200)
        inStock = True
        elem.click()
        # return elem[0]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # driver.get("https://www.bestbuy.com/login")
    # login()
    #driver.get("https://www.bestbuy.com/site/corsair-icue-h100i-elite-capellix-cpu-cooler-black/6422732.p?skuId=6422732")
    #assert "NVIDIA GeForce RTX 3060 Ti 8GB GDDR6 PCI Express 4.0 Graphics Card Steel and Black 900-1G142-2520-000 - Best Buy" in driver.title
    #elem = driver.find_element_by_id("fulfillment-add-to-cart-button-d2b42b8c-894a-4e10-9a2e-7527de123ca0")

    #FE 3060ti
    #driver.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402")
    winsound.Beep(6500, 800)

    while(inStock == False):
        elementOfStock = checkInStock()

    # addToCart(elementOfStock)



