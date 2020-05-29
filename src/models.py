from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todo(db.Model):
    __tablename__="todos"
    id = db.Column(db.Interger, primary_key=True)
    label = db.Column(db.String(50), nullable=False)
    done = db.Column(db.boolean, default=False)

    def __repr__(self):
        return "<Todo %r>" % self.label

    def serialize(self):
        return{
            "id": self.id,
            "label": self.label,
            "done": self.done,
        
        }


    def get_all_todos(self):
        return self._todos

    def get_todo(self,id):
        todo = list(filter(lambda item: item["id"]==id, self.get_all_todos))
        return(todo)
    
    def add_todo(self,todo):
        todo = {
            "id": todo.id,
            "label": todo.label,
            "done": todo.done
        }
        self.todos.append(todo)
        return todo
    
    def delete_todo(self,id):
        todo = self.get_todo(id)
        todo.remove()