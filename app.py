from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
import openai

load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/organizar', methods=['POST'])
def organizar():
    data = request.json
    tareas = data.get('tareas')

    prompt = f"""
    Tengo estas tareas: {tareas}

    Ordénalas por prioridad teniendo en cuenta:
    - urgencia
    - impacto
    - carga mental

    Devuélvelo en JSON con:
    [
        {{
            "tarea": "",
            "prioridad": "alta/media/baja",
            "explicacion": ""
        }}
    ]

    Además añade:
    "consejo": "..."
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return jsonify({
            "resultado": response['choices'][0]['message']['content']
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)