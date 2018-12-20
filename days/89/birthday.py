from marshmallow import (
    Schema, pre_load, pre_dump, post_load, validates_schema,
    validates, fields, ValidationError, pprint
)


class Person(object):

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def __repr__(self):
        return self.name


class PersonSchema(Schema):

    name = fields.String()
    birthday = fields.Date()

    @post_load
    def create_person(self, info):
        return Person(**info)


my_data = [{"name": 'Benjamin Franklin', "birthday": '01/17/1706'},
           {"name": 'George Washington', "birthday": '02/22/1732'}]


schema = PersonSchema(many=True)
birthdays = schema.load(my_data)
pprint(birthdays.data)
