from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/enviar_mensaje_con_foto', methods=['POST'])
def enviar_mensaje_con_foto():
    nombre = request.form['nombre']
    detalle = request.form['detalle']
    patente = request.form['patente']
    tipo = request.form['tipo']
    imagen = request.files['imagen']

    # Construir el mensaje
    mensaje = f"➥ 𝗡𝗼𝗺𝗯𝗿𝗲 𝗜𝗖: {nombre}\n➥ 𝗧𝗶𝗽𝗼 𝗱𝗲 𝗺𝗼𝗱𝗶𝗳𝗶𝗰𝗮𝗰𝗶𝗼𝗻 𝘆 𝗽𝗿𝗲𝗰𝗶𝗼 : {detalle}\n➥ 𝗠𝗼𝗱𝗲𝗹𝗼 𝗩𝗲𝗵𝗶𝗰𝘂𝗹𝗼 : {tipo}\n➥ 𝗣𝗮𝘁𝗲𝗻𝘁𝗲 𝗩𝗲𝗵𝗶𝗰𝘂𝗹𝗼: {patente}"

    # Enviar el mensaje y la imagen a través de Discord webhook
    webhook_url = "https://discord.com/api/webhooks/1205028468899975208/5ITTVGYF8hcEaegmuJCl1r59KpgprXBKXIOq3SVR47pLKelyHY1PaBCf7oRLkjH_JPCU"
    payload = {"content": mensaje}
    files = {"file": (imagen.filename, imagen.stream, imagen.content_type)}

    response = requests.post(webhook_url, data=payload, files=files)

    if response.status_code == 200:
        return jsonify({"mensaje": "Mensaje enviado correctamente"})
    else:
        return jsonify({"error": "Error al enviar el mensaje"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
