from flask import Flask  #from nombre de libreria import nombre del archivo
from flask import request #esto es para el metodo post
from flask import abort #esto es para mandar un req malo
from flask import render_template #esto es para renderear htmls
from flask import Response
from flask import jsonify
import mysql.connector
import json
import mysql_repo

app=Flask(__name__)


#testeo, endpoint GET hacia la tabla BD
@app.route('/records/getall')
def get_data():
    return mysql_repo.get()

#POST request
@app.route('/api/storedatapost',methods=['POST','GET'])
def store_datapost(data=None):
    data=request.json
    mysql_repo.store_data(data=data)
    return Response(status=201)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#endpoint para la grafica
@app.route('/api/line')
def line():
    return render_template('content.html', title='API TEST', max=17000)

#esto fue para testear la grafica
@app.route('/api/chart')
def get_chart():
    labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
    ]
    values = [
        967.67, 1190.89, 1079.75, 1349.19,
        2328.91, 2504.28, 2873.83, 4764.87,
        4349.29, 6458.30, 9907, 16297
    ]
    return {
        'labels':labels,
        'values':values
    }