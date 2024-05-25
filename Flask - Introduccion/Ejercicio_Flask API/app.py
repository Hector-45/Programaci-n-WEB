from flask import Flask,render_template

#render_template se debe importar

app = Flask(__name__)

#Ruta raiz
@app.route("/")
def index():
    #return "<h1>Hola Mundo</h1>"
    #diccionario
    #Se usa {{ nombre de la variable}} motor de plantilas jinja2
    #Tambien podemos agregar listas
    cursos=['PHP','HTML','CSS','PYTHON','C++']
    data ={
        'titulo':'index',
        'bienvenida':'Saludos',
        'cursos':cursos,
        'numero_cursos':len
    }
    return render_template('index.html',VarData=data)


if __name__ =='__main__':
    app.run(debug=True)