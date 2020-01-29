# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common-index-format.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common-index-format.proto',
  package='cif',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x19\x63ommon-index-format.proto\x12\x03\x63if\"$\n\x07Posting\x12\r\n\x05\x64ocid\x18\x01 \x01(\x05\x12\n\n\x02tf\x18\x02 \x01(\x05\"S\n\x0cPostingsList\x12\x0c\n\x04term\x18\x01 \x01(\t\x12\n\n\x02\x64\x66\x18\x02 \x01(\x03\x12\n\n\x02\x63\x66\x18\x03 \x01(\x03\x12\x1d\n\x07posting\x18\x04 \x03(\x0b\x32\x0c.cif.Postingb\x06proto3'
)




_POSTING = _descriptor.Descriptor(
  name='Posting',
  full_name='cif.Posting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='docid', full_name='cif.Posting.docid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tf', full_name='cif.Posting.tf', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=70,
)


_POSTINGSLIST = _descriptor.Descriptor(
  name='PostingsList',
  full_name='cif.PostingsList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='term', full_name='cif.PostingsList.term', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='df', full_name='cif.PostingsList.df', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cf', full_name='cif.PostingsList.cf', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='posting', full_name='cif.PostingsList.posting', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=155,
)

_POSTINGSLIST.fields_by_name['posting'].message_type = _POSTING
DESCRIPTOR.message_types_by_name['Posting'] = _POSTING
DESCRIPTOR.message_types_by_name['PostingsList'] = _POSTINGSLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Posting = _reflection.GeneratedProtocolMessageType('Posting', (_message.Message,), {
  'DESCRIPTOR' : _POSTING,
  '__module__' : 'common_index_format_pb2'
  # @@protoc_insertion_point(class_scope:cif.Posting)
  })
_sym_db.RegisterMessage(Posting)

PostingsList = _reflection.GeneratedProtocolMessageType('PostingsList', (_message.Message,), {
  'DESCRIPTOR' : _POSTINGSLIST,
  '__module__' : 'common_index_format_pb2'
  # @@protoc_insertion_point(class_scope:cif.PostingsList)
  })
_sym_db.RegisterMessage(PostingsList)


# @@protoc_insertion_point(module_scope)

