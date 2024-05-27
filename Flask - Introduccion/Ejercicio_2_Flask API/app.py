from flask import Flask,jsonify,request
from flask_mysqldb import MySQL

from config import config

app = Flask(__name__)

#CONEXION DE LA BASE DE DATOS
conexion = MySQL(app)

#METODO GET
@app.route('/cursos',methods=['GET'])
def listar_cursos():
    #return "Texto prueba"
    try:
        cursor = conexion.connection.cursor()
        sql ="SELECT cod_lib, descripcion, titulo, autor, editorial, precio FROM LIBROS"
        cursor.execute(sql)
        #fetchall convierte toda la respuesta en algo entendible para PYTHON
        datos = cursor.fetchall()
        #MOSTRAR COMO JSON
        cursos=[]
        for fila in datos:
            curso = {'cod_lib':fila[0],'descripcion':fila[1],'titulo':fila[2],
                     'autor':fila[3],'editorial':fila[4],'precio':fila[5]}
            cursos.append(curso)
        return jsonify({'cursos':cursos,'Mensaje':"Cursos listados."})
        #print(datos)
        #return "CURSOS LISTADOS"
    except Exception as ex:
        return jsonify({'Mensaje':"ERROR"})

@app.route('/cursos/<cod_lib>',methods=['GET'])
def leer_alumnos(cod_lib):
        #return "Texto prueba"
    try:
        cursor = conexion.connection.cursor()
        sql ="SELECT cod_lib, descripcion, titulo, autor FROM LIBROS WHERE cod_lib='{0}'".format(cod_lib)
        cursor.execute(sql)
        #fetchone seleccionara un solo elemento - convierte toda la respuesta en algo entendible para PYTHON
        datos = cursor.fetchone()
        #MOSTRAR COMO JSON
        if datos != None:
            alumno = {'cod_lib':datos[0],'descripcion':datos[1],'titulo':datos[2],'autor':datos[3]}
            return jsonify({'alumno':alumno,'Mensaje':"Alumno listado."})
        else:
             return jsonify({'Mensaje':"ALUMNO NO ENCONTRADO"})
    except Exception as ex:
        return jsonify({'Mensaje':"ERROR"})

@app.route('/cursos',methods=['POST'])
def registrar_cursos():
    try:
        #print(request.json)
        cursor = conexion.connection.cursor()
        sql="""INSERT INTO LIBROS(cod_lib, descripcion, titulo, autor, editorial, precio) 
        VALUES ('{0}','{1}','{2}','{3}','{4}',{5})""".format(request.json['cod_lib'],request.json['descripcion'],
                                                             request.json['titulo'],request.json['autor'],
                                                             request.json['editorial'],request.json['precio'])
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la accion de insercion
        return jsonify({'Mensaje':"CURSO REGISTRADO"})
    except Exception as ex:
        return jsonify({'Mensaje':"ERROR"})

@app.route('/cursos/<cod_lib>',methods=['PUT'])
def actualizar_cursos(cod_lib):
    try:
        #print(request.json)
        cursor = conexion.connection.cursor()
        sql="""UPDATE LIBROS SET descripcion='{0}', titulo='{1}', autor='{2}', editorial='{3}', precio={4}
            WHERE cod_lib='{5}'""".format(request.json['descripcion'],request.json['titulo'],
                                          request.json['autor'],request.json['editorial'],request.json['precio'],cod_lib)
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la accion de insercion
        return jsonify({'Mensaje':"CURSO ACTUALIZADO"}) 
    except Exception as ex:
        return jsonify({'Mensaje':"ERROR"})


@app.route('/cursos/<cod_lib>',methods=['DELETE'])
def eliminar_cursos(cod_lib):
    try:
        #print(request.json)
        cursor = conexion.connection.cursor()
        sql="DELETE FROM LIBROS WHERE cod_lib='{0}'".format(cod_lib)
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la accion de insercion
        return jsonify({'Mensaje':"CURSO ELIMINADO"})
    except Exception as ex:
        return jsonify({'Mensaje':"ERROR"})

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()