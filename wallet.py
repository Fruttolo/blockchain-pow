import helpers
from transaction import Transaction

class Wallet:
    def __init__(self):
        self.publicKey, self.privateKey = helpers.generate_keys()

    def sendMoney(self, receiverPublicKey, amount):
        transaction = Transaction(receiverPublicKey, self.publicKey, amount)
        transaction.signTransaction(self.privateKey)
        return transaction

    def getPublicKey(self):
        return self.publicKey