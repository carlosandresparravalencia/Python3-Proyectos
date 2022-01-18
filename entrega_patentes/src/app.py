from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:contrasena@localhost/patentescarlos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class ClasePatente(db.Model):
    id = db.Column(db.String(7), primary_key=True)
    nombre_patente = db.Column(db.String(70), unique=True)
    descripcion = db.Column(db.String(100))

    def __init__(self, id, nombre_patente, descripcion):
        self.id = id
        self.nombre_patente = nombre_patente
        self.descripcion = descripcion

db.create_all()

class PatenteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre_patente', 'descripcion')

entrega_schema = PatenteSchema()
patentes_schema = PatenteSchema(many=True)

@app.route('/patentes', methods=['Post'])
def create_entrega():
  # Si existen registros, utilizar la funcion dominio sino ingresar el primer id
  id  = 'AAAA000'
  nombre_patente = request.json['nombre_patente']
  descripcion = request.json['descripcion']

  new_entrega= ClasePatente(id, nombre_patente, descripcion)

  db.session.add(new_entrega)
  db.session.commit()

  return entrega_schema.jsonify(new_entrega)

@app.route('/patentes', methods=['GET'])
def get_patentes():
  all_patentes = ClasePatente.query.all()
  result = patentes_schema.dump(all_patentes)
  return jsonify(result)

@app.route('/patentes/<id>', methods=['GET'])
def get_entrega(id):
  entrega = ClasePatente.query.get(id)
  return entrega_schema.jsonify(entrega)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Bienvenido a la API Patentes'})



if __name__ == "__main__":
    app.run(debug=True)