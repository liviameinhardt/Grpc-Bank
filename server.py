from argon2 import PasswordHasher
from bank_pb2_grpc import BankServicer

class Client:
    def __init__(self,num_conta:int,nome:str) -> None:
        self.conta = num_conta 
        self.nome = nome
        self.saldo = 0


class Bank(BankServicer):

    def __init__(self) -> None:
        self.clients = []

    def get_new_account_number(self) -> int:
        return len(self.clients)+1

    def CreateAccount(self, request, context):
        new_client = Client(self.get_new_account_number(),request.nome)
        self.clients.append(new_client)
        return new_client.conta

    def GetAccoountInfo(self, request, context):
        pass

    def GetBalance(self, request, context):
        pass

    def Deposit(self, request, context):
        pass

    def Withdraw(self, request, context):
        pass


class Bank(BankServicer):

    def __init__(self) -> None:
        self.clients = []

    def get_new_account_number(self) -> int:
        return len(self.clients)+1

    def create_account(self,nome:str) -> None:
        new_client = Client(self.get_new_account_number(),nome)
        self.clients.append(new_client)

    def get_account_info(self,number:int) -> str:
        client = self.clients[number]
        return f"Cliente: {client.nome} | Saldo: {client.saldo}"

    def get_saldo(self,number:int) -> int:
        return  self.clients[number].saldo

    def depositar(self,number:int,amount:float) -> int:
            self.clients[number].saldo += amount
 
    def sacar(self,number:int,amount:float) -> None:

        if  self.clients[number].saldo  > amount:
            self.clients[number].saldo -= amount
            return 1 
        else: 
            return 0
    