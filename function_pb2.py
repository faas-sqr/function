# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: function.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x66unction.proto\"e\n\x05\x45vent\x12 \n\x05heads\x18\x01 \x03(\x0b\x32\x11.Event.HeadsEntry\x12\x0c\n\x04\x62ody\x18\x02 \x01(\t\x1a,\n\nHeadsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x15\n\x05Reply\x12\x0c\n\x04\x62ody\x18\x01 \x01(\t2/\n\x0bHandleEvent\x12 \n\x0cProcessEvent\x12\x06.Event\x1a\x06.Reply\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'function_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EVENT_HEADSENTRY._options = None
  _EVENT_HEADSENTRY._serialized_options = b'8\001'
  _EVENT._serialized_start=18
  _EVENT._serialized_end=119
  _EVENT_HEADSENTRY._serialized_start=75
  _EVENT_HEADSENTRY._serialized_end=119
  _REPLY._serialized_start=121
  _REPLY._serialized_end=142
  _HANDLEEVENT._serialized_start=144
  _HANDLEEVENT._serialized_end=191
# @@protoc_insertion_point(module_scope)
