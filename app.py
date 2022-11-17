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
    full_name = CharField()
    phone = IntegerField()


db.connect()
db.drop_tables([Contact])
db.create_tables([Contact])

Contact(full_name='Batman', phone=3105555555).save()
Contact(full_name='Superman', phone=9175555555).save()

app = Flask(__name__)
