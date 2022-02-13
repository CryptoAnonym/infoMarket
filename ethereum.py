from web3 import Web3

infura= "https://mainnet.infura.io/v3/2c6b6d6fcb964eee88bc0e2e83c8f654"
web3 = Web3(Web3.HTTPProvider(infura))
nr_bloku = web3.eth.block_number 

def eth():

    print("\n***** Witaj w przeglądarce sieci ETHEREUM *****")
    print("***** Aktualny nr bloku Ethereum: " + str(nr_bloku) +" *****")

    def eth_balans(wallet):  

        balance = web3.eth.get_balance(wallet)          #wyszukiwarka adresu
        b_wallet = web3.fromWei(balance, "ether")

        print("\nAdres posiada: " + str(b_wallet) + " ETH \n" )

    in_data = input("\nWpisz adres na sieci ETHEREUM: ")

    eth_balans(in_data)
