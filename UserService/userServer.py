from flask import Flask
from routes.userRoutes import user_bp


userServer = Flask(__name__)

# including routes
userServer.register_blueprint(user_bp, url_prefix='/users')


@userServer.get('/')
def hello_world():
    return "hello"



if __name__ == "__main":
    # userServer.debug = True
    userServer.run()