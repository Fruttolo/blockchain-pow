import hashlib
import random

class Wallet:
    def __init__(self, publicKey, privateKey, amount=0):
        self.publicKey = publicKey
        self.privateKey = privateKey
        self.balance = amount

    def getBalance(self):
        return self.balance
    
    def getpublicKey(self):
        return self.publicKey
    
    def getprivateKey(self):
        return self.privateKey
    
    def addAmount(self, transaction):
        if transaction.getReceiver() == self.publicKey:
            self.balance += transaction.getAmount()
    
    def subtractAmount(self, transaction):
        check = calculate_sha256(self.getprivateKey() + transaction.getReceiver())
        if(transaction.getAmount() > self.balance):
            print("Insufficient balance")
            return
        if check == transaction.getFirm():
            self.balance -= transaction.getAmount()
            transaction.confirmTransaction(random.randint(0, 1000000))
        else:
            print("Transaction not verified")
    
class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def getSender(self):
        return self.sender
    
    def getReceiver(self):
        return self.receiver
    
    def getAmount(self):
        return self.amount
    
    def getFirm(self):
        return self.firm
    
    def getPassed(self):
        return self.passed
    
    def createFirm(self, privateKey):
        self.firm = calculate_sha256(self.receiver + privateKey)
    
    def confirmTransaction(self, idConfirm):
        self.firm = calculate_sha256(self.firm + idConfirm)

    def tryConfirmTransaction(self, idConfirm):
        if self.firm == calculate_sha256(self.firm + idConfirm):
            self.passed = idConfirm
        

def executeTransaction(wallet1, wallet2, amount):
    transaction = Transaction(wallet1.getpublicKey(), wallet2.getpublicKey(), amount)
    transaction.createFirm(wallet1.getprivateKey())
    wallet1.subtractAmount(transaction)
    wallet2.addAmount(transaction)

def calculate_sha256(input):
    return hashlib.sha256(input.encode()).hexdigest()

# Main

passW1 = input("Enter the public key of the sender: ")
privateKeyW1 = calculate_sha256(passW1)
publicKeyW1 = calculate_sha256(privateKeyW1)

passW2 = input("Enter the public key of the receiver: ")
privateKeyW2 = calculate_sha256(passW2)
publicKeyW2 = calculate_sha256(privateKeyW2)

wallet1 = Wallet(privateKeyW1, publicKeyW1, 100)
wallet2 = Wallet(privateKeyW2, publicKeyW2)

print(wallet1.getBalance())
print(wallet2.getBalance())

executeTransaction(wallet1, wallet2, 10)

print(wallet1.getBalance())
print(wallet2.getBalance())
