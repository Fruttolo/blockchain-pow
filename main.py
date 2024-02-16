from wallet import Wallet
from blockchain import Blockchain
import time

wallet1 = Wallet()
wallet2 = Wallet()
wallet3 = Wallet()

blockchain = Blockchain()

# Loop for performing actions multiple times
for i in range(4):
    print("Wallet 1 balance: " + str(blockchain.getBalanceOfAddress(wallet1.getPublicKey())))
    print("Wallet 2 balance: " + str(blockchain.getBalanceOfAddress(wallet2.getPublicKey())))
    print("Wallet 3 balance: " + str(blockchain.getBalanceOfAddress(wallet3.getPublicKey())))

    transaction1 = wallet1.sendMoney(wallet2.getPublicKey(), 10)
    transaction2 = wallet2.sendMoney(wallet3.getPublicKey(), 5)
    transaction3 = wallet3.sendMoney(wallet1.getPublicKey(), 15)

    blockchain.addTransaction(transaction1)
    blockchain.addTransaction(transaction2)
    blockchain.addTransaction(transaction3)

    blockchain.minePendingTransactions(wallet1.getPublicKey())

    print()

    time.sleep(1)

print(blockchain.isChainValid())
