from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def metals():
    print("Please wait...")

    chrome_options = Options()                  
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome("chromedriver.exe", options=chrome_options)
    driver.get('https://goldenmark.com/pl/wiedenscy-filharmonicy-1-uncja-zlota/#/282-cennik-1_dzień')
    price_g = driver.find_element_by_xpath("/html/body/main/section/div[2]/div/section/div[1]/div[2]/div[2]/div[1]/div/span")
    gold = (price_g.text)

    print("Please wait...")
    
    driver.get('https://goldenmark.com/pl/britannia-1-uncja-srebra-3039/#/282-cennik-1_dzień')
    price_s =  driver.find_element_by_xpath("/html/body/main/section/div[2]/div/section/div[1]/div[2]/div[2]/div[1]/div/span")
    silver = (price_s.text)

    driver.get('https://www.zlotagotowka.pl/#ceny-skupu')
    gold_buy =  driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div/div[12]/div/div/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[2]/td[2]')
    gold_b_g = gold_buy.text
    #gold_b_oz = str(float(gold_b_g) * 31.1)

    #driver.get('https://skup.zlota.pl/ceny-skupu')
    #silver_buy =  driver.find_element_by_xpath("/html/body/div/div[2]/div/table/tbody/tr[33]/td[5]")
    #silver_b = (silver_buy.text)


    print("\n***** CENY MONET BULIONOWYCH *****\n")
    print("GOLD 1 OZ: " + gold)
    print("SILVER 1 OZ: " + silver +"\n")
    print("\nGOLD 1 OZ (BUY): " + gold_b_g + " zl")
    #print("SILVER 1 OZ: " + silver_b +"\n")
    input("\nEnter, aby kontynuowac.")

