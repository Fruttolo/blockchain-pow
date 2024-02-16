import helpers
from transaction import Transaction

class Block:
    def __init__ (self, transactions = [], previousHash = ""):
        self.transactions = transactions
        self.previousHash = previousHash
        self.nonce = 0
        self.hash = self.calculateHash()

    def calculateHash(self):
        return helpers.hash(str(self.transactions) + self.previousHash + str(self.nonce))
    
    def mineBlock(self, difficulty):
        while self.hash[0:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculateHash()
        print("Block mined: " + self.hash)

    def hasValidTransactions(self):
        for transaction in self.transactions:
            if not transaction.verifyTransaction():
                return False
        return True
    
    def getTransactionsToString(self):
        transactionsString = ""
        for transaction in self.transactions:
            transactionsString += transaction.getTransactionWithSignature()
        return transactionsString
    
    def getBlockToString(self):
        return str(self.previousHash) + self.getTransactionsToString() + str(self.nonce)