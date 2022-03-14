from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def metals():
    print("Please wait...")

    chrome_options = Options()                  
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome("C:\chromedriver.exe", options=chrome_options)
    driver.get('https://goldenmark.com/pl/wiedenscy-filharmonicy-1-uncja-zlota/#/282-cennik-1_dzień')
    price_g = driver.find_element_by_xpath("/html/body/main/section/div[2]/div/section/div[1]/div[2]/div[2]/div[1]/div/span")
    gold = (price_g.text)

    print("Please wait...")
    
    driver.get('https://goldenmark.com/pl/britannia-1-uncja-srebra-3039/#/282-cennik-1_dzień')
    price_s =  driver.find_element_by_xpath("/html/body/main/section/div[2]/div/section/div[1]/div[2]/div[2]/div[1]/div/span")
    silver = (price_s.text)

    print("\n***** CENY MONET BULIONOWYCH *****\n")
    print("GOLD 1 OZ: " + gold)
    print("SILVER 1 OZ: " + silver +"\n")
    input("\nEnter, aby kontynuowac.")