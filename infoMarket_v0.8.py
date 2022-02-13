import time
from info import global_info
from zonda import exchange
from nbp import nbp
from ethereum import eth


while True:
  print("=======================================================")
  print("============= infoMarket terminal version =============")
  print("=========== Start: %s ===========" % time.ctime())

  print("""
    info - ogólne informacje o rynku
    paprica - informacje o krypto z serwisu coinpaprica
    zonda - wyszukiwarka rynków na giełdzie ZONDA
    nbp - kursy walut z Narodowego Banku Polskiego
    eth - przegląd sieci Ethereum
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


  input("\nEnter aby kontynuować")
