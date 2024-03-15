import datetime as dt

from marshmallow import Schema, fields


class ApplicationDetails(object):
    def __init__(self, channel, seller, orig_rate, orig_upb, orig_term, oltv, ocltv, num_bo, dti, cscore_b, cscore_c, first_flag, 
    purpose, prop, no_units, occ_stat, relocation_mortgage_indicator, act_period_year, act_period_month, orig_date_year, orig_date_month, first_pay_year,
    first_pay_month, lat, long, type):
        self.channel = channel 
        self.seller = seller
        self.orig_rate = orig_rate
        self.orig_upb = orig_upb
        self.orig_term = orig_term 
        self.oltv = oltv
        self.ocltv = ocltv
        self.num_bo = num_bo
        self.dti = dti
        self.cscore_b = cscore_b
        self.cscore_c = cscore_c
        self.first_flag = first_flag
        self.purpose = purpose
        self.prop = prop
        self.no_units = no_units
        self.occ_stat = occ_stat
        self.relocation_mortgage_indicator = relocation_mortgage_indicator
        self.act_period_year = act_period_year
        self.act_period_month = act_period_month
        self.orig_date_year = orig_date_year
        self.orig_date_month = orig_date_month
        self.first_pay_year = first_pay_year
        self.first_pay_month = first_pay_month
        self.lat = lat
        self.long = long
        self.created_at = dt.datetime.now()
        self.type = type

    def __repr__(self):
        return '<ApplicationDetails(name={self.channel!r})>'.format(self=self)


class ApplicationDetailsSchema(Schema):
    channel = fields.Str()
    seller = fields.Str()
    orig_rate = fields.Float()
    orig_upb = fields.Float()
    orig_term = fields.Int()
    oltv = fields.Int()
    ocltv = fields.Float()
    num_bo = fields.Float()
    dti = fields.Int()
    cscore_b = fields.Float()
    cscore_c = fields.Float()
    first_flag  = fields.Str()
    purpose = fields.Str()
    prop = fields.Str()
    no_units = fields.Int()
    occ_stat = fields.Str()
    relocation_mortgage_indicator = fields.Str()
    act_period_year = fields.Int()
    act_period_month = fields.Int()
    orig_date_year = fields.Int()
    orig_date_month = fields.Int()
    first_pay_year = fields.Int()
    first_pay_month = fields.Int()
    lat = fields.Float()
    long = fields.Float()
    created_at = fields.Date()
    type = fields.Str()