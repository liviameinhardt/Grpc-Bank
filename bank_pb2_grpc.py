# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import bank_pb2 as bank__pb2


class BankStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateAccount = channel.unary_unary(
                '/Bank/CreateAccount',
                request_serializer=bank__pb2.ClientInfo.SerializeToString,
                response_deserializer=bank__pb2.AccountNumber.FromString,
                )
        self.GetAccoountInfo = channel.unary_unary(
                '/Bank/GetAccoountInfo',
                request_serializer=bank__pb2.AccountNumber.SerializeToString,
                response_deserializer=bank__pb2.AccountInfo.FromString,
                )
        self.GetBalance = channel.unary_unary(
                '/Bank/GetBalance',
                request_serializer=bank__pb2.AccountNumber.SerializeToString,
                response_deserializer=bank__pb2.Balance.FromString,
                )
        self.Deposit = channel.unary_unary(
                '/Bank/Deposit',
                request_serializer=bank__pb2.OperationInfo.SerializeToString,
                response_deserializer=bank__pb2.Sucess.FromString,
                )
        self.Withdraw = channel.unary_unary(
                '/Bank/Withdraw',
                request_serializer=bank__pb2.OperationInfo.SerializeToString,
                response_deserializer=bank__pb2.Sucess.FromString,
                )


class BankServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAccoountInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBalance(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Deposit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Withdraw(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BankServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateAccount,
                    request_deserializer=bank__pb2.ClientInfo.FromString,
                    response_serializer=bank__pb2.AccountNumber.SerializeToString,
            ),
            'GetAccoountInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAccoountInfo,
                    request_deserializer=bank__pb2.AccountNumber.FromString,
                    response_serializer=bank__pb2.AccountInfo.SerializeToString,
            ),
            'GetBalance': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBalance,
                    request_deserializer=bank__pb2.AccountNumber.FromString,
                    response_serializer=bank__pb2.Balance.SerializeToString,
            ),
            'Deposit': grpc.unary_unary_rpc_method_handler(
                    servicer.Deposit,
                    request_deserializer=bank__pb2.OperationInfo.FromString,
                    response_serializer=bank__pb2.Sucess.SerializeToString,
            ),
            'Withdraw': grpc.unary_unary_rpc_method_handler(
                    servicer.Withdraw,
                    request_deserializer=bank__pb2.OperationInfo.FromString,
                    response_serializer=bank__pb2.Sucess.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Bank', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Bank(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Bank/CreateAccount',
            bank__pb2.ClientInfo.SerializeToString,
            bank__pb2.AccountNumber.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAccoountInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Bank/GetAccoountInfo',
            bank__pb2.AccountNumber.SerializeToString,
            bank__pb2.AccountInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBalance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Bank/GetBalance',
            bank__pb2.AccountNumber.SerializeToString,
            bank__pb2.Balance.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Deposit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Bank/Deposit',
            bank__pb2.OperationInfo.SerializeToString,
            bank__pb2.Sucess.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Withdraw(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Bank/Withdraw',
            bank__pb2.OperationInfo.SerializeToString,
            bank__pb2.Sucess.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
