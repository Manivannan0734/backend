from flask import Flask,jsonify
from flask_cors import CORS 
import mysql.connector
from dotenv import load_dotenv
import os
SECRET_KEY = os.getenv("MY_SECRET")
load_dotenv()
app=Flask(__name__)
CORS(app)

db_config={
    'host': os.getenv('MYSQL_HOST'),
    'database': os.getenv('MYSQL_DATABASE'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
}

@app.route('/api/data',methods=['GET'])
def get_data():
    try:
        conn=mysql.connector.connect(**db_config)
        cursor=conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM employees")
        rows = cursor.fetchall()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)