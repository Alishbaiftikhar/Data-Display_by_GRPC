# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import car_pb2 as car__pb2


class CarServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCars = channel.unary_unary(
                '/car.CarService/GetCars',
                request_serializer=car__pb2.GetCarsRequest.SerializeToString,
                response_deserializer=car__pb2.GetCarsResponse.FromString,
                )


class CarServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetCars(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CarServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCars': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCars,
                    request_deserializer=car__pb2.GetCarsRequest.FromString,
                    response_serializer=car__pb2.GetCarsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'car.CarService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CarService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetCars(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/car.CarService/GetCars',
            car__pb2.GetCarsRequest.SerializeToString,
            car__pb2.GetCarsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
