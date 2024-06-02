from flask import Flask,jsonify,request
from flask_mysqldb import MySQL
from flask_cors import CORS

from config import config

app = Flask(__name__)

#CONEXION DE LA BASE DE DATOS
conexion = MySQL(app)
CORS(app)

#METODO POST (REGISTRAR)
@app.route('/usuarios',methods=['POST'])
def registrar_usuarios():
    try:
        #print(request.json)
        cursor = conexion.connection.cursor()
        sql="""INSERT INTO USUARIOS(nombre, contrasena) 
        VALUES ('{0}','{1}')""".format(request.json['nombre'],request.json['contrasena'])
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la accion de insercion
        return jsonify({'Mensaje':"USUARIO REGISTRADO"})
    except Exception as ex:
        return jsonify({'Mensaje':"ERROR DEL BACKEND"})
    

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()