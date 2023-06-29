from flask import Flask



userServer = Flask(__name__)

@userServer.get('/')
def hello_world():
    return "hello"



if __name__ == "__main":
    userServer.run()