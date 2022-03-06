from asyncore import ExitNow
import time
from info import global_info
from zonda import exchange
from nbp import nbp
from ethereum import eth
from paprika import paprika


while True:
  print("=======================================================")
  print("============= infoMarket terminal version =============")
  print("=========== Start: %s ===========" % time.ctime())

  print("""
    info - ogólne informacje o rynku
    paprika - informacje o krypto z serwisu coinpaprica
    zonda - wyszukiwarka rynków na giełdzie ZONDA
    nbp - kursy walut z Narodowego Banku Polskiego
    eth - przegląd sieci Ethereum
    exit - wyjscie

    """)


  action = input("Action: ")


  if action.upper() == "ZONDA":
    exchange()
  if action.upper() == "INFO":
    global_info()
  if action.upper() == "NBP":
    nbp()
  if action.upper() == "ETH":
    eth()
  if action.upper() == "PAPRIKA":
    paprika()
  if action.upper() == "EXIT":
    break
    


  input("\nEnter aby kontynuować")
