import requests

odpNBP = requests.get("http://api.nbp.pl/api/exchangerates/tables/a?format=json")

if odpNBP.ok == True:  
    data = odpNBP.json()[0]

    def nbp():

        table = data["table"]
        no = data["no"]
        effectiveDate = data["effectiveDate"]
        rates = data["rates"]

        print("***** KURSY WALUT Z NARODOWEGO BANKU POLSKIEGO *****")
        print("Kursy walut dla: " + "tabela: " + table + " " + "numer: " + no + " " + "data:" + " " + effectiveDate)
        print("")

        in_data = input("Wpisz jakiej waluty szukasz lub all dla wszystkich: ")
        print("")

        
        if in_data == "all":
            for rate in rates:
                waluta = rate["currency"]
                tiker = rate["code"]
                price4 = rate["mid"]
                print("|"+ tiker + "|" + waluta.upper() + "= "+ str(price4)+ " " + "|PLN|" )
        else:
            for rate in rates:
                    waluta = rate["currency"]
                    tiker = rate["code"]
                    price4 = rate["mid"]
                    if tiker == in_data.upper() :
                        print("|"+ tiker + "|" + waluta.upper() + "= "+ str(price4)+ " " + "|PLN|" )
                    else: 
                        continue