from flask import Blueprint
from controller.userController import *
from middleware.middleware import *

user_bp = Blueprint('user_bp',__name__)


user_bp.route('/register',methods = ['POST'])(register)