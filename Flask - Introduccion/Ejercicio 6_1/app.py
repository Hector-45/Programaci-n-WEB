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

#METODO POST (ACTUALIZAR)
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

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()