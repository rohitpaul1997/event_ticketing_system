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
    return Response(response='{"Success":"User registered Successfully"}', mimetype='application/json', status=200)



def login():
    login_details = request.get_json()

    # getting data from database 
    cursor = con.cursor()
    email_verification_query = "select password from user where email = '{}';".format(login_details['email'])
    try:
        cursor.execute(email_verification_query)
        encrypted_pass = cursor.fetchall()
    except:
        pass    
    if encrypted_pass == []:
        return Response(response='{"error":"Email doesnot match...."}',mimetype= 'application/json',status = 404)
    else:
        encrypted_pass = encrypted_pass[0][0].encode('utf-8')
        print(encrypted_pass) 
        if bcrypt.checkpw(login_details['password'].encode('utf-8'), encrypted_pass):
            return Response(response='{"Success":"Login Successfully"}',mimetype='application/json',status=200)
        else:
            return Response(response='{"error":"Password doesnot match...."}',mimetype= 'application/json',status = 404)
    return "okay"
