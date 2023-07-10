from flask import request
import bcrypt


#inporting modules
from middleware.middleware import *
from model.dbConn import con


@check_reg_details
@check_db
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
    query = "insert into user values({},'{}','{}',{},'{}','{}');".format(data, user_details['email'],hashedPassword,user_details['phone'],'user',user_details['location'])
    print(query)
    # return str(user_details['phone'])
    try:
        cursor.execute(query)
        con.commit()
        return Response(response='{"Success":"User registered Successfully"}', mimetype='application/json', status=200)
    except Exception as e:
        print(str(e))
        return str(e)



def login():
    login_details = request.get_json()

    # getting data from database 
    cursor = con.cursor()
    email_verification_query = "select password from user where email = '{}';".format(login_details['email'])
    try:
        cursor.execute(email_verification_query)
        encrypted_pass = cursor.fetchall()
    except Exception as e:
        print(str(e))
        return Response(response='{"error":"Something went wrong, please try again later..."}',mimetype= 'application/json',status = 500)
    if encrypted_pass == []:
        return Response(response='{"error":"Email doesnot match...."}',mimetype= 'application/json',status = 404)
    else:
        encrypted_pass = encrypted_pass[0][0].encode('utf-8')
        print(encrypted_pass) 
        if bcrypt.checkpw(login_details['password'].encode('utf-8'), encrypted_pass):
            return Response(response='{"Success":"Login Successfully"}',mimetype='application/json',status=200)
        else:
            return Response(response='{"error":"Password doesnot match...."}',mimetype= 'application/json',status = 404)


def user_details(email):
    cursor = con.cursor()
    get_user_details_query = "select * from user where email = '{}'".format(email)
    try:
        cursor.execute(get_user_details_query)
        user_details = cursor.fetchall()
        # print(user_details[0][0])
        return {"email": user_details[0][1], "phone": user_details[0][3],"location":user_details[0][4]}
    except Exception as e:
        return str(e)       
