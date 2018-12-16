from flask import Flask
from flask_restful import abort, Api, fields, marshal_with, reqparse, Resource
from datetime import datetime
from pytz import utc

from models import MessageModel
import status


class MessageManager():
    """
    This class will be used to persist the MessageModel instances in an in-memory dictionary. Our API methods will call methods for the MEssageManager class to retrieve, insert, update, and delete MessageModel instances. 
    """

    # The MessageManager class declares a last_id class attribute and initializes it to 0. This class attribute stores the last id that has been generated and assigned to a MessageModel instance stored in a dictionary

    last_id = 0

    def __init__(self):
        # The constructor, that is, the __init__ method, creates and initializes the messages attribute as an empty dictionary.
        self.messages = {}

    def insert_message(self, message):
        """
        Receives a recently created MessageModel instance in the message argument.
        """
        # Increases the value of the last_id class attribute. The code uses self.__class__ to reference the type of the current instance
        self.__class__.last_id += 1

        # Assigns value of last_id to the message
        message.id = self.__class__.last_id

        # Adds message to the messages dictionary by using last_id as the KEY, and the message as the VALUE.
        self.messages[self.__class__.last_id] = message

    def get_message(self, id):
        """
        Receives the id of the message that has to be retrieved from the self.messages dictionary. The code returns the value related to the key that matches the received id in the self.messages dictionary that we are using as our data source.
        """

        return self.messages[id]

    def delete_message(self, id):
        """
        Receives the id of the message that has to be removed from the self.messages dictionary. The code deletes the key-value pair whose key matches the received id in the self.messages dictionary that we are using as our data source.
        """

        del self.messages[id]


# The message_fields dictionary will be used to control the data that we want Flask-RESTful to render in the response, when we return MessageModel instances.
# fields is declared in the flask_restful.fields module.
# https://flask-restful.readthedocs.io/en/latest/fields.html


message_fields = {
    'id': fields.Integer,
    'uri': fields.Url('message_endpoint'),
    'message': fields.String,
    'duration': fields.Integer,
    'creation_date': fields.DateTime,  # outputs a formated datetime string
    'message_category': fields.String,
    'printed_times': fields.Integer,
    'printed_once': fields.Boolean
}


message_manager = MessageManager()
