import grpc
import bank_pb2
import bank_pb2_grpc 


with grpc.insecure_channel('localhost:50051') as channel:

    stub = bank_pb2_grpc.BankStub(channel)
        
    # Create account 
    request = bank_pb2.ClientInfo(client_name="Livia")
    response = stub.CreateAccount(request)

    request = bank_pb2.ClientInfo(client_name="Luiz")
    response = stub.CreateAccount(request)

    request = bank_pb2.ClientInfo(client_name="Rafael")
    response = stub.CreateAccount(request)

    # Get account info from Livia 
    request = bank_pb2.AccountNumber(account_number=1)
    response = stub.GetAccoountInfo(request)
    print(response)

    # Deposit in Luiz account
    request = bank_pb2.OperationInfo(account_number=2,amount=100)
    response = stub.Deposit(request)
    print(response)

    # Get balance from Luiz account
    request = bank_pb2.AccountNumber(account_number=2)
    response = stub.GetBalance(request)
    print(response)

    # Get balance from Livia account
    request = bank_pb2.AccountNumber(account_number=1)
    response = stub.GetBalance(request)
    print(response)

    # Deposit in Rafael account
    request = bank_pb2.OperationInfo(account_number=2,amount=50)
    response = stub.Deposit(request)
    print(response)
    
    # Withdraw from Livia account
    request = bank_pb2.OperationInfo(account_number=1,amount=20)
    response = stub.Withdraw(request)
    print(response)

    # Withdraw from Luiz account
    request = bank_pb2.OperationInfo(account_number=1,amount=50)
    response = stub.Withdraw(request)
    print(response)

    # Get balance from Luiz account
    request = bank_pb2.AccountNumber(account_number=2)
    response = stub.GetBalance(request)
    print(response)


