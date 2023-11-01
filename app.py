from flask import Flask, render_template , request
import jinja2
import os
import subprocess
import requests
import json
URL_API = "http://127.0.0.1:5001"
app = Flask(__name__)
@app.route("/")
def index():
    response = requests.get(f"{URL_API}/api/etudiants/")
    content = response.content.decode("utf-8")
    data = json.loads(content)
    print("info *******************",data)
    return render_template("index.html", etudiants=data)

@app.route("/etudiant/" ,methods=['GET'])
def etudiant():
    response = requests.get(f"{URL_API}/api/etudiants/")
    content = response.content.decode("utf-8")
    data = json.loads(content)
    print("info *******************",data)
    return render_template("index.html", etudiants=data)

if __name__ == "__main__":
    app.run(debug=True)