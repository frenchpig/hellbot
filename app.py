from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/enviar_mensaje_con_foto')
def enviar_mensaje_con_foto():
    webhook_url = "https://discord.com/api/webhooks/1205028468899975208/5ITTVGYF8hcEaegmuJCl1r59KpgprXBKXIOq3SVR47pLKelyHY1PaBCf7oRLkjH_JPCU"
    mensaje = "Hola mundo!"
    imagen_path = "xuek.png"
    
    imagen = {"file": ("xuek.png", open("xuek.png", "rb"), "image/png")}
    
    payload = {
        "content": mensaje
    }
    
    requests.post(webhook_url, data=payload, files=imagen)
    
    return jsonify({"mensaje": "Mensaje enviado correctamente"})

if __name__ == '__main__':
    app.run(debug=True)
