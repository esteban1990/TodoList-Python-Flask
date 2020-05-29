import os
from flask import Flask, render_template, jsonify, request
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS
from models import db, Todo

todos=[
  {"label": "My first task", "done": False },
  { "label": "My second task", "done": True }
]

BASE_DIR = os.path.abspath(os.path.dirname( __file__))  #guarda la ruta del directorio de mi aplicacion// donde estoy ubic

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'dev.db') #cual va ser la base de datos que voi a utilizar
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # EVITA QUE MI BASE DE DATOS GUARDE CAMBIOS INNECESARIOS CADA VEZ QUE HAGO UNA MODIFICACION A NIVEL DE TABLAS

db.init_app(app)
migrate = Migrate(app, db)#genera los comandos para crear la migracion.

manager = Manager(app)
manager.add_command('db', MigrateCommand)#ejecuta mis migraciones por consola
CORS(app) #evite que tenga problemas con el navegador,para que pueda utilizarse en manera de desarollo

@app.route("/todos", methods=["GET"])
def helloworld():
    if request.method =="GET":
        todos = Todo.get.all_todos()
        return jsonify(todos)

@app.route("/todos", methods=["POST"])
def addTodo():
    if request.method =="POST":
        todo.id = request.json.get("id")
        todo.label= request.json.get("label")
        todo.done = request.json.get("done")

        todo = todos.add_todo(todos)
        return jsonify(todos),200

@app.route("/todos/<int:position>", methods=["DELETE"])
def deleteTodo():
    if request.method =="DELETE":
      todo = todos.query.get.(id)

      db.session.delete_todo(todo)
      return jsonify({"msge": "todo has been deleted"})
      






















if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)