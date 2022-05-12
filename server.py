from matplotlib.pyplot import new_figure_manager
import bank_pb2_grpc
import bank_pb2
import grpc
from concurrent import futures

class Client:
    def __init__(self,num_conta,nome):
        self.conta = num_conta 
        self.nome = nome
        self.saldo = 0.0

class Bank(bank_pb2_grpc.BankServicer):

    def __init__(self):
        self.clients = []

    def get_new_account_number(self):
        return len(self.clients)+1

    def CreateAccount(self, request, context):
        new_number = self.get_new_account_number()
        new_client = Client(new_number,str(request.client_name))
        self.clients.append(new_client)
        print(f"New Client: {new_client.nome} | Account: {new_client.conta}")
        return bank_pb2.AccountNumber(account_number=new_number)

    def GetAccoountInfo(self, request, context):
        client = self.clients[request.account_number-1]
        response = f"Cliente: {client.nome} | Conta: {client.conta} | Saldo: {client.saldo}"
        return bank_pb2.AccountInfo(info=response)

    def GetBalance(self, request, context):
        saldo  = self.clients[request.account_number-1].saldo
        return bank_pb2.Balance(balance=saldo)
        

    def Deposit(self, request, context):
        self.clients[request.account_number-1].saldo += float(request.amount)
        print("Sucess")
        return bank_pb2.Sucess(status=1)
    

    def Withdraw(self, request, context):
        if self.clients[request.account_number-1].saldo  > request.amount:
            self.clients[request.account_number-1].saldo -= request.amount
            print("Sucess")
            return bank_pb2.Sucess(status=1)
        else: 
            print("Fail")
            return bank_pb2.Sucess(status=0)
    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bank_pb2_grpc.add_BankServicer_to_server(Bank(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    print("Server Started")
    serve()