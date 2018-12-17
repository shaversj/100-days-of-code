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


# Flask-RESTful uses resources built on top of Flask pluggable views as the main building block for a RESTful API.
# Create a subclass of flask_restful.Resource class and declare the mthods for each supported HTTP verb. A subclass of flask_restful.Resource represents a RESTful resource and therefore, we will have to declare one class to represent the collection of messages and another one to represent the message resource.

class Message(Resource):
    def abort_if_message_doesnt_exist(self, id):
        if id not in message_manager.messages:
            abort(
                status.HTTP_404_NOT_FOUND,
                message="Message {0} doesn't exist".format(id))

    @marshal_with(message_fields)
    def get(self, id):
        self.abort_if_message_doesnt_exist(id)
        return message_manager.get_message(id)

    def delete(self, id):
        self.abort_if_message_doesnt_exist(id)
        message_manager.delete_message(id)
        return '', status.HTTP_204_NO_CONTENT

    @marshal_with(message_fields)
    def patch(self, id):
        self.abort_if_message_doesnt_exist(id)
        message = message_manager.get_message(id)
        parser = reqparse.RequestParser()
        parser.add_argument('message', type=str)
        parser.add_argument('duration', type=int)
        parser.add_argument('printed_times', type=int)
        parser.add_argument('printed_once', type=bool)
        args = parser.parse_args()
        if 'message' in args:
            message.message = args['message']
        if 'duration' in args:
            message.duration = args['duration']
        if 'printed_times' in args:
            message.printed_times = args['printed_times']
        if 'printed_once' in args:
            message.printed_once = args['printed_once']
        return message


class MessageList(Resource):
    @marshal_with(message_fields)
    def get(self):
        return [v for v in message_manager.messages.values()]

    @marshal_with(message_fields)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('message', type=str, required=True,
                            help='Message cannot be blank!')
        parser.add_argument('duration', type=int, required=True,
                            help='Duration cannot be blank!')
        parser.add_argument('message_category', type=str,
                            required=True, help='Message category cannot be blank!')
        args = parser.parse_args()
        message = MessageModel(
            message=args['message'],
            duration=args['duration'],
            creation_date=datetime.now(utc),
            message_category=args['message_category']
        )
        message_manager.insert_message(message)
        return message, status.HTTP_201_CREATED


app = Flask(__name__)
api = Api(app)
api.add_resource(MessageList, '/api/messages/')
api.add_resource(Message, '/api/messages/<int:id>',
                 endpoint='message_endpoint')


if __name__ == '__main__':
    app.run(debug=True)
