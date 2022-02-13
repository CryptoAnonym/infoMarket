import requests

daneZonda = requests.get("https://api.zonda.exchange/rest/trading/ticker")

if daneZonda.ok == True:
    dane3 = daneZonda.json()["items"]

    def exchange():
        def zonda(rynek): # wyszukiwarka rynków w zondzie(bitbay)  
                     
                test = dane3[rynek]

                bid = test["highestBid"]
                ask = test["lowestAsk"]
            
            
                print("\nNajwyższa oferta kupna: " + str(bid)[0:6] + " " + str(rynek)[4:7] )
                print("Najniższa oferta sprzedaży: " + str(ask)[0:6] + " "+ str(rynek)[4:7] + "\n")
            

        print("\n***** Witaj w wyszukiwarce rynków na giełdzie ZONDA! *****")
        print("        (Rynek wyszukujemy wg schematu: BTC-PLN)     ")
        
        in_data = input("\nPodaj rynek, którego szukasz: ")

        if len(in_data) == 7:
            if in_data.find("-") != -1:
                zonda(in_data.upper())
            else :
                print("Błędny rynek!")
        else :
            print("Błędny rynek!")

else:
    print("Connect with Zonda API ERROR!")
