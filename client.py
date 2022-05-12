import grpc
import bank_pb2_grpc


channel = grpc.insecure_channel('localhost:50051')
stub = bank_pb2_grpc.BankStub(channel)

livia = stub.CreateAccount("Lívia")
luiz = stub.CreateAccount("Luiz")

print(livia)
