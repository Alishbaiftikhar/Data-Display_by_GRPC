# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: car.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tcar.proto\x12\x03\x63\x61r\"$\n\x0eGetCarsRequest\x12\x12\n\nindex_name\x18\x01 \x01(\t\"q\n\x03\x43\x61r\x12\r\n\x05title\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\t\x12\r\n\x05place\x18\x03 \x01(\t\x12\x17\n\x0f\x65ngine_capacity\x18\x04 \x01(\t\x12\x15\n\rregistered_in\x18\x05 \x01(\t\x12\r\n\x05image\x18\x06 \x01(\t\")\n\x0fGetCarsResponse\x12\x16\n\x04\x63\x61rs\x18\x01 \x03(\x0b\x32\x08.car.Car2B\n\nCarService\x12\x34\n\x07GetCars\x12\x13.car.GetCarsRequest\x1a\x14.car.GetCarsResponseb\x06proto3')



_GETCARSREQUEST = DESCRIPTOR.message_types_by_name['GetCarsRequest']
_CAR = DESCRIPTOR.message_types_by_name['Car']
_GETCARSRESPONSE = DESCRIPTOR.message_types_by_name['GetCarsResponse']
GetCarsRequest = _reflection.GeneratedProtocolMessageType('GetCarsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCARSREQUEST,
  '__module__' : 'car_pb2'
  # @@protoc_insertion_point(class_scope:car.GetCarsRequest)
  })
_sym_db.RegisterMessage(GetCarsRequest)

Car = _reflection.GeneratedProtocolMessageType('Car', (_message.Message,), {
  'DESCRIPTOR' : _CAR,
  '__module__' : 'car_pb2'
  # @@protoc_insertion_point(class_scope:car.Car)
  })
_sym_db.RegisterMessage(Car)

GetCarsResponse = _reflection.GeneratedProtocolMessageType('GetCarsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCARSRESPONSE,
  '__module__' : 'car_pb2'
  # @@protoc_insertion_point(class_scope:car.GetCarsResponse)
  })
_sym_db.RegisterMessage(GetCarsResponse)

_CARSERVICE = DESCRIPTOR.services_by_name['CarService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETCARSREQUEST._serialized_start=18
  _GETCARSREQUEST._serialized_end=54
  _CAR._serialized_start=56
  _CAR._serialized_end=169
  _GETCARSRESPONSE._serialized_start=171
  _GETCARSRESPONSE._serialized_end=212
  _CARSERVICE._serialized_start=214
  _CARSERVICE._serialized_end=280
# @@protoc_insertion_point(module_scope)
