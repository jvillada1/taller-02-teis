from flask import Flask, jsonify, render_template
import random
import json
import socket

app = Flask(__name__)

# Leer datos del archivo JSON
with open('pokeneas.json','r') as f:
    pokeneas = json.load(f)

@app.route('/api/pokenea', methods=['GET'])
def get_pokenea():
    pokenea = random.choice(pokeneas)
    container_id = socket.gethostname()
    response = {
        'id': pokenea['id'],
        'nombre': pokenea['nombre'],
        'altura': pokenea['altura'],
        'habilidad': pokenea['habilidad'],
        'container_id': container_id
    }
    return jsonify(response)

@app.route('/pokenea')
def show_pokenea():
    pokenea = random.choice(pokeneas)
    container_id = socket.gethostname()
    return render_template('pokenea.html', pokenea=pokenea, container_id=container_id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
