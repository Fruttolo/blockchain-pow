import helpers
from transaction import Transaction
from block import Block

class Blockchain:
    def __init__(self):
        self.chain = [self.createGenesisBlock()] # The first block in the blockchain
        self.difficulty = 5 # The number of leading zeros that the hash must have
        self.pendingTransactions = [] # Transactions that are not yet in a block
        self.miningReward = 100 # The reward for mining a block

    def createGenesisBlock(self):
        return Block()
    
    def getLatestBlock(self):
        return self.chain[len(self.chain) - 1]
    
    def minePendingTransactions(self, miningRewardAddress):
        block = Block(self.pendingTransactions, self.getLatestBlock().hash)
        block.mineBlock(self.difficulty)
        self.chain.append(block)
        self.pendingTransactions = [Transaction(miningRewardAddress, None, self.miningReward)]

    def addTransaction(self, transaction):
        if transaction.verifyTransaction() == False:
            print("Transaction failed to verify")
            return
        if transaction.amount <= 0:
            print("Transaction failed amount")
            return
        if self.getBalanceOfAddress(transaction.senderPublicKey) < transaction.amount:
            print("Transaction failed balance")
            return
        self.pendingTransactions.append(transaction)

    def getBalanceOfAddress(self, address):
        balance = 0
        for block in self.chain:
            for transaction in block.transactions:
                if transaction.receiverPublicKey == address:
                    balance += transaction.amount
                if transaction.senderPublicKey == address:
                    balance -= transaction.amount
        return balance
    
    def isChainValid(self):
        for i in range(1, len(self.chain)):
            currentBlock = self.chain[i]
            previousBlock = self.chain[i - 1]
            if currentBlock.hash != currentBlock.calculateHash():
                return False
            if currentBlock.previousHash != previousBlock.hash:
                return False
            if not currentBlock.hasValidTransactions():
                return False
        return True
    
    def printChain(self):
        for block in self.chain:
            print("Previous Hash: " + block.previousHash)
            print("Transactions: " + block.getTransactionsToString())
            print("Nonce: " + str(block.nonce))
            print("Hash: " + block.hash)
            print("\n")