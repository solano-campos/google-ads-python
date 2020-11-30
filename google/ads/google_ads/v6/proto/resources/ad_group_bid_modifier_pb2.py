# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v6/proto/resources/ad_group_bid_modifier.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v6.proto.common import criteria_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_common_dot_criteria__pb2
from google.ads.google_ads.v6.proto.enums import bid_modifier_source_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_bid__modifier__source__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v6/proto/resources/ad_group_bid_modifier.proto',
  package='google.ads.googleads.v6.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v6.resourcesB\027AdGroupBidModifierProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V6.Resources\312\002!Google\\Ads\\GoogleAds\\V6\\Resources\352\002%Google::Ads::GoogleAds::V6::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nCgoogle/ads/googleads_v6/proto/resources/ad_group_bid_modifier.proto\x12!google.ads.googleads.v6.resources\x1a\x33google/ads/googleads_v6/proto/common/criteria.proto\x1a=google/ads/googleads_v6/proto/enums/bid_modifier_source.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xf7\x08\n\x12\x41\x64GroupBidModifier\x12J\n\rresource_name\x18\x01 \x01(\tB3\xe0\x41\x05\xfa\x41-\n+googleads.googleapis.com/AdGroupBidModifier\x12?\n\x08\x61\x64_group\x18\r \x01(\tB(\xe0\x41\x05\xfa\x41\"\n googleads.googleapis.com/AdGroupH\x01\x88\x01\x01\x12\x1e\n\x0c\x63riterion_id\x18\x0e \x01(\x03\x42\x03\xe0\x41\x03H\x02\x88\x01\x01\x12\x19\n\x0c\x62id_modifier\x18\x0f \x01(\x01H\x03\x88\x01\x01\x12\x44\n\rbase_ad_group\x18\x10 \x01(\tB(\xe0\x41\x03\xfa\x41\"\n googleads.googleapis.com/AdGroupH\x04\x88\x01\x01\x12h\n\x13\x62id_modifier_source\x18\n \x01(\x0e\x32\x46.google.ads.googleads.v6.enums.BidModifierSourceEnum.BidModifierSourceB\x03\xe0\x41\x03\x12\x64\n\x19hotel_date_selection_type\x18\x05 \x01(\x0b\x32:.google.ads.googleads.v6.common.HotelDateSelectionTypeInfoB\x03\xe0\x41\x05H\x00\x12j\n\x1chotel_advance_booking_window\x18\x06 \x01(\x0b\x32=.google.ads.googleads.v6.common.HotelAdvanceBookingWindowInfoB\x03\xe0\x41\x05H\x00\x12Z\n\x14hotel_length_of_stay\x18\x07 \x01(\x0b\x32\x35.google.ads.googleads.v6.common.HotelLengthOfStayInfoB\x03\xe0\x41\x05H\x00\x12V\n\x12hotel_check_in_day\x18\x08 \x01(\x0b\x32\x33.google.ads.googleads.v6.common.HotelCheckInDayInfoB\x03\xe0\x41\x05H\x00\x12\x41\n\x06\x64\x65vice\x18\x0b \x01(\x0b\x32*.google.ads.googleads.v6.common.DeviceInfoB\x03\xe0\x41\x05H\x00\x12V\n\x11preferred_content\x18\x0c \x01(\x0b\x32\x34.google.ads.googleads.v6.common.PreferredContentInfoB\x03\xe0\x41\x05H\x00:z\xea\x41w\n+googleads.googleapis.com/AdGroupBidModifier\x12Hcustomers/{customer_id}/adGroupBidModifiers/{ad_group_id}~{criterion_id}B\x0b\n\tcriterionB\x0b\n\t_ad_groupB\x0f\n\r_criterion_idB\x0f\n\r_bid_modifierB\x10\n\x0e_base_ad_groupB\x84\x02\n%com.google.ads.googleads.v6.resourcesB\x17\x41\x64GroupBidModifierProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V6.Resources\xca\x02!Google\\Ads\\GoogleAds\\V6\\Resources\xea\x02%Google::Ads::GoogleAds::V6::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads__v6_dot_proto_dot_common_dot_criteria__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_bid__modifier__source__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_ADGROUPBIDMODIFIER = _descriptor.Descriptor(
  name='AdGroupBidModifier',
  full_name='google.ads.googleads.v6.resources.AdGroupBidModifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.resources.AdGroupBidModifier.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005\372A-\n+googleads.googleapis.com/AdGroupBidModifier', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ad_group', full_name='google.ads.googleads.v6.resources.AdGroupBidModifier.ad_group', index=1,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005\372A\"\n googleads.googleapis.com/AdGroup', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='criterion_id', full_name='google.ads.googleads.v6.resources.AdGroupBidModifier.criterion_id', index=2,
      number=14, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bid_modifier', full_name='google.ads.googleads.v6.resources.AdGroupBidModifier.bid_modifier', index=3,
      number=15, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base_ad_group', full_name='google.ads.googleads.v6.resources.AdGroupBidModifier.base_ad_group', index=4,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003\372A\"\n googleads.googleapis.com/AdGroup', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bid_modifier_source', full_name='google.ads.googleads.v6.resources.AdGroupBidModifier.bid_modifier_source', index=5,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hotel_date_selection_type', full_name='google.ads.googleads.v6.resources.AdGroupBidModifier.hotel_date_selection_type', index=6,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hotel_advance_booking_window', full_name='google.ads.googleads.v6.resources.AdGroupBidModifier.hotel_advance_booking_window', index=7,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hotel_length_of_stay', full_name='google.ads.googleads.v6.resources.AdGroupBidModifier.hotel_length_of_stay', index=8,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hotel_check_in_day', full_name='google.ads.googleads.v6.resources.AdGroupBidModifier.hotel_check_in_day', index=9,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device', full_name='google.ads.googleads.v6.resources.AdGroupBidModifier.device', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='preferred_content', full_name='google.ads.googleads.v6.resources.AdGroupBidModifier.preferred_content', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352Aw\n+googleads.googleapis.com/AdGroupBidModifier\022Hcustomers/{customer_id}/adGroupBidModifiers/{ad_group_id}~{criterion_id}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='criterion', full_name='google.ads.googleads.v6.resources.AdGroupBidModifier.criterion',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_ad_group', full_name='google.ads.googleads.v6.resources.AdGroupBidModifier._ad_group',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_criterion_id', full_name='google.ads.googleads.v6.resources.AdGroupBidModifier._criterion_id',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_bid_modifier', full_name='google.ads.googleads.v6.resources.AdGroupBidModifier._bid_modifier',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_base_ad_group', full_name='google.ads.googleads.v6.resources.AdGroupBidModifier._base_ad_group',
      index=4, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=313,
  serialized_end=1456,
)

_ADGROUPBIDMODIFIER.fields_by_name['bid_modifier_source'].enum_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_bid__modifier__source__pb2._BIDMODIFIERSOURCEENUM_BIDMODIFIERSOURCE
_ADGROUPBIDMODIFIER.fields_by_name['hotel_date_selection_type'].message_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_common_dot_criteria__pb2._HOTELDATESELECTIONTYPEINFO
_ADGROUPBIDMODIFIER.fields_by_name['hotel_advance_booking_window'].message_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_common_dot_criteria__pb2._HOTELADVANCEBOOKINGWINDOWINFO
_ADGROUPBIDMODIFIER.fields_by_name['hotel_length_of_stay'].message_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_common_dot_criteria__pb2._HOTELLENGTHOFSTAYINFO
_ADGROUPBIDMODIFIER.fields_by_name['hotel_check_in_day'].message_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_common_dot_criteria__pb2._HOTELCHECKINDAYINFO
_ADGROUPBIDMODIFIER.fields_by_name['device'].message_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_common_dot_criteria__pb2._DEVICEINFO
_ADGROUPBIDMODIFIER.fields_by_name['preferred_content'].message_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_common_dot_criteria__pb2._PREFERREDCONTENTINFO
_ADGROUPBIDMODIFIER.oneofs_by_name['criterion'].fields.append(
  _ADGROUPBIDMODIFIER.fields_by_name['hotel_date_selection_type'])
_ADGROUPBIDMODIFIER.fields_by_name['hotel_date_selection_type'].containing_oneof = _ADGROUPBIDMODIFIER.oneofs_by_name['criterion']
_ADGROUPBIDMODIFIER.oneofs_by_name['criterion'].fields.append(
  _ADGROUPBIDMODIFIER.fields_by_name['hotel_advance_booking_window'])
_ADGROUPBIDMODIFIER.fields_by_name['hotel_advance_booking_window'].containing_oneof = _ADGROUPBIDMODIFIER.oneofs_by_name['criterion']
_ADGROUPBIDMODIFIER.oneofs_by_name['criterion'].fields.append(
  _ADGROUPBIDMODIFIER.fields_by_name['hotel_length_of_stay'])
_ADGROUPBIDMODIFIER.fields_by_name['hotel_length_of_stay'].containing_oneof = _ADGROUPBIDMODIFIER.oneofs_by_name['criterion']
_ADGROUPBIDMODIFIER.oneofs_by_name['criterion'].fields.append(
  _ADGROUPBIDMODIFIER.fields_by_name['hotel_check_in_day'])
_ADGROUPBIDMODIFIER.fields_by_name['hotel_check_in_day'].containing_oneof = _ADGROUPBIDMODIFIER.oneofs_by_name['criterion']
_ADGROUPBIDMODIFIER.oneofs_by_name['criterion'].fields.append(
  _ADGROUPBIDMODIFIER.fields_by_name['device'])
_ADGROUPBIDMODIFIER.fields_by_name['device'].containing_oneof = _ADGROUPBIDMODIFIER.oneofs_by_name['criterion']
_ADGROUPBIDMODIFIER.oneofs_by_name['criterion'].fields.append(
  _ADGROUPBIDMODIFIER.fields_by_name['preferred_content'])
_ADGROUPBIDMODIFIER.fields_by_name['preferred_content'].containing_oneof = _ADGROUPBIDMODIFIER.oneofs_by_name['criterion']
_ADGROUPBIDMODIFIER.oneofs_by_name['_ad_group'].fields.append(
  _ADGROUPBIDMODIFIER.fields_by_name['ad_group'])
_ADGROUPBIDMODIFIER.fields_by_name['ad_group'].containing_oneof = _ADGROUPBIDMODIFIER.oneofs_by_name['_ad_group']
_ADGROUPBIDMODIFIER.oneofs_by_name['_criterion_id'].fields.append(
  _ADGROUPBIDMODIFIER.fields_by_name['criterion_id'])
_ADGROUPBIDMODIFIER.fields_by_name['criterion_id'].containing_oneof = _ADGROUPBIDMODIFIER.oneofs_by_name['_criterion_id']
_ADGROUPBIDMODIFIER.oneofs_by_name['_bid_modifier'].fields.append(
  _ADGROUPBIDMODIFIER.fields_by_name['bid_modifier'])
_ADGROUPBIDMODIFIER.fields_by_name['bid_modifier'].containing_oneof = _ADGROUPBIDMODIFIER.oneofs_by_name['_bid_modifier']
_ADGROUPBIDMODIFIER.oneofs_by_name['_base_ad_group'].fields.append(
  _ADGROUPBIDMODIFIER.fields_by_name['base_ad_group'])
_ADGROUPBIDMODIFIER.fields_by_name['base_ad_group'].containing_oneof = _ADGROUPBIDMODIFIER.oneofs_by_name['_base_ad_group']
DESCRIPTOR.message_types_by_name['AdGroupBidModifier'] = _ADGROUPBIDMODIFIER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdGroupBidModifier = _reflection.GeneratedProtocolMessageType('AdGroupBidModifier', (_message.Message,), {
  'DESCRIPTOR' : _ADGROUPBIDMODIFIER,
  '__module__' : 'google.ads.googleads_v6.proto.resources.ad_group_bid_modifier_pb2'
  ,
  '__doc__': """Represents an ad group bid modifier.
  
  Attributes:
      resource_name:
          Immutable. The resource name of the ad group bid modifier. Ad
          group bid modifier resource names have the form:  ``customers/
          {customer_id}/adGroupBidModifiers/{ad_group_id}~{criterion_id}
          ``
      ad_group:
          Immutable. The ad group to which this criterion belongs.
      criterion_id:
          Output only. The ID of the criterion to bid modify.  This
          field is ignored for mutates.
      bid_modifier:
          The modifier for the bid when the criterion matches. The
          modifier must be in the range: 0.1 - 10.0. The range is 1.0 -
          6.0 for PreferredContent. Use 0 to opt out of a Device type.
      base_ad_group:
          Output only. The base ad group from which this draft/trial
          adgroup bid modifier was created. If ad\_group is a base ad
          group then this field will be equal to ad\_group. If the ad
          group was created in the draft or trial and has no
          corresponding base ad group, then this field will be null.
          This field is readonly.
      bid_modifier_source:
          Output only. Bid modifier source.
      criterion:
          The criterion of this ad group bid modifier.  Required in
          create operations starting in V5.
      hotel_date_selection_type:
          Immutable. Criterion for hotel date selection (default dates
          vs. user selected).
      hotel_advance_booking_window:
          Immutable. Criterion for number of days prior to the stay the
          booking is being made.
      hotel_length_of_stay:
          Immutable. Criterion for length of hotel stay in nights.
      hotel_check_in_day:
          Immutable. Criterion for day of the week the booking is for.
      device:
          Immutable. A device criterion.
      preferred_content:
          Immutable. A preferred content criterion.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.resources.AdGroupBidModifier)
  })
_sym_db.RegisterMessage(AdGroupBidModifier)


DESCRIPTOR._options = None
_ADGROUPBIDMODIFIER.fields_by_name['resource_name']._options = None
_ADGROUPBIDMODIFIER.fields_by_name['ad_group']._options = None
_ADGROUPBIDMODIFIER.fields_by_name['criterion_id']._options = None
_ADGROUPBIDMODIFIER.fields_by_name['base_ad_group']._options = None
_ADGROUPBIDMODIFIER.fields_by_name['bid_modifier_source']._options = None
_ADGROUPBIDMODIFIER.fields_by_name['hotel_date_selection_type']._options = None
_ADGROUPBIDMODIFIER.fields_by_name['hotel_advance_booking_window']._options = None
_ADGROUPBIDMODIFIER.fields_by_name['hotel_length_of_stay']._options = None
_ADGROUPBIDMODIFIER.fields_by_name['hotel_check_in_day']._options = None
_ADGROUPBIDMODIFIER.fields_by_name['device']._options = None
_ADGROUPBIDMODIFIER.fields_by_name['preferred_content']._options = None
_ADGROUPBIDMODIFIER._options = None
# @@protoc_insertion_point(module_scope)