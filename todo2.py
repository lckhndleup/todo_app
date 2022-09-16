from flask import Flask,redirect,url_for,request,render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/mehmetali/Desktop/Kodlama Egzersizleri/todo_app/todo2.db'
db = SQLAlchemy(app)
@app.route("/")
def index():
    todos =Todo.query.all()
    return render_template("index.html",todos=todos)
@app.route("/add",methods=["POST"])
def addTodo():
    title= request.form.get("title")
    newTodo = Todo(title = title,complete =False)
    db.session.add(newTodo)
    db.session.commit()

    return redirect(url_for("index"))

class Todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(80))

    complete=db.Column(db.Boolean)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)


