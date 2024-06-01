from flask import Flask,jsonify,request
from flask_mysqldb import MySQL

from config import config

app = Flask(__name__)

#CONEXION DE LA BASE DE DATOS
conexion = MySQL(app)

#METODO POST (REGISTRAR)
@app.route('/usuarios',methods=['POST'])
def registrar_usuarios():
    try:
        #print(request.json)
        cursor = conexion.connection.cursor()
        sql="""INSERT INTO usuarios(id, nombre, contrasena) 
        VALUES ('{0}','{1}','{2}')""".format(request.json['id'],request.json['nombre'],request.json['contrasena'])
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la accion de insercion
        return jsonify({'Mensaje':"USUARIO REGISTRADO"})
    except Exception as ex:
        return jsonify({'Mensaje':"ERROR"})
    

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()