from wallet import Wallet
from blockchain import Blockchain
from transaction import Transaction
import time

wallet1 = Wallet()
wallet2 = Wallet()
wallet3 = Wallet()

blockchain = Blockchain()

# Loop for performing actions multiple times
for i in range(4):
    print("Wallet 1 balance: " + str(wallet1.getBalance(blockchain)))
    print("Wallet 2 balance: " + str(wallet2.getBalance(blockchain)))
    print("Wallet 3 balance: " + str(wallet3.getBalance(blockchain)))

    transaction1 = wallet1.sendMoney(wallet2.getPublicKey(), 10)
    transaction2 = wallet2.sendMoney(wallet3.getPublicKey(), 5)
    transaction3 = wallet3.sendMoney(wallet1.getPublicKey(), 15)

    blockchain.addTransaction(transaction1)
    blockchain.addTransaction(transaction2)
    blockchain.addTransaction(transaction3)

    blockchain.minePendingTransactions(wallet1.getPublicKey())

    print()

    time.sleep(1)

blockchain.printChain()
