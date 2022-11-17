from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('contacts', user='',
                        password='', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class BaseModel(Model):
    class Meta:
        database = db


class Contact(BaseModel):
    first_name = CharField()
    last_name = CharField()
    phone = BigIntegerField()


db.connect()
db.drop_tables([Contact])
db.create_tables([Contact])

Contact(first_name='Michael', last_name='Bluth', phone=3105555555).save()
Contact(first_name='Buster', last_name='Bluth', phone=9175555555).save()

# find by first name
michael = Contact.select().where(Contact.first_name == 'Michael').get()
print(michael)

# find all
for contact in Contact.select():
    print(contact.first_name)
