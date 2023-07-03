from flask import request
import bcrypt


#inporting modules
from middleware.middleware import *
from model.dbConn import con


@check_reg_details
def register():
    user_details = request.get_json()
    password = user_details['password']
    #encrypting password
    password = password.encode('utf-8')
    hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt(10)).decode('utf-8')
    # print(hashedPassword.decode('utf-8'))
    
    # saving data into database
    cursor = con.cursor()
    retrive_query = "select MAX(id) from user;"
    cursor.execute(retrive_query)
    data = cursor.fetchall()[0][0]
    if data == None:
        data = 1
    else:
        data += 1    
    query = "insert into user values({},'{}','{}',{},'{}');".format(data, user_details['email'],hashedPassword,user_details['phone'],user_details['location'])
    print(query)
    try:
        cursor.execute(query)
        con.commit()
    except Exception as e:
        print(str(e))
    return "register"
