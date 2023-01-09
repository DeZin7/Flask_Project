from marshmallow import Schema, fields

class PlainItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
   

class PlainStoresSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()


class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoresSchema(), dump_only=True) #when return data to the client, not when receiving data from the client

class StoresSchema(PlainStoresSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)

    #using PlainStoresSchemas and PLainItemSchema so that when we use  nesting, we can only include a part of the fields
