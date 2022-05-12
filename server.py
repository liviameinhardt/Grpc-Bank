from argon2 import PasswordHasher
from bank_pb2_grpc import BankServicer

class Client:
    def __init__(self,num_conta:float,nome:str) -> None:
        self.conta = num_conta 
        self.nome = nome
        self.saldo = 0.0


class Bank(BankServicer):

    def __init__(self) -> None:
        self.clients = []

    def get_new_account_number(self) -> int:
        return len(self.clients)+1

    def CreateAccount(self, request, context):
        new_client = Client(self.get_new_account_number(),request.client_name)
        self.clients.append(new_client)
        return new_client.conta

    def GetAccoountInfo(self, request, context):
        client = self.clients[request.account_number]
        return f"Cliente: {client.nome} | Saldo: {client.saldo}"

    def GetBalance(self, request, context):
        return  self.clients[request.account_number].saldo
        

    def Deposit(self, request, context):
        if request.account_number in self.clients:
            self.clients[request.account_number].saldo += request.amount
            return 1 
        else: return 0


    def Withdraw(self, request, context):

        if  request.account_number in self.clients:

            if self.clients[request.account_number].saldo  > request.amount:
                self.clients[request.account_number].saldo -= request.amount
                return 1 

            return 0 

        else: return 0
    

