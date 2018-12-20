# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/resources/billing_setup.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v0.proto.enums import billing_setup_status_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_billing__setup__status__pb2
from google.ads.google_ads.v0.proto.enums import time_type_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_time__type__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/resources/billing_setup.proto',
  package='google.ads.googleads.v0.resources',
  syntax='proto3',
  serialized_pb=_b('\n;google/ads/googleads_v0/proto/resources/billing_setup.proto\x12!google.ads.googleads.v0.resources\x1a>google/ads/googleads_v0/proto/enums/billing_setup_status.proto\x1a\x33google/ads/googleads_v0/proto/enums/time_type.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xbb\x07\n\x0c\x42illingSetup\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\'\n\x02id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12X\n\x06status\x18\x03 \x01(\x0e\x32H.google.ads.googleads.v0.enums.BillingSetupStatusEnum.BillingSetupStatus\x12\x36\n\x10payments_account\x18\x0b \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x62\n\x15payments_account_info\x18\x0c \x01(\x0b\x32\x43.google.ads.googleads.v0.resources.BillingSetup.PaymentsAccountInfo\x12\x37\n\x0fstart_date_time\x18\t \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x00\x12O\n\x0fstart_time_type\x18\n \x01(\x0e\x32\x34.google.ads.googleads.v0.enums.TimeTypeEnum.TimeTypeH\x00\x12\x35\n\rend_date_time\x18\r \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x01\x12M\n\rend_time_type\x18\x0e \x01(\x0e\x32\x34.google.ads.googleads.v0.enums.TimeTypeEnum.TimeTypeH\x01\x1a\xca\x02\n\x13PaymentsAccountInfo\x12\x39\n\x13payments_account_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12;\n\x15payments_account_name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x39\n\x13payments_profile_id\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12;\n\x15payments_profile_name\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x43\n\x1dsecondary_payments_profile_id\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\x0c\n\nstart_timeB\n\n\x08\x65nd_timeB\xd6\x01\n%com.google.ads.googleads.v0.resourcesB\x11\x42illingSetupProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v0/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V0.Resources\xca\x02!Google\\Ads\\GoogleAds\\V0\\Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_billing__setup__status__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_time__type__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_BILLINGSETUP_PAYMENTSACCOUNTINFO = _descriptor.Descriptor(
  name='PaymentsAccountInfo',
  full_name='google.ads.googleads.v0.resources.BillingSetup.PaymentsAccountInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payments_account_id', full_name='google.ads.googleads.v0.resources.BillingSetup.PaymentsAccountInfo.payments_account_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payments_account_name', full_name='google.ads.googleads.v0.resources.BillingSetup.PaymentsAccountInfo.payments_account_name', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payments_profile_id', full_name='google.ads.googleads.v0.resources.BillingSetup.PaymentsAccountInfo.payments_profile_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payments_profile_name', full_name='google.ads.googleads.v0.resources.BillingSetup.PaymentsAccountInfo.payments_profile_name', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secondary_payments_profile_id', full_name='google.ads.googleads.v0.resources.BillingSetup.PaymentsAccountInfo.secondary_payments_profile_id', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=847,
  serialized_end=1177,
)

_BILLINGSETUP = _descriptor.Descriptor(
  name='BillingSetup',
  full_name='google.ads.googleads.v0.resources.BillingSetup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.resources.BillingSetup.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v0.resources.BillingSetup.id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v0.resources.BillingSetup.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payments_account', full_name='google.ads.googleads.v0.resources.BillingSetup.payments_account', index=3,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payments_account_info', full_name='google.ads.googleads.v0.resources.BillingSetup.payments_account_info', index=4,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_date_time', full_name='google.ads.googleads.v0.resources.BillingSetup.start_date_time', index=5,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time_type', full_name='google.ads.googleads.v0.resources.BillingSetup.start_time_type', index=6,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_date_time', full_name='google.ads.googleads.v0.resources.BillingSetup.end_date_time', index=7,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time_type', full_name='google.ads.googleads.v0.resources.BillingSetup.end_time_type', index=8,
      number=14, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BILLINGSETUP_PAYMENTSACCOUNTINFO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='start_time', full_name='google.ads.googleads.v0.resources.BillingSetup.start_time',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='end_time', full_name='google.ads.googleads.v0.resources.BillingSetup.end_time',
      index=1, containing_type=None, fields=[]),
  ],
  serialized_start=248,
  serialized_end=1203,
)

_BILLINGSETUP_PAYMENTSACCOUNTINFO.fields_by_name['payments_account_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_BILLINGSETUP_PAYMENTSACCOUNTINFO.fields_by_name['payments_account_name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_BILLINGSETUP_PAYMENTSACCOUNTINFO.fields_by_name['payments_profile_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_BILLINGSETUP_PAYMENTSACCOUNTINFO.fields_by_name['payments_profile_name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_BILLINGSETUP_PAYMENTSACCOUNTINFO.fields_by_name['secondary_payments_profile_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_BILLINGSETUP_PAYMENTSACCOUNTINFO.containing_type = _BILLINGSETUP
_BILLINGSETUP.fields_by_name['id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_BILLINGSETUP.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_billing__setup__status__pb2._BILLINGSETUPSTATUSENUM_BILLINGSETUPSTATUS
_BILLINGSETUP.fields_by_name['payments_account'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_BILLINGSETUP.fields_by_name['payments_account_info'].message_type = _BILLINGSETUP_PAYMENTSACCOUNTINFO
_BILLINGSETUP.fields_by_name['start_date_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_BILLINGSETUP.fields_by_name['start_time_type'].enum_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_time__type__pb2._TIMETYPEENUM_TIMETYPE
_BILLINGSETUP.fields_by_name['end_date_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_BILLINGSETUP.fields_by_name['end_time_type'].enum_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_time__type__pb2._TIMETYPEENUM_TIMETYPE
_BILLINGSETUP.oneofs_by_name['start_time'].fields.append(
  _BILLINGSETUP.fields_by_name['start_date_time'])
_BILLINGSETUP.fields_by_name['start_date_time'].containing_oneof = _BILLINGSETUP.oneofs_by_name['start_time']
_BILLINGSETUP.oneofs_by_name['start_time'].fields.append(
  _BILLINGSETUP.fields_by_name['start_time_type'])
_BILLINGSETUP.fields_by_name['start_time_type'].containing_oneof = _BILLINGSETUP.oneofs_by_name['start_time']
_BILLINGSETUP.oneofs_by_name['end_time'].fields.append(
  _BILLINGSETUP.fields_by_name['end_date_time'])
_BILLINGSETUP.fields_by_name['end_date_time'].containing_oneof = _BILLINGSETUP.oneofs_by_name['end_time']
_BILLINGSETUP.oneofs_by_name['end_time'].fields.append(
  _BILLINGSETUP.fields_by_name['end_time_type'])
_BILLINGSETUP.fields_by_name['end_time_type'].containing_oneof = _BILLINGSETUP.oneofs_by_name['end_time']
DESCRIPTOR.message_types_by_name['BillingSetup'] = _BILLINGSETUP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BillingSetup = _reflection.GeneratedProtocolMessageType('BillingSetup', (_message.Message,), dict(

  PaymentsAccountInfo = _reflection.GeneratedProtocolMessageType('PaymentsAccountInfo', (_message.Message,), dict(
    DESCRIPTOR = _BILLINGSETUP_PAYMENTSACCOUNTINFO,
    __module__ = 'google.ads.google_ads.v0.proto.resources.billing_setup_pb2'
    ,
    __doc__ = """Container of Payments account information for this billing.
    
    
    Attributes:
        payments_account_id:
            A 16 digit id used to identify the Payments account associated
            with the billing setup.  This must be passed as a string with
            dashes, e.g. "1234-5678-9012-3456".
        payments_account_name:
            The name of the Payments account associated with the billing
            setup.  This enables the user to specify a meaningful name for
            a Payments account to aid in reconciling monthly invoices.
            This name will be printed in the monthly invoices.
        payments_profile_id:
            A 12 digit id used to identify the Payments profile associated
            with the billing setup.  This must be passed in as a string
            with dashes, e.g. "1234-5678-9012".
        payments_profile_name:
            The name of the Payments profile associated with the billing
            setup.
        secondary_payments_profile_id:
            A secondary payments profile id present in uncommon
            situations, e.g. when a sequential liability agreement has
            been arranged.
    """,
    # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.resources.BillingSetup.PaymentsAccountInfo)
    ))
  ,
  DESCRIPTOR = _BILLINGSETUP,
  __module__ = 'google.ads.google_ads.v0.proto.resources.billing_setup_pb2'
  ,
  __doc__ = """A billing setup across Ads and Payments systems; an association between
  a Payments account and an advertiser. A billing setup is specific to one
  advertiser.
  
  
  Attributes:
      resource_name:
          The resource name of the billing setup. BillingSetup resource
          names have the form:
          ``customers/{customer_id}/billingSetups/{billing_setup_id}``
      id:
          The ID of the billing setup.
      status:
          The status of the billing setup.
      payments_account:
          The resource name of the Payments account associated with this
          billing setup. Payments resource names have the form:
          ``customers/{customer_id}/paymentsAccounts/
          {payments_profile_id}_{payments_account_id}`` When setting up
          billing, this is used to signup with an existing Payments
          account (and then payments\_account\_info should not be set).
          When getting a billing setup, this and payments\_account\_info
          will be populated.
      payments_account_info:
          The Payments account information associated with this billing
          setup. When setting up billing, this is used to signup with a
          new Payments account (and then payments\_account should not be
          set). When getting a billing setup, this and payments\_account
          will be populated.
      start_time:
          When creating a new billing setup, this is when the setup
          should take effect. NOW is the only acceptable start time if
          the customer doesn't have any approved setups.  When fetching
          an existing billing setup, this is the requested start time.
          However, if the setup was approved (see status) after the
          requested start time, then this is the approval time.
      start_date_time:
          The start date time in yyyy-MM-dd or yyyy-MM-dd HH:mm:ss
          format. Only a future time is allowed.
      start_time_type:
          The start time as a type. Only NOW is allowed.
      end_time:
          When the billing setup ends / ended. This is either FOREVER or
          the start time of the next scheduled billing setup.
      end_date_time:
          The end date time in yyyy-MM-dd or yyyy-MM-dd HH:mm:ss format.
      end_time_type:
          The end time as a type. The only possible value is FOREVER.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.resources.BillingSetup)
  ))
_sym_db.RegisterMessage(BillingSetup)
_sym_db.RegisterMessage(BillingSetup.PaymentsAccountInfo)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n%com.google.ads.googleads.v0.resourcesB\021BillingSetupProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v0/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V0.Resources\312\002!Google\\Ads\\GoogleAds\\V0\\Resources'))
# @@protoc_insertion_point(module_scope)