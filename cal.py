from nbp import forex_price
from paprika import paprica_price_pln

def cal():
    print(""" \n***** Witaj w kalkulatorze KRYPTO-FIAT ! *****
    \n Wybierz rodzaj wymiany:
        1. KRYPTO --> FIAT
        2. FIAT --> KRYPTO
    """)

    action = input(" Action (1 or 2): ")

    if action == "1":
        krypto = input("Podaj kryptowalute (np. btc) do zamiany: ")
        ktypo_price = paprica_price_pln(krypto.upper())
        fiat = input("Podaj na jaka walute (np. usd) zamieniamy: ")
        
        if fiat.upper() == "PLN":
            ile = input("Ile " + krypto.upper() + " wymieniamy na " + fiat.upper() + ": ")
            wynik_pln = ktypo_price * float(ile)
            print("Otrzymasz: " + str(wynik_pln)[0:8] + " " + str(fiat.upper()))
            
            input("\nEnter aby kontynuowac.")

        else:

            fiat_price = forex_price(fiat.upper())
            dzialanie = ktypo_price / fiat_price
            ile = input("Ile " + krypto.upper() + " wymieniamy na " + fiat.upper() + ": ")
            wynik = dzialanie * float(ile)

            print("Otrzymasz: " + str(wynik)[0:8] + " " + str(fiat.upper()) )
            input("\nEnter aby kontynuowac.")

    elif action == "2":
        fiat1 = input("Podaj walute (np. usd) do zamiany: ")
        fiat_price = forex_price(fiat1.upper())

        krypto1 = input("Podaj na jaka kryptowalute (np. btc) zamieniamy: ")
        ktypo_price = paprica_price_pln(krypto1.upper())

        if fiat1.upper() == "PLN":
            ile = input("Ile " + fiat1.upper() + " wymieniamy na " + krypto1.upper() + ": ")
            wynik2_pln = float(ile) / ktypo_price 
            print("Otrzymasz: " + str(wynik2_pln)[0:8] + " " + str(krypto1.upper()) )
            input("\nEnter aby kontynuowac.")
        else:
            dzialanie2 = fiat_price / ktypo_price 

            ile = input("Ile " + fiat1.upper() + " wymieniamy na " + krypto1.upper() + ": ")
            wynik2 = dzialanie2 * float(ile)

            print("Otrzymasz: " + str(wynik2)[0:8] + " " + str(krypto1.upper()) )
            input("\nEnter aby kontynuowac.")
    else: 
        print("\n Bledny wybor. Sproboj jeszcze raz.")
    