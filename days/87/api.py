from flask import Flask, abort
from flask.views import MethodView
from marshmallow import Schema, fields
from flask_rest_api import Api, Blueprint
from pytz import utc
from datetime import datetime

from models import MessageModel
import status


app = Flask(__name__)
api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(app)


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


# @api.definition('MessageModel')
class MessageFields(Schema):

    # This is needed
    class Meta:
        strict = True
        ordered = True

    id = fields.Integer()
    uri = fields.URL('message_endpoint')
    message = fields.String()
    duration = fields.Integer()
    creation_date = fields.DateTime()  # outputs a formated datetime string
    message_category = fields.String()
    printed_times = fields.Integer()
    printed_once = fields.Boolean()


message_manager = MessageManager()


@api_bp.route('/messages/<int:id>')
class Message(MethodView):
    def abort_if_message_doesnt_exist(self, id):
        if id not in message_manager.messages:
            abort(status.HTTP_404_NOT_FOUND,
                  "Message {0} doesn't exist".format(id))

    @api_bp.response(MessageFields)
    def get(self, id):
        self.abort_if_message_doesnt_exist(id)
        return message_manager.get_message(id)

    @api_bp.response()
    def delete(self, id):
        self.abort_if_message_doesnt_exist(id)
        message_manager.delete_message(id)
        return '', status.HTTP_204_NO_CONTENT

    @api_bp.response(MessageFields)
    def patch(self, id):
        self.abort_if_message_doesnt_exist(id)
        message = message_manager.get_message(id)

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


@api_bp.route('/messages/')
class MessageList(MethodView):

    # Add the many=True to return more than one result
    @api_bp.response(MessageFields(many=True))
    def get(self):
        # return message_manager.messages
        return [v for v in message_manager.messages.values()]

    # api_bp.arguments specify the values that are associated with d.
    @api_bp.arguments(MessageFields)
    # Prevents you from specifying code in return
    @api_bp.response(MessageFields, code=201)
    def post(self, d):
        creation_date = datetime.now(utc)
        message = MessageModel(**d, creation_date=creation_date)
        message_manager.insert_message(message)
        # return(message, status.HTTP_201_CREATED)
        return(message)


api.register_blueprint(api_bp)

# api.add_resource(MessageList, '/api/messages/')
# api.add_resource(Message, '/api/messages/<int:id>', endpoint = 'message_endpoint')


# if __name__ == '__main__':
app.run(debug=True)
