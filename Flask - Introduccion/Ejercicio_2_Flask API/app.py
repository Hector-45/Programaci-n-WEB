from flask import Flask,jsonify
from flask_mysqldb import MySQL

from config import config

app = Flask(__name__)

#CONEXION DE LA BASE DE DATOS
conexion = MySQL(app)

#METODO GET
@app.route('/cursos')
def listar_cursos():
    #return "Texto prueba"
    try:
        cursor = conexion.connection.cursor()
        sql ="SELECT cod_lib, descripcion, titulo, autor FROM LIBROS"
        cursor.execute(sql)
        #fetchall convierte toda la respuesta en algo entendible para PYTHON
        datos = cursor.fetchall()
        #MOSTRAR COMO JSON
        cursos=[]
        for fila in datos:
            curso = {'cod_lib':fila[0],'descripcion':fila[1],'titulo':fila[2],'autor':fila[3]}
            cursos.append(curso)
        return jsonify({'cursos':cursos,'Mensaje':"Cursos listados."})
        #print(datos)
        #return "CURSOS LISTADOS"
    except Exception as ex:
        return jsonify({'Mensaje':"ERROR"})
    

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()