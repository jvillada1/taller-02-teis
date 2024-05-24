from flask import Flask, jsonify, render_template
import random
import json
import socket

app = Flask(__name__)

# Cargar los datos de Pokeneas desde el archivo JSON
with open('pokeneas.json', 'r') as f:
    data = json.load(f)
    pokeneas = data['pokeneas']

def get_container_id():
    # Obtener el nombre del host como un identificador del contenedor
    return socket.gethostname()

@app.route('/api/pokenea', methods=['GET'])
def get_pokenea():
    pokenea = random.choice(pokeneas)
    container_id = get_container_id()
    response = {
        "id": pokenea["id"],
        "nombre": pokenea["nombre"],
        "altura": pokenea["altura"],
        "habilidad": pokenea["habilidad"],
        "container_id": container_id
    }
    return jsonify(response)

@app.route('/pokenea', methods=['GET'])
def show_pokenea():
    pokenea = random.choice(pokeneas)
    container_id = get_container_id()
    return render_template('pokenea.html', pokenea=pokenea, container_id=container_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
