from flask import Flask, jsonify, request
import pymysql
from flask_cors import CORS

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'hector'
app.config['MYSQL_DB'] = 'libreria'

conexion = pymysql.connect(
    host = app.config['MYSQL_HOST'],
    user = app.config['MYSQL_USER'],
    password= app.config['MYSQL_PASSWORD'],
    db = app.config['MYSQL_DB']
)

CORS(app)

#@app.route("/")

#def hola():
#    return "<h1>Hola Mundo</h1>"

@app.route("/usuario",methods = ['GET'])
def listar_usuarios():
    try:
        cursor = conexion.cursor()
        sql = "SELECT * FROM usuario"
        cursor.execute(sql)
        datos = cursor.fetchall()
        usuarios=[]
        for fila in datos:
            usuario = {'id': fila[0], 'nombre': fila[1], 'usuario': fila[2], 'password': fila[3]}
            usuarios.append(usuario)
        return jsonify({'usuarios': usuarios, 'mensaje': "usuarios listados.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})
    
