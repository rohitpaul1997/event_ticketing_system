from flask import request
from middleware.middleware import *

@check_reg_details
def register():
    print(request.get_json())
    return "register"