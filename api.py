from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
app = Flask(__name__)
class Connection:
    __USER = "root"
    __PW = "example"
    __DB_NAME = "etudiant"

    @classmethod
    def connexion(cls):
        print(f"mongodb://{cls.__USER}:{cls.__PW}@127.0.0.1:27017")
        cls.client = MongoClient(f"mongodb://{cls.__USER}:{cls.__PW}@127.0.0.1:27017")
        cls.db = cls.client[cls.__DB_NAME]
        return cls.db

    @classmethod
    def deconnexion(cls):
        cls.client.close()

def get_etudiants(db):
    etudiants = db.etudiants.find({})
    return list(etudiants)

def get_etudiant_uni(db,id):
    print('bonjour id = ',id)
    #etudiants = db.etudiants.find_one({"_id":id})
    etudiants = db.etudiants.find_one({"_id":ObjectId("64e860af36c7802ae137d5e6")})
    print("mongo etudiant",etudiants)
    return etudiants

@app.route("/api/etudiant/<string:id>", methods=['GET', 'PUT', 'DELETE'])
def etudiant(id):
    if request.method == 'GET':
        db = Connection.connexion()
        etudiant = get_etudiant_uni(db, id)
        Connection.deconnexion()
        print("etudiantchoisi", etudiant)
        return etudiant
    if request.method == 'PUT':
        pass

@app.route("/api/etudiants/", methods=['GET'])
def get_etudiant():
    db = Connection.connexion()
    etudiants = get_etudiants(db)
    Connection.deconnexion()
    print(etudiants)
    for etudiant in etudiants:
        etudiant['_id'] = str(etudiant['_id'])
    return jsonify(etudiants), 200

@app.errorhandler(404)
def page_not_found(e):
    return "erreur", 404

if __name__ == "__main__":
    app.run(debug=True, port=5001)