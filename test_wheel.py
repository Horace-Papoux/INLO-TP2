# import depuis les sources
from src.wallet import Wallet

# import depuis le .whl TP2
# from TP2.wallet import Wallet

if __name__ == "__main__":
    my_wallet = Wallet(100)
    my_wallet.add_cash(120)
    print("Congratulations. You successfully installed the TP2 package !")
