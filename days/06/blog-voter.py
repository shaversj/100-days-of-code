from __future__ import print_function
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

ddb = boto3.resource('dynamodb').Table('editor-votes')


def build_response(message, message_type="Close", session_attributes=None):
    resp = {
        "dialogAction": {
            "type": message_type,
            "message": {
                "contentType": "PlainText",
                "content": message
            }
        }
    }
    if message_type is 'Close':
        resp['dialogAction']["fulfillmentState"] = "Fulfilled"
    if session_attributes:
        resp["sessionAttributes"] = session_attributes
    return resp


def lambda_handler(event, context):
    if 'ConnectToAgent' == event['currentIntent']['name']:
        return build_response("Ok, connecting you to an agent.")
    elif 'VoteEditor' == event['currentIntent']['name']:
        print(event)
        editor = event['currentIntent']['slots']['editor']
        resp = ddb.update_item(
            Key={"name": editor.lower()},
            UpdateExpression="SET votes = :incr + if_not_exists(votes, :default)",
            ExpressionAttributeValues={":incr": 1, ":default": 0},
            ReturnValues="ALL_NEW"
        )
        msg = "Awesome, now {} has {} votes!".format(
            resp['Attributes']['name'],
            resp['Attributes']['votes'])
        return build_response(msg)
    else:
        return build_response("That intent is not supported yet.")
