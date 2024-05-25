from flask import Flask,jsonify
from flask_mysqldb import MySQL

from config import config

app = Flask(__name__)

#CONEXION DE LA BASE DE DATOS
conexion = MySQL(app)

#METODO GET
@app.route('/alumnos',methods=['GET'])
def listar_alumnos():
    #return "Texto prueba"
    try:
        cursor = conexion.connection.cursor()
        sql ="SELECT id, nombre, apellido, correo, edad, carrera FROM estudiante"
        cursor.execute(sql)
        #fetchall convierte toda la respuesta en algo entendible para PYTHON
        datos = cursor.fetchall()
        #MOSTRAR COMO JSON
        alumnos=[]
        for fila in datos:
            alumno = {'id':fila[0],'nombre':fila[1],'apellido':fila[2],'correo':fila[3],'edad':fila[4],'carrera':fila[5]}
            alumnos.append(alumno)
        return jsonify({'alumnos':alumnos,'Mensaje':"Alumnos listados."})
        #print(datos)
    except Exception as ex:
        return jsonify({'Mensaje':"ERROR"})
    
@app.route('/alumnos/<id>',methods=['GET'])
def leer_alumnos(id):
        #return "Texto prueba"
    try:
        cursor = conexion.connection.cursor()
        sql ="SELECT id, nombre, apellido, correo, edad, carrera FROM estudiante WHERE id='{0}'".format(id)
        cursor.execute(sql)
        #fetchone seleccionara un solo elemento - convierte toda la respuesta en algo entendible para PYTHON
        datos = cursor.fetchone()
        #MOSTRAR COMO JSON
        if datos != None:
            alumno = {'id':datos[0],'nombre':datos[1],'apellido':datos[2],'correo':datos[3],'edad':datos[4],'carrera':datos[5]}
            return jsonify({'alumno':alumno,'Mensaje':"Alumno listado."})
        else:
             return jsonify({'Mensaje':"ALUMNO NO ENCONTRADO"})
    except Exception as ex:
        return jsonify({'Mensaje':"ERROR"})


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()