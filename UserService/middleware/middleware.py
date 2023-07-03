from flask import request, Response
from functools import wraps
import re


# registration field checking middleware
def check_reg_details(func):
    @wraps(func)
    def check_reg(*args, **kargs):
        userData = request.get_json()
        fields = ['email', 'password', 'phone', 'location']
        for field in fields:
            if field not in userData:
                return Response(response='{"error":"please provide all fields."}', mimetype='application/json', status=400)
        password = userData['password']
        phone = userData['phone']
        email = userData['email']
        pass_reg = "[A-Za-z0-9!@#$%^&*]{6,20}$"
        pass_com = re.compile(pass_reg)
        email_reg = '[a-z0-9]+@[a-z]+\.[a-z]{2,3}'
        email_com = re.compile(email_reg)
        if re.search(pass_com, password) == None:
            return Response(response='{"error":"please provide a correct password"}', mimetype='application/json', status=400)
        if re.search(email_reg, email) == None:
            return Response(response='{"error":"please provide a correct email"}', mimetype='application/json', status=400)
        if len(str(phone)) != 10:
            return Response(response='{"error":"please provide a correct Phone Number"}', mimetype='application/json', status=400)
        return func(*args, **kargs)
    return check_reg
