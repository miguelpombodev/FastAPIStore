from marshmallow import Schema, fields


class Product(Schema):
    id = fields.Str()
    type_id = fields.Int()
    brand_id = fields.Int()
    sku = fields.Str()
    name = fields.Str()
    value = fields.Float()
    stock_amount = fields.Int()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
