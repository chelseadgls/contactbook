from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('contacts', user='chelseadgls',
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
    phone = IntegerField()


db.connect()
db.drop_tables([Contact])
db.create_tables([Contact])

Contact(first_name='Michael', last_name='Bluth', phone=3105555555).save()
Contact(first_name='Buster', last_name='Bluth', phone=9175555555).save()

app = Flask(__name__)

# routes

# get route
# put route
# update route
# delete route

app.run(debug=True, port=9000)
