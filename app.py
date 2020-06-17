from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os #esta es una librería

# La ruta absoluta de la DB y se puede tener en cualquier dirección hasta en internet hasta en un servior externo pero en esta ocación se ceará localmente. Hay diferente maneras de escribir la ruta pero la siguiente forma es para estandarizar los procesos.


#conector		     + Tola la ruta absoluta actual +   nombre de la db
					 #equivale a plantilla\db
dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) +	"/database.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
	# pasa la variable app que esta asignada arriba de este comentario			
db=SQLAlchemy(app)

# Esquema de la DB 
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/s
class Posts(db.Model):
	# Columnas 
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(50)) 

@app.route("/") 		
def index():
	return render_template("index.html")	

#agregar un registro.
@app.route("/insert/default")
def insertar_registro():
	new_post = Posts(title="Default Title") #nombre de la variable del esquema
	db.session.add(new_post) #Agregarlo a la base de datos
	db.session.commit() #confirmar los cambios q se van agregar en la DB

	return "Registro creado."

#hacer una consulta.
#		      /URL puede llamarse como sea 
@app.route("/select/default")
def select_default(): 
	# Especificar por cual campo se va a buscar
	post = Posts.query.filter_by(id=1).first() # Variable post más el nombre de clase Posts Agragada arriba.

	#imprimir la variable asignada en este bloque en consola el título de post.
	# select * from posts;
	
	print(post.title)

	return "Consulta realizada."


#Condicional
if __name__ == "__main__":
	db.create_all() #cuando se ejecuta el módulo se crea esta db. SQLALCHEMY identifica si la db está creada o no y si está creada no la sobre escribe.
	app.run(debug=True) 	
		