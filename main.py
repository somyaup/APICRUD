import pymysql
from flaskext.mysql import MySQL
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request,Flask
# from werkzeug import generate_password_hash, check_password_hash
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/',methods =['GET'])
def home():
    resp = jsonify('Home')
    resp.status_code = 200
    return resp
@app.route('/add', methods=['POST'])
def add_store():
    conn = None
    cursor = None
    try:
        _json = request.json
        _trans_id = _json['id']
        _init_time = _json['time']
        _message = _json['sms']
        _customer_id = _json['customer']
        _store_id=_json['store']
        # validate the received values
        if _trans_id and _init_time and _message and _customer_id and _store_id and request.method == 'POST':
            # do not save password as a plain text
            #_hashed_password = generate_password_hash(_password)
            # save edits
            sql = "INSERT INTO sms_log VALUES(%s, %s, %s, %s,%s)"
            data = ( _trans_id,_init_time, _message, _customer_id ,_store_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Sms_log added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/sms_log')
def sms_log_all():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT transaction_id id , init_time time, message sms, sms_customer_id customer ,sms_store_id store FROM sms_log")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/sms_log/<int:id>')
def sms_log(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT transaction_id id , init_time time, message sms, sms_customer_id customer ,sms_store_id store FROM sms_log WHERE transaction_id=%s", id)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update', methods=['PUT'])
def update_log():
    conn = None
    cursor = None
    try:
        _json = request.json
        _trans_id = _json['trans_id']
        _init_time = _json['time']
        _message = _json['sms']
        _customer_id = _json['customer']
        _store_id = _json['store']
        # validate the received values
        if _trans_id and _init_time and _message and _customer_id and _store_id and request.method == 'PUT':
            # do not save password as a plain text
            #_hashed_password = generate_password_hash(_password)
            # save edits
            sql = "UPDATE sms_log SET  init_time= %s, message= %s, sms_customer_id= %s ,sms_store_id= %s WHERE transaction_id= %s"
            data = ( _init_time, _message, _customer_id ,_store_id,_trans_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('SMS LOG updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_log(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM sms_log WHERE transaction_id=%s", (id,))
        conn.commit()
        resp = jsonify('Log deleted successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == "__main__":
    app.run()
