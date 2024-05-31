from flask import Flask,jsonify,request
from flask_mysqldb import MySQL

from config import config

app = Flask(__name__)

#CONEXION DE LA BASE DE DATOS
conexion = MySQL(app)

#METODO POST (REGISTRAR)
@app.route('/clientes',methods=['POST'])
def registrar_clientes():
    try:
        #print(request.json)
        cursor = conexion.connection.cursor()
        sql="""INSERT INTO CLIENTES(codCliente, Nombre, apellidos, empresa, puesto, CP, provincia, telefono, fechaNacimiento) 
        VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}',{7},'{8}')""".format(request.json['codCliente'],
                                                                               request.json['Nombre'],
                                                                               request.json['apellidos'],
                                                                               request.json['empresa'],
                                                                               request.json['puesto'],
                                                                               request.json['CP'],
                                                                               request.json['provincia'],
                                                                               request.json['telefono'],
                                                                               request.json['fechaNacimiento'])
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la accion de insercion
        return jsonify({'Mensaje':"CLIENTE REGISTRADO"})
    except Exception as ex:
        return jsonify({'Mensaje':"ERROR"})
    
@app.route('/articulos',methods=['POST'])
def registrar_articulos():
    try:
        #print(request.json)
        cursor = conexion.connection.cursor()
        sql="""INSERT INTO ARTICULOS(codArticulo, Nombre, Descripcion, precioUnidad, unidadesStock, stockSeguridad, imagen) 
        VALUES ('{0}','{1}','{2}',{3},{4},'{5}','{6}')""".format(
            request.json['codArticulo'],
            request.json['Nombre'],
            request.json['Descripcion'],
            request.json['precioUnidad'],
            request.json['unidadesStock'],
            request.json['stockSeguridad'],
            request.json['imagen'])
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la accion de insercion
        return jsonify({'Mensaje':"CLIENTE REGISTRADO"})
    except Exception as ex:
        return jsonify({'Mensaje':"ERROR"})

#METODO GET (LISTAR O LEER)
@app.route('/clientes',methods=['GET'])
def listar_clientes():
    #return "Texto prueba"
    try:
        cursor = conexion.connection.cursor()
        sql ="SELECT codCliente, Nombre, apellidos, empresa, puesto, CP, provincia, telefono, fechaNacimiento FROM CLIENTES"
        cursor.execute(sql)
        #fetchall convierte toda la respuesta en algo entendible para PYTHON
        datos = cursor.fetchall()
        #MOSTRAR COMO JSON
        clientes=[]
        for fila in datos:
            cliente = {'codCliente':fila[0],'Nombre':fila[1],'apellidos':fila[2],
                     'empresa':fila[3],'puesto':fila[4],'CP':fila[5],'provincia':fila[6],
                     'telefono':fila[7],'fechaNacimiento':fila[8]}
            clientes.append(cliente)
        return jsonify({'clientes':clientes,'Mensaje':"CLIENTES LISTADOS"})
        #print(datos)
    except Exception as ex:
        return jsonify({'Mensaje':"ERROR"})
    
@app.route('/articulos',methods=['GET'])
def listar_articulos():
    #return "Texto prueba"
    try:
        cursor = conexion.connection.cursor()
        sql ="SELECT codArticulo, Nombre, Descripcion, precioUnidad, unidadesStock, stockSeguridad, imagen FROM ARTICULOS"
        cursor.execute(sql)
        #fetchall convierte toda la respuesta en algo entendible para PYTHON
        datos = cursor.fetchall()
        #MOSTRAR COMO JSON
        articulos=[]
        for fila in datos:
            articulo = {
                'codArticulo':fila[0],'Nombre':fila[1],'Descripcion':fila[2],
                'precioUnidad':fila[3],'unidadesStock':fila[4],'stockSeguridad':fila[5],'imagen':fila[6]}
            articulos.append(articulo)
        return jsonify({'clientes':articulos,'Mensaje':"ARTICULOS LISTADOS"})
        #print(datos)
    except Exception as ex:
        return jsonify({'Mensaje':"ERROR"})

#METODO PUT (ACTUALIZAR)
@app.route('/clientes/<codCliente>',methods=['PUT'])
def actualizar_clientes(codCliente):
    try:
        #print(request.json)
        cursor = conexion.connection.cursor()
        sql="""UPDATE CLIENTES SET Nombre='{0}', apellidos='{1}', empresa='{2}', puesto='{3}', CP='{4}',
        provincia ='{5}', telefono={6}, fechaNacimiento='{7}'
        WHERE codCliente='{8}'""".format(request.json['Nombre'],
                                      request.json['apellidos'],
                                      request.json['empresa'],
                                      request.json['puesto'],
                                      request.json['CP'],
                                      request.json['provincia'],
                                      request.json['telefono'],
                                      request.json['fechaNacimiento'],codCliente)
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la accion de insercion
        return jsonify({'Mensaje':"CLIENTE ACTUALIZADO"}) 
    except Exception as ex:
        return jsonify({'Mensaje':"ERROR"})
    
@app.route('/articulos/<codArticulo>',methods=['PUT'])
def actualizar_articulos(codArticulo):
    try:
        #print(request.json)
        cursor = conexion.connection.cursor()
        sql="""UPDATE ARTICULOS SET 
        Nombre='{0}', Descripcion='{1}', precioUnidad={2}, 
        unidadesStock={3}, stockSeguridad='{4}', imagen='{5}'
        WHERE codArticulo='{6}'""".format(
            request.json['Nombre'],
            request.json['Descripcion'],
            request.json['precioUnidad'],
            request.json['unidadesStock'],
            request.json['stockSeguridad'],
            request.json['imagen'],codArticulo)
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la accion de insercion
        return jsonify({'Mensaje':"CLIENTE ACTUALIZADO"}) 
    except Exception as ex:
        return jsonify({'Mensaje':"ERROR"})

#METODO DELETE (ELIMINAR)
@app.route('/clientes/<codCliente>',methods=['DELETE'])
def eliminar_clientes(codCliente):
    try:
        #print(request.json)
        cursor = conexion.connection.cursor()
        sql="DELETE FROM CLIENTES WHERE codCliente='{0}'".format(codCliente)
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la accion de insercion
        return jsonify({'Mensaje':"CLIENTE ELIMINADO"})
    except Exception as ex:
        return jsonify({'Mensaje':"ERROR"})
    
@app.route('/articulos/<codArticulo>',methods=['DELETE'])
def eliminar_articulos(codArticulo):
    try:
        #print(request.json)
        cursor = conexion.connection.cursor()
        sql="DELETE FROM ARTICULOS WHERE codArticulo='{0}'".format(codArticulo)
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la accion de insercion
        return jsonify({'Mensaje':"ARTICULO ELIMINADO"})
    except Exception as ex:
        return jsonify({'Mensaje':"ERROR"})

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()