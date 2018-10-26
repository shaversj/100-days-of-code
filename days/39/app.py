from flask import Flask
from flask import request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/sms', methods=['GET', 'POST'])
def sms():
    response = MessagingResponse()
    #body = request.form['Body']
    #response.message("You sent me: {0}".format(body))
    response.message("The Robots are coming! Head for the hills!")

    return str(response)

@app.route('/hello', methods=['GET'])
def hello_world():
    return 'Hello World!'


if __name__ == "__main__":
    app.debug = True
    app.run()