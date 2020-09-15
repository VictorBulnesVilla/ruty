from flask import Response
from flask import jsonify
import mysql.connector
import json

#conexion a bd mysql
cnx = mysql.connector.connect(host="localhost",
                             user="root",         
                             passwd="",  
                             db="chart") 
#objeto Cursor.ejecuta todos los queries
cur = cnx.cursor()

#tester un metodo get
#ruta metodo GET para traer datos de la BD mysql 
def get():
    try:
        cur.execute( "SELECT * FROM records" )
        rows = cur.fetchall()
        resp = jsonify(rows)
        resp.status_code=200
        return resp
    except Exception as e:
        print(e)
    finally:
        cur.close()
        cnx.close()



#sql para el POST Request
def store_data(data):
    cur.execute("INSERT INTO records(value) VALUES ("+str(data["valor"])+ ");")
    cnx.commit()




